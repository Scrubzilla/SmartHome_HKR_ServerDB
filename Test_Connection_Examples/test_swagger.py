#
# no current code for swagger
#
import requests
import json


url = 'http://smarthomeinterface.azurewebsites.net/unit/hkr_channel'
payload = {'sensorId': 'data', 'value':'test2','notification':'test3'}

r = requests.post(url, json=payload)
print(r.text)

