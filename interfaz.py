import serial
#import serial.tools.list_ports
 
bytes = b'\x00'

serialcomm = serial.Serial("COM3", 9600)

while True:
    if serialcomm.in_waiting:
        bytes = serialcomm.read()
        
        print(bytes)
        
        entero = int.from_bytes(bytes, "big")
        print(entero)
        print(" ")