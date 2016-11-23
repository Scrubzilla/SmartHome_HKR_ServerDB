import serial

class Singleton(object):
    instance = None
    PORT = 'COM7'                         #Modify port to the one that the XBEE is connected to.
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
        self.ser.write(command.encode())  # Outgoing command: encodes the string to bytes
        print("Object Singelton: Wrote successfully to the arduino.")

    # Used to read a command from the arduino
    def listen_to_arduino(self):
        response = self.ser.read(6).decode()
        print("Object Singelton: Got a response...")
        return response

    def get_arduino_is_busy(self):
        return self.deviceBusy

    def set_arduino_is_busy(self, status):
        self.deviceBusy = status

