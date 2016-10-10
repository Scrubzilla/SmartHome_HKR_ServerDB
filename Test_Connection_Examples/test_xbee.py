from concurrent.futures import thread

import serial
import time


#
#   This Class is a working example for connecting to Arduino with Xbee.
#


PORT = 'COM4'       # USB has COM4 as port
BAUD_RATE = 9600

ser = serial.Serial(PORT, BAUD_RATE)  # Opens serial connection

# Open serial port
def commandToArduino(command):
    ser.write(command.encode())             # Outgoing command: encodes the string to bytes
    print(command)
    print(ser.read().decode())              # Incomming command: decodes the bytes to string

def listenFromArduino():
    print(ser.read().decode())


#connectionToArduino( "A" )  # A is to turn on the light
#time.sleep( 1 )             # Sleep for 1 sec
#connectionToArduino( "B" )  # B is to turn off the light

# The following letters will do:
# a     : turn on light
# b     : turn off light
# A     : turn on light
# B     : turn off light

while 1:
    command = input("Write Command: ")
    commandToArduino(command)

    if command == "end":
        ser.close()  # Closes serial connection
        break

