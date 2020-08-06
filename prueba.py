## Instructions to Use this ##

## Step 1 - Fork this repl
## Step 2 - Edit the Serial Number to that of your camera in line number 13 and 24. Serial Number is of the format Q2PV-4ZLD-97X9
## Step 3 - Edit your "To" phone number to your number on line 39

import requests
import json
import time

## Live API
print('MV Sense Live API')
meraki_live_url = 'https://api.meraki.com/api/v0/devices/Q2PV-4ZLD-97X9/camera/analytics/live'
meraki_headers = {'X-Cisco-Meraki-API-Key': 'ab8f4eb5b3cef9f4bc998acfbe44b1ab269a4836'}
meraki_live_response = requests.get(meraki_live_url, headers=meraki_headers)
meraki_live_response_json=json.loads(meraki_live_response.text)
num_of_person_detected=meraki_live_response_json['zones']['0']['person']

print(num_of_person_detected)

print('Snapshot API')

## Snapshot API
meraki_snapshot_url='https://api.meraki.com/api/v0/networks/L_647955396387936094/cameras/Q2PV-4ZLD-97X9/snapshot'
meraki_snapshot_response = requests.post(meraki_snapshot_url, headers=meraki_headers)
time.sleep(10)
meraki_snapshot_response_json=json.loads(meraki_snapshot_response.text)
snapshot_url=meraki_snapshot_response_json['url']

print(snapshot_url)

print('Sending Message via Twilio API')

## Twilio API
account_sid = 'ACf4082f75b52c030c9a2afeb0416cb690'
auth_token = '224a486ed710b92fbd35241b4c9404ae'
twilio_url = "https://api.twilio.com/2010-04-01/Accounts/ACf4082f75b52c030c9a2afeb0416cb690/Messages.json"
twilio_message="Number of people detected " + str(num_of_person_detected)
twilio_payload={"To":"+18122727620","From":"+14158516561","Body":twilio_message,"MediaUrl":snapshot_url}
twilio_response=requests.post(twilio_url,auth=(account_sid,auth_token),data=twilio_payload)
print(twilio_response,twilio_response.json())
