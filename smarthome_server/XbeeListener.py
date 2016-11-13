from threading import Thread

from smarthome_server import XbeeConnectionInit
from smarthome_server import UnitConnection


class XbeeListener(Thread):
    def run(self):
        print("Starting to listen...")

        while True:
            #Gets the instance of the Singleton and listens to the arduino continously.
            communicator = XbeeConnectionInit.Singleton.get()
            xbeeMessage = communicator.listen_to_arduino()

            print("Xbee said: ", xbeeMessage)

            #Checks if the messages is a command that exists, if it is it contacts the XBEE
            if self.check_message(xbeeMessage) is True:
                print("Command exists, sending to api...")
                unitMessager = UnitConnection.UnitConnection("0", xbeeMessage, "0")
                unitMessager.send_to_api()

        print("Closing thread...")

    def check_message(self, message):
        commandList = ["340001", "350001", "360001"]

        for i in range(0, len(commandList)):
            if(message) in commandList[i]:
                return True

        return False
