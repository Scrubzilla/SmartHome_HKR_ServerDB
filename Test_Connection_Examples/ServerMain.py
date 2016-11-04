from builtins import print
from pubnub import Pubnub
from Test_Connection_Examples.ServerConnection import ServerConnection
from Test_Connection_Examples import XbeeListener

#Sets up a pubnub channel and starts to listen to it, also starts to listen to calls from the arduino.
def main():
    # Setup PubNub connection key
    print("Starting up...")
    pubnub = Pubnub(publish_key="pub-c-f97a90e1-2aa2-4db6-aee7-6187431f9dff", subscribe_key="sub-c-57c88d10-7fe9-11e6-82db-0619f8945a4f")

    print("Setting up pubnub connection...")
    # Start PubNub connection
    pubnub.subscribe(channels='hkr_channel', callback=createConnection, error=connectionError, connect=connect, reconnect=reconnect, disconnect=disconnect)

    deviceListener = XbeeListener.XbeeListener()
    deviceListener.start()

#When a message is recieved on the pubnub channel, a new connection that will send it to the arduino and then to the unit is created.
def createConnection(message, channel):
    print(message)

    connection = ServerConnection(connectionMessage=message)
    connection.start()

#If there is an error with the connection, it will print it.
def connectionError():
    print("Error")

def connect(message):
    print("CONNECTED")

def reconnect(message):
    print("RECONNECTED")

def disconnect(message):
    print("DISCONNECTED")

#----------------------------------------------------------------------------------------------------------------------#
#Program starts to run here.
main()
