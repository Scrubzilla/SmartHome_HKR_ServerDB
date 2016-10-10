import sys
from pubnub import Pubnub
import time
import serial

#
# Complete relay code from PubNub to Devices*
    # *(This class will only work if the Xbee is connected, current message format isn't formated with JSON only send one letter)
#

#1 HomeServer and device codes: Start
PORT = 'COM4'       # USB has COM4 as port
BAUD_RATE = 9600
ser = serial.Serial(PORT, BAUD_RATE)  # Opens serial connection

# method to send command to Arduino through Xbee
def commandToArduino(command):
    ser.write(command.encode())             # Outgoing command: encodes the string to bytes
    print(command)
    print(ser.read().decode())              # Incomming command: decodes the bytes to string

#1 HomeServer and device codes: End

#2 HomeServer and PubNub codes: Start

def callback(message, channel):
    print(message)
    commandToArduino(message) # relay command from PubNub


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

#2 HomeServer and PubNub codes:






#
# The loop below is to read keyboard inputs for sending commands to Pubnub
#

while 1:
    time.sleep(0.5)
    command = input("Command input: ")
    if command == "end":
        break

    elif len(command) is not 0:
        # publish method is used to send message to pubnub and everyone will receive the message
        pubnub.publish(channel='Hkr_channel', message=command)


# publish method is used to send message to pubnub and everyone will receive the message
pubnub.publish(channel='Hkr_channel', message="HomeServer Disconnected")


sys.exit()