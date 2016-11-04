from builtins import print
import serial

class XbeeConnection(object):
    PORT = 'COM7'
    BAUD_RATE = 9600

    #Will start a serial connection on initialization
    def __init__(self):
        self.ser = serial.Serial(self.PORT, self.BAUD_RATE)  # Opens serial connection

    #Used to send a command to the arduino
    def commandToArduino(self, command):
        print("Writing: ", command)
        self.ser.write(command.encode())  # Outgoing command: encodes the string to bytes
        # print(command)
        # print(ser.read().decode())              # Incomming command: decodes the bytes to string

    # Used to read a command from the arduino
    def listenFromArduino(self):
        response = self.ser.read(6).decode()

        print("Response is: ", response)
        return response