# Data
a  section  that  describes  the  data source(s),  the format/contents  of  the  data, the  rights  associated  with  the data;
(Pretty Sure We Describe the Raw Data not the cleaned)

### Bitcoin tweets + prices
Usage information: license - cc0:public domain CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
"The person who associated a work with this deed has dedicated the work to the public domain by waiving all of his or her rights to the work worldwide under copyright law, including all related and neighboring rights, to the extent allowed by law.
You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission." 

The data was from Kaggle, uploaded on 2019-02-13 by Jaime Badiola who used the github ‘GetOldTweets’ to download the 17.7 million + tweets from 2017-08-02(01) to 2019-01-22 with which  order to create the dataset. The most recent update was Version 2 (Tweets filtered to avoid bots sentiment skewing averages) on 2019-06-15. (which is what was used in this project) the Data has 12936 rows (not including header) and 14 columns. the data is presented in hourly periods with onformation about the number of tweets in that period and also sentiment data associated with those tweets  the creater gave  sentiment score was assigned to each tweet using library VaderSentiment which assings a numerical value to h, where numeric sclae with 0 beign neutral and - beeing native and + values corresponding to posistive setniments. Other than information on tweets the dataset also contains bitcoin information at the same hourly time periods the tweets are sorted in.
 
I added about 30 expressions  and words to the dictionary. To score the expressions I used the same methodology as the authors described in their paper.
 
Date: the start time of the 1 hr Time span for which all data in a row corresponds to date yyyy-mm-dd hh:mm:ss 24 hour time
Compound_Score:Average of all sentiment scores. 
n:Total volume of tweets
Count_Negatives: Total volume of negative tweets
Count_Positives: Total volume of positive tweets
Count_Neutrals: Total volume of neutral tweets
Sent_Negatives :Average of Negative sentiment only
Sent_Positives: Average of Positive sentiment only
Open:Start of the price
High:The highest price bitcoin had during the period (1h)
Low:The lowest price bitcoin had during the period (1h)
Close:The last price during the period (1h)
Volume (BTC):The volume of bitcoin in bitcoins that was in transactions
Volume (Currency):The volume of bitcoin in dollars 
 
Strenghts and weaknesses: Some days have missing data on tweets Setniment analysis obc has room for issues such as sarcasm spelling mistakes etc and since op did not provide list of 30 phrases we cannot comment on validity, i think spam tweets are filteres out (?)
doesnt really give us a time zone 

### Chicago Crime
from chicago "This dataset reflects reported incidents of crime (with the exception of murders where data exists for each victim) that occurred in the City of Chicago from 2001 to present, minus the most recent seven days. Data is extracted from the Chicago Police Department's CLEAR (Citizen Law Enforcement Analysis and Reporting) system. In order to protect the privacy of crime victims, addresses are shown at the block level only and specific locations are not identified."

constantly updated

ID: unique identifier,  
Case Number: Chicago Police Department Records Division  Number also unique, 
Date: date + time sometimes just an estimate, 
Block: partially redacted address such that block remains the same, 
IUCR: Illinois Uniform Crime Reporting (IUCR) codes are four digit codes that law enforcement agencies use to classify criminal incidents when taking individual reports is directly linked to primary tyep and descriptionn, 
Primary Type: primary description of IUCR, 
Description: secondary description of IUCR primary description subcategory, 
Location Description: description of location like location type, 
Arrest: T/F if arrest was made, 
Domestic: T/F if classified as domestic related by Illnois Domestic Violence Act, 
Beat: beat where it occured smallest police geographic area, 
District: police district , 
Ward: ward a city council district, 
Community Area: community area there are 77 in chicago, 
FBI Code: calssification code under National Incident-Based Reporting System (NIBRS), 
X Coordinate, 
Y Coordinate, 
Year, 
Updated On: date and time, 
Latitude, 
Longitude, 
Location: combines long ang lat,

all location shifted for partial redaction but block remains same
DD/MM/YYY 12hr amp/pm h:m:s 

22 col 2099624 (incl header)  2017-08-01
Information about location (slightly off or generalised as a form of redaction) as longtidude and latitude as well as x coordinates and 

liability/disclaimer: The City of Chicago (“City”) voluntarily provides the data on this website as a service to the public. 
Any user of this website providing any software application, or other secondary or derivative application using data supplied at this website shall do the following:
Include the following disclaimer at the site where the software application, or other secondary or derivative application can be accessed or downloaded:
“This site provides applications using data that has been modified for use from its original source, www.cityofchicago.org, the official website of the City of Chicago.  The City of Chicago makes no claims as to the content, accuracy, timeliness, or completeness of any of the data provided at this site.  The data provided at this site is subject to change at any time.  It is understood that the data provided at this site is being used at one’s own risk.”
Comply with any additional Terms of Use set forth by the City agency or department providing data used by the software application, or other secondary or derivative application, including, without limitation, requirements to include additional citations or disclaimers at the site where the application can be accessed or downloaded. 

strenghts weakness: a lot of detail in columns,
"These crimes may be based upon preliminary information supplied to the Police Department by the reporting parties that have not been verified. The preliminary crime classifications may be changed at a later date based upon additional investigation and there is always the possibility of mechanical or human error. Therefore, the Chicago Police Department does not guarantee (either expressed or implied) the accuracy, completeness, timeliness, or correct sequencing of the information and the information should not be used for comparison purposes over time. The Chicago Police Department will not be responsible for any error or omission, or for the use of, or the results obtained from the use of this information"

### Gold Prices
https://www.quandl.com/data/WGC-Gold-Prices?page=3
‘This database contains all of the available indicators published by the World Gold Council, included is data on the trading prices on all the major gold trading countries.
This is open data that we’ve sourced and made freely available to you.’

2 x 2542 incl header  
Date	Value 2019-09-27 TO 2010-01-01

From quandl which has compiled data from https://www.gold.org/goldhub/data/gold-prices. States that ‘If you are using free data from Quandl, you have to adhere to the terms and conditions of the original source of the data, including their terms for citing/redistributing data.’ https://help.quandl.com/article/362-what-are-the-terms-of-use-for-free-data-feeds
 
Use of this website: This Website and the information and materials on this Website are provided for general informational and educational purposes only.
You are permitted to save, display or print out information contained on this Website only for your personal, non-commercial use.

USD per troy ounce  | Sources: ICE Benchmark Administration, London Metal Exchange, Shanghai Gold Exchange, World Gold Council;

ADV AND DIS: simple
