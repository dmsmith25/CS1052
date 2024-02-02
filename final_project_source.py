import numpy as np
import pandas as pd
import pickle
import hashlib

class LSH:

    def cosine_hash_with_seed(self, real_vector, seed, r):
        """
        Calculates the sign of inner product between real vector and random vector for a given seed.

        Args:
            real_vector: A numpy array of 0s and 1s.
            seed: The seed for the hash function.

        Returns:
            The sign of the real vector and random vector.
        """

        # Seed so randomness is always the same
        np.random.seed(seed)

        # Get *seeded* random vector
        random_matrix = np.random.normal(size=(r, len(real_vector)))

        sign = np.sign(random_matrix@real_vector)

        return sign
    

    def hash_tuple_with_seed(self, tuple_object, m, seed):
        """
        Hashes a tuple object to an integer between 1 and m using a seed.

        Args:
            tuple_object: The tuple object to hash.
            m: The upper bound of the hash value (inclusive).
            seed: The seed for the hash function.

        Returns:
            An integer between 1 and m.
        """

        # Convert the tuple object to a string.
        tuple_string = str(tuple_object)

        # Create a hash object with the specified seed.
        hash_object = hashlib.sha256(str(seed).encode('utf-8'))

        # Update the hash object with the tuple string.
        hash_object.update(tuple_string.encode('utf-8'))

        # Get the hash value as a hexadecimal string.
        hash_value = hash_object.hexdigest()

        # Convert the hexadecimal string to an integer.
        hash_value_int = int(hash_value, 16)

        # Return the hash value modulo m.
        return hash_value_int % m + 1
    

    
    def generateTable(self, dataset, df_features, seeds, seeds_t, df_labels, t, r):
        table = []

        for m in range(t):
            table_m = []
            for x in range(len(dataset)):
                table_m.append([])

            table.append(table_m)


        for u in range(t):

            cosine_hash_list = []

            for i in range(len(dataset)):
                cosine_hash_list.append(tuple(self.cosine_hash_with_seed(df_features.iloc[i, :], seeds[u], r)))


            hash_vals = []

            counter = 0

            for h in range(len(cosine_hash_list)):
                hash_val = self.hash_tuple_with_seed(cosine_hash_list[h], len(dataset) - 1, seeds_t[u])
                table[u][hash_val].append(df_labels.iloc[h, :])
                if hash_val in hash_vals:
                    counter = counter + 1
                else:
                    hash_vals.append(hash_val)

            print(str(u) + "/" + str(t))

        return table
    

    def testAlgorithm(self, table, seeds, seeds_t, dataset, testing_features, testing_labels, t, r):

        preds = []
        res = []
        score = []


        for c in range(3000):
            entries = []

            for q in range(t):
                test_hash = []
                for n in range(r):
                    test_hash.append(self.cosine_hash_with_seed(testing_features.iloc[c, :], seeds[q], r))

                entries.append(tuple(test_hash))


            home_scores = []
            away_scores = []


            for a in range(t):
                val = self.hash_tuple_with_seed(entries[a], len(dataset) - 1, seeds_t[a])
                data = table[a][val]
                if len(data) > 0:
                    for stat in data:
                        home_scores.append(int(stat['Home_Result']))
                        away_scores.append(int(stat["Away_Result"]))


            if len(home_scores) > 0:
                home_mean = np.median(home_scores)
                away_mean = np.median(away_scores)

                pred_res = home_mean - away_mean
                real_res = testing_labels.iloc[c, 1]
                spread = testing_labels.iloc[c, 0]

                preds.append(pred_res)
                res.append(real_res)

                if (real_res + spread) * (pred_res + spread) > 0:
                    score.append(1)
                else:
                    score.append(0)


        mse = np.mean((np.array(preds) - np.array(res)) ** 2)
        acc = np.sum(score) / len(score)

        print("MSE: " + str(mse))
        print("ACC: " + str(acc))