import serial
import time
ser=serial.Serial('COM27',9600)
time.sleep(5)
while True:
    ser.write(b'ff')

    
    
    