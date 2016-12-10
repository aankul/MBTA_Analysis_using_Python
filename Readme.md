===========================================
Performance Analysis of MBTA using Python
===========================================

## Data Acquisition

**Boston’s Massachusetts Bay Transit Authority (MBTA)** operates the 4th busiest subway system in the U.S. after New York, Washington, and Chicago. If you live in or around the city you have probably ridden on it. The MBTA recently began publishing substantial amount of subway data through its public APIs. They provide the full schedule in General Transit Feed Specification (GTFS) format which powers Google’s transit directions. MBTA also releases yearly reports on Finances, Reliablility, Ridership and Customer Service. Also, at the end of the year, they release a pdf containing information about the wages of every worker at MBTA. For analysis perpose we have used the folloing data :- 

- MBTA Real-Time API
- MBTA_Wages_2014 data (in pdf format)
- MBTA_customersatisfaction_20150101-20161231 data from MBTA website
- MBTA_financial_20150101-20161231 data from MBTA website

Using the above data, I performed five analysis covering the following fields :
- **Performance** -> Travel time and Dwell time
- **Finance** -> Wage analysis, Revenue and Expenses
- **Customer Satisfaction** -> Ratings and Surveys



## Analysis 1

At what time of the day, the probability of the train reaching the destination late is the highest?

In Analysis 1, I analyzed the performance of MBTA with respect to travel time. Since it was not possible to calculate the travel time of every station to all the other stations, for analysis puspose, I have considered only path from Park Street to Harvard Square since it has most number of ridership, hence is the worst case. I calculated the number of times the train took longer than scheduled time to go from Park Street to Harvard Square. This shows the time at which the probability of train reacing late is highest.





## Motivation

A short description of the motivation behind the creation and maintenance of the project. This should explain **why** the project exists.

## Installation

Provide code examples and explanations of how to get the project.

## API Reference

Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.

## Tests

Describe and show how to run the tests with code examples.

## Contributors

Let people know how they can dive into the project, include important links to things like issue trackers, irc, twitter accounts if applicable.

## License

A short snippet describing the license (MIT, Apache, etc.)
