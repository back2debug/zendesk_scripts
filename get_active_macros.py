#!/usr/bin/env python3
"""
Getting list of active macros from Zendesk and writing to CSV.
"""
import requests
import csv

url = 'https://yourdomain.zendesk.com/api/v2/macros.json'
user = 'email address' + '/token'
pwd = ''

response = requests.get(url, auth=(user, pwd))

if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

data = response.json()

with open('active_macros.csv', 'w') as output_file:
    outputWriter = csv.writer(output_file)
    for macro in data["macros"]:
        if macro['active'] is True:
            row_array = [macro[attribute] for attribute in macro]
            outputWriter.writerow(row_array)

