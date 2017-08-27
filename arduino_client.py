import serial


# sudo pip install requests
# sudo pip install pySerial

class Arduino:
    def __init__(self):
        self.ser = serial.Serial('/dev/cu.usbserial-12345678', 9600, timeout=5)

    def send(self, value):
        serial.time.sleep(5)
        print 'hi !!'
        self.ser.flush()
        print 'writing.....'
        self.ser.write(value)
        print 'wrote.......'
        read_val = self.ser.read(size=64)
        print 'read :' + read_val
        serial.time.sleep(2)
