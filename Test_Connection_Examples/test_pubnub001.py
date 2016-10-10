import sys
from pubnub import Pubnub
import time

#This class includes the communication parts for pubnub



def callback(message, channel):
    print(message)


def error(message):
    print("ERROR : " + str(message))


def connect(message):
    print("CONNECTED")

    pubnub.publish(channel='Hkr_channel', message='Hello from the PubNub Python SDK, Home Server Connected to PubNub')


def reconnect(message):
    print("RECONNECTED")


def disconnect(message):
    print("DISCONNECTED")


# Setup PubNub connection keys
pubnub = Pubnub(publish_key="pub-c-f97a90e1-2aa2-4db6-aee7-6187431f9dff", subscribe_key="sub-c-57c88d10-7fe9-11e6-82db-0619f8945a4f")


# Start PubNub connection
pubnub.subscribe(channels='Hkr_channel', callback=callback, error=callback, connect=connect, reconnect=reconnect, disconnect=disconnect)




#
# The loop below is to read keyboard inputs for sending commands to Pubnub
#

while 1:
    time.sleep(0.5)
    command = input("Command input: ")
    if command == "end":
        break

    elif len(command) is not 0:
        pubnub.publish(channel='Hkr_channel', message=command) # publish method is used to send message to pubnub and everyone will receive the message



pubnub.publish(channel='Hkr_channel', message="HomeServer Disconnected")  # publish method is used to send message to pubnub and everyone will receive the message



sys.exit()
