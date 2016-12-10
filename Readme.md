===========================================
Performance Analysis of MBTA using Python
===========================================

## About the Data

**Boston’s Massachusetts Bay Transit Authority (MBTA)** operates the 4th busiest subway system in the U.S. after New York, Washington, and Chicago. If you live in or around the city you have probably ridden on it. The MBTA recently began publishing substantial amount of subway data through its public APIs. They provide the full schedule in General Transit Feed Specification (GTFS) format which powers Google’s transit directions. MBTA also releases yearly reports on Finances, Reliablility, Ridership and Customer Service. Also, at the end of the year, they release a pdf containing information about the wages of every worker at MBTA. For analysis perpose we have used the folloing data :- 

- MBTA Real-Time API
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
  python collect_data_api.py

To convert the pdf file into a space delimited text life so that python can load it into the dataframe, I first downloaded pdftotext on my system and ran the following script :
  python collect_data_pdf.py



## Analysis 1

**At what time of the day, the probability of the train reaching the destination later than scheduled time, the highest?**

In Analysis 1, I analyzed the performance of MBTA with respect to travel time. Since it was not possible to calculate the travel time of every station to all the other stations, for analysis puspose, I have considered only path from Park Street to Harvard Square since it has most number of ridership, hence is the worst case. I calculated the number of times the train took longer than scheduled time to go from Park Street to Harvard Square. This shows the time at which the probability of train reacing late is highest.

To run the script :-
  python Analysis_1.py 2016-01-14


![alt tag](https://github.com/aankul/MBTA_Analysis_using_Python/blob/master/Analysis_1/Analysis_1.jpg)




## Analysis 2

**At what time of the day, the probability of the train stopping at a station more than its scheduled time, the highest?**

In Analysis 2, I analyzed the performance of MBTA with respect to dwell time (waiting time) at a stop. Since it was not possible to calculate the travel time of every station to all the other stations, due to API restrictions. For analysis puspose, I have considered only Park Street dwell time since it has most number of ridership, hence is the worst case. I plotted a timeseries graph between the dwelling time at different hour of the day. I have also plotted a reference line for referencing the average stopping time with the actual dwell time.

To run the script :-
  python Analysis_2.py 2016-01-14


![alt tag](https://github.com/aankul/MBTA_Analysis_using_Python/blob/master/Analysis_2/Analysis_2.jpg)



## Analysis 3

**How much does MBTA spend on the wages of different categories of MBTA employees?**

In Analysis 3, firstly a lot of pre-processing steps were involved since the data was scraped from a pdf file. After cleaning of data, I grouped together different designations under a certain category after some research. I plotted the graph to show which category earns the highest and on which category, MBTA spends the most.

To run the code :-
  python Analysis_3.py


![alt tag](https://github.com/aankul/MBTA_Analysis_using_Python/blob/master/Analysis_3/Analysis_3_part1.jpg)



![alt tag](https://github.com/aankul/MBTA_Analysis_using_Python/blob/master/Analysis_3/Analysis_3_part2.jpg)



## Analysis 4

**What are the relations between revenues and expenses in MBTA and where does the revenue come from?**

In Analysis 4, I have tried to visualize what percntage of revenue & expenses comes from the operating source and what percentage comes from non operating source for the specified month. I have also shown the relation between budgeted expenses with the actual expenses. This analysis gives a clear idea about the expenses and revenue of MBTA.

To run the code :-
  python Analysis_4.py JUN-2015
  
  
 ![alt tag](https://github.com/aankul/MBTA_Analysis_using_Python/blob/master/Analysis_4/Analysis_4_part1.jpg)
 
 
 
 ![alt tag](https://github.com/aankul/MBTA_Analysis_using_Python/blob/master/Analysis_4/Analysis_4_part2.jpg)
 
 
 
 
 ## Analysis 5

**How satisfied are the customers with MBTA?**

In Analysis 5, I have tried to visualize the customer satisfaction of MBTA customers. I have first plotted the time series graph of customer ratings for the past 2 years. It gives a good indication of the performance and changes every month. Apart from that, I have also plotted responses to some of the surveys that were asked to the MBTA users. This gives a clear idea about how happy the customers are with MBTA services.

To run the code :-
  python Analysis_5.py JUN-2015


![alt tag](https://github.com/aankul/MBTA_Analysis_using_Python/blob/master/Analysis_5/Analysis_5_part1.jpg)



![alt tag](https://github.com/aankul/MBTA_Analysis_using_Python/blob/master/Analysis_5/Analysis_5_part2.jpg)


