# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 21:05:11 2015

@author: David
"""
'''
Reference Codes for Countries, District, Foreign Port, NAICS, HTS, 
End-use Codes, Country Sub-Codes, and more can be found at:
    
    http://www.census.gov/foreign-trade/reference/codes/index.html
    
    '''
    
    
import pandas as pd
import numpy as np
import requests
import json 

#constants
apikey = "b43fd4e4cd857fab2c0a1692e8ef061d9d17999f"


#Loading the list of census country codes
CountryListDF = pd.read_csv('CountryCodeList-02.2014.csv')
    
#Check the new DF for null values
CountryListDF.isnull().sum()

#Sample Query
#http://api.census.gov/data/2014/intltrade/imp_exp?get=EXPALL2013,COUNTRY&SCHEDULE=7960&key=b43fd4e4cd857fab2c0a1692e8ef061d9d17999f



for country in CountryListDF['Code']:
    try:
        temp =  requests.get("http://api.census.gov/data/2014/intltrade/imp_exp?get=EXPALL2013,COUNTRY&SCHEDULE=" + str(country) + "&key=" + apikey)
        print temp.json()[1][1], ": ", temp.json()[1][2]
    except: pass


    
#test = requests.get("http://api.census.gov/data/2014/intltrade/imp_exp?get=EXPALL2013,COUNTRY&SCHEDULE=7960&key=b43fd4e4cd857fab2c0a1692e8ef061d9d17999f")     

'''
country = CountryListDF['Code'][0]
temp =  requests.get("http://api.census.gov/data/2014/intltrade/imp_exp?get=EXPALL2013,COUNTRY&SCHEDULE=" + str(country) + "&key=" + apikey)
print temp.json()
'''