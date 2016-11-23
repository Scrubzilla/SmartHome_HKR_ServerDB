from threading import Thread

from smarthome_server import XbeeConnectionInit
from smarthome_server import UnitConnection


class XbeeListener(Thread):
    def run(self):
        print("Listener thread: Starting to listen...")

        while True:
            # Gets the instance of the Singleton and listens to the arduino continously.
            communicator = XbeeConnectionInit.Singleton.get()
            xbeeMessage = communicator.listen_to_arduino()

            print("Listener thread: Xbee said: ", xbeeMessage)

            # Checks if the messages is a command that exists, if it is it contacts the XBEE
            if check_message_emergency(self, xbeeMessage) is True:
                print("Listener thread: Emergency command, notifying the unit...")
                unitMessager = UnitConnection.UnitConnection("0", xbeeMessage, "0")
                unitMessager.send_to_api()
                print("Listener thread: The unit was notified.")
            elif check_message_normal(self, xbeeMessage) is True:
                print("Listener thread: Normal command, sending back to the user...")
                unitConnection = UnitConnection.UnitConnection("0", xbeeMessage, "0")
                unitConnection.send_to_api()
                print("Listener thread: Sent back to the unit.")
            else:
                print("\nListener thread: The command " + xbeeMessage + " does not exists, scrapping this message.")

        print("Listener thread: Closing thread...")


def check_message_emergency(self, message):
    emergencyList = ["340001", "350001", "360001"]

    for i in range(0, len(emergencyList)):
        if (message) in emergencyList[i]:
            return True

    return False


def check_message_normal(self, message):
    commandList = ["11", "11100", "12000", "12200", "13000", "14000", "15000", "16000", "17000", "18000", "19000", "21000", "22000", "25000", "26000", "27000"]

    for i in range(0, len(commandList)):
        if commandList[i] in message:
            return True

    return False
