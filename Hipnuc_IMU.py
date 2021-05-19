# ------------------------------------------------
# Test program for Hipnuc IMU Hi221 and CH110
#         by Andy Cherng   20200917
#         function name: hipnuc_IMU.py
# ------------------------------------------------
import struct   # C語言中的結構體 可作為轉換python與C語言結構體形式資料的轉換
import serial   # must be pyserial
#import numpy as np
#import scipy
#import matplotlib

    #選擇序列埠
#imu_comport = input("請選擇COM Port:\nCOM Port = ")
#imu_comport = imu_comport.upper()    #小寫轉大寫
#if 'COM' in imu_comport:   # 使用in運算子檢查
   # pass 
#elif imu_comport:
   # imu_comport = "COM"+imu_comport
#print("已選擇",imu_comport)

    #連接序列埠
ser = serial.Serial('com25',115200)
ser.flushInput()    # 擷取資料前先清空暫存器。原應有誤為flush()：等待所有數據寫出。

    #開始讀取
#以下的資料格式為超核數據包新格式0x91，共76字節，請自行參考中文版手冊第12~13頁以及第15頁
# Hi221是九軸IMU，CH110是六軸IMU，沒有磁場感測器(資料可忽略)
count=0   # 計數變數，因為清空暫存器不表示每回第一個擷取的資料就是對的
#for k in range(0,100):   # 試著先讀100次看看，可以修改為While迴圈
while True:  
    data=ser.read(1)    # 先讀一個byte資料就好
    count+=1    # 計數加一
        
    if data[0]==0x5A:    # 如果此byte是第一個標頭(Header)hex 5A，也就是Int. 90
        data=ser.read(1) # 接著檢查第二個byte
        
        # print(data,data[0])  
        
        if data[0]==0xA5:      # 如果是第二個標頭hex A5，即Int. 165   
            # print('this is AAAAAAAAA5555555')
           
            data=ser.read(1)  
            if data[0]==76:   # 第三個byte必須是76，hex 4C, Int. 76
                              # 表示總共有76個資料
                data=ser.read(1)
                if data[0]==0: # 第四個byte必須是0，hex 4C，Int. 00
                          # 其實第三與第四個byte是連在一起的little-endian
                          
               #帧头:5A A5
               #帧数据域⻓度:4C 00: (0x00<<8) + 0x4C = 76
               #帧CRC校验值:6C 51:(0x51<<8) + 0x6C = 0x516C
               # 就表示後面連續76個byte就是數據資料
                    break  # 此時就跳出(結束)for迴圈
               # 請注意，break內縮(indentation)的位置要與前面的if格式相同
# ------------ end of for-loop ------------

print('count is ',count)  # 如果不是1，就表示暫存器裡面有垃圾資料..但沒關係
print('Headers are correct...')   

# 接著檢查CRC的2個byte是否正確，我們在此忽略，因為...太難了
data=ser.read(2)  # we skip the validation
# print(data)

# 接著讀取連續76個byte
# the rest 76 bytes are IMU data in order

# the first 1 byte is the data format, must be 0x91
data=ser.read(1) # 0x91 or b'\x91'
#print(data,data[0])

# the 2nd byte is the ID of the sensor, usually 0
data=ser.read(1) # 0x00 or b'\x00'
#print(data,data[0])

# the next 6 bytes are reserved, so we skip them
data=ser.read(6)   # 保留用的6個byte，直接跳過

print()
print('Here are the received data...')
# start of the IMU data

# the first 4 bytes are timestamp, an Integer of 4 bytes
data=ser.read(4) #
time_stamp=struct.unpack('I',data)
print(time_stamp)
#  -------------------------------------------------
# the next 4 bytes are the x_acceleration (unit: G)
# in little-endian format, and must be converted to
# single precision floating point (from int32)
#'<f' means floating point in little-endian
#'>f' means floating point in big-endian

# x_acceleration
data=ser.read(4)
x_acc=struct.unpack('<f',data)

# y_acceleration
data=ser.read(4)
y_acc=struct.unpack('<f',data)

# z_acceleration
data=ser.read(4)
z_acc=struct.unpack('<f',data)
print(x_acc,y_acc,z_acc)

# next 12 bytes are three components of gyro data
# i.e., angular velocity (unit: deg./s)

# x_gyro
data=ser.read(4)
x_gyr=struct.unpack('<f',data)

# y_gyro
data=ser.read(4)
y_gyr=struct.unpack('<f',data)

# z_gyro
data=ser.read(4)
z_gyr=struct.unpack('<f',data)
print(x_gyr,y_gyr,z_gyr)

# the next 12 bytes are three components of
# magnetic field data, unit: uT (micro Tesla)

# x_magnetic strength
data=ser.read(4)
x_mag=struct.unpack('<f',data)

# y_magnetic strength
data=ser.read(4)
y_mag=struct.unpack('<f',data)

# z_magnetic strength
data=ser.read(4)
z_mag=struct.unpack('<f',data)
print(x_mag,y_mag,z_mag)

# the next 12 bytes are the Euler angles, unit: degree

# roll_Euler angle
data=ser.read(4)
roll_eul=struct.unpack('<f',data)

# Pitch_Euler angle
data=ser.read(4)
pitch_eul=struct.unpack('<f',data)

# Yaw_Euler angle
data=ser.read(4)
yaw_eul=struct.unpack('<f',data)
print(roll_eul,pitch_eul,yaw_eul)

# the last 16 bytes are the four components of
# Quaternion values, 

# w_quaternion
data=ser.read(4)
w_quat=struct.unpack('<f',data)
w_quat=round(w_quat[0],2)
# x_quaternion
data=ser.read(4)
x_quat=struct.unpack('<f',data)
x_quat=round(x_quat[0],2)
# y_quaternion
data=ser.read(4)
y_quat=struct.unpack('<f',data)
y_quat=round(y_quat[0],2)
# z_quaternion
data=ser.read(4)
z_quat=struct.unpack('<f',data)
z_quat=round(z_quat[0],2)
print(w_quat,x_quat,y_quat,z_quat)


ser.close()   # 關閉此COM埠

# -------------- end of program -------------
