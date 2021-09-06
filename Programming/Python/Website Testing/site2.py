#pip requests
#pip install pandas 
#pip install xlrd==1.2.0

import requests
from requests import ConnectionError
import pandas as pd
from requests.exceptions import HTTPError

sites = pd.read_excel("sites.xlsx")

for index, websites in sites.iterrows():
    try:
        response = requests.get(websites['site'])
        a = sites.at[index, "status_code"] = "Site is available {}".format(response.status_code)
        #print('\n', index, websites, a, '\n') 
    except:
        u = sites.at[index, "status_code"] = "Site isn't available."
        #print('\n', index, websites, u, '\n') 

print(sites)  
