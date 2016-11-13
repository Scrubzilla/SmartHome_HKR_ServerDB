import serial

class Singleton(object):
    instance = None
    PORT = 'COM7'  # USB has COM4 as port
    BAUD_RATE = 9600
    ser = serial.Serial(PORT, BAUD_RATE)  # Opens serial connection

    @classmethod
    def get(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance

    # Used to send a command to the arduino
    def command_to_arduino(self, command):
        print("Writing to arduino: ", command)
        self.ser.write(command.encode())  # Outgoing command: encodes the string to bytes
        print("Wrote successfully to the arduino.")

    # Used to read a command from the arduino
    def listen_to_arduino(self):
        response = self.ser.read(6).decode()
        print("Got a response...")
        return response
