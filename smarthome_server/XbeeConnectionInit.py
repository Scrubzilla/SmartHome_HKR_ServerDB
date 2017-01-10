import serial
from smarthome_server import LogHolder

class Singleton(object):
    instance = None
    PORT = 'COM4'                         #Modify port to the one that the XBEE is connected to.
    BAUD_RATE = 9600
    ser = serial.Serial(PORT, BAUD_RATE)  # Opens serial connection
    deviceBusy = False

    @classmethod
    def get(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance

    # Used to send a command to the arduino
    def command_to_arduino(self, command):

        print("Object Singelton: Writing to arduino: ", command)
        if (len(command) == 9):
            self.ser.write(command.encode())  # Outgoing command: encodes the string to bytes
            print("Object Singelton: Wrote successfully to the arduino.")
        else:
            print("Object Singelton: Command " + command + " was not sent to the arduino.")

        logStorage = LogHolder.Singleton.get()
        logStorage.add_text_to_log("The message was successfully forwared to the arduino (" + command +")")

    # Used to read a command from the arduino
    def listen_to_arduino(self):
        response = self.ser.read(9).decode()
        print("Object Singelton: Got a response...")

        logStorage = LogHolder.Singleton.get()
        logStorage.add_text_to_log("Got a response from the arduino:" + response)

        return response