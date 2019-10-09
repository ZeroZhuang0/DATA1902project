# Bitcoin, Gold & Crime

## Data sources
https://www.kaggle.com/jaimebadiola/bitcoin-tweets-and-price/downloads/bitcoin-tweets-and-price.zip/2
https://www.quandl.com/data/WGC/GOLD_DAILY_USD-Gold-Prices-Daily-Currency-USD
https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2/data

To Do/Details (more info abt cleaning and prelim analysis at bottom)

•Submit pdf. This should be submitted through  Turnitin,  via  the  link  in  the Canvassite.  The  report  should be targeted  at  a  tutor  or  lecturer  whose  goal  is  to  see  what  you  did,  so  they can allocate a mark. The report should have a three-section structure that corresponds  to  the  marking  scheme:  
data, that you have clearly shown where you obtained the data,  that  you  have  described  the  contents  of  the  dataset  (explaining clearly  both  the  format,  and  the  meaning  of  the  various  aspects)
your description shows clearly that you have appropriate rights to use the data in the ways that you do use it, and  your  explanation  shows  sensible  reflection  of  the  strengths  and limitations  of  the  data  that  you  obtained. 
to be considered for full marks,  there  must  be  a  real  challenge  in  relating  the  data  values  in  the threesets.  It  is  not  enough  to  simply  take  datasets  that  use  the  same definitions of attributes etc, nor is it ok just to use unrelated data, where there is not connection made across the information. (maybe in introduction explain potential link between data sets)

### Intro

# Data
a  section  that  describes  the  data source(s),  the format/contents  of  the  data, the  rights  associated  with  the data;
(Pretty Sure We Describe the Raw Data not the cleaned)

### Bitcoin tweets + prices
Usage information: license - cc0:public domain CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
"The person who associated a work with this deed has dedicated the work to the public domain by waiving all of his or her rights to the work worldwide under copyright law, including all related and neighboring rights, to the extent allowed by law.
You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission." 

The data was from Kaggle, uploaded on 2019-02-13 by Jaime Badiola who used the github ‘GetOldTweets’ to download the 17.7 million + tweets from 2017-08-02(01) to 2019-01-22 with which  order to create the dataset. The most recent update was Version 2 on 2019-06-15. (which is what was used in this project) the Data has 12936 rows (not including header) and 14 columns. the data is presented in hourly periods with onformation about the number of tweets in that period and also sentiment data associated with those tweets  the creater gave  sentiment score was assigned to each tweet using library VaderSentiment which assings a numerical value to h, where numeric sclae with 0 beign neutral and - beeing native and + values corresponding to posistive setniments. Other than information on tweets the dataset also contains bitcoin information at the same hourly time periods the tweets are sorted in.


Used GetOldTweets to download all tweets of the period. Jaime Badiola
2017-08-02 to 2019-01-22
Date created 2019-02-13 Last updated 2019-06-15 Current version Version 2
 
Small description
 I collected over 17.7 million tweets  This dataset contains the average sentiment of all tweets about bitcoin  How did I do sentiment analysis? library VaderSentiment. I added about 30 expressions  and words to the dictionary. To score the expressions I used the same methodology as the authors described in their paper.It also contains the financial data of bitcoin for that same period.
 
 
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

ID: unique identifier,  
Case Number: Chicago Police Department Records Division Number also unique, 
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
- Historical Wards 2003-2015, Zip Codes,	Community Areas,	Census Tracts,	Wards,	Boundaries - ZIP Codes,	Police Districts, Police Beats

22 col  6,981,560(???) 6,982,341
Information about location (slightly off or generalised as a form of redaction) as longtidude and latitude as well as x coordinates and 

liability/disclaimer: The City of Chicago (“City”) voluntarily provides the data on this website as a service to the public. 
Any user of this website providing any software application, or other secondary or derivative application using data supplied at this website shall do the following:
Include the following disclaimer at the site where the software application, or other secondary or derivative application can be accessed or downloaded:
“This site provides applications using data that has been modified for use from its original source, www.cityofchicago.org, the official website of the City of Chicago.  The City of Chicago makes no claims as to the content, accuracy, timeliness, or completeness of any of the data provided at this site.  The data provided at this site is subject to change at any time.  It is understood that the data provided at this site is being used at one’s own risk.”
Comply with any additional Terms of Use set forth by the City agency or department providing data used by the software application, or other secondary or derivative application, including, without limitation, requirements to include additional citations or disclaimers at the site where the application can be accessed or downloaded. 

strenghts weakness: a lot of detail in columns,
"These crimes may be based upon preliminary information supplied to the Police Department by the reporting parties that have not been verified. The preliminary crime classifications may be changed at a later date based upon additional investigation and there is always the possibility of mechanical or human error. Therefore, the Chicago Police Department does not guarantee (either expressed or implied) the accuracy, completeness, timeliness, or correct sequencing of the information and the information should not be used for comparison purposes over time. The Chicago Police Department will not be responsible for any error or omission, or for the use of, or the results obtained from the use of this information"

Gold Prices (Now Redundant)
https://www.quandl.com/data/WGC-Gold-Prices?page=3
‘This database contains all of the available indicators published by the World Gold Council, included is data on the trading prices on all the major gold trading countries.
This is open data that we’ve sourced and made freely available to you.’

From quandl which has compiled data from https://www.gold.org/goldhub/data/gold-prices. States that ‘If you are using free data from Quandl, you have to adhere to the terms and conditions of the original source of the data, including their terms for citing/redistributing data.’ 
 
Use of this website: This Website and the information and materials on this Website are provided for general informational and educational purposes only.
You are permitted to save, display or print out information contained on this Website only for your personal, non-commercial use.

USD per troy ounce  | Sources: ICE Benchmark Administration, London Metal Exchange, Shanghai Gold Exchange, World Gold Council;

investing.com
Investing.com is an online data and news website that provides financial information.

under 'Use Our Data' Our services are provided for free and you are welcome to use the information and tools we provide, just please make sure to include full disclosure to Investing.com brand, logo, watermark and links if possible.

Risk Disclosure: Trading in financial instruments and/or cryptocurrencies involves high risks including the risk of losing some, or all, of your investment amount, and may not be suitable for all investors. Prices of cryptocurrencies are extremely volatile and may be affected by external factors such as financial, regulatory or political events. Trading on margin increases the financial risks.
Before deciding to trade in financial instrument or cryptocurrencies you should be fully informed of the risks and costs associated with trading the financial markets, carefully consider your investment objectives, level of experience, and risk appetite, and seek professional advice where needed.
Fusion Media would like to remind you that the data contained in this website is not necessarily real-time nor accurate. The data and prices on the website are not necessarily provided by any market or exchange, but may be provided by market makers, and so prices may not be accurate and may differ from the actual price at any given market, meaning prices are indicative and not appropriate for trading purposes. Fusion Media and any provider of the data contained in this website will not accept liability for any loss or damage as a result of your trading, or your reliance on the information contained within this website.
It is prohibited to use, store, reproduce, display, modify, transmit or distribute the data contained in this website without the explicit prior written permission of Fusion Media and/or the data provider. All intellectual property rights are reserved by the providers and/or the exchange providing the data contained in this website.
Fusion Media may be compensated by the advertisers that appear on the website, based on your interaction with the advertisements or advertisers.


Cleaning
a  section  that  describes  the  initial  transformation  and  cleaning  that you  did  (include  here  the parts  of  Python code  that  you  used,  or  a description  that  is  detailed  enough  to  be followed);  

Preliminary Analysis
and  a  section  that describes  and  explains some simple  analysis  that  you  have  done  (again, show the code and also the output of the analysis). 

There is no required minimum or maximum length for the report; write whatever is needed to show the reader that you have earned the marks, and don’t say more than that!

#Reference
https://creativecommons.org/publicdomain/zero/1.0/
https://www.kaggle.com/jaimebadiola/bitcoin-tweets-and-price/downloads/bitcoin-tweets-and-price.zip/2
