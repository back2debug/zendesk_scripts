import requests
import json
import pickle


USER = 'EMAIL' + '/token'
PWD = 'TOKEN'

ticket_list = []
user_list = []
organizations_list = []
metrics_sets_list = []

url = 'https://your domain.zendesk.com/api/v2/incremental/tickets.json?start_time=1493640000&include=users,organizations,metric_sets'
session = requests.Session()
session.auth = (USER, PWD)
count = 1000

while (count==1000):
	response = session.get(url)
	if response.status_code == 429:
		print('rate limited')
		time.sleep(int(response.headers['retry-after']))
		continue
	if response.status_code != 200:
		print('Error with status code {}'.format(response.status_code))
		exit()
	data = response.json()
	ticket_list.extend(data['tickets'])
	user_list.extend(data['users'])
	organizations_list.extend(data['organizations'])
	metrics_sets_list.extend(data['metric_sets'])
	count = data['count']
	url = data['next_page']

ticket_data = {'tickets': ticket_list, 'users': user_list, 'organizations': organizations_list, 'metric_sets': metrics_sets_list}
with open ('inc_serialized_data_file.p', mode='wb') as f:
	pickle.dump(ticket_data,f)


#check
#for ticket in ticket_review:
	#assignee = 'anonymous'
	#for user in user_list:
		#if user['id'] == ticket['assignee_id']:
			#assignee = user['name']
			#break
	#print('{} assigned to {}'.format(ticket['id'], assignee))	