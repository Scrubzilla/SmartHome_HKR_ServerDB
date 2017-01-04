from builtins import print
from pubnub import Pubnub
from smarthome_server.ServerConnection import ServerConnection
from smarthome_server import XbeeListener
from smarthome_server import LogPrinter
from smarthome_server import LogHolder

#Sets up a pubnub channel and starts to listen to it, also starts to listen to calls from the arduino.
def main():
    print("Starting up...")
    pubnub = Pubnub(publish_key="pub-c-f97a90e1-2aa2-4db6-aee7-6187431f9dff", subscribe_key="sub-c-57c88d10-7fe9-11e6-82db-0619f8945a4f")
    print("Setting up pubnub connection...")

    # Start PubNub connection.
    pubnub.subscribe(channels='hkr_channel', callback=create_connection, error=connection_error, connect=connect, reconnect=reconnect, disconnect=disconnect)

    #Start a connection to the arduino and listen to it.
    deviceListener = XbeeListener.XbeeListener()
    deviceListener.start()

    logger = LogPrinter.LogPrinter()
    logger.start()

#When a message is recieved on the pubnub channel, a new connection that will send it to the arduino and then to the unit is created.
def create_connection(message, channel):
    print("New message from a unit: " + message['commandId'])
    connection = ServerConnection(connectionMessage=message['commandId'])
    connection.start()

#If there is an error with the connection, it will print it.
def connection_error():
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
