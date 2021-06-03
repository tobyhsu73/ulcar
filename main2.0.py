import readarduinoulpwm as ul
import time
import serial
import Hipnuc_IMU as imu
oldimu=123#old imu =init value
ser=serial.Serial('/dev/ttyUSB_ardco',9600)
imuset=0
imunum=0
imuc=0
i=2
t=0
d=0
dis=40
disr=38
time.sleep(1)
while True:
    
    ulf,umf,urf,ull,urr,ubb,method,race,move=ul.readul()
    
    if method=='h':
        imuset=0
        imuc=0
        ser.write(str.encode(race))
        ser.write(str.encode(move))
    elif method=='u':
        imuc=imuc+1
        if imuc==1 :
            oldimu,maximu,minimu=imu.zero()      
            imuset=1
            
        if imuset==1:
            ulf,umf,urf,ull,urr,ubb,method,race,move=ul.readul()
            imuset=0
            
        imur=imu.imu()
        imur=int(imur[0])
        imur=imur-oldimu+360

        print(imur,oldimu)
        if 540>=maximu:
            j=180
            if imur<=180 or imur>=360+i:
                print('r')
                ser.write(b'frc')
                continue
            elif imur>180 and imur <=360-i:
                print('l')
                ser.write(b'frl')
                continue
        elif 540<maximu:
            j=540
            if imur>360+i and imur<540:
                print('r')
                ser.write(b'frc')
                continue
            elif imur<=360-i or imur>=540:
                print('l')
                ser.write(b'flc')
                continue
        if t>=2:
            dis=55
        else:
            dis=40
        if ulf<=7 or umf<=7 or urf<=7:
            ser.write(b'hrd')
            t=0
            d=1
        elif ull <=50 and urr<=50 and umf >=40 and ulf>=40 and urf>=40:
            ser.write(b'mf')
            t=0
            d=1
        elif urr<=disr:
            ser.write(b'mll')
            print('mll')
            t=0
            d=1
        elif ull<=disr:
            ser.write(b'mrr')
            print('mrr')
            t=0
            d=1

        elif urr<=40 and ulf<=40:
            d=1
            t=0
            while umf<=50:
                ulf,umf,urf,ull,urr,ubb,method,race,move=ul.readul()
                ser.write(b'mll')
        elif ull<=60 and ulf<=40:
            d=1
            t=0
            while umf<=50:
                ulf,umf,urf,ull,urr,ubb,method,race,move=ul.readul()
                ser.write(b'mrr')
    
        elif ulf<=dis and umf<=dis:
            d=1
            ser.write(b'mrr')
            t=0
            
        elif umf<=dis:
            d=1
            print('mllumf')
            ser.write(b'mll')
            t=0
        elif ulf<=dis:
            ser.write(b'mrr')
            print('mrrulf')
            t=0
            d=1
        elif urf<=dis:
            ser.write(b'mll')
            print('mllurf')
            t=0
            d=1 
        else:
            ser.write(b'mf')
            print('f')
            if d==0:
                t=0
            t=t+1
            if t==17 and j==180:
                d=0
                imuset=0
                imuc=0
                ser.write(b'mrc')
                time.sleep(3.5)

                while True:
                    imur=imu.imu()
                    imur=int(imur[0])
                    imur=imur-oldimu+360
                    if imur<177 or imur>360:
                        ser.write(b'flc')
                    elif imur>177 and imur<183:
                        break
                    else:
                        ser.write(b'frc')
            elif t==17 and j==540:
                d=0
                imuset=0
                imuc=0
                ser.write(b'mrc')
                time.sleep(3.5)
                while True:
                    imur=imu.imu()
                    imur=int(imur[0])
                    imur=imur-oldimu+360
                    if imur<537 and imur >360:
                        ser.write(b'flc')
                    elif imur>537 and imur<543:
                        break
                    else:
                        ser.write(b'frc')                
        print(t)