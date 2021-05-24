import serial

import time
ser=serial.Serial('com22',115200)
while True:
    ser.write(b't')