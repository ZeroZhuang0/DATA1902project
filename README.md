# Bitcoin, Gold & Crime

## Data sources
https://www.kaggle.com/jaimebadiola/bitcoin-tweets-and-price/downloads/bitcoin-tweets-and-price.zip/2
https://www.quandl.com/data/WGC/GOLD_DAILY_USD-Gold-Prices-Daily-Currency-USD
https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2/data

•Submit pdf. This should be submitted through  Turnitin,  via  the  link  in  the Canvassite.  The  report  should be targeted  at  a  tutor  or  lecturer  whose  goal  is  to  see  what  you  did,  so  they can allocate a mark. The report should have a three-section structure that corresponds  to  the  marking  scheme:  
data, that you have clearly shown where you obtained the data,  that  you  have  described  the  contents  of  the  dataset  (explaining clearly  both  the  format,  and  the  meaning  of  the  various  aspects)
your description shows clearly that you have appropriate rights to use the data in the ways that you do use it, and  your  explanation  shows  sensible  reflection  of  the  strengths  and limitations  of  the  data  that  you  obtained. 

# Data
a  section  that  describes  the  data source(s),  the format/contents  of  the  data, the  rights  associated  with  the data;

### Bitcoin tweets + prices
Usage information: license - cc0:public domain CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
The person who associated a work with this deed has dedicated the work to the public domain by waiving all of his or her rights to the work worldwide under copyright law, including all related and neighboring rights, to the extent allowed by law.
You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission. See Other Information below.

The data was from Kaggle, uploaded on 2019-02-13 by Jaime Badiola who used the github ‘GetOldTweets’ to download tweets from 2017-08-02(01) to 2019-01-22 in order to create the dataset. The most recent update was Version 2 on 2019-06-15. (which is what was used in this project) 


Used GetOldTweets to download all tweets of the period. Jaime Badiola
2017-08-02 to 2019-01-22
Date created 2019-02-13 Last updated 2019-06-15 Current version Version 2
 
Small description
 I collected over 17.7 million tweets  This dataset contains the average sentiment of all tweets about bitcoin  How did I do sentiment analysis? library VaderSentiment. I added about 30 expressions  and words to the dictionary. To score the expressions I used the same methodology as the authors described in their paper.It also contains the financial data of bitcoin for that same period.
 
 
Date: Time span for which all data in a row corresponds to 
Compound_Score:Average of all sentiment scores. It is very small because the amount of neutrals dilutes the sentiment, where numeric sclae with 0 beign neutral and - beeing native and + values corresponding to posistive setniments
nTotal volume of tweets
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
 
Some days have missing data on tweets Setniment analysis obc has room for issues such as sarcasm spelling mistakees etc, i think spam tweets are filteres out

### Chicago Crime
ID,  Case Number, Date, Block, IUCR, Primary Type, Description, Location Description, Arrest, Domestic, Beat, District, Ward, Community Area, FBI Code, X Coordinate, Y Coordinate, Year, Updated On, 
Latitude, Longitude, Location

Information about location (slightly off or generalised as a form of redaction) as longtidude and latitude as well as x coordinates and 

liability/disclaimer: The City of Chicago (“City”) voluntarily provides the data on this website as a service to the public. 
Any user of this website providing any software application, or other secondary or derivative application using data supplied at this website shall do the following:
Include the following disclaimer at the site where the software application, or other secondary or derivative application can be accessed or downloaded:
“This site provides applications using data that has been modified for use from its original source, www.cityofchicago.org, the official website of the City of Chicago.  The City of Chicago makes no claims as to the content, accuracy, timeliness, or completeness of any of the data provided at this site.  The data provided at this site is subject to change at any time.  It is understood that the data provided at this site is being used at one’s own risk.”
Comply with any additional Terms of Use set forth by the City agency or department providing data used by the software application, or other secondary or derivative application, including, without limitation, requirements to include additional citations or disclaimers at the site where the application can be accessed or downloaded. 



Cleaning
a  section  that  describes  the  initial  transformation  and  cleaning  that you  did  (include  here  the parts  of  Python code  that  you  used,  or  a description  that  is  detailed  enough  to  be followed);  

Preliminary Analysis
and  a  section  that describes  and  explains some simple  analysis  that  you  have  done  (again, show the code and also the output of the analysis). 

There is no required minimum or maximum length for the report; write whatever is needed to show the reader that you have earned the marks, and don’t say more than that!

