#!/usr/bin/env python3
"""
Getting list of active articles from Zendesk and writing to CSV.
"""
import requests
import csv

url = 'https://yourdomain.zendesk.com/api/v2/help_center/articles.json?'
user = 'email address' + '/token'
pwd = ''

with open("active_articles.csv", "w") as output_file:
    outputWriter = csv.writer(output_file)
    while url:
        response = requests.get(url, auth=(user, pwd))
        if response.status_code != 200:
            print('Status:', response.status_code, 'Problem with the request. Exiting.')
            exit()
        data = response.json()
        for article in data['articles']:
            if article['draft'] is False:
                row_array = [article[attribute] for attribute in article]
                outputWriter.writerow(row_array)
        url = data['next_page']
