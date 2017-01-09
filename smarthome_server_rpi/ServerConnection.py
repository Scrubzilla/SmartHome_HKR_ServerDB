from threading import Thread

from XbeeConnectionInit import XbeeConnectionInit
from LogHolder import LogHolder


class ServerConnection(Thread):

    #The connection will handle a specific message which is retrieved from a unit
    def __init__(self, connectionMessage):
        super(ServerConnection, self).__init__()
        self.message = connectionMessage
        return

    def run(self):
        # The connection will then create a connection to the device and send it and immediatly after listen for a response.
        logStorage = LogHolder.get()
        logStorage.add_text_to_log("Message was recieved from a unit: " + self.message)

        connection = XbeeConnectionInit.get()
        connection.command_to_arduino(self.message)
