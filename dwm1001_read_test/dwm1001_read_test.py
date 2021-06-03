import time
import serial
import numpy as np
import struct
t=0
#--------------------------------------------------------------------------------------------
   #  Sending the following commands multiple times will turn on/off this functionality.
    
    #ser.writ(b'les\r')    # Show distances to ranging anchors and the position
                           # if location engine is enabled.

#Example:
#dwm> les
#1151[5.00,8.00,2.25]=6.48 0CA8[0.00,8.00,2.25]=6.51 111C[5.00,0.00,2.25]=3.18
#1150[0.00,0.00,2.25]=3.16 le_us=2576 est[2.57,1.98,1.68,100]    


    #ser.write(b'lec\r')  # show measurements and positions in CSV format
                          # if location engine is enabled.
#Example:
#dwm> lec
#DIST,4,AN0,1151,5.00,8.00,2.25,6.44,AN1,0CA8,0.00,8.00,2.25,6.50,AN2,111C,5.00,0.00,2.25,
#3.24,AN3,1150,0.00,0.00,2.25,3.19,POS,2.55,2.01,1.71,98
#

    #ser.write(b'lep\r')  # show positions in CSV format

#Example:
#dwm> lep
#POS,2.57,2.00,1.67,97
#---------------------------------------------------------------------------------------------

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
time.sleep(1)
    
print('setup measurements')


# sending '\lec' and enter ('\r') commands to acquire data from DWM, 
#DIST,Number of Anchors,[AN+Anchor number,Anchor ID,X-Position,Y-Position,Z-Position,Distance to the tag],
#POS,X-Position of Tag,Y-Position of Tag,Z-Position of Tag
ser.write(b'lec\r')


data=ser.readline()  # read twice to ensure data-flushing in buffer
#data=ser.readline()

print(data)
print(len(data))

#data=str(data)   # convert to string
#print(data)
#print(type(data))
#b=struct.unpack('s',data)
#data=np.frombuffer(data)

time.sleep(0.05)
#ser.write(b'lec\r')   # send this command second time to switch off

#ser.write(b'lep\r') 
#data=ser.readline()
#print(data)
#print(type(data))

#
#ser.write(b'lec\r')

ser.flushInput()
print('data transfer as follows')

while True:
    try:
        
        data=ser.readline()    # class 'bytes'
        print(data)
        data=data.decode()     # decoding to UTF-8 format
        data=str(data)
        # convert bytes to string
        data = data.replace("\r\n", "")  # to remove \r\n in string
        #data=data.rstrip("\r\n")         # or using rstrip to remove \r\n
        print(data)
       
        
        time.sleep(0.01)
              
            
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
                    # the class of pos is 'dict'
                    #print(pos)
                    #print(type(pos))
                    
                    #a=[pos['x'],pos['y'],pos['z']]
                    #b=np.array(a)
                    #print(a[1])
                    #print(b[1])
                    #print(type(b))               
                    
                    time.sleep(0.05)
                    t=t+1
                print(pos_AN)
                print(pos)
                print(t)
    except Exception as e:
        
        ser.write(b'\r\r')   # to toggle the state of issuing command 
        ser.close()
        print(e)
        pass
    except KeyboardInterrupt:
        ser.write(b'\r\r')   # to toggle the state of issuing command 
        ser.close()