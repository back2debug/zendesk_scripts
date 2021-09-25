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
url = 'https://yourdomain.zendesk.com/api/v2/help_center/articles.json?'
user = 'email address'+ '/token'
pwd = ''

output_file = open("active_articles.csv","w")

outputWriter = csv.writer(output_file)


while url:
# Do the HTTP get request
    response = requests.get(url, auth=(user, pwd))
    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()
    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    #Write the active rticles to file from each call
    for article in data['articles']:
        if article['draft'] is False:
            row_array =[]
            for attribute in article:
                row_array.append(article[attribute])
            outputWriter.writerow(row_array)
    url = data['next_page']
	

#source_file.close()
output_file.close()
@tmart134
