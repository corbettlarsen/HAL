import serial
class ArduinoConnect:
    def __init__(self):
            self.ser = serial.Serial('/dev/ttyACM0',9600)
        
    def readline(self):
        read =  self.ser.readline()
        try:
            return int(read)
        except:
            return 0
