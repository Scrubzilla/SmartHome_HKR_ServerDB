import sys

from builtins import print
from pubnub import Pubnub
import time
import serial
import requests

PORT = 'COM7'       # USB has COM4 as port
BAUD_RATE = 9600

ser = serial.Serial(PORT, BAUD_RATE)  # Opens serial connection



#This class includes the communication parts for pubnub


# Open serial port
def commandToArduino(command):
    print("Writing: ", command)
    ser.write(command.encode())             # Outgoing command: encodes the string to bytes
    #print(command)
    #print(ser.read().decode())              # Incomming command: decodes the bytes to string

def listenFromArduino():
    response = ser.read(6).decode()

    print("Response is: ", response)
    return response

def callback(message, channel):
   # print(message.__class__)

    print(message)
    #print(message['commandId'])

    if "25000" in message['commandId']:
        print("Reading...")
        print(message['slotId'])
        print(message['deviceId'])

        commandToArduino(message['commandId'])
        arduinoResp = listenFromArduino()

        send_to_api(message['slotId'], arduinoResp, message['deviceId'])
    if "26000" in message['commandId']:
        print("Doing...")
        commandToArduino(message['commandId'])
        arduinoResp = listenFromArduino()
        print("Got response from arduino... ")
        send_to_api(message['slotId'], arduinoResp, message['deviceId'])
        print("Sent to server...")

def send_to_api(sensorId, value , notification):
    url = 'http://smarthomeinterface.azurewebsites.net/unit/hkr_channel_unit'
    payload = {'sensorId': sensorId, 'value': value, 'notification': notification}

    r = requests.post(url, json=payload)
    print(r.text)




def error(message):
    print("ERROR : " + str(message))


def connect(message):
    print("CONNECTED")

    #pubnub.publish(channel='hkr_channel', message='Hello from the PubNub Python SDK, Home Server Connected to PubNub')


def reconnect(message):
    print("RECONNECTED")


def disconnect(message):
    print("DISCONNECTED")


# Setup PubNub connection keys
pubnub = Pubnub(publish_key="pub-c-f97a90e1-2aa2-4db6-aee7-6187431f9dff", subscribe_key="sub-c-57c88d10-7fe9-11e6-82db-0619f8945a4f")


# Start PubNub connection
pubnub.subscribe(channels='hkr_channel', callback=callback, error=callback, connect=connect, reconnect=reconnect, disconnect=disconnect)



#
# The loop below is to read keyboard inputs for sending commands to Pubnub
#


