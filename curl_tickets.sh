#GET A TICKET

curl https://{subdomain}.zendesk.com/api/v2/tickets/{id}.json \
  -v -u {email_address}:{password}

curl https://{subdomain}.zendesk.com/api/v2/tickets/10229.json -v -u email:password | python -mjson.tool

#Update a ticket

curl https://{subdomain}.zendesk.com/api/v2/tickets/10282.json -H "Content-Type: application/json" -d '{"ticket": {"status": "pending", "comment": { "body": "The smoke is very colorful.", "author_id": {author_id} }}}' -v -u email:password -X PUT


curl https://{subdomain}.zendesk.com/api/v2/tickets/10343.json -H "Content-Type: application/json" -d '{"ticket": {"custom_fields": [{"id": {custom_field_id_1}, "value": 5}, {"id": {custom_field_id_2}, "value": "This is some test feedback"}]}}' -v -u email/token:{token} -X PUT
