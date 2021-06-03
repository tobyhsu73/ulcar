import time
import serial
import numpy as np
import struct


ser = serial.Serial()
#ser.port = '/dev/ttyUSB0'
ser.port='COM30'
ser.baudrate = 115200
ser.bytesize = serial.EIGHTBITS 
ser.parity =serial.PARITY_NONE 
ser.stopbits = serial.STOPBITS_ONE 
ser.timeout = 1
ser.open()
ser.write(b'\r\r')   # enter shell mode from generic mode
ser.write(b'lec\r')

def uwbread():
    oldpos={'x': '0', 'y': '0', 'z': '0'}
    while True:
        ser.flushInput()
    
    
        data=ser.readline()    # class 'bytes'
        if len(data)==0:
            ser.write(b'\r\r')
            ser.write(b'lec\r')
            print('xxxxx')
           
            continue
            
        data=data.decode()     # decoding to UTF-8 format
        
        data=str(data)
        # convert bytes to string
        data = data.replace("\r\n", "")  # to remove \r\n in string
        #data=data.rstrip("\r\n")         # or using rstrip to remove \r\n
        
       
        

              
            
        if (("DIST" in data) and ("AN0" in data) and ("AN1" in data) and ("AN2" in data) and ("AN3" in data)):
                                
                data = data.split(",")   # splitting string 
                
                #print('data after splitting')
                #print(data)
                # the class of data is 'list' with [ ]
                #print(type(data))
                if("DIST" in data):
                    anchor_Nummber = int(data[data.index("DIST")+1])
                    for i in range(anchor_Nummber):
                        pos_AN = {"id": data[data.index("AN"+str(i))+1], "x": data[data.index("AN"+str(i))+2],
                                  "y": data[data.index("AN"+str(i))+3],"z": data[data.index("AN"+str(i))+4],
                                  "dist": data[data.index("AN"+str(i))+5]}
                        # the class of pos_AN is 'dict'
                        
                if("POS" in data):
                    pos = {'x': data[data.index('POS')+1],
                           'y': data[data.index('POS')+2],
                           'z': data[data.index('POS')+3]}
                    oldpos = pos
                else:
                    pos = oldpos
                    # the class of pos is 'dict'
                    #print(pos)
                    #print(type(pos))
                    
                    #a=[pos['x'],pos['y'],pos['z']]
                    #b=np.array(a)
                    #print(a[1])
                    #print(b[1])
                    #print(type(b))               

                break



            
    
 
#             
    return pos, pos_AN
   # ser.close()

if __name__=='__main__':
    while True:
        a,b=uwbread()
        print(a,b)

    
    