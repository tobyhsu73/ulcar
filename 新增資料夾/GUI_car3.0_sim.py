'''
GUI_car3.0

巡航車位置GUI

'''

import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkFont

#import matplotlib.animation as animation
import time
import numpy as np

import give_data as sort_data

S_cale =100
Title_1 = "UlcarGui"  #視窗標題
Title_2 = "避障車介面"


def dir(d):    #判斷車輪轉向
    if d == 0:
        return '後','前'
    elif d == 1:
        return '後','後'
    elif d == 2:
        return '前','前'
    elif d == 3:
        return '前','後'
    
def deg_(xy):    #繪布座標轉換
    #x0~500  y0~1900
    #比例 1:100  (公尺)
    y=450-xy[1]*S_cale
    x=400+xy[0]*S_cale
    return [x,y]

def motion(win):
        
    #win = tk.Tk()
    
    #====================視窗====================
    win.title(Title_1)  #視窗標題
    #win.geometry('1920x1080')    #視窗初始解析度
    #========================================    
    #====================數值建立====================
    
    data=sort_data.getdata()  #讀取
        #環境
    Tem = tk.DoubleVar()  #建立tk數值儲存物件
    Hum = tk.DoubleVar()
    Pressure = tk.DoubleVar()
    WindSpeed = tk.DoubleVar()
    CO2 = tk.IntVar()
        #座標
    x_deg = tk.DoubleVar()
    y_deg = tk.DoubleVar()
    z_deg = tk.DoubleVar()
        #IMU
    Yaw_deg = tk.DoubleVar()
    """  
    roll_eul = tk.DoubleVar()
    yaw_eul = tk.DoubleVar()
    pitch_eul = tk.DoubleVar()
    """
        #導航
    P0 = tk.StringVar()  #起點座標
    P1 = tk.StringVar()  #終點座標
    Vgo = tk.StringVar()  #導航修正方向的單位向量
    Aaims = tk.DoubleVar()  #目標角度
    ADeviation = tk.DoubleVar()  #車頭方向與目標方向偏差
    round_count = tk.IntVar()  #繞行圈數
        #馬達
    pwmA1 = tk.IntVar()
    pwmA2 = tk.IntVar()
    pwmB1 = tk.IntVar()
    pwmB2 = tk.IntVar()
    
    TfA1 = tk.IntVar()
    TfB1 = tk.IntVar()
    TfA2 = tk.IntVar()
    TfB2 = tk.IntVar()
    
    FA1 = tk.IntVar()
    FB1 = tk.IntVar()
    FA2 = tk.IntVar()
    FB2 = tk.IntVar()
    
    over1 = tk.IntVar()
    over2 = tk.IntVar()
    
    spL = tk.IntVar()
    spR = tk.IntVar()  
    dirA1 = tk.StringVar()
    dirB1 = tk.StringVar()
    dirA2 = tk.StringVar()
    dirB2 = tk.StringVar()
#Anchor
    
    Ax1 = tk.StringVar()  #x座標
    Ax2 = tk.StringVar()
    Ax3 = tk.StringVar()
    Ax4 = tk.StringVar()
    Ay1 = tk.StringVar()  #y座標
    Ay2 = tk.StringVar()
    Ay3 = tk.StringVar()
    Ay4 = tk.StringVar()
    Az1 = tk.StringVar()  #z座標
    Az2 = tk.StringVar()
    Az3 = tk.StringVar()
    Az4 = tk.StringVar()
    Ad1 = tk.StringVar()  #距離
    Ad2 = tk.StringVar()
    Ad3 = tk.StringVar()
    Ad4 = tk.StringVar()
    
#超音波
    
    FL = tk.StringVar()  #前偏左
    FR = tk.StringVar()
    LF = tk.StringVar()
    RF = tk.StringVar()
    
    #========================================
    
    
    #====================數值更新====================
        #環境

    try:    
        Tem.set('{:6.1f}'.format(data['Tem']))  #幫tk數值儲存物件賦值
        Hum.set('{:6.1f}'.format(data['Hum']))
        Pressure.set('{:6.1f}'.format(data['Pressure']))
        WindSpeed.set('{:6.1f}'.format(data['WindSpeed']))
        CO2.set('{:6.0f}'.format(data['CO2']))
        
    except:
        pass
        #座標
    x_deg.set('{:6.2f}'.format(eval(data['x'])))
    y_deg.set('{:6.2f}'.format(eval(data['y'])))
    z_deg.set('{:6.2f}'.format(eval(data['z'])))
        #IMU    
    Yaw_deg.set('{:6.2f}'.format(data['Yaw_deg']))
    """  
    roll_eul.set('{:6.2f}'.format(data['roll_eul']))
    yaw_eul.set('{:6.2f}'.format(data['yaw_eul']))
    pitch_eul.set('{:6.2f}'.format(data['pitch_eul']))
    """
        #導航
    P0.set(repr(data['P0']))
    P1.set(repr(data['P1']))
    Vgo.set(repr(data['Vgo']))
    Aaims.set('{:6.2f}'.format(data['Aaims']))
    ADeviation.set('{:6.2f}'.format(data['ADeviation']))
    round_count.set('{:6.0f}'.format(data['round_count']))
        #馬達
    pwmA1.set('{:6.0f}'.format(data['pwmA1']))
    pwmA2.set('{:6.0f}'.format(data['pwmA2']))
    pwmB1.set('{:6.0f}'.format(data['pwmB1']))
    pwmB2.set('{:6.0f}'.format(data['pwmB2']))
    TfA1.set('{:6.0f}'.format(data['TfA1']))
    TfB1.set('{:6.0f}'.format(data['TfB1']))
    TfA2.set('{:6.0f}'.format(data['TfA2']))
    TfB2.set('{:6.0f}'.format(data['TfB2']))
    FA1.set('{:6.0f}'.format(data['FA1']))
    FB1.set('{:6.0f}'.format(data['FA2']))
    FA2.set('{:6.0f}'.format(data['FB1']))
    FB2.set('{:6.0f}'.format(data['FB2']))
    over1.set('{:6.0f}'.format(data['over1']))
    over2.set('{:6.0f}'.format(data['over1']))
    spL.set('{:6.0f}'.format(data['spL']))
    spR.set('{:6.0f}'.format(data['spR']))
    dirL,dirR = dir(data['dir1'])
    dirA1.set(dirL)
    dirB1.set(dirR)
    dirL,dirR = dir(data['dir2'])
    dirA2.set(dirL)
    dirB2.set(dirR)
        #Anchor
    
    Ax1.set(data['Ax'][0])
    Ax2.set(data['Ax'][1])
    Ax3.set(data['Ax'][2])
    Ax4.set(data['Ax'][3])
    Ay1.set(data['Ay'][0])
    Ay2.set(data['Ay'][1])
    Ay3.set(data['Ay'][2])
    Ay4.set(data['Ay'][3])
    Az1.set(data['Az'][0])
    Az2.set(data['Az'][1])
    Az3.set(data['Az'][2])
    Az4.set(data['Az'][3])
    Ad1.set(data['ADist'][0])
    Ad2.set(data['ADist'][1])
    Ad3.set(data['ADist'][2])
    Ad4.set(data['ADist'][3])
    
        #超音波
    FL.set(data['ultrasound'][2])
    FR.set(data['ultrasound'][1])
    LF.set(data['ultrasound'][3])
    RF.set(data['ultrasound'][0])
    #========================================
     
    
    
      #字體設定
    dfont0 = tkFont.Font(family="Helvetica",size=30,weight='normal')  #標題Title_Label字型
    dfont = tkFont.Font(family="Helvetica",size=20,weight='normal')  #各欄標題字型
    dfont2 = tkFont.Font(family='Courier',size=16,weight= 'normal')
    
    #====================第一排標題====================
                      #width=100, height=100,沒作用?
    Title_Label = tk.Label(win, width=100, height=1, text = Title_2, font = dfont0)
    Title_Label.pack(fill="x", expand="yes")  #fill=x/y/both  視窗變化時，隨視窗變化的軸    expand置1 使能fill属性
    #========================================
    
    #frame = tk.Frame(width=800, height=50, bg="#C0C0C0", colormap="new",bd=1,relief=tk.SUNKEN)
    #frame.pack()
    #win.label_1=frame.label(100, 50, text="text")
    cvs = tk.Canvas(win, width=800, height=520, bg='white')  #建立畫布(在1080P螢幕上測量)
    cvs.pack(side='right',fill="both",expand="yes")
    
    #cvs.create_oval(10,10,30,30, fill='red',width=1,outline='red')  #创建一个圆
    #==============================


    #===============畫布比例及座標設定===============
    # 我們建置的場地為8mx4m。畫布canvas的尺寸為600*600 pixels
    # 若加上預留上下左右的畫布邊緣以及保持尺寸的比例尺，我們可以用的範圍大約可以是300*450
    dx=10
    dy=10

    #  anchor layout in canvas, unit: pixel
    #    W=500  # width of the anchor plane
    #    H=750  # height of the anchor plane

    scale=S_cale/1 # 比例尺，or 450/9, scale from physical space to canvas pixel
    
    # coordinate transformation between Map and Canvas
    X0=400   # 笛卡爾座標原點x相對於畫布的原點
    Y0=450 
    #====================第一橫欄====================
    LF0 = tk.LabelFrame(win, width=100, height=100, text="環境感測器", font=dfont)
    w=10  #格子寬度
    #第一排
        #溫度Tem
    Tem_T = tk.Label(LF0, text="溫度:",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    Tem_T.grid(row=0, column=0, columnspan=1, sticky="W")
    Tem_V = tk.Label(LF0, textvariable=Tem, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    Tem_V.grid(row=0, column=1,columnspan=1,sticky="W")
    Tem_U = tk.Label(LF0, text="℃", font=dfont2,  width=w, pady=0, padx=0, bg='white')
    Tem_U.grid(row=0, column=2,columnspan=1,sticky='w')
        #濕度Hum
    Hum_T = tk.Label(LF0, text="濕度:",font=dfont2,  width=w, pady=0, padx=2, bg='#C0C0C0')
    Hum_T.grid(row=0, column=3, columnspan=1, sticky="W")
    Hum_V = tk.Label(LF0, textvariable=Hum, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    Hum_V.grid(row=0, column=4,columnspan=1,sticky="W")
    Hum_U = tk.Label(LF0, text="%", font=dfont2,  width=w, pady=0, padx=0, bg='white')
    Hum_U.grid(row=0, column=5,columnspan=1,sticky='w')
        #風速WindSpeed
    WindSpeed_T = tk.Label(LF0, text="風速:",font=dfont2,  width=w, pady=0, padx=2, bg='#C0C0C0')
    WindSpeed_T.grid(row=0, column=6, columnspan=1, sticky="W")
    WindSpeed_V = tk.Label(LF0, textvariable=WindSpeed, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    WindSpeed_V.grid(row=0, column=7,columnspan=1,sticky="W")
    WindSpeed_U = tk.Label(LF0, text="m/s", font=dfont2,  width=w, pady=0, padx=0, bg='white')
    WindSpeed_U.grid(row=0, column=8,columnspan=1,sticky='w')
        #壓力Pressure
    Pressure_T = tk.Label(LF0, text="氣壓:",font=dfont2,  width=w, pady=0, padx=2, bg='#C0C0C0')
    Pressure_T.grid(row=0, column=9, columnspan=1, sticky="W")
    Pressure_V = tk.Label(LF0, textvariable=Pressure, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    Pressure_V.grid(row=0, column=10,columnspan=1,sticky="W")
    Pressure_U = tk.Label(LF0, text="Pa", font=dfont2,  width=w, pady=0, padx=0, bg='white')
    Pressure_U.grid(row=0, column=11,columnspan=1,sticky='w')
        #CO2 CO2
    CO2_T = tk.Label(LF0, text="CO2:",font=dfont2,  width=w, pady=0, padx=2, bg='#C0C0C0')
    CO2_T.grid(row=0, column=12, columnspan=1, sticky="W")
    CO2_V = tk.Label(LF0, textvariable=CO2, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    CO2_V.grid(row=0, column=13,columnspan=1,sticky="W")
    CO2_U = tk.Label(LF0, text="ppm", font=dfont2,  width=w, pady=0, padx=0, bg='white')
    CO2_U.grid(row=0, column=14,columnspan=1,sticky='w')
        #打包以上並顯示
    LF0.pack(fill="x", expand="yes")
    #========================================
    
    #====================第二橫欄====================
    LF2 = tk.LabelFrame(win, width=100, height=100, text="馬達控制參數", font=dfont)
    # 注意
    w=8  #格子寬
    #第一行 馬達
    motorA1_T = tk.Label(LF2, text="左前:", font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    motorA1_T.grid(row=1, column=0,columnspan=1,sticky='w')
    motorB1_T = tk.Label(LF2, text="左後:",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    motorB1_T.grid(row=2, column=0,columnspan=1,sticky="W")
    motorA2_T = tk.Label(LF2, text="右前:", font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    motorA2_T.grid(row=1, column=7,columnspan=1,sticky='w')
    motorB2_T = tk.Label(LF2, text="右後:", font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    motorB2_T.grid(row=2, column=7,columnspan=1,sticky='w')
    #第一列 標題
    spL_T = tk.Label(LF2, text="速度指令", font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    spL_T.grid(row=0, column=1,columnspan=1,sticky='w')
    TfL_T = tk.Label(LF2, text="目標頻率", font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    TfL_T.grid(row=0, column=2,columnspan=1,sticky='w')
    FL_T = tk.Label(LF2, text="當前頻率",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    FL_T.grid(row=0, column=3,columnspan=1,sticky="W")
    pwmL_T = tk.Label(LF2, text="PWM", font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    pwmL_T.grid(row=0, column=4,columnspan=1,sticky='w')
    dirL_T = tk.Label(LF2, text="方向", font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    dirL_T.grid(row=0, column=5,columnspan=1,sticky='w')    
    overL_T = tk.Label(LF2, text="過電流", font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    overL_T.grid(row=0, column=6,columnspan=1,sticky='w')
    
    spL_T = tk.Label(LF2, text="速度指令", font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    spL_T.grid(row=0, column=8,columnspan=1,sticky='w')
    TfR_T = tk.Label(LF2, text="目標頻率", font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    TfR_T.grid(row=0, column=9,columnspan=1,sticky='w')
    FR_T = tk.Label(LF2, text="當前頻率",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    FR_T.grid(row=0, column=10,columnspan=1,sticky="W")
    pwmR_T = tk.Label(LF2, text="PWM", font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    pwmR_T.grid(row=0, column=11,columnspan=1,sticky='w')
    dirR_T = tk.Label(LF2, text="方向", font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    dirR_T.grid(row=0, column=12,columnspan=1,sticky='w') 
    overR_T = tk.Label(LF2, text="過電流", font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    overR_T.grid(row=0, column=13,columnspan=1,sticky='w')
    #A1
    spA1_V = tk.Label(LF2, textvariable=spL, font=dfont2,  width=w, pady=0, padx=0, bg='white')
    spA1_V.grid(row=1, column=1,columnspan=1,sticky='w')
    TfA1_V = tk.Label(LF2, textvariable=TfA1, font=dfont2,  width=w, pady=0, padx=0, bg='white')
    TfA1_V.grid(row=1, column=2,columnspan=1,sticky='w')
    FA1_V = tk.Label(LF2, textvariable=FA1,font=dfont2,  width=w, pady=0, padx=0, bg='white')
    FA1_V.grid(row=1, column=3,columnspan=1,sticky='w')
    pwmA1_V = tk.Label(LF2, textvariable=pwmA1, font=dfont2,  width=w, pady=0, padx=0, bg='white')
    pwmA1_V.grid(row=1, column=4,columnspan=1,sticky='w')
    dirA1_V = tk.Label(LF2, textvariable=dirA1, font=dfont2,  width=w, pady=0, padx=0, bg='white')
    dirA1_V.grid(row=1, column=5,columnspan=1,sticky='w')
    overA1_V = tk.Label(LF2, textvariable=over1, font=dfont2,  width=w, pady=0, padx=0, bg='white')
    overA1_V.grid(row=1, column=6,columnspan=1,sticky='w')
    #B1
    
    spB1_V = tk.Label(LF2, textvariable=spR, font=dfont2,  width=w, pady=0, padx=0, bg='white')
    spB1_V.grid(row=1, column=8,columnspan=1,sticky='w')
    TfB1_V = tk.Label(LF2, textvariable=TfB1, font=dfont2,  width=w, pady=0, padx=0, bg='white')
    TfB1_V.grid(row=1, column=9,columnspan=1,sticky='w')
    FB1_V = tk.Label(LF2, textvariable=FB1,font=dfont2,  width=w, pady=0, padx=0, bg='white')
    FB1_V.grid(row=1, column=10,columnspan=1,sticky='w')
    pwmB1_V = tk.Label(LF2, textvariable=pwmB1, font=dfont2,  width=w, pady=0, padx=0, bg='white')
    pwmB1_V.grid(row=1, column=11,columnspan=1,sticky='w')
    dirB1_V = tk.Label(LF2, textvariable=dirB1, font=dfont2,  width=w, pady=0, padx=0, bg='white')
    dirB1_V.grid(row=1, column=12,columnspan=1,sticky='w')
    overB1_V = tk.Label(LF2, textvariable=over1, font=dfont2,  width=w, pady=0, padx=0, bg='white')
    overB1_V.grid(row=1, column=13,columnspan=1,sticky='w')
    
    #A2
    
    spA2_V = tk.Label(LF2, textvariable=spL, font=dfont2,  width=w, pady=0, padx=0, bg='white')
    spA2_V.grid(row=2, column=1,columnspan=1,sticky='w')
    TfA2_V = tk.Label(LF2, textvariable=TfA2, font=dfont2,  width=w, pady=0, padx=0, bg='white')
    TfA2_V.grid(row=2, column=2,columnspan=1,sticky='w')
    FA2_V = tk.Label(LF2, textvariable=FA2,font=dfont2,  width=w, pady=0, padx=0, bg='white')
    FA2_V.grid(row=2, column=3,columnspan=1,sticky='w')
    pwmA2_V = tk.Label(LF2, textvariable=pwmA2, font=dfont2,  width=w, pady=0, padx=0, bg='white')
    pwmA2_V.grid(row=2, column=4,columnspan=1,sticky='w')
    dirA2_V = tk.Label(LF2, textvariable=dirA2, font=dfont2,  width=w, pady=0, padx=0, bg='white')
    dirA2_V.grid(row=2, column=5,columnspan=1,sticky='w')
    overA2_V = tk.Label(LF2, textvariable=over1, font=dfont2,  width=w, pady=0, padx=0, bg='white')
    overA2_V.grid(row=2, column=6,columnspan=1,sticky='w')
    
    #B2
    
    spB2_V = tk.Label(LF2, textvariable=spR, font=dfont2,  width=w, pady=0, padx=0, bg='white')
    spB2_V.grid(row=2, column=8,columnspan=1,sticky='w')
    TfB2_V = tk.Label(LF2, textvariable=TfB2, font=dfont2,  width=w, pady=0, padx=0, bg='white')
    TfB2_V.grid(row=2, column=9,columnspan=1,sticky='w')
    FB2_V = tk.Label(LF2, textvariable=FB2,font=dfont2,  width=w, pady=0, padx=0, bg='white')
    FB2_V.grid(row=2, column=10,columnspan=1,sticky='w')
    pwmB2_V = tk.Label(LF2, textvariable=pwmB2, font=dfont2,  width=w, pady=0, padx=0, bg='white')
    pwmB2_V.grid(row=2, column=11,columnspan=1,sticky='w')
    dirB2_V = tk.Label(LF2, textvariable=dirB2, font=dfont2,  width=w, pady=0, padx=0, bg='white')
    dirB2_V.grid(row=2, column=12,columnspan=1,sticky='w')
    overB2_V = tk.Label(LF2, textvariable=over1, font=dfont2,  width=w, pady=0, padx=0, bg='white')
    overB2_V.grid(row=2, column=13,columnspan=1,sticky='w')
        #打包以上並顯示
    LF2.pack(fill="x", expand="yes")
    
    #========================================
    
    
    #====================第三橫欄====================
    LF3 = tk.LabelFrame(win, width=100, height=100, text="定位及導航", font=dfont)
        
    deg_T = tk.Label(LF3, text="座標及方向:",font=dfont2,  width=2*w, pady=0, padx=0, bg='white')
    deg_T.grid(row=0, column=0, columnspan=2, sticky="W")
    x_deg_T = tk.Label(LF3, text="X座標:",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    x_deg_T.grid(row=0, column=2, columnspan=1, sticky="W")
    x_deg_V = tk.Label(LF3, textvariable=x_deg, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    x_deg_V.grid(row=0, column=3,columnspan=1,sticky="W")
    
    y_deg_T = tk.Label(LF3, text="Y座標:",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    y_deg_T.grid(row=0, column=4, columnspan=1, sticky="W")
    y_deg_V = tk.Label(LF3, textvariable=y_deg, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    y_deg_V.grid(row=0, column=5,columnspan=1,sticky="W")
    
    z_deg_T = tk.Label(LF3, text="Z座標:",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    z_deg_T.grid(row=0, column=6, columnspan=1, sticky="W")
    z_deg_V = tk.Label(LF3, textvariable=z_deg, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    z_deg_V.grid(row=0, column=7,columnspan=1,sticky="W")
    Yaw_deg_T = tk.Label(LF3, text="方向角:",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    Yaw_deg_T.grid(row=0, column=8, columnspan=1, sticky="W")
    Yaw_deg_V = tk.Label(LF3, textvariable=Yaw_deg, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    Yaw_deg_V.grid(row=0, column=9,columnspan=1,sticky="W")
    Aaims_T = tk.Label(LF3, text="導航方向:",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    Aaims_T.grid(row=0, column=10, columnspan=1, sticky="W")
    Aaims_V = tk.Label(LF3, textvariable=Aaims, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    Aaims_V.grid(row=0, column=11,columnspan=1,sticky="W")
    ADeviation_T = tk.Label(LF3, text="偏差角度:",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    ADeviation_T.grid(row=0, column=12, columnspan=1, sticky="W")
    ADeviation_V = tk.Label(LF3, textvariable=ADeviation, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    ADeviation_V.grid(row=0, column=13,columnspan=1,sticky="W")
    
    
    P0_T = tk.Label(LF3, text="階段起點:",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    P0_T.grid(row=1, column=2, columnspan=1, sticky="W")
    P0_V = tk.Label(LF3, textvariable=P0, font=dfont2,  width=w*2, pady=0, padx=2, bg='white')
    P0_V.grid(row=1, column=3,columnspan=2,sticky="W")
    P1_T = tk.Label(LF3, text="階段終點:",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    P1_T.grid(row=1, column=5, columnspan=1, sticky="W")
    P1_V = tk.Label(LF3, textvariable=P1, font=dfont2,  width=w*2, pady=0, padx=2, bg='white')
    P1_V.grid(row=1, column=6,columnspan=2,sticky="W")
    Vgo_T = tk.Label(LF3, text="導航向量:",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    Vgo_T.grid(row=1, column=8, columnspan=1, sticky="W")
    Vgo_V = tk.Label(LF3, textvariable=Vgo, font=dfont2,  width=w*2, pady=0, padx=2, bg='white')
    Vgo_V.grid(row=1, column=9,columnspan=2,sticky="W")
        #打包以上並顯示
    LF3.pack(fill="x", expand="yes")
    #========================================

    
    #====================第四橫欄====================
    LF4 = tk.LabelFrame(win, width=100, height=100, text="UWB定位資訊  超音波偵測資訊", font=dfont)
        #UWB直標題
    A1_T = tk.Label(LF4, text="Anchor1:",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    A1_T.grid(row=1, column=0, columnspan=1, sticky="W")
    A2_T = tk.Label(LF4, text="Anchor2:",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    A2_T.grid(row=2, column=0, columnspan=1, sticky="W")
    A3_T = tk.Label(LF4, text="Anchor3:",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    A3_T.grid(row=3, column=0, columnspan=1, sticky="W")
    A4_T = tk.Label(LF4, text="Anchor4:",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    A4_T.grid(row=4, column=0, columnspan=1, sticky="W")
        #UWB橫標題
    Ax_T = tk.Label(LF4, text="X座標",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    Ax_T.grid(row=0, column=1, columnspan=1, sticky="W")
    Ay_T = tk.Label(LF4, text="Y座標",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    Ay_T.grid(row=0, column=2, columnspan=1, sticky="W")
    Az_T = tk.Label(LF4, text="Z座標",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    Az_T.grid(row=0, column=3, columnspan=1, sticky="W")
    Ad_T = tk.Label(LF4, text="距離",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    Ad_T.grid(row=0, column=4, columnspan=1, sticky="W")
        #UWB
    Ax1_V = tk.Label(LF4, textvariable=Ax1, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    Ax1_V.grid(row=1, column=1,columnspan=1,sticky="W")
    Ax2_V = tk.Label(LF4, textvariable=Ax2, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    Ax2_V.grid(row=2, column=1,columnspan=1,sticky="W")
    Ax3_V = tk.Label(LF4, textvariable=Ax3, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    Ax3_V.grid(row=3, column=1,columnspan=1,sticky="W")
    Ax4_V = tk.Label(LF4, textvariable=Ax4, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    Ax4_V.grid(row=4, column=1,columnspan=1,sticky="W")
    Ay1_V = tk.Label(LF4, textvariable=Ay1, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    Ay1_V.grid(row=1, column=2,columnspan=1,sticky="W")
    Ay2_V = tk.Label(LF4, textvariable=Ay2, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    Ay2_V.grid(row=2, column=2,columnspan=1,sticky="W")
    Ay3_V = tk.Label(LF4, textvariable=Ay3, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    Ay3_V.grid(row=3, column=2,columnspan=1,sticky="W")
    Ay4_V = tk.Label(LF4, textvariable=Ay4, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    Ay4_V.grid(row=4, column=2,columnspan=1,sticky="W")
    Az1_V = tk.Label(LF4, textvariable=Az1, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    Az1_V.grid(row=1, column=3,columnspan=1,sticky="W")
    Az2_V = tk.Label(LF4, textvariable=Az2, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    Az2_V.grid(row=2, column=3,columnspan=1,sticky="W")
    Az3_V = tk.Label(LF4, textvariable=Az3, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    Az3_V.grid(row=3, column=3,columnspan=1,sticky="W")
    Az4_V = tk.Label(LF4, textvariable=Az4, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    Az4_V.grid(row=4, column=3,columnspan=1,sticky="W")
    Ad1_V = tk.Label(LF4, textvariable=Ad1, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    Ad1_V.grid(row=1, column=4,columnspan=1,sticky="W")
    Ad2_V = tk.Label(LF4, textvariable=Ad2, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    Ad2_V.grid(row=2, column=4,columnspan=1,sticky="W")
    Ad3_V = tk.Label(LF4, textvariable=Ad3, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    Ad3_V.grid(row=3, column=4,columnspan=1,sticky="W")
    Ad4_V = tk.Label(LF4, textvariable=Ad4, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    Ad4_V.grid(row=4, column=4,columnspan=1,sticky="W")
        #=====超音波=====
        #超音波直標題
    A1_T = tk.Label(LF4, text="左",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    A1_T.grid(row=0, column=7, columnspan=1, sticky="W")
    A2_T = tk.Label(LF4, text="偏左",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    A2_T.grid(row=0, column=8, columnspan=1, sticky="W")
    A3_T = tk.Label(LF4, text="偏右",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    A3_T.grid(row=0, column=9, columnspan=1, sticky="W")
    A4_T = tk.Label(LF4, text="右",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    A4_T.grid(row=0, column=10, columnspan=1, sticky="W")
        #超音波橫標題
    Ax_T = tk.Label(LF4, text="前",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    Ax_T.grid(row=1, column=6, columnspan=1, sticky="W")
    Ay_T = tk.Label(LF4, text="偏前",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    Ay_T.grid(row=2, column=6, columnspan=1, sticky="W")
    Az_T = tk.Label(LF4, text="偏後",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    Az_T.grid(row=3, column=6, columnspan=1, sticky="W")
    Ad_T = tk.Label(LF4, text="後",font=dfont2,  width=w, pady=0, padx=0, bg='#C0C0C0')
    Ad_T.grid(row=4, column=6, columnspan=1, sticky="W")
        #超音波
    FL_V = tk.Label(LF4, textvariable=FL, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    FL_V.grid(row=1, column=8,columnspan=1,sticky="W")
    FR_V = tk.Label(LF4, textvariable=FR, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    FR_V.grid(row=1, column=9,columnspan=1,sticky="W")
    LF_V = tk.Label(LF4, textvariable=LF, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    LF_V.grid(row=2, column=7,columnspan=1,sticky="W")
    RF_V = tk.Label(LF4, textvariable=RF, font=dfont2,  width=w, pady=0, padx=2, bg='white')
    RF_V.grid(row=2, column=10,columnspan=1,sticky="W")
        #隔離帶
    nc1 = tk.Label(LF4, text=" ",font=dfont2,  width=w, pady=0, padx=0)
    nc1.grid(row=0, column=5, columnspan=1, sticky="W") 
    nc2 = tk.Label(LF4, text="  ",font=dfont2,  width=w, pady=0, padx=0)
    nc2.grid(row=1, column=5, columnspan=1, sticky="W") 
    nc3 = tk.Label(LF4, text="  ",font=dfont2,  width=w, pady=0, padx=0)
    nc3.grid(row=2, column=5, columnspan=1, sticky="W") 
    nc4 = tk.Label(LF4, text="  ",font=dfont2,  width=w, pady=0, padx=0)
    nc4.grid(row=3, column=5, columnspan=1, sticky="W") 
    nc5 = tk.Label(LF4, text="  ",font=dfont2,  width=w, pady=0, padx=0)
    nc5.grid(row=4, column=5, columnspan=1, sticky="W") 
    
        #打包以上並顯示
    LF4.pack(fill="x", expand="yes")
    #========================================

    

# --------------------------------------------------------------------------------
#
    #開始繪圖
    
    #===============建立畫布===============

    #==============================
    

#------------------------------------------------------------------------------------------------------
    
    while True:
        #====================數值更新====================
            #環境
        try:    
            Tem.set('{:6.1f}'.format(data['Tem']))  #幫tk數值儲存物件賦值
            Hum.set('{:6.1f}'.format(data['Hum']))
            Pressure.set('{:6.1f}'.format(data['Pressure']))
            WindSpeed.set('{:6.1f}'.format(data['WindSpeed']))
            CO2.set('{:6.0f}'.format(data['CO2']))
        except:
            pass
            #座標
        x_deg.set('{:6.2f}'.format(eval(data['x'])))
        y_deg.set('{:6.2f}'.format(eval(data['y'])))
        z_deg.set('{:6.2f}'.format(eval(data['z'])))
            #IMU
        Yaw_deg.set('{:6.2f}'.format(data['Yaw_deg']))
        """  
        roll_eul.set('{:6.2f}'.format(data['roll_eul']))
        yaw_eul.set('{:6.2f}'.format(data['yaw_eul']))
        pitch_eul.set('{:6.2f}'.format(data['pitch_eul']))
        """
            #導航
        P0.set(repr(data['P0']))
        P1.set(repr(data['P1']))
        Vgo.set(repr(data['Vgo']))
        Aaims.set('{:6.2f}'.format(data['Aaims']))
        ADeviation.set('{:6.2f}'.format(data['ADeviation']))
        round_count.set('{:6.0f}'.format(data['round_count']))
            #馬達
        pwmA1.set('{:6.0f}'.format(data['pwmA1']))
        pwmA2.set('{:6.0f}'.format(data['pwmA2']))
        pwmB1.set('{:6.0f}'.format(data['pwmB1']))
        pwmB2.set('{:6.0f}'.format(data['pwmB2']))
        TfA1.set('{:6.0f}'.format(data['TfA1']))
        TfB1.set('{:6.0f}'.format(data['TfB1']))
        TfA2.set('{:6.0f}'.format(data['TfA2']))
        TfB2.set('{:6.0f}'.format(data['TfB2']))
        FA1.set('{:6.0f}'.format(data['FA1']))
        FB1.set('{:6.0f}'.format(data['FA2']))
        FA2.set('{:6.0f}'.format(data['FB1']))
        FB2.set('{:6.0f}'.format(data['FB2']))
        over1.set('{:6.0f}'.format(data['over1']))
        over2.set('{:6.0f}'.format(data['over1']))
        spL.set('{:6.0f}'.format(data['spL']))
        spR.set('{:6.0f}'.format(data['spR']))
        dirL,dirR = dir(data['dir1'])
        dirA1.set(dirL)
        dirB1.set(dirR)
        dirL,dirR = dir(data['dir2'])
        dirA2.set(dirL)
        dirB2.set(dirR)
        
        #Anchor
        
        Ax1.set(data['Ax'][0])
        Ax2.set(data['Ax'][1])
        Ax3.set(data['Ax'][2])
        Ax4.set(data['Ax'][3])
        Ay1.set(data['Ay'][0])
        Ay2.set(data['Ay'][1])
        Ay3.set(data['Ay'][2])
        Ay4.set(data['Ay'][3])
        Az1.set(data['Az'][0])
        Az2.set(data['Az'][1])
        Az3.set(data['Az'][2])
        Az4.set(data['Az'][3])
        Ad1.set(data['ADist'][0])
        Ad2.set(data['ADist'][1])
        Ad3.set(data['ADist'][2])
        Ad4.set(data['ADist'][3])
            #超音波
        FL.set(data['ultrasound'][2])
        FR.set(data['ultrasound'][1])
        LF.set(data['ultrasound'][3])
        RF.set(data['ultrasound'][0])
        #========================================

        
        #===============畫4個anchor===============
           #從UWB傳回4個anchor的座標
        anchor=np.array([[float(data['Ax'][0]),float(data['Ay'][0])], 
                         [float(data['Ax'][1]),float(data['Ay'][1])], 
                         [float(data['Ax'][2]),float(data['Ay'][2])], 
                         [float(data['Ax'][3]),float(data['Ay'][3])]])
        
        mat_1=np.array([[1,0],[0,-1]])    #座標轉換矩陣
        trans=np.array([[X0,Y0]])     # 1-by-2 translation array
        
        an2=np.ones((4,1))*trans + scale*anchor.dot(mat_1)
        
        rect_color='#00BFFF'
        for i in range(4):
            cvs.create_rectangle(an2[i][0]-dx, an2[i][1]-dy, an2[i][0]+dx, an2[i][1]+dy, fill=rect_color, width=5,outline=rect_color)        
        #==============================
        
        
        #===============畫kp===============
        kpt=np.array([[1,6],[4,1]])
        kp=np.ones((2,1))*trans + scale*kpt.dot(mat_1)
            #畫當前路徑
        line_0 = cvs.create_line(deg_(data['P0'])[0],deg_(data['P0'])[1],deg_(data['P1'])[0],deg_(data['P1'])[1],fill='red', width=4)
        r=5  # radius
        print(deg_(data['P0'])[0],deg_(data['P0'])[1])
        
        oval_1=cvs.create_oval(deg_(data['P0'])[0]-r,deg_(data['P0'])[1]-r,deg_(data['P0'])[0]+r,deg_(data['P0'])[1]+r, fill='green', width=2)
        oval_2=cvs.create_oval(deg_(data['P1'])[0]-r,deg_(data['P1'])[1]-r,deg_(data['P1'])[0]+r,deg_(data['P1'])[1]+r, fill='green',width=2)
        #==============================
        
        
        #===============畫車子===============
        pngImage = Image.open("car arrow_6.png")
        photo = ImageTk.PhotoImage(pngImage.rotate(30))   # rotate image by 30 degrees

        car_x2=(float(data['x']))  #車子座標
        car_y2=(float(data['y']))
        try:
            car_x1+1  #此句用於測試car_x1是否存在，不存在即是第一次運行，則例外處理car1先設為car2
        except:
            car_x1 = car_x2
            car_y1 = car_y2
        imag_1=cvs.create_image(car_x1,car_y1, anchor = tk.CENTER, image=photo)
        car=np.array([[car_x1,car_y1],[car_x2,car_y2]])
        car2=np.ones((2,1))*trans + scale*car.dot(mat_1)
            #車的貼圖
        photo = ImageTk.PhotoImage(pngImage.rotate(data['Yaw_deg']-90))
        imag_1=cvs.create_image(car2[1][0],car2[1][1], anchor = tk.CENTER, image=photo)
            #畫軌跡
        cvs.create_line(car2[0][0], car2[0][1], car2[1][0], car2[1][1], fill="yellow", width=2)
        #==============================
        
        
        #=====畫車到Anchor的線=====
        car_anchor_line_color='red'
        line_1=cvs.create_line(car2[1][0], car2[1][1], an2[0][0], an2[0][1], fill=car_anchor_line_color, width=3,dash = (2, 2))
        line_2=cvs.create_line(car2[1][0], car2[1][1], an2[1][0], an2[1][1], fill=car_anchor_line_color, width=3,dash = (2, 2))
        line_3=cvs.create_line(car2[1][0], car2[1][1], an2[2][0], an2[2][1], fill=car_anchor_line_color, width=3,dash = (2, 2))
        line_4=cvs.create_line(car2[1][0], car2[1][1], an2[3][0], an2[3][1], fill=car_anchor_line_color, width=3,dash = (2, 2))
        #===============


        #=====畫方向線=====
        car = [float(data['x']),float(data['y'])]
        v1 = v1 = [car[0]+data['Vgo'][0],car[1]+data['Vgo'][1]]
        
        #line_5=cvs.create_line(car2[1][0], car2[1][1], proj_vec[0],proj_vec[1], fill='blue', width=2)
            
        cvs.update()
        
        car_x1=car_x2
        car_y1=car_y2
        
        
        #讀取需要時間,讀取完才能刪畫布
        time.sleep(0.1)
        data=sort_data.getdata()  #讀取
        
        #刪除要重繪的東西
        cvs.delete(line_0,line_1,line_2,line_3,line_4)  #刪除!!
        cvs.delete(oval_1,oval_2)  #刪除!!
        
    #cvs.pack()
    
    #關閉畫布用?  有bug但不管它
    win.mainloop()
    win.bind("<Destroy>", _destroy)    # stop program




#對win做更新?
def animate(win):
    tk.Canvas.cvs.update()



if __name__ == "__main__":
    #sort_data.Open()
    
    #先讀取幾次把剛開機不完整的資料讀取掉
    for n in range(0,10):
        time.sleep(0.1)
        data=sort_data.getdata()
    """
    time.sleep(0.1)
    data=sort_data.getdata()
    time.sleep(0.1)
    data=sort_data.getdata()
    time.sleep(0.1)
    data=sort_data.getdata()
    """
    
    win = tk.Tk()
    motion(win)


   
