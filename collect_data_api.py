
# coding: utf-8

# In[129]:

import requests
import json,os
import time
import datetime
import argparse
import pandas as pd
from datetime import date, timedelta as td


# In[150]:

# function to convert normal date_time to epoch time 
def date_to_epoch(normal_time):
    pattern = '%Y-%m-%d'
    epoch_time = int(time.mktime(time.strptime(normal_time, pattern)))
    return epoch_time


# In[131]:

# function to convert epoch time to normal date_time
def epoch_to_date(epoch_time):
    normal_time = datetime.datetime.fromtimestamp(epoch_time) # 1973-11-29 22:33:09
    return normal_time


# In[132]:

# function to calculate no. of days in between two dates
def time_diff_in_days(dt1,dt2):
    dt1 = epoch_to_date(epoch_fromdate) # 1973-11-29 22:33:09
    dt2 = epoch_to_date(epoch_todate) # 1977-06-07 23:44:50
    timediff = dt2-dt1
    return timediff.days


# In[133]:

# function to write json data in file
def write_data_in_file(file_name,data_dict) :
    with open('data//'+file_name,'w') as f:
        json.dump(data_dict,f)
        f.close() 
        return True
    return False


# In[134]:

if not os.path.exists('data') :
    os.mkdir('data', 755 )
    
if not os.path.exists('data//Traveltime') :
    os.mkdir('data//Traveltime', 755 )
    
if not os.path.exists('data//Dwelltime') :
    os.mkdir('data//Dwelltime', 755 )


# In[136]:

key = "r5z0yefoAESXRjwjZ8Im1A"


# In[ ]:

dateList = []
d1 = date(2016, 1, 1)
d2 = date(2016, 12, 9)
delta = d2 - d1
for i in range(delta.days + 1):
    d = d1 + td(days=i)
    dateList.append(str(d))

for i in range(1,len(dateList)-1) :
#Creating parameters
    payload_questions={}
    payload_questions["format"] = "json"
    payload_questions["api_key"] = key
    payload_questions["from_datetime"] = date_to_epoch(dateList[i])
    payload_questions["to_datetime"] = date_to_epoch(dateList[i+1])
    payload_questions["from_stop"] = 70067
    payload_questions["to_stop"] = 70075
    url_questions= "http://realtime.mbta.com/developer/api/v2.1/traveltimes"

#API call
    travel_times = requests.get(url_questions,params=payload_questions)
    travel_times

    if travel_times.ok:
        travel_times_json = travel_times.json()
        users_file_name = "Traveltime//traveltime_"+dateList[i]+".json"
        write_data_in_file(users_file_name,travel_times_json)


# In[164]:

dateList = []
d1 = date(2016, 1, 1)
d2 = date(2016, 12, 9)
delta = d2 - d1
for i in range(delta.days + 1):
    d = d1 + td(days=i)
    dateList.append(str(d))

for i in range(1,len(dateList)-1) :


#Creating parameters for dwell times
    payload_questions={}
    payload_questions["format"] = "json"
    payload_questions["api_key"] = key
    payload_questions["from_datetime"] = date_to_epoch(dateList[i])
    payload_questions["to_datetime"] = date_to_epoch(dateList[i+1])
    payload_questions["stop"] = 70075
    url_questions= "http://realtime.mbta.com/developer/api/v2.1/dwells"

#API call
    dwell_time = requests.get(url_questions,params=payload_questions) 

    if dwell_time.ok:
        dwell_time_json = dwell_time.json()
        users_file_name = "Dwelltime//dwelltime_"+dateList[i]+".json"
        write_data_in_file(users_file_name,dwell_time_json)


# In[153]:




# In[ ]:




# In[ ]:



