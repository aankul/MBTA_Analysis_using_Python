
# coding: utf-8

# In[2]:

import os


# In[3]:

input1 = '//data//MBTA_Wages2014.pdf'
output = '//data//MBTA_Wages2014.txt'
os.system(("pdftotext -layout %s %s") %( input1, output))


# In[ ]:




# In[ ]:




# In[ ]:



