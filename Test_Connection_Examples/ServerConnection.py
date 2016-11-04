from threading import Thread
from Test_Connection_Examples import XbeeConnection
from Test_Connection_Examples import UnitConnection

class ServerConnection(Thread):

    #The connection will handle a specific message which is retrieved from a unit
    def __init__(self, connectionMessage):
        super(ServerConnection, self).__init__()
        self.message = connectionMessage
        return

    def run(self):
        # The connection will then create a connection to the device and send it and immediatly after listen for a response.
        connection = XbeeConnection.XbeeConnection()
        connection.commandToArduino(self.message)

        response = connection.listenFromArduino()
        print("Response from the arduino is: " + response)

        #When a response has been recieved, it will send it back to the unit.
        unitConnection = UnitConnection.UnitConnection(0,response,0)
        unitConnection.send_to_api()
