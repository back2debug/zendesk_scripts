import pickle
import dateutil.parser
import pandas as pd 



with open('serialized_data_file.p', mode='rb') as f:
	ticket_review = pickle.load(f)

#.p file is in the same directory as script
#read data in serialized file and store in a variable ticket_review
ticket_review = pd.read_pickle('serialized_data_file.p')

#create dataframes for all the lists
tickets_df = pd.DataFrame(ticket_review['tickets'], columns=['id', 'url', 'type', 'subject', 'priority', 'status','assignee_id','organization_id', 'tags', 'created_at'])
users_df = pd.DataFrame(ticket_review['users'], columns=['id', 'name']).drop_duplicates(subset=['id'])
organizations_df = pd.DataFrame(ticket_review['organizations'], columns=['id', 'name']).drop_duplicates(subset=['id'])
metric_sets_df = pd.DataFrame(ticket_review['metric_sets'], columns=['id','ticket_id', 'reopens', 'replies', 'solved_at', 'reply_time_in_minutes','full_resolution_time_in_minutes', 'first_resolution_time_in_minutes'])


#check
#print(tickets_df)
#print(users_df)
#print(organizations_df)
#print(metric_sets_df)

#merge dfs tickets and users
merged_users_df = pd.merge(tickets_df, users_df, how='left',left_on='assignee_id', right_on='id')
merged_orgs_df = pd.merge(merged_users_df, organizations_df, how='left', left_on='organization_id', right_on='id')
merged_final_df = pd.merge(merged_orgs_df, metric_sets_df, how='left', left_on='id_x', right_on='ticket_id')

#rename and drop fields
merged_final_df.rename(columns={'id_x': 'ticket number', 'name_x': 'assignee', 'name_y': 'organization'}, inplace=True)
merged_final_df.drop(['assignee_id', 'organization_id', 'id_y', 'id', 'ticket_id'], axis=1, inplace=True)

#fix up the dates from strings to python date objects
merged_final_df['created_at'] = merged_final_df['created_at'].apply(lambda x: dateutil.parser.parse(x).date())
merged_final_df['solved_at'] = merged_final_df['solved_at'].apply(lambda x: dateutil.parser.parse(x).date() if x is not None else x)


#check column headers
#print(list(merged_final_df))

#write excel file index False prevents labeling the rows in excel file
merged_final_df.to_excel('ticket_review.xlsx', index=False)
