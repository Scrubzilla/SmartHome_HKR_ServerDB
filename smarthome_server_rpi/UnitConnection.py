from builtins import print
import requests

class UnitConnection(object):
    #Will be handling a sensor, value as well as a notification.
    def __init__(self, sensorId, value, notification):
        self.sensorId = sensorId
        self.value = value
        self.notification = notification

    #Sends the sensor, value and notifciation that the object has been associated with to the unit.
    def send_to_api(self):
        url = 'http://smarthomeinterface.azurewebsites.net/unit/hkr_channel_unit'
        payload = {'sensorId': self.sensorId, 'value': self.value, 'notification': self.notification}

        r = requests.post(url, json=payload)
        print(r.text)
