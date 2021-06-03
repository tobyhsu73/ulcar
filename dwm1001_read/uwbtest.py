import time
import serial
import numpy as np
import struct
t=0
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


while True:
    ser.flushInput()


    data=ser.readline()    # class 'bytes'
    if len(data)==0:
        ser.write(b'\r\r')
        ser.write(b'lec\r')
        print('xxxxx')
        time.sleep(0.01)
        continue
        
    data=data.decode()     # decoding to UTF-8 format
    
    data=str(data)
    # convert bytes to string
    data = data.replace("\r\n", "")  # to remove \r\n in string
    #data=data.rstrip("\r\n")         # or using rstrip to remove \r\n
    
   
    

          
        
    if (("DIST" in data) and ("AN0" in data) and ("AN1" in data) and ("AN2" in data) and ("AN3" in data)):
                            
            data = data.split(",")   # splitting string 
            anchor_info={'Anchor No':[],'ID':[],'x':[],'y':[],'z':[],'Dist':[]}
            #print('data after splitting')
            #print(data)
            # the class of data is 'list' with [ ]
            #print(type(data))
            if("DIST" in data):
                anchor_Nummber = int(4)
                for i in range(anchor_Nummber):
                    
                    anchor_data = {"id": data[data.index("AN"+str(i))+1], "x": data[data.index("AN"+str(i))+2],
                                     "y": data[data.index("AN"+str(i))+3],"z": data[data.index("AN"+str(i))+4],
                                     "dist": data[data.index("AN"+str(i))+5]}
                            # the class of pos_AN is 'dict'
           # print(anchor_info)
                    anchor_info['Anchor No'].append(data[data.index("AN"+str(i))])
                    anchor_info['ID'].append(data[data.index("AN"+str(i))+1])
                    anchor_info['x'].append(data[data.index("AN"+str(i))+2])
                    anchor_info['y'].append(data[data.index("AN"+str(i))+3])
                    anchor_info['z'].append(data[data.index("AN"+str(i))+4])
                    anchor_info['Dist'].append(data[data.index("AN"+str(i))+5])
                    # the class of pos_AN is 'dict'
                    
            if("POS" in data):
                pos = {'x': data[data.index('POS')+1],
                       'y': data[data.index('POS')+2],
                       'z': data[data.index('POS')+3]}
                t=t+1
                # the class of pos is 'dict'
                #print(pos)
                #print(type(pos))
                
                #a=[pos['x'],pos['y'],pos['z']]
                #b=np.array(a)
                #print(a[1])
                #print(b[1])
                #print(type(b))               
                print(t)
                print(pos,anchor_info)



            
    
 

