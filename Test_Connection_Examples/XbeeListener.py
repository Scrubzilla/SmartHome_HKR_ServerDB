from threading import Thread
from Test_Connection_Examples import UnitConnection

import serial

class XbeeListener(Thread):
    def run(self):
        print("starting to listen...")
        PORT = 'COM7'  # USB has COM4 as port
        BAUD_RATE = 9600
        ser = serial.Serial(PORT, BAUD_RATE)  # Opens serial connection

        while True:
            xbeeMessage = ser.read(6).decode()
            print("Xbee said: ", xbeeMessage)

            if self.checkMessage(xbeeMessage) is True:
                print("Command exists, sending to api...")
                #Insert method for creeating connection to unit here
                unitMessager = UnitConnection.UnitConnection("0", xbeeMessage, "0")
                unitMessager.send_to_api()

        print("Closing thread...")

    def checkMessage(self, message):
        commandList = ["250000", "260000"]

        for i in range(0, len(commandList)):
            if(message) in commandList[i]:
                return True

        return False
