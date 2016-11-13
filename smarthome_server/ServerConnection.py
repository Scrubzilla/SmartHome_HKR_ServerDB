from threading import Thread

from smarthome_server import XbeeConnectionInit
from smarthome_server import UnitConnection


class ServerConnection(Thread):

    #The connection will handle a specific message which is retrieved from a unit
    def __init__(self, connectionMessage):
        super(ServerConnection, self).__init__()
        self.message = connectionMessage
        return

    def run(self):
        # The connection will then create a connection to the device and send it and immediatly after listen for a response.
        connection = XbeeConnectionInit.Singleton.get()
        connection.command_to_arduino(self.message)

        response = connection.listen_to_arduino()
        print("Response from the arduino is: " + response)

        #When a response has been recieved, it will send it back to the unit.
        unitConnection = UnitConnection.UnitConnection(0, response, 0)
        unitConnection.send_to_api()
