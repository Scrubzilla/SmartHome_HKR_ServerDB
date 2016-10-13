import threading

import serial

#
#   This Class is a working example for connecting to Arduino with Xbee. With threading
#


PORT = 'COM4'       # USB has COM4 as port
BAUD_RATE = 9600

ser = serial.Serial(PORT, BAUD_RATE)  # Opens serial connection

# Open serial port
def commandToArduino(command):
    ser.write(command.encode())             # Outgoing command: encodes the string to bytes

def listenFromArduino():
    print(ser.read().decode(), end='')


def keyInput():
    while 1:
        command = input("Write Command: ")
        print(command)
        commandToArduino(command)
        if command == "end":
            ser.close()  # Closes serial connection
            threading.current_thread();
            break

def readArduino():
    try:
        while 1:
            if ser.is_open:
                listenFromArduino()
    except:
        print("listenFromArduino Stopped")

t1 = threading.Thread(target=keyInput)
t2 = threading.Thread(target=readArduino)
#t1.daemon = False
#t2.daemon = False
t1.start()
t2.start()