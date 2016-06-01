import serial_connect
x = serial_connect.ArduinoConnect()
while(1):
    read = x.readline()
    print bin(int(read))

