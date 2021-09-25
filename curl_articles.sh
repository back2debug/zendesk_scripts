#Retrieve Articles

curl https://{subdomain}.zendesk.com/api/v2/help_center/{locale}/articles.json \
-v -u {email_address}:{password}

#Retrieve next batch of articles

curl -u email_address:password -X GET "https://{domain}.zendesk.com/api/v2/help_center/articles.json?page=2&per_page=30" | python -mjson.tool > source.json