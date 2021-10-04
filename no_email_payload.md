{% assign customer_email = ticket.requester.email | strip %}
{% if customer_email and customer_email != "" %}
  customer_email
{% else %}
  "no_email"
{% endif %}