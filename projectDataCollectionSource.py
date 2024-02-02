# imports
import numpy as np
import pandas as pd
import time
from datetime import datetime, timedelta
from IPython.display import display

# Team id's for sr
final_sr = ['abilene-christian', 'air-force', 'akron', 'alabama', 'alabama-am', 'alabama-birmingham', 'alabama-state', 'albany-ny', 'alcorn-state', 'american', 'appalachian-state', 'arizona', 'arizona-state', 'arkansas', 'arkansas-little-rock', 'arkansas-pine-bluff', 'arkansas-state', 'army', 'auburn', 'austin-peay', 'ball-state', 'baylor', 'bellarmine' , 'belmont', 'bethune-cookman', 'binghamton', 'boise-state', 'boston-college', 'boston-university', 'bowling-green-state', 'bradley', 'brigham-young', 'brown', 'bryant', 'bucknell', 'buffalo', 'butler', 'cal-poly', 'cal-state-bakersfield', 'cal-state-fullerton', 'cal-state-northridge', 'california', 'california-davis', 'california-irvine', 'california-riverside', 'california-santa-barbara', 'campbell', 'canisius', 'central-arkansas', 'central-connecticut-state', 'central-michigan', 'charleston-southern', 'charlotte', 'chattanooga', 'chicago-state', 'cincinnati', 'clemson', 'cleveland-state', 'coastal-carolina', 'colgate', 'college-of-charleston', 'colorado', 'colorado-state', 'columbia', 'connecticut', 'coppin-state', 'cornell', 'creighton', 'dartmouth', 'davidson', 'dayton', 'delaware', 'delaware-state', 'denver', 'depaul', 'detroit-mercy', 'drake', 'drexel', 'duke', 'duquesne', 'east-carolina', 'east-tennessee-state', 'eastern-illinois', 'eastern-kentucky', 'eastern-michigan', 'eastern-washington', 'elon', 'evansville', 'fairfield', 'fairleigh-dickinson', 'florida', 'florida-am', 'florida-atlantic', 'florida-gulf-coast', 'florida-international', 'florida-state', 'fordham', 'fresno-state', 'furman', 'gardner-webb', 'george-mason', 'george-washington', 'georgetown', 'georgia', 'georgia-southern', 'georgia-state', 'georgia-tech', 'gonzaga', 'grambling', 'grand-canyon', 'green-bay', 'hampton', 'harvard', 'hawaii', 'high-point', 'hofstra', 'holy-cross', 'houston', 'houston-baptist', 'howard', 'idaho', 'idaho-state', 'illinois', 'illinois-chicago', 'illinois-state', 'incarnate-word', 'indiana', 'indiana-state', 'iona', 'iowa', 'iowa-state', 'iupui', 'jackson-state', 'jacksonville', 'jacksonville-state', 'james-madison', 'kansas', 'kansas-state', 'kennesaw-state', 'kent-state', 'kentucky', 'la-salle', 'lafayette', 'lamar', 'lehigh', 'liberty', 'lipscomb', 'long-beach-state', 'long-island-university', 'longwood', 'louisville', 'loyola-il', 'loyola-md', 'maine', 'manhattan', 'marist', 'marquette', 'marshall', 'maryland', 'maryland-eastern-shore', 'massachusetts', 'massachusetts-lowell', 'memphis', 'mercer', 'miami-fl', 'miami-oh', 'michigan', 'michigan-state', 'middle-tennessee', 'milwaukee', 'minnesota', 'mississippi-state', 'mississippi-valley-state', 'missouri', 'missouri-state', 'citadel', 'mcneese-state', 'mississippi', 'monmouth', 'montana', 'montana-state', 'morehead-state', 'morgan-state', 'mount-st-marys', 'murray-state', 'navy', 'nebraska', 'nebraska-omaha', 'nevada', 'new-hampshire', 'new-mexico', 'new-mexico-state', 'new-orleans', 'niagara', 'nicholls-state', 'njit', 'norfolk-state', 'north-carolina-at', 'north-dakota', 'north-dakota-state', 'north-texas', 'northeastern', 'northern-arizona', 'northern-colorado', 'northern-illinois', 'northern-iowa', 'northern-kentucky', 'northwestern', 'northwestern-state', 'notre-dame', 'oakland', 'ohio', 'ohio-state', 'oklahoma', 'oklahoma-state', 'old-dominion', 'oral-roberts', 'oregon', 'oregon-state', 'pacific', 'penn-state', 'pennsylvania', 'pepperdine', 'pittsburgh', 'portland', 'portland-state', 'prairie-view', 'presbyterian', 'princeton', 'providence', 'purdue', 'quinnipiac', 'radford', 'rhode-island', 'rice', 'richmond', 'rider', 'robert-morris', 'rutgers', 'sacramento-state', 'sacred-heart', 'saint-josephs', 'saint-louis', 'saint-marys-ca', 'sam-houston-state', 'samford', 'san-diego', 'san-diego-state', 'san-francisco', 'san-jose-state', 'santa-clara', 'seattle', 'seton-hall', 'siena', 'south-alabama', 'south-carolina', 'south-dakota', 'south-florida', 'st-bonaventure', 'st-francis-ny', 'st-johns-ny', 'stanford', 'stetson', 'stony-brook', 'syracuse', 'temple', 'tennessee', 'tennessee-state', 'tennessee-tech', 'texas', 'texas-am', 'texas-am-corpus-christi', 'texas-christian', 'texas-southern', 'texas-state', 'texas-tech', 'toledo', 'towson', 'troy', 'tulane', 'tulsa', 'ucla', 'utah', 'utah-state', 'utah-valley', 'valparaiso', 'vanderbilt', 'vermont', 'villanova', 'virginia', 'virginia-commonwealth', 'virginia-military-institute', 'virginia-tech', 'wagner', 'wake-forest', 'washington', 'washington-state', 'weber-state', 'west-virginia', 'wichita-state', 'william-mary', 'winthrop', 'wisconsin', 'wofford', 'wright-state', 'wyoming', 'xavier', 'yale', 'youngstown-state', 'central-florida', 'ipfw', 'louisiana-lafayette', 'louisiana-monroe', 'louisiana-state', 'louisiana-tech', 'loyola-marymount', 'maryland-baltimore-county', 'missouri-kansas-city', 'nevada-las-vegas', 'north-carolina', 'north-carolina-asheville', 'north-carolina-central', 'north-carolina-greensboro', 'north-carolina-state', 'north-carolina-wilmington', 'north-florida', 'saint-francis-pa', 'saint-peters', 'south-carolina-state', 'south-carolina-upstate', 'south-dakota-state', 'southeast-missouri-state', 'southeastern-louisiana', 'southern', 'southern-california', 'southern-illinois', 'southern-illinois-edwardsville', 'southern-methodist', 'southern-mississippi', 'southern-utah', 'stephen-f-austin', 'tennessee-martin', 'texas-arlington', 'texas-el-paso', 'texas-pan-american', 'texas-san-antonio', 'western-carolina', 'western-illinois', 'western-kentucky', 'western-michigan']

# Team id's for CBS
final_cbs = ['Abilene Chr.', 'Air Force', 'Akron', 'Alabama', 'Alabama A&M', 'UAB', 'Alabama St.', 'Albany', 'Alcorn St.', 'American', 'App. St.', 'Arizona', 'Arizona St.', 'Arkansas', 'Little Rock', 'Ark.-Pine Bluff', 'Arkansas St.', 'Army', 'Auburn', 'Austin Peay', 'Ball St.', 'Baylor', 'Bellarmine', 'Belmont', 'Bethune-Cook.', 'Binghamton', 'Boise St.', 'Boston College', 'Boston U.', 'Bowling Green', 'Bradley', 'BYU', 'Brown', 'Bryant', 'Bucknell', 'Buffalo', 'Butler', 'Cal Poly', 'Cal-Baker.', 'CSFullerton', 'CSNorthridge', 'California', 'UC Davis', 'UC Irvine', 'UC Riverside', 'UCSB', 'Campbell', 'Canisius', 'Cent. Arkansas', 'CCSU', 'C. Michigan', 'Charleston So.', 'Charlotte', 'Chattanooga', 'Chicago St.', 'Cincinnati', 'Clemson', 'Clev. St.', 'C. Carolina', 'Colgate', 'Charleston', 'Colorado', 'Colorado St.', 'Columbia', 'Connecticut', 'Coppin St.', 'Cornell', 'Creighton', 'Dartmouth', 'Davidson', 'Dayton', 'Delaware', 'Delaware St.', 'Denver', 'DePaul', 'Detroit', 'Drake', 'Drexel', 'Duke', 'Duquesne', 'East Carolina', 'ETSU', 'E. Illinois', 'E. Kentucky', 'E. Michigan', 'E. Washington', 'Elon', 'Evansville', 'Fairfield', 'FDU', 'Florida', 'Florida A&M', 'FAU', 'FGCU', 'FIU', 'Florida St.', 'Fordham', 'Fresno St.', 'Furman', 'Gardner-Webb', 'George Mason', 'George Wash.', 'Georgetown', 'Georgia', 'Ga. Southern', 'Georgia St.', 'Ga. Tech', 'Gonzaga', 'Grambling', 'Grand Canyon', 'Green Bay', 'Hampton', 'Harvard', 'Hawaii', 'High Point', 'Hofstra', 'Holy Cross', 'Houston', 'Houston Bap.', 'Howard', 'Idaho', 'Idaho St.', 'Illinois', 'Ill.-Chicago', 'Illinois St.', 'Incarnate Word', 'Indiana', 'Indiana St.', 'Iona', 'Iowa', 'Iowa St.', 'IUPUI', 'Jackson St.', 'Jacksonville', 'Jax. State', 'James Madison', 'Kansas', 'Kansas St.', 'Kennesaw St.', 'Kent St.', 'Kentucky', 'La Salle', 'Lafayette', 'Lamar', 'Lehigh', 'Liberty', 'Lipscomb', 'LBSU', 'LIU', 'Longwood', 'Louisville', 'Loyola Chi.', 'Loyola-Md.', 'Maine', 'Manhattan', 'Marist', 'Marquette', 'Marshall', 'Maryland','Md.-E. Shore','Massachusetts', 'UMass Lowell', 'Memphis', 'Mercer', 'Miami (Fla.)', 'Miami (Ohio)', 'Michigan', 'Michigan St.', 'Middle Tenn.', 'Milwaukee', 'Minnesota', 'Miss. State', 'Miss Valley St.', 'Missouri', 'Missouri St.', 'The Citadel', 'McNeese St.', 'Ole Miss', 'Monmouth', 'Montana', 'Montana St.', 'Morehead St.', 'Morgan St.', "Mt St Mary's", 'Murray St.', 'Navy', 'Nebraska', 'Neb.-Omaha', 'Nevada', 'New Hamp.', 'New Mexico', 'N. Mex. St.', 'New Orleans', 'Niagara', 'Nicholls St.', 'N.J. Tech', 'Norfolk St.', 'NC A&T', 'North Dakota', 'N. Dak. St.', 'North Texas', 'Northeastern', 'N. Arizona', 'N. Colorado', 'N. Illinois', 'Northern Iowa', 'N. Kentucky', 'Northwestern', 'Northwestern St.', 'Notre Dame', 'Oakland', 'Ohio', 'Ohio St.', 'Oklahoma', 'Okla. St.', 'Old Dominion', 'Oral Roberts', 'Oregon', 'Oregon St.', 'Pacific', 'Penn St.', 'Penn', 'Pepperdine', 'Pittsburgh', 'Portland', 'Portland St.', 'Prairie View', 'Presbyterian', 'Princeton', 'Providence', 'Purdue', 'Quinnipiac', 'Radford', 'Rhode Island', 'Rice', 'Richmond', 'Rider', 'Robert Morris', 'Rutgers', 'Sacramento St.', 'Sacred Heart', "Saint Joseph's", 'Saint Louis', "Saint Mary's", 'Sam Houston', 'Samford', 'San Diego', 'San Diego St', 'San Fran.', 'San Jose St.', 'Santa Clara', 'Seattle', 'Seton Hall', 'Siena', 'South Alabama', 'South Carolina', 'South Dakota', 'South Florida', 'St. Bona.', 'St. Fran.-NY', "St. John's", 'Stanford', 'Stetson', 'Stony Brook', 'Syracuse', 'Temple', 'Tennessee', 'Tennessee St.', 'Tenn. Tech', 'Texas', 'Texas A&M', 'Texas A&M-CC', 'TCU', 'Texas So.', 'Texas St.', 'Texas Tech', 'Toledo', 'Towson', 'Troy', 'Tulane', 'Tulsa', 'UCLA', 'Utah', 'Utah St.', 'Utah Valley', 'Valparaiso', 'Vanderbilt', 'Vermont', 'Villanova', 'Virginia', 'VCU', 'VMI', 'Va. Tech', 'Wagner', 'Wake Forest', 'Washington', 'Washington St.', 'Weber St.', 'West Virginia', 'Wichita St.', 'William & Mary', 'Winthrop', 'Wisconsin', 'Wofford', 'Wright St.', 'Wyoming', 'Xavier', 'Yale', 'Youngstown St.', 'UCF', 'PFW', 'Louisiana', 'UL-Monroe', 'LSU', 'La. Tech', 'LMU', 'UMBC', 'UMKC', 'UNLV', 'N. Carolina', 'UNC-Ash.', 'NC Central', 'UNCG', 'NC State', 'UNC-Wilm.', 'North Florida', 'St. Fran.-Pa.', "St. Peter's", 'SC State', 'SC Upstate', 'S. Dak. St.', 'SE Missouri St.', 'SE Louisiana', 'Southern U.', 'USC', 'S. Illinois', 'SIUE', 'SMU', 'So. Miss', 'So. Utah', 'SF Austin', 'UT Martin', 'UT-Arlington', 'UTEP', 'UT-Rio Grande Valley', 'UTSA', 'W. Carolina', 'W. Illinois', 'W. Kentucky', 'W. Michigan']

# Team id's for tr
final_tr = ['Abl Christian', 'Air Force', 'Akron', 'Alabama', 'Alab A&M', 'UAB', 'Alabama St', 'Albany', 'Alcorn State', 'American', 'App State', 'Arizona', 'Arizona St', 'Arkansas', 'AR Lit Rock', 'Ark Pine Bl', 'Arkansas St', 'Army', 'Auburn', 'Austin Peay', 'Ball State', 'Baylor', 'Bellarmine' , 'Belmont', 'Beth-Cook', 'Binghamton', 'Boise State', 'Boston Col', 'Boston U', 'Bowling Grn', 'Bradley', 'BYU', 'Brown', 'Bryant', 'Bucknell', 'Buffalo', 'Butler', 'Cal Poly', 'CS Bakersfld', 'CS Fullerton', 'Cal St Nrdge', 'California', 'UC Davis', 'UC Irvine', 'UC Riverside', 'UCSB', 'Campbell', 'Canisius', 'Central Ark', 'Central Conn', 'Central Mich', 'Charl South', 'Charlotte', 'Chattanooga', 'Chicago St', 'Cincinnati', 'Clemson', 'Cleveland St', 'Coastal Car', 'Colgate', 'Col Charlestn', 'Colorado', 'Colorado St', 'Columbia', 'Connecticut', 'Coppin State', 'Cornell', 'Creighton', 'Dartmouth', 'Davidson', 'Dayton', 'Delaware', 'Delaware St', 'Denver', 'DePaul', 'Detroit', 'Drake', 'Drexel', 'Duke', 'Duquesne', 'E Carolina', 'E Tenn St', 'E Illinois', 'E Kentucky', 'E Michigan', 'E Washingtn', 'Elon', 'Evansville', 'Fairfield', 'F Dickinson', 'Florida', 'Florida A&M', 'Fla Atlantic', 'Fla Gulf Cst', 'Florida Intl', 'Florida St', 'Fordham', 'Fresno St', 'Furman', 'Gard-Webb', 'Geo Mason', 'Geo Wshgtn', 'Georgetown', 'Georgia', 'GA Southern', 'Georgia St', 'GA Tech', 'Gonzaga', 'Grambling St', 'Grd Canyon', 'WI-Grn Bay', 'Hampton', 'Harvard', 'Hawaii', 'High Point', 'Hofstra', 'Holy Cross', 'Houston', 'Houston Bap', 'Howard', 'Idaho', 'Idaho State', 'Illinois', 'IL-Chicago', 'Illinois St', 'Incar Word', 'Indiana', 'Indiana St', 'Iona', 'Iowa', 'Iowa State', 'IUPUI', 'Jackson St', 'Jacksonville', 'Jksnville St', 'James Mad', 'Kansas', 'Kansas St', 'Kennesaw St', 'Kent State', 'Kentucky', 'La Salle', 'Lafayette', 'Lamar', 'Lehigh', 'Liberty', 'Lipscomb', 'Lg Beach St', 'LIU', 'Longwood', 'Louisville', 'Loyola-Chi', 'Loyola-MD', 'Maine', 'Manhattan', 'Marist', 'Marquette', 'Marshall', 'Maryland', 'Maryland ES', 'U Mass', 'Mass Lowell', 'Memphis', 'Mercer', 'Miami (FL)', 'Miami (OH)', 'Michigan', 'Michigan St', 'Middle Tenn', 'WI-Milwkee', 'Minnesota', 'Miss State', 'Miss Val St', 'Missouri', 'Missouri St', 'Citadel', 'McNeese St', 'Mississippi', 'Monmouth', 'Montana', 'Montana St', 'Morehead St', 'Morgan St', 'Mt St Marys', 'Murray St', 'Navy', 'Nebraska', 'Neb Omaha', 'Nevada', 'N Hampshire', 'New Mexico', 'N Mex State', 'New Orleans', 'Niagara', 'Nicholls St', 'NJIT', 'Norfolk St', 'NC A&T', 'North Dakota', 'N Dakota St', 'North Texas', 'Northeastrn', 'N Arizona', 'N Colorado', 'N Illinois', 'N Iowa', 'N Kentucky', 'Northwestern', 'NW State', 'Notre Dame', 'Oakland', 'Ohio', 'Ohio State', 'Oklahoma', 'Oklahoma St', 'Old Dominion', 'Oral Roberts', 'Oregon', 'Oregon St', 'Pacific', 'Penn State', 'U Penn', 'Pepperdine', 'Pittsburgh', 'Portland', 'Portland St', 'Prairie View', 'Presbyterian', 'Princeton', 'Providence', 'Purdue', 'Quinnipiac', 'Radford', 'Rhode Island', 'Rice', 'Richmond', 'Rider', 'Rob Morris', 'Rutgers', 'Sac State', 'Sacred Hrt', 'St Josephs', 'Saint Louis', 'St Marys', 'Sam Hous St', 'Samford', 'San Diego', 'San Diego St', 'San Fransco', 'San Jose St', 'Santa Clara', 'Seattle', 'Seton Hall', 'Siena', 'S Alabama', 'S Carolina', 'South Dakota', 'S Florida', 'St Bonavent', 'St Fran (NY)', 'St Johns', 'Stanford', 'Stetson', 'Stony Brook', 'Syracuse', 'Temple', 'Tennessee', 'TN State', 'TN Tech', 'Texas', 'Texas A&M', 'TX A&M-CC', 'TX Christian', 'TX Southern', 'Texas State', 'Texas Tech', 'Toledo', 'Towson', 'Troy', 'Tulane', 'Tulsa', 'UCLA', 'Utah', 'Utah State', 'Utah Val St', 'Valparaiso', 'Vanderbilt', 'Vermont', 'Villanova', 'Virginia', 'VCU', 'VA Military', 'VA Tech', 'Wagner', 'Wake Forest', 'Washington', 'Wash State', 'Weber State', 'W Virginia', 'Wichita St', 'Wm & Mary', 'Winthrop', 'Wisconsin', 'Wofford', 'Wright State', 'Wyoming', 'Xavier', 'Yale', 'Youngs St', 'Central FL', 'IPFW', 'LA Lafayette', 'LA Monroe', 'LSU', 'LA Tech', 'Loyola Mymt', 'Maryland BC', 'UMKC', 'UNLV', 'N Carolina', 'NC-Asheville', 'NC Central', 'NC-Grnsboro', 'NC State', 'NC-Wilmgton', 'N Florida', 'St Fran (PA)', 'St Peters', 'S Car State', 'SC Upstate', 'S Dakota St', 'SE Missouri', 'SE Louisiana', 'Southern', 'USC', 'S Illinois', 'SIU Edward', 'S Methodist', 'S Mississippi', 'S Utah', 'Ste F Austin', 'TN Martin', 'TX-Arlington', 'TX El Paso', 'TX-Pan Am', 'TX-San Ant', 'W Carolina', 'W Illinois', 'W Kentucky', 'W Michigan']

# Team Sites for N
final_arenas = ['Moody Coliseum', 'Cadet Field House', 'James A. Rhodes Arena', 'Coleman Coliseum', 'Elmore Gymnasium', 'Bartow Arena', 'Dunn-Oliver Acadome', 'SEFCU Arena', 'David L. Whitney Gymnasium', 'Bender Arena', 'George M. Holmes Convocation Center', 'McKale Memorial Center', 'Desert Financial Arena', 'Bud Walton Arena', 'Jack Stephens Center', 'K. L. Johnson Complex', 'First National Bank Arena', 'Christl Arena', 'Auburn Arena', 'Dunn Center', 'Worthen Arena', 'Ferrell Center', 'Curb Event Center', 'Moore Gymnasium', 'Binghamton University Events Center', 'ExtraMile Arena', 'Conte Forum', 'Case Gym', 'Stroh Center', 'Carver Arena', 'Marriott Center', 'Pizzitola Sports Center', 'Chace Athletic Center', 'Sojka Pavilion', 'Alumni Arena', 'Hinkle Fieldhouse', 'Robert A. Mott Gym', 'Icardo Center', 'Titan Gym', 'Matadome', 'Haas Pavilion', 'The Pavilion at ARC', 'Bren Events Center', 'Student Recreation Center Arena', 'UC Santa Barbara Events Center', 'John W. Pope, Jr. Convocation Center', 'Koessler Athletic Center', 'Farris Center', 'William H. Detrick Gymnasium', 'McGuirk Arena', 'Buccaneer Field House', 'Dale F. Halton Arena', 'McKenzie Arena', 'Emil and Patricia Jones Convocation Center', 'Fifth Third Arena', 'Littlejohn Coliseum', 'Wolstein Center', 'HTC Center', 'Cotterell Court', 'TD Arena', 'CU Events Center', 'Moby Arena', 'Francis S. Levien Gymnasium', 'Harry A. Gampel Pavilion', 'Physical Education Complex', 'Newman Arena', 'CHI Health Center Omaha', 'Leede Arena', 'John M. Belk Arena', 'University of Dayton Arena', 'Bob Carpenter Center', 'Memorial Hall', 'Magness Arena', 'Wintrust Arena[c]', 'Calihan Hall', 'Knapp Center', 'Daskalakis Athletic Center', 'Cameron Indoor Stadium', 'UPMC Cooper Fieldhouse', 'Williams Arena at Minges Coliseum', 'Freedom Hall Civic Center', 'Lantz Arena', 'Alumni Coliseum', 'George Gervin GameAbove Center', 'Reese Court', 'Schar Center', 'Ford Center', 'Webster Bank Arena at Harbor Yard', 'Rothman Center',  "Stephen C. O'Connell Center ", 'Al Lawson Center', 'FAU Arena', 'Alico Arena', 'Ocean Bank Convocation Center', 'Donald L. Tucker Center', 'Rose Hill Gym', 'Save Mart Center', 'Timmons Arena', 'Paul Porter Arena', 'EagleBank Arena', 'Charles E. Smith Center', 'Capital One Arena', 'Stegeman Coliseum', 'Hanner Fieldhouse', 'GSU Sports Arena', 'McCamish Pavilion', 'McCarthey Athletic Center', 'Fredrick C. Hobdy Assembly Center', 'Grand Canyon University Arena', 'Resch Center', 'Hampton Convocation Center', 'Chase Family Arena', 'Lavietes Pavilion', 'Stan Sheriff Center', 'Nido & Mariana Qubein Arena and Conference Center', 'Mack Sports Complex', 'Hart Center', 'Fertitta Center', 'Sharp Gymnasium', 'Burr Gymnasium', 'ICCU Arena', 'Holt Arena', 'State Farm Center', 'Credit Union 1 Arena', 'Redbird Arena', 'Alice P. McDermott Convocation Center', 'Simon Skjodt Assembly Hall', 'Hulman Center', 'Hynes Athletics Center', 'Carver–Hawkeye Arena', 'Hilton Coliseum', 'Indiana Farmers Coliseum', 'Williams Center', 'Swisher Gym', 'Pete Mathews Coliseum', 'Atlantic Union Bank Center', 'Allen Fieldhouse', 'Fred Bramlage Coliseum', 'KSU Convocation Center', 'Memorial A & C Center', 'Rupp Arena', 'Tom Gola Arena', 'Kirby Sports Center', 'Montagne Center', 'Stabler Arena', 'Liberty Arena', 'Allen Arena', 'The Walter Pyramid', 'Steinberg Wellness Center', 'Willett Hall', 'KFC Yum! Center', 'Joseph J. Gentile Arena', 'Reitz Arena', 'Cross Insurance Center', 'Draddy Gymnasium', 'McCann Arena', 'Fiserv Forum', 'Cam Henderson Center', 'Xfinity Center', 'William P Hytche Athletic Center', 'Mullins Center', 'Costello Athletic Center', 'FedExForum', 'Hawkins Arena', 'Watsco Center', 'John D. Millett Hall', 'Crisler Center', 'Jack Breslin Student Events Center', 'Murphy Center', 'UW–Milwaukee Panther Arena', 'Williams Arena', 'Humphrey Coliseum', 'Harrison HPER Complex', 'MIzzou Arena', 'JQH Arena', 'McAlister Field House', 'The Legacy Center', 'The Pavilion at Ole Miss', 'OceanFirst Bank Center', 'Dahlberg Arena', 'Brick Breeden Fieldhouse', 'Ellis Johnson Arena', 'Talmadge L. Hill Field House', 'Knott Arena', 'CFSB Center', 'Alumni Hall', 'Pinnacle Bank Arena', 'Baxter Arena', 'Lawlor Events Center', 'Lundholm Gym', 'The Pit', 'Pan American Center', 'Lakefront Arena', 'Gallagher Center', 'David R. Stopher Gym', 'Wellness and Events Center', 'Echols Hall', 'Corbett Sports Center', 'Betty Engelstad Sioux Center', 'Scheels Center', 'UNT Coliseum', 'Matthews Arena', 'Walkup Skydome', 'Bank of Colorado Arena', 'Convocation Center', 'McLeod Center', 'BB&T Arena', 'Welsh-Ryan Arena', 'Prather Coliseum', 'Purcell Pavilion at the Joyce Center',  "Athletics Center O'rena ", 'Convocation Center', 'Value City Arena', 'Lloyd Noble Center', 'Gallagher-Iba Arena', 'Chartway Arena', 'Mabee Center', 'Matthew Knight Arena', 'Gill Coliseum', 'Alex G. Spanos Center', 'Bryce Jordan Center', 'Palestra', 'Firestone Fieldhouse', 'Petersen Events Center', 'Chiles Center', 'Viking Pavilion', 'William J. Nicks Building', 'Templeton Physical Education Center', 'Jadwin Gymnasium',  "Dunkin' Donuts Center ", 'Mackey Arena',  "People's United Center ", 'Dedmon Center', 'Ryan Center', 'Tudor Fieldhouse', 'Robins Center', 'Alumni Gymnasium', 'UPMC Events Center',  "Jersey Mike's Arena", 'Hornets Nest', 'William H. Pitt Center', 'Michael J. Hagan \'85 Arena', 'Chaifetz Arena', 'University Credit Union Pavilion', 'Bernard Johnson Coliseum', 'Pete Hanna Center', 'Jenny Craig Pavilion', 'Viejas Arena at Aztec Bowl', 'The Sobrato Center', 'Provident Credit Union Event Center', 'Leavey Center', 'Redhawk Center', 'Prudential Center', 'Times Union Center', 'Mitchell Center', 'Colonial Life Arena', 'Sanford Coyote Sports Center', 'Yuengling Center', 'Reilly Center', 'Generoso Pope Athletic Complex', 'Madison Square Garden', 'Maples Pavilion', 'Edmunds Center', 'Island Federal Credit Union Arena', 'Carrier Dome', 'Liacouras Center', 'Thompson-Boling Arena', 'Gentry Complex', 'Eblen Center', 'Frank Erwin Center', 'Reed Arena', 'American Bank Center Arena', 'Schollmaier Arena', 'Health & PE Center', 'Strahan Arena', 'United Supermarkets Arena', 'Savage Arena', 'SECU Arena', 'Trojan Arena', 'Fogelman Arena in Devlin Fieldhouse', 'Donald Reynolds Center', 'Pauley Pavilion', 'Jon M. Huntsman Center', 'Smith Spectrum', 'UCCU Center', 'Athletics–Recreation Center', 'Memorial Gymnasium', 'Roy L Patrick Gymnasium', 'Finneran Pavilion[f]', 'John Paul Jones Arena', 'Siegel Center', 'Cameron Hall', 'Cassell Coliseum', 'Spiro Sports Center', 'Lawrence Joel Veterans Memorial Coliseum', 'Alaska Airlines Arena', 'Wallis Beasley Performing Arts Coliseum', 'Dee Events Center', 'WVU Coliseum', 'Charles Koch Arena', 'Kaplan Arena', 'Winthrop Coliseum', 'Kohl Center', 'Jerry Richardson Indoor Stadium', 'Ervin J. Nutter Center', 'Arena-Auditorium', 'Cintas Center', 'John J. Lee Amphitheater', 'Beeghly Center', 'Addition Financial Arena', 'Allen County War Memorial Coliseum', 'Cajundome', 'Fant–Ewing Coliseum', 'Pete Maravich Assembly Center', 'Thomas Assembly Center', 'Gersten Pavilion', 'Chesapeake Employers Insurance Arena', 'Swinney Recreation Center', 'Thomas & Mack Center', 'Dean Smith Center', 'Kimmel Arena', 'McDougald–McLendon Gymnasium', 'Greensboro Coliseum', 'PNC Arena', 'Trask Coliseum', 'UNF Arena', 'DeGol Arena', 'Yanitelli Center', 'SHM Memorial Center', 'G. B. Hodge Center', 'Frost Arena', 'Show Me Center', 'University Center', 'F. G. Clark Center', 'Galen Center', 'Banterra Center', 'Vadalabene Center', 'Moody Coliseum', 'Reed Green Coliseum', 'America First Event Center', 'William R. Johnson Coliseum', 'Kathleen and Tom Elam Center', 'College Park Center', 'Don Haskins Center', 'UTRGV Fieldhouse', 'UTSA Convocation Center', 'Ramsey Center', 'Western Hall', 'E.A. Diddle Arena', 'University Arena in Read Fieldhouse']




class Scraper:
    

    def getGameLog(self, teamID, year):
        print("https://www.sports-reference.com/cbb/schools/" + str(teamID) + "/men/" + str(year) + "-gamelogs-advanced.html")
        Adv = pd.DataFrame(pd.read_html("https://www.sports-reference.com/cbb/schools/" + str(teamID) + "/men/" + str(year) + "-gamelogs-advanced.html")[0])
        Reg = pd.DataFrame(pd.read_html("https://www.sports-reference.com/cbb/schools/" + str(teamID) + "/men/" + str(year) + "-gamelogs.html")[0])
        Adv.columns = Adv.columns.get_level_values(1)

        Adv.drop(Adv.columns.values[[17,22]], axis=1, inplace=True)

        for w in range(1,5):
            Adv.columns.values[-w] = "Def_" + Adv.columns.values[-w]

        Reg.columns = Reg.columns.get_level_values(1)
        Reg.columns.values[2] = "H/A"
        Reg["H/A"] = Reg["H/A"].fillna("H")

        for i in range(16):
            Reg.columns.values[i + 24] = "Opp_" + Reg.columns.values[i + 24]


        Reg = Reg.join(Adv[Adv.columns.values[7:]])


        Reg.columns.values[3] = "Opp_ID"


        Reg.drop(Reg.columns.values[23], axis=1, inplace=True)
        Reg = Reg.dropna()

        return Reg



    def getAvgs(self, df, date_index, limit):
        if date_index >= limit:
            meansDF = df[df.columns.values[5:]].iloc[(date_index - limit):date_index]
            meansDF = meansDF.apply(pd.to_numeric, errors='coerce').dropna()
            means = meansDF.median()
            tempDF = pd.DataFrame([means.values], columns=df.columns.values[5:])
            tempDF["Games Played"] = [date_index + 1]
            #tempDF["Date"] = df.loc[date_index][1]
            return tempDF
        else:
            meansDF = df[df.columns.values[5:]].iloc[:date_index]
            meansDF = meansDF.apply(pd.to_numeric, errors='coerce').dropna()
            means = meansDF.median()
            tempDF = pd.DataFrame([means.values], columns=df.columns.values[5:])
            tempDF["Games Played"] = [date_index + 1]
            #tempDF["Date"] = df.loc[date_index][1]
            return tempDF
        

    def combineData(self, homeDf, awayDf, n,home_res,away_res, spread=100):

        home_cols = homeDf.columns.values.tolist()
        away_cols = awayDf.columns.values.tolist()

        home_data = homeDf.iloc[0].tolist()
        away_data = awayDf.iloc[0].tolist()

        for i in range(len(home_cols)):
            home_cols[i] = "Home_" + home_cols[i]

        for r in range(len(away_cols)):
            away_cols[r] = "Away_" + away_cols[r]

        final_cols = home_cols + away_cols
        final_data = home_data + away_data

        tempDF = pd.DataFrame([final_data], columns=final_cols)

        tempDF['N'] = n
        if spread != 100:
            tempDF['Home_Spread'] = spread

        tempDF['Home_Result'] = home_res
        tempDF["Away_Result"] = away_res

        return tempDF
    

    def getGameEntry(self, data1, data2, team1, team2, date):

        tournament_starts = {
            "2023" : 16,
            "2022" : 17,
            "2021" : 18,
            "2020" : 19,
            "2019" : 21,
            "2018" : 15,
            "2017" : 16,
            "2016" : 17,
            "2015" : 19,
            "2014" : 20,
            "2013" : 21,
            "2012" : 15,
            "2011" : 17,
            "2010" : 18
        }

        tournament_game = 0

        if (int(date[5:7]) == 3 or int(date[5:7]) == 4) and int(date[8:]) >= tournament_starts[date[0:4]]:
            tournament_game = 1

        #data1 = self.getGameLog(team1, 2023)
        #data2 = self.getGameLog(team2, 2023)
            
        #display(data1)
        #print(date)

        date_index1 = data1.index[data1['Date'] == date].tolist()[0]
        date_index2 = data2.index[data2['Date'] == date].tolist()[0]

        avgs1 = self.getAvgs(data1, date_index1, 100)

        avgs2 = self.getAvgs(data2, date_index2, 100)

        home_avgs = avgs1
        away_avgs = avgs2

        res1 = data1.loc[date_index1][5]
        res2 = data2.loc[date_index2][5]

        n = 0

        site = data1.loc[date_index1][2]

        if site == 'A':
            away_avgs = avgs1
            home_avgs = avgs2
            temp = res2
            res2 = res1
            res1 = temp
            name_temp = team2
            team2 = team1
            team1 = name_temp
            
            
        elif site == 'N':
            n = 1
            if avgs1["Tm"].iloc[0] < avgs2["Tm"].iloc[0]:
                away_avgs = avgs1
                home_avgs = avgs2
                temp = res2
                res2 = res1
                res1 = temp
                name_temp = team2
                team2 = team1
                team1 = name_temp




        home_result = res1
        away_result = res2

        data_combined = self.combineData(home_avgs, away_avgs, n, home_result, away_result)

        data_combined["Home_Team_Name"] = [team1]
        data_combined["Away_Team_Name"] = [team2]
        data_combined["Date"] = [date]
        data_combined["Tournament_Game"] = [tournament_game]

        return data_combined
    

    def getDailyGames(self, date):


        def drop_rank(entry):
            arr = str(entry).split(" ")

            try:
                rank = int(arr[0])
                new_name = ""

                for i in range(1, len(arr)):
                    new_name = new_name + arr[i]

                return new_name

            except:
                return entry
            

        cbs_year = str(date.year)
        cbs_month = date.month
        cbs_day = date.day

        if cbs_month < 10:
            cbs_month = "0" + str(cbs_month)
        else:
            cbs_month = str(cbs_month)

        if cbs_day < 10:
            cbs_day = "0" + str(cbs_day)
        else:
            cbs_day = str(cbs_day)
        
        cbs_date = cbs_year + cbs_month + cbs_day

        print("https://www.cbssports.com/college-basketball/schedule/ALL/" + str(cbs_date) + "/")

        daily_games = pd.DataFrame(pd.read_html("https://www.cbssports.com/college-basketball/schedule/ALL/" + str(cbs_date) + "/")[0])

        daily_games = daily_games.drop('Result', axis=1)

        daily_games["Away"] = daily_games["Away"].apply(drop_rank)
        daily_games["Home"] = daily_games["Home"].apply(drop_rank)

        return daily_games
    

    def getYearlyLogs(self, year):

        team_logs_now = []

        for team in final_sr:
            time.sleep(4)
            try:
                team_logs_now.append(self.getGameLog(team, year))
            except:
                team_logs_now.append(pd.DataFrame())

            print(str(final_sr.index(team)) + "/350")

        return team_logs_now
    

    def getData(self, year_start, year_end):

        database = pd.DataFrame()

        for year in range(year_start, year_end):

            yearly_logs = self.getYearlyLogs(year)

            date = datetime(year - 1, 11, 1).date()

            while date.month < 5 or date.year != year:

                games_for_date = pd.DataFrame()

                try:
                
                    games_for_date = self.getDailyGames(date)

                except:
                    pass

                sr_year = str(date.year)
                sr_month = date.month
                sr_day = date.day

                if sr_month < 10:
                    sr_month = "0" + str(sr_month)
                else:
                    sr_month = str(sr_month)

                if sr_day < 10:
                    sr_day = "0" + str(sr_day)
                else:
                    sr_day = str(sr_day)

                sr_date = sr_year + "-" + sr_month + "-" + sr_day

                for g in range(len(games_for_date)):

                    try:
                        cbs_home_team = games_for_date.iloc[g][0]
                        cbs_away_team = games_for_date.iloc[g][1]

                        home_ind = final_cbs.index(cbs_home_team)
                        away_ind = final_cbs.index(cbs_away_team)

                        home_team = final_sr[home_ind]
                        away_team = final_sr[away_ind]

                        home_log = yearly_logs[home_ind]
                        away_log = yearly_logs[away_ind]

                        entry = self.getGameEntry(home_log, away_log, home_team, away_team, sr_date)

                        try:
                            database = pd.concat([database, entry], axis=0)
                        except:
                            database = entry
                    except:
                        pass

                date = date + timedelta(days=1)
                print(str(date.month) + "/" + str(date.day) + "/" + str(date.year) + ": " + str(len(database)))


        return database
                        
                    



