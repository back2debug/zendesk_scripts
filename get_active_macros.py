#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 11:30:38 2018
@author: traceymartin
"""

"""
Getting list of articles from Zendesk and converting to CSV
"""

import requests
import csv

# Set the request parameters
url = 'https://yourdomain.zendesk.com/api/v2/macros.json'
user = 'email address'+ '/token'
pwd = 'token'

# Do the HTTP get request
response = requests.get(url, auth=(user, pwd))

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()
else:
    print(response.text)    

# Decode the JSON response into a dictionary and use the data
data = response.json()


output_file = open('active_macros.csv','w')

outputWriter = csv.writer(output_file)

for macro in data["macros"]:
    if macro['active'] is True:
        row_array =[]
        for attribute in macro:
            row_array.append(macro[attribute])
        outputWriter.writerow(row_array)
	

#source_file.close()
output_file.close()

