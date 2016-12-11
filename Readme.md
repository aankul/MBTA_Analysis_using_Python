===========================================
Performance Analysis of MBTA using Python
===========================================

## About the Data

**Boston’s Massachusetts Bay Transit Authority (MBTA)** operates the 4th busiest subway system in the U.S. after New York, Washington, and Chicago. If you live in or around the city you have probably ridden on it. The MBTA recently began publishing substantial amount of subway data through its public APIs. They provide the full schedule in General Transit Feed Specification (GTFS) format which powers Google’s transit directions. MBTA also releases yearly reports on Finances, Reliablility, Ridership and Customer Service. Also, at the end of the year, they release a pdf containing information about the wages of every worker at MBTA. For analysis perpose we have used the folloing data :- 

- [MBTA Real-Time API] (http://realtime.mbta.com/portal)
- MBTA_Wages_2014 data (in pdf format)
- MBTA_customersatisfaction_20150101-20161231 data from MBTA website
- MBTA_financial_20150101-20161231 data from MBTA website


Using the above data, I performed five analysis covering the following fields :
- **Performance** -> Travel time and Dwell time
- **Finance** -> Wage analysis, Revenue and Expenses
- **Customer Satisfaction** -> Ratings and Surveys



## Collect Data
**MBTA Real-time API**
I collected two API calls to get the travel time and dwell time. As the name suggests travel time is the actual travel time between two stations, in my case its between Park Street and Harvard Square. Dwell time is the waiting time at a stop, it largly depends on the number of passangers entering and exiting the train but adds to the delay overhead. The data is collected for over an year starting from 2-JAN 2016 to 10-DEC 2016.

To run the script :
```
python collect_data_api.py
```


To convert the pdf file into a space delimited text life so that python can load it into the dataframe, I first downloaded pdftotext on my system and ran the following script :
  python collect_data_pdf.py



## Analysis 1

**At what time of the day, the probability of the train reaching the destination later than scheduled time, the highest?**

In Analysis 1, I analyzed the performance of MBTA with respect to travel time. Since it was not possible to calculate the travel time of every station to all the other stations, for analysis puspose, I have considered only path from Park Street to Harvard Square since it has most number of ridership, hence is the worst case. I calculated the number of times the train took longer than scheduled time to go from Park Street to Harvard Square. This shows the time at which the probability of train reacing late is highest.

To run the script :-
```
python Analysis_1.py 2016-01-14
```

Outout CSV file :

| hour :| l_count |
|------|---------|
| 00   | 1       |
| 05   | 3       |
| 06   | 7       |
| 07   | 3       |
| 08   | 10      |
| 09   | 12      |
| 10   | 8       |
| 11   | 2       |
| 13   | 2       |
| 14   | 4       |
| 15   | 9       |
| 17   | 10      |
| 18   | 10      |
| 20   | 9       |
| 21   | 7       |
| 22   | 6       |
| 23   | 7       |




![alt tag](https://github.com/aankul/MBTA_Analysis_using_Python/blob/master/Analysis_1/Analysis_1.jpg)

Insights - We can clearly see that as expected, the travel time between 8am to 10am and between 4pm to 6pm is the highest as they are rush hours. Apart from that, there are few late trains.


## Analysis 2

**At what time of the day, the probability of the train stopping at a station more than its scheduled time, the highest?**

In Analysis 2, I analyzed the performance of MBTA with respect to dwell time (waiting time) at a stop. Since it was not possible to calculate the travel time of every station to all the other stations, due to API restrictions. For analysis puspose, I have considered only Park Street dwell time since it has most number of ridership, hence is the worst case. I plotted a timeseries graph between the dwelling time at different hour of the day. I have also plotted a reference line for referencing the average stopping time with the actual dwell time.

To run the script :-
```  
python Analysis_2.py 2016-01-14
```

  Outout CSV file :
  
| arr_dt              :| dwell_time_sec :|
|---------------------|----------------|
| 2016-04-04 00:00:15 | 81             |
| 2016-04-04 00:09:33 | 64             |
| 2016-04-04 00:19:14 | 82             |
| 2016-04-04 00:31:14 | 75             |
| 2016-04-04 00:43:48 | 60             |
| 2016-04-04 01:01:59 | 60             |
| 2016-04-04 01:15:00 | 82             |
| 2016-04-04 05:42:05 | 69             |
| 2016-04-04 05:48:46 | 66             |
| 2016-04-04 05:57:14 | 67             |
| 2016-04-04 06:01:57 | 69             |
| 2016-04-04 06:14:13 | 75             |
| 2016-04-04 06:26:56 | 85             |
| 2016-04-04 06:33:59 | 96             |
| 2016-04-04 06:38:06 | 65             |


![alt tag](https://github.com/aankul/MBTA_Analysis_using_Python/blob/master/Analysis_2/Analysis_2.jpg)


Insights - We can clearly see that as expected, the dwell time between 8am to 10am and between 4pm to 6pm is the highest as they are rush hours, so there will be more crowd going in and going out of the train. This is similar to what i found in Analysis 1. Therefore, travel time is probably higher because of the dwell time during these hours.


## Analysis 3

**How much does MBTA spend on the wages of different categories of MBTA employees?**

In Analysis 3, firstly a lot of pre-processing steps were involved since the data was scraped from a pdf file. After cleaning of data, I grouped together different designations under a certain category after some research. I plotted the graph to show which category earns the highest and on which category, MBTA spends the most.

To run the code :-
```
python Analysis_3.py
```

Output CSV file :-

| max       :| median            :| 90th               :| subtot             :| num    |
|-----------|-------------------|--------------------|--------------------|--------|
| 179688.71 | 102388.16         | 125192.49799999999 | 13384403.779999994 | 137.0  |
| 221909.81 | 94398.07          | 154386.12999999998 | 21490870.590000007 | 225.0  |
| 235194.22 | 92374.48000000001 | 128312.01000000001 | 138312703.46       | 1502.0 |
| 161804.44 | 91090.07500000001 | 116019.378         | 10340880.95        | 118.0  |
| 215365.46 | 90005.19          | 123982.114         | 50937517.190000005 | 587.0  |
| 186731.39 | 86785.51          | 117346.81800000001 | 39656224.54        | 493.0  |
| 196809.15 | 86025.64          | 114689.10800000001 | 117418209.28999998 | 1495.0 |
| 220000.04 | 89073.075         | 127461.135         | 86389270.27000007  | 986.0  |



![alt tag](https://github.com/aankul/MBTA_Analysis_using_Python/blob/master/Analysis_3/Analysis_3_part1.jpg)



![alt tag](https://github.com/aankul/MBTA_Analysis_using_Python/blob/master/Analysis_3/Analysis_3_part2.jpg)


Insights - We can see that most of the salary expenditure is during maintenance and bus operations. MBTA can think of saving some wages on these dept. 


## Analysis 4

**What are the relations between revenues and expenses in MBTA and where does the revenue come from?**

In Analysis 4, I have tried to visualize what percntage of revenue & expenses comes from the operating source and what percentage comes from non operating source for the specified month. I have also shown the relation between budgeted expenses with the actual expenses. This analysis gives a clear idea about the expenses and revenue of MBTA.

To run the code :-
```
python Analysis_4.py JUN-2015
```


Output CSV file :-


| Reporting Fiscal Year :| Reporting Date :| Category    :| Subcategory            :| Month to Date Actual Amount :| Month to Date Budgeted Amount :|
|-----------------------|----------------|-------------|------------------------|-----------------------------|-------------------------------|
| 2015                  | JUN-2015       | Expenses    | Debt Service           | 24729467.69                 | 32739022.51                   |
| 2015                  | JUN-2015       | Expenses    | Operating Expenses     | 145087793.06                | 124309483.518                 |
| 2015                  | JUN-2015       | Revenue     | Non-Operating Revenues | 142500323.55                | 121956788.0                   |
| 2015                  | JUN-2015       | Revenue     | Operating Revenues     | 57387316.447                | 56642013.861                  |
| 2016                  | JUL-2015       | Expenses    | Debt Service           | 37354128.82                 | 38206625.0                    |
| 2016                  | JUL-2015       | Expenses    | Operating Expenses     | 126154664.44                | 135076774.657                 |
| 2016                  | JUL-2015       | Revenue     | Non-Operating Revenues | 75615762.97                 | 80072786.325                  |
| 2016                  | JUL-2015       | Revenue     | Operating Revenues     | 58522967.296                | 57740386.203                  |
| 2016                  | AUG-2015       | Expenses    | Debt Service           | 36070311.73                 | 36943793.0                    |
| 2016                  | AUG-2015       | Expenses    | Operating Expenses     | 118476759.5                 | 128941022.348                 |
| 2016                  | AUG-2015       | Revenue     | Non-Operating Revenues | 86047878.78                 | 84366038.504                  |
| 2016                  | AUG-2015       | Revenue     | Operating Revenues     | 57208100.218                | 56724721.235                  |



| Category :| Type                          :| Amount        |
|----------|-------------------------------|---------------|
| Expenses | Month to Date Actual Amount   | 169817260.75  |
| Expenses | Month to Date Budgeted Amount | 157048506.028 |
| Revenue  | Month to Date Actual Amount   | 199887639.997 |
| Revenue  | Month to Date Budgeted Amount | 178598801.861 |

  
 ![alt tag](https://github.com/aankul/MBTA_Analysis_using_Python/blob/master/Analysis_4/Analysis_4_part1.jpg)
 
 
 
 ![alt tag](https://github.com/aankul/MBTA_Analysis_using_Python/blob/master/Analysis_4/Analysis_4_part2.jpg)
 
 
Insights - We can see that 79.2% of the expenses are operating expenses and 20% of the expenses are spent on prior debt payment. However, only 31.7% of the revenue comes from the Operating revenues and rest from government funds. Hence, rise in prices of operating of MBTA is justified. Also, we have seen the difference between actual and budgetted amount. Even thought MBTA is in debt, the budgetted amount is always greater than the actual amount.
 

## Analysis 5


**How satisfied are the customers with MBTA?**

In Analysis 5, I have tried to visualize the customer satisfaction of MBTA customers. I have first plotted the time series graph of customer ratings for the past 2 years. It gives a good indication of the performance and changes every month. Apart from that, I have also plotted responses to some of the surveys that were asked to the MBTA users. This gives a clear idea about how happy the customers are with MBTA services.

To run the code :-
```
python Analysis_5.py JUN-2015
```

Output CSV file :-

| Survey Date :| Question Text                                                                       :| Respondents :| Average Rating Out of 7 |
|-------------|-------------------------------------------------------------------------------------|-------------|-------------------------|
| 01-JUL-2015 | The mbta is a good value for the money.                                             | 489         | 4.41                    |
| 01-JUL-2015 | The mbta has a fleet of trains and buses that are clean and well maintained.        | 492         | 3.34                    |
| 01-JUL-2015 | Wait time at stop                                                                   | 498         | 5.39                    |
| 01-JUL-2015 | Stop condition &amp; cleanliness                                                    | 491         | 4.93                    |
| 01-JUL-2015 | Seat availability / crowdedness                                                     | 500         | 4.99                    |
| 01-JUL-2015 | Vehicle cleanliness                                                                 | 500         | 4.94                    |
| 01-JUL-2015 | Speed/travel time                                                                   | 500         | 5.04                    |
| 01-JUL-2015 | Parking availability                                                                | 187         | 5.27                    |
| 01-JUL-2015 | Mbta website                                                                        | 449         | 5.05                    |
| 01-JUL-2015 | Real time arrival signage ("countdown timers")                                      | 456         | 5.05                    |
| 01-JUL-2015 | In-station delay announcements                                                      | 453         | 4.37                    |
| 01-JUL-2015 | On-vehicle delay announcements                                                      | 456         | 4.04                    |
| 01-JUL-2015 | T-alerts                                                                            | 439         | 4.48                    |
| 01-JUL-2015 | Real-time mobile apps (e.g. nextbus)                                                | 314         | 5.12                    |
| 01-JUL-2015 | Scheduled service interruptions                                                     | 418         | 4.41                    |




| Survey Date :| Question Text                        :| variable                   :| value              |
|-------------|--------------------------------------|----------------------------|--------------------|
| JUL-2015    | How would you rate the mbta overall? | Strongly Disagree          | 1.94617846         |
| JUL-2015    | How would you rate the mbta overall? | Disagree                   | 6.33606409         |
| JUL-2015    | How would you rate the mbta overall? | Slightly Disagree          | 16.89039194        |
| JUL-2015    | How would you rate the mbta overall? | Neither Agree nor Disagree | 10.336532550000001 |
| JUL-2015    | How would you rate the mbta overall? | Slightly Agree             | 40.21962811        |
| JUL-2015    | How would you rate the mbta overall? | Agree                      | 22.32581076        |
| JUL-2015    | How would you rate the mbta overall? | Strongly Agree             | 1.9453940900000002 |





![alt tag](https://github.com/aankul/MBTA_Analysis_using_Python/blob/master/Analysis_5/Analysis_5_part1.jpg)



![alt tag](https://github.com/aankul/MBTA_Analysis_using_Python/blob/master/Analysis_5/Analysis_5_part2.jpg)


Insights -  The ratings increase and decrease every month but the average rating comes out to be around 4.5 out of 7. The visualization of survey question shows that customers somewhat agree that MBTA's performance is satisfactory.


## Conclusion

We have evaluated the following parameters of performance of MBTA based on Reliability, Finance, Revenue, Expenses, Budget and Customer Satisfaction.

