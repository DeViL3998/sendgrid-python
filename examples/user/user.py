import sendgrid
import json
import os


sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

##################################################
# Get a user's account information. #
# GET /user/account #

response = sg.client.user.account.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve your credit balance #
# GET /user/credits #

response = sg.client.user.credits.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update your account email address #
# PUT /user/email #

data = {
  "email": "example@example.com"
}
response = sg.client.user.email.put(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve your account email address #
# GET /user/email #

response = sg.client.user.email.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update your password #
# PUT /user/password #

data = {
  "new_password": "new_password", 
  "old_password": "old_password"
}
response = sg.client.user.password.put(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get a user's profile #
# GET /user/profile #

response = sg.client.user.profile.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update a user's profile #
# PATCH /user/profile #

data = {
  "city": "Orange", 
  "first_name": "Example", 
  "last_name": "User"
}
response = sg.client.user.profile.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Cancel or pause a scheduled send #
# POST /user/scheduled_sends #

data = {
  "batch_id": "YOUR_BATCH_ID", 
  "status": "pause"
}
response = sg.client.user.scheduled_sends.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve all scheduled sends #
# GET /user/scheduled_sends #

response = sg.client.user.scheduled_sends.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve scheduled send #
# GET /user/scheduled_sends/{batch_id} #

batch_id = "test_url_param"
response = sg.client.user.scheduled_sends._(batch_id).get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete a cancellation or pause of a scheduled send #
# DELETE /user/scheduled_sends/{batch_id} #

batch_id = "test_url_param"
response = sg.client.user.scheduled_sends._(batch_id).delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update user scheduled send information #
# PATCH /user/scheduled_sends/{batch_id} #

data = {
  "status": "pause"
}
batch_id = "test_url_param"
response = sg.client.user.scheduled_sends._(batch_id).patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve current Enforced TLS settings. #
# GET /user/settings/enforced_tls #

response = sg.client.user.settings.enforced_tls.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update Enforced TLS settings #
# PATCH /user/settings/enforced_tls #

data = {
  "require_tls": true, 
  "require_valid_cert": false
}
response = sg.client.user.settings.enforced_tls.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update your username #
# PUT /user/username #

data = {
  "username": "test_username"
}
response = sg.client.user.username.put(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve your username #
# GET /user/username #

response = sg.client.user.username.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve Event Webhook settings #
# GET /user/webhooks/event/settings #

response = sg.client.user.webhooks.event.settings.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update Event Notification Settings #
# PATCH /user/webhooks/event/settings #

data = {
  "bounce": true, 
  "click": true, 
  "deferred": true, 
  "delivered": true, 
  "dropped": true, 
  "enabled": true, 
  "group_resubscribe": true, 
  "group_unsubscribe": true, 
  "open": true, 
  "processed": true, 
  "spam_report": true, 
  "unsubscribe": true, 
  "url": "url"
}
response = sg.client.user.webhooks.event.settings.patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Test Event Notification Settings  #
# POST /user/webhooks/event/test #

data = {
  "url": "url"
}
response = sg.client.user.webhooks.event.test.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve Parse Webhook settings #
# GET /user/webhooks/parse/settings #

response = sg.client.user.webhooks.parse.settings.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieves Inbound Parse Webhook statistics. #
# GET /user/webhooks/parse/stats #

params = {'aggregated_by': 'day', 'limit': 'test_string', 'start_date': '2016-01-01', 'end_date': '2016-04-01', 'offset': 'test_string'}
response = sg.client.user.webhooks.parse.stats.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

