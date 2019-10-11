# Data
a  section  that  describes  the  data source(s),  the format/contents  of  the  data, the  rights  associated  with  the data;
(Pretty Sure We Describe the Raw Data not the cleaned)

### Bitcoin tweets + prices
Usage information: license - 'cc0:public domain' CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
"The person who associated a work with this deed has dedicated the work to the public domain by waiving all of his or her rights to the work worldwide under copyright law, including all related and neighboring rights, to the extent allowed by law.
You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission." 
The license for the data set is listed under CC0:Public Domain which 'You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission.'

This data was from Kaggle, uploaded on 2019-02-13 by Jaime Badiola who used the github ‘GetOldTweets’ to download the 17.7 million + tweets related to bitcoin (from 2017-08-01 to 2019-01-22) from which data was extracted to form the dataset. The most recent update, which is the version used for this project, was Version 2. It was updated on 2019-06-15 and made sentiment data more accurate by filtering out bot and spam tweets and eliminating their sentiment scores therefore average sentiment is not skewed by these tweets. The data has 12937 rows (including headers) and 16 columns. The data is presented in hourly periods with each row containing data on the number of tweets and the sentiment data associated with those tweets within the same time period. The creater assigned a sentiment score to each tweet using the library VaderSentiment which is used to calculate how positive or negative 'social media texts' are with a more postive tweet obtaining a higher postive number, neutral tweets obtaining a score of 0 and negative tweets being lower and lower negative values the more negative the tweet is.  assings a numerical value to h, where numeric sclae with 0 beign neutral and - beeing native and + values corresponding to posistive setniments. score between +1 to -1
The dataset also contains 6 columns of bitcoin price information for each hourly time period.

Brief Description for Each 
Date: the starting time of the 1 hr time span for which all data in a row corresponds to in 24 hour time, format: yyyy-mm-dd hh:mm:ss
Compound_Score: average of sentiment scores for all tweets after filtering out bot and spam tweets
n: total number of tweets, includes bot and spam tweets
Count_Negatives: total number of negative tweets, doesnt include bot/span tweets
Count_Positives: total number of positive tweets, doesnt include bot/span tweets
Count_Neutrals: total number of neutral tweets, doesnt include bot/span tweets
Sent_Negatives: average of all negative sentiment scores only, doesnt include bot/span tweets
Sent_Positives: average of all positive sentiment scores only, doesnt include bot/span tweets
Count_News: number of tweets that contains a link
Count_Bots: number of tweets classified as bots
Open: first price during the 1 hr time span, units:
High: highest price bitcoin had during the 1 hr time span, units:
Low: lowest price bitcoin had during the 1 hr time span, units:
Close: last price during during the 1 hr time span, units:
Volume (BTC): the amount of bitcoin that underwent transactions, units: BTC
Volume (Currency): the amount of bitcoin that underwent transactions, units: dollars  (currecny unspecified but seems to be smth worth higher than USD )
 
Strenghts and weaknesses: Some days have missing data on tweets Setniment analysis obc has room for issues such as sarcasm spelling mistakes etc and since op did not provide list of 30 phrases we cannot comment on validity, i think spam tweets are filteres out (?)
doesnt really give us a time zone. doesnt specify if fitering out tweets to avoid skewing sentiment data also filtered out tweets from number of tweets, presumably just downloaded all tweets that said "bitcoin'

After analyzing individual messages, I have found some messages do not talk about bitcoin, or they only mention other cryptocurrencies like bitcoin gold, other messages try to sell you bitcoin, or promoting their channels/content trying to get subscribers. Other messages were classified as bots in the hashtag and some others constantly informed about the price of bitcoin and other finantial mesurments. All these messages are filtered, and classified as bots/spam. The sentiment of these messages is eliminated, but we keep the information as a volume mesarument in Count_bots.
 
I added about 30 expressions  and words to the dictionary. To score the expressions I used the same methodology as the authors described in their paper.
 

### Chicago Crime
from chicago "This dataset reflects reported incidents of crime  that occurred in the City of Chicago from 2001 to present, minus the most recent seven days. Data is extracted from the Chicago Police Department's CLEAR (Citizen Law Enforcement Analysis and Reporting) system. In order to protect the privacy of crime victims, addresses are shown at the block level only and specific locations are not identified."

all location shifted for partial redaction but block remains same

from a constantly updated downloaded 22 col 2099624 (incl header),each reported incident of crime  each row is data for a single crime has its own ID and case number 
date and time of the crime which stes smtimes just an estimate , different formats for location thats with more sepcific forms its partially redacted so that the block remainds the same ,and duscriotion of fcrime through different several forms of classification for the type of crime. whether or not dometisc or if an arrest was made and the date when the data fro that row was last updated

22 col 2099624 (incl header)  2017-08-01
Information about location (slightly off or generalised as a form of redaction) as longtidude and latitude as well as x coordinates and
9/28/2019   10/05/2019
04/04/2012       2/10/2016 02/04/2016


ID: unique identifier,  
Case Number: Chicago Police Department Records Division  Number also unique 
Date: date + time sometimes just an estimate, mm:dd:yyyy 12hr amp/pm h:m:s 
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
Updated On: date and time,  mm:dd:yyyy 12hr amp/pm h:m:s 
Latitude, 
Longitude, 
Location: combines long ang lat,

 
used and manipulated provded that the following disclaimer is included whenebver

liability/disclaimer: The City of Chicago (“City”) voluntarily provides the data on this website as a service to the public. 
Any user of this website providing any software application, or other secondary or derivative application using data supplied at this website shall do the following:
Include the following disclaimer at the site where the software application, or other secondary or derivative application can be accessed or downloaded:
“This site provides applications using data that has been modified for use from its original source, www.cityofchicago.org, the official website of the City of Chicago.  The City of Chicago makes no claims as to the content, accuracy, timeliness, or completeness of any of the data provided at this site.  The data provided at this site is subject to change at any time.  It is understood that the data provided at this site is being used at one’s own risk.”
Comply with any additional Terms of Use set forth by the City agency or department providing data used by the software application, or other secondary or derivative application, including, without limitation, requirements to include additional citations or disclaimers at the site where the application can be accessed or downloaded. 

strenghts weakness: a lot of detail in columns,
"These crimes may be based upon preliminary information supplied to the Police Department by the reporting parties that have not been verified. The preliminary crime classifications may be changed at a later date based upon additional investigation and there is always the possibility of mechanical or human error. Therefore, the Chicago Police Department does not guarantee (either expressed or implied) the accuracy, completeness, timeliness, or correct sequencing of the information and the information should not be used for comparison purposes over time. The Chicago Police Department will not be responsible for any error or omission, or for the use of, or the results obtained from the use of this information" 
 (with the exception of murders where data exists for each victim) excpet in case of murders where there r multiple victims, then data is for each victim

### Gold Prices
https://www.quandl.com/data/WGC-Gold-Prices?page=3
‘This database contains all of the available indicators published by the World Gold Council, included is data on the trading prices on all the major gold trading countries.
This is open data that we’ve sourced and made freely available to you.’

2 x 2542 incl header  
Date	Value 2019-09-27 TO 2010-01-01 yyyy:mm:dd

From quandl which has compiled data from https://www.gold.org/goldhub/data/gold-prices. States that ‘If you are using free data from Quandl, you have to adhere to the terms and conditions of the original source of the data, including their terms for citing/redistributing data.’ https://help.quandl.com/article/362-what-are-the-terms-of-use-for-free-data-feeds
 
Use of this website: This Website and the information and materials on this Website are provided for general informational and educational purposes only.
You are permitted to save, display or print out information contained on this Website only for your personal, non-commercial use.

USD per troy ounce  | Sources: ICE Benchmark Administration, London Metal Exchange, Shanghai Gold Exchange, World Gold Council;

ADV AND DIS: simple


# References
https://creativecommons.org/publicdomain/zero/1.0/
https://www.kaggle.com/jaimebadiola/bitcoin-tweets-and-price/version/2
https://medium.com/analytics-vidhya/simplifying-social-media-sentiment-analysis-using-vader-in-python-f9e6ec6fc52f

https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2/data
https://www.chicago.gov/city/en/narr/foia/data_disclaimer.html

https://www.quandl.com/data/WGC-Gold-Prices?page=3
https://help.quandl.com/article/362-what-are-the-terms-of-use-for-free-data-feeds
https://www.gold.org/goldhub/data/gold-prices 
https://www.gold.org/terms-and-conditions 
