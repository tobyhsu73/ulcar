import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkFont
import time
import numpy as np
import paho.mqtt.client as mqtt #import the client1
import math
import givedataul
broker_address="broker.emqx.io"
r=0

def on_message(client, userdata, message):
    global r
    global datam
    
    datam=str(message.payload.decode("utf-8"))
    if message.retain==0:
        r=5



S_cale =50
Title_1 = "UlcarGui"  #視窗標題
Title_2 = "介面"




   
#def deg_(xy):    #繪布座標轉換
    #x0~500  y0~1900
    #比例 1:100  (公尺)
   # y=1150-xy*S_cale
   # x=400+xy*S_cale
   # return [x,y]

def motion(win):
    def chan(a,b,c,d):
        global angle
        pointxc=220
        pointyc=300
        ax=(a-pointxc)*math.cos(angle)-(b-pointyc)*math.sin(angle)+pointxc
        ay=(a-pointxc)*math.sin(angle)+(b-pointyc)*math.cos(angle)+pointyc
        bx=(c-pointxc)*math.cos(angle)-(d-pointyc)*math.sin(angle)+pointxc
        by=(c-pointxc)*math.sin(angle)+(d-pointyc)*math.cos(angle)+pointyc
        return ax,ay,bx,by
    
    global r
    global datam
    print(123456)
    '''
    while True:
       
        r=0
        client = mqtt.Client("ddg") #create new instance要記得更改，隨便一個id都可以
        datam=client.on_message=on_message #attach function to callback
        client.connect(broker_address) #connect to broker
        client.subscribe("ulcar/toby")
        client.loop_start() #start the loop
        time.sleep(0.5)
        client.loop_stop()
        
        
        if r==5 :
            global data
            data=eval(datam)
            print(data)
            
            break
    '''
    data=givedataul.getdata()
    win.title(Title_2)
    win.geometry('1920x1080')


    a1=str(data['a'])+','+str(data['b'])
    b1=str(data['oldx'])+','+str(data['oldy'])
    data['imuc']=int(data['imuc'])
    if data['mode']=='navigation':
        data['mode']='導航'
    elif data['mode']=='avoidance':
        data['mode']='避障'
    imude=tk.DoubleVar()
    mode=tk.StringVar()
    status=tk.StringVar()
    ubb=tk.IntVar()
    ul2=tk.IntVar()
    ull=tk.IntVar()
    urr=tk.IntVar()
    ur2=tk.IntVar()
    urf=tk.IntVar()
    umf=tk.IntVar()
    ulf=tk.IntVar()
    lld=tk.IntVar()
    l1d=tk.IntVar()
    rrd=tk.IntVar()
    r1d=tk.IntVar()
    imur=tk.DoubleVar()
    a=tk.StringVar()
    b=tk.StringVar()
    
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
    imuc=tk.DoubleVar()
    imudeg=tk.DoubleVar()
    x=tk.DoubleVar()
    y=tk.DoubleVar()
    z=tk.DoubleVar()
    
    a.set(a1)
    b.set(b1)
    
    imude=int(data['imur']-data['imuc'])
    print(imudeg)
    
    imudeg.set(imudeg)
    ulf.set(data['ulf'])
    urf.set(data['urf'])
    umf.set(data['umf'])
    ull.set(data['ull'])
    urr.set(data['urr'])
    ubb.set(data['ubb'])
    ul2.set(data['ul2'])
    ur2.set(data['ur2'])
    lld.set(data['lld'])
    rrd.set(data['rrd'])
    l1d.set(data['l1d'])
    r1d.set(data['r1d'])
    ur2.set(data['ur2'])
    ul2.set(data['ul2'])
    
    imur.set(data['imur']-data['minimu'])
    imuc.set(int(data['imuc'])-int(data['minimu']))
    mode.set(data['mode'])
    status.set(data['status'])
    
    Ax1.set(data['posan']['Ax'][0])
    Ax2.set(data['posan']['Ax'][1])
    Ax3.set(data['posan']['Ax'][2])
    Ax4.set(data['posan']['Ax'][3])
    Ay1.set(data['posan']['Ay'][0])
    Ay2.set(data['posan']['Ay'][1])
    Ay3.set(data['posan']['Ay'][2])
    Ay4.set(data['posan']['Ay'][3])
    Az1.set(data['posan']['Az'][0])
    Az2.set(data['posan']['Az'][1])
    Az3.set(data['posan']['Az'][2])
    Az4.set(data['posan']['Az'][3])
    
    Ad1.set(data['posan']['ADist'][0])
    Ad2.set(data['posan']['ADist'][1])
    Ad3.set(data['posan']['ADist'][2])
    Ad4.set(data['posan']['ADist'][3])
    
    x.set(data['pos']['x'])
    y.set(data['pos']['y'])
    z.set(data['pos']['z'])
    
    cvs = tk.Canvas(win, width=1200, height=520, bg='white')  #建立畫布(在1080P螢幕上測量)
    cvs.pack(side='left',fill="both",expand="yes")
  
    dx=10
    dy=10
    scale=S_cale # 比例尺，or 450/9, scale from physical space to canvas pixel
    
    # coordinate transformation between Map and Canvas
    
    X0=450   # 笛卡爾座標原點x相對於畫布的原點
    Y0=800
    

    dfont0 = tkFont.Font(family="Helvetica",size=25,weight='normal')  #標題Title_Label字型
    dfont = tkFont.Font(family="Helvetica",size=20,weight='normal')  #各欄標題字型
    dfont2 = tkFont.Font(family='Courier',size=16,weight= 'normal')   
    Title_Label = tk.Label(win, width=100, height=0, text = Title_2, font = dfont0)
    Title_Label.pack(fill="x", expand="yes")    
   
    
    LF0 = tk.LabelFrame(win, width=100, height=10, text="避障感測資料", font=dfont)
    w=10
    
    ulff = tk.Label(LF0, text="左前",font=dfont2,  width=w, pady=10, padx=20, bg='lightpink')
    ulff.grid(row=0, column=0, columnspan=1, sticky="W")
    ulffdata = tk.Label(LF0,textvariable=ulf,font=dfont2,  width=w, pady=10, padx=20, bg='white')
    ulffdata.grid(row=1, column=0, columnspan=1, sticky="W")
    umff = tk.Label(LF0, text="中前",font=dfont2,  width=w, pady=10, padx=20, bg='PaleGreen')
    umff.grid(row=0, column=1, columnspan=1, sticky="W")
    ulffdata = tk.Label(LF0,textvariable=ulf,font=dfont2,  width=w, pady=10, padx=20, bg='white')
    ulffdata.grid(row=1, column=1, columnspan=1, sticky="W")
    urff = tk.Label(LF0, text="右前",font=dfont2,  width=w, pady=10, padx=20, bg='lightpink')
    urff.grid(row=0, column=2, columnspan=1, sticky="W")
    urffdata = tk.Label(LF0,textvariable=urf,font=dfont2,  width=w, pady=10, padx=20, bg='white')
    urffdata.grid(row=1, column=2, columnspan=1, sticky="W")
    ubbb = tk.Label(LF0, text="後方",font=dfont2,  width=w, pady=10, padx=20, bg='PaleGreen')
    ubbb.grid(row=0, column=3, columnspan=1, sticky="W")
    ubbbdata = tk.Label(LF0,textvariable=ubb,font=dfont2,  width=w, pady=10, padx=20, bg='white')
    ubbbdata.grid(row=1, column=3, columnspan=1, sticky="W")
    ulll = tk.Label(LF0, text="左一",font=dfont2,  width=w, pady=10, padx=20, bg='lightpink')
    ulll.grid(row=2, column=0, columnspan=1, sticky="W")
    ullldata = tk.Label(LF0,textvariable=ull,font=dfont2,  width=w, pady=10, padx=20, bg='white')
    ullldata.grid(row=3, column=0, columnspan=1, sticky="W")
    ul22 = tk.Label(LF0, text="左二",font=dfont2,  width=w, pady=10, padx=20, bg='PaleGreen')
    ul22.grid(row=2, column=1, columnspan=1, sticky="W")
    ul22data = tk.Label(LF0,textvariable=ul2,font=dfont2,  width=w, pady=10, padx=20, bg='white')
    ul22data.grid(row=3, column=1, columnspan=1, sticky="W")
    urrr = tk.Label(LF0, text="右一",font=dfont2,  width=w, pady=10, padx=20, bg='lightpink')
    urrr.grid(row=2, column=2, columnspan=1, sticky="W")
    urrrdata = tk.Label(LF0,textvariable=urr,font=dfont2,  width=w, pady=10, padx=20, bg='white')
    urrrdata.grid(row=3, column=2, columnspan=1, sticky="W")    
    ur22 = tk.Label(LF0, text="右二",font=dfont2,  width=w, pady=10, padx=20, bg='PaleGreen')
    ur22.grid(row=2, column=3, columnspan=1, sticky="W")
    ur22data = tk.Label(LF0,textvariable=ur2,font=dfont2,  width=w, pady=10, padx=20, bg='white')
    ur22data.grid(row=3, column=3, columnspan=1, sticky="W")
    lldd = tk.Label(LF0, text="左左前",font=dfont2,  width=w, pady=10, padx=20, bg='lightpink')
    lldd.grid(row=4, column=0, columnspan=1, sticky="W")
    lldddata = tk.Label(LF0,textvariable=lld,font=dfont2,  width=w, pady=10, padx=20, bg='white')
    lldddata.grid(row=5, column=0, columnspan=1, sticky="W")
    rrdd = tk.Label(LF0, text="右右前",font=dfont2,  width=w, pady=10, padx=20, bg='PaleGreen')
    rrdd.grid(row=4, column=1, columnspan=1, sticky="W")
    rrdddata = tk.Label(LF0,textvariable=rrd,font=dfont2,  width=w, pady=10, padx=20, bg='white')
    rrdddata.grid(row=5, column=1, columnspan=1, sticky="W")
    ul11 = tk.Label(LF0, text="左斜前",font=dfont2,  width=w, pady=10, padx=20, bg='lightpink')
    ul11.grid(row=4, column=2, columnspan=1, sticky="W")
    ul11data = tk.Label(LF0,textvariable=l1d,font=dfont2,  width=w, pady=10, padx=20, bg='white')
    ul11data.grid(row=5, column=2, columnspan=1, sticky="W")
    ur11 = tk.Label(LF0, text="右斜前",font=dfont2,  width=w, pady=10, padx=20, bg='PaleGreen')
    ur11.grid(row=4, column=3, columnspan=1, sticky="W")
    ur11data = tk.Label(LF0,textvariable=r1d,font=dfont2,  width=w, pady=10, padx=20, bg='white')
    ur11data.grid(row=5, column=3, columnspan=1, sticky="W")
    LF0.pack(fill="x", expand="yes")
    
    
    LF2 = tk.LabelFrame(win, width=100, height=100, text="行進狀態顯示", font=dfont)
    w=8
    imurr = tk.Label(LF2, text="目前方向角",font=dfont2,  width=w, pady=5, padx=10, bg='lightpink')
    imurr.grid(row=0, column=0, columnspan=1, sticky="W")
    imurrdata = tk.Label(LF2,textvariable=imur,font=dfont2,  width=w, pady=0, padx=10, bg='white')
    imurrdata.grid(row=1, column=0, columnspan=1, sticky="W")
    mode1 = tk.Label(LF2, text="模式",font=dfont2,  width=w, pady=5, padx=10, bg='PaleGreen')
    mode1.grid(row=0, column=1, columnspan=1, sticky="W")
    modedata = tk.Label(LF2,textvariable=mode,font=dfont2,  width=w, pady=5, padx=10, bg='white')
    modedata.grid(row=1, column=1, columnspan=1, sticky="W")
    status1 = tk.Label(LF2, text="狀態",font=dfont2,  width=w, pady=5, padx=10, bg='lightpink')
    status1.grid(row=0, column=2, columnspan=1, sticky="W")
    statusdata = tk.Label(LF2,textvariable=status,font=dfont2,  width=w, pady=5, padx=10, bg='white')
    statusdata.grid(row=1, column=2, columnspan=1, sticky="W")
    pointa = tk.Label(LF2, text="起點",font=dfont2,  width=w, pady=5, padx=20, bg='PaleGreen')
    pointa.grid(row=0, column=3, columnspan=1, sticky="W")
    pointadata = tk.Label(LF2,textvariable=a,font=dfont2,  width=w, pady=5, padx=20, bg='white')
    pointadata.grid(row=1, column=3, columnspan=1, sticky="W")
    pointb = tk.Label(LF2, text="終點",font=dfont2,  width=w, pady=5, padx=20, bg='lightpink')
    pointb.grid(row=0, column=4, columnspan=1, sticky="W")
    pointbdata = tk.Label(LF2,textvariable=b,font=dfont2,  width=w, pady=5, padx=20, bg='white')
    pointbdata.grid(row=1, column=4, columnspan=1, sticky="W")
    
    diraw = tk.Label(LF2, text="導航方向角",font=dfont2,  width=w, pady=5, padx=10,bg='lightpink')
    diraw.grid(row=2, column=0, columnspan=1, sticky="W")
    dirawdata = tk.Label(LF2,textvariable=imuc,font=dfont2,  width=w, pady=5, padx=10, bg='white')
    dirawdata.grid(row=3, column=0, columnspan=1, sticky="W")
    
    diavia = tk.Label(LF2, text="偏差角度",font=dfont2,  width=w, pady=5, padx=10, bg='PaleGreen')
    diavia.grid(row=2, column=1, columnspan=1, sticky="W")
    diaviadata = tk.Label(LF2,textvariable=imudeg,font=dfont2,  width=w, pady=5, padx=10, bg='white')
    diaviadata.grid(row=3, column=1, columnspan=1, sticky="W")
    
    x_deg_T = tk.Label(LF2, text="X座標:",font=dfont2,  width=w, pady=5, padx=10, bg='lightpink')
    x_deg_T.grid(row=2, column=2, columnspan=1, sticky="W")
    x_deg_V = tk.Label(LF2, textvariable=x, font=dfont2,  width=w, pady=5, padx=10, bg='white')
    x_deg_V.grid(row=3, column=2,columnspan=1,sticky="W")
    
    y_deg_T = tk.Label(LF2, text="Y座標:",font=dfont2,  width=w, pady=5, padx=20, bg='PaleGreen')
    y_deg_T.grid(row=2, column=3, columnspan=1, sticky="W")
    y_deg_V = tk.Label(LF2, textvariable=y, font=dfont2,  width=w, pady=5, padx=20, bg='white')
    y_deg_V.grid(row=3, column=3,columnspan=1,sticky="W")
    
    z_deg_T = tk.Label(LF2, text="Z座標:",font=dfont2,  width=w, pady=5, padx=20, bg='lightpink')
    z_deg_T.grid(row=2, column=4, columnspan=1, sticky="W")
    z_deg_V = tk.Label(LF2, textvariable=z, font=dfont2,  width=w, pady=5, padx=20, bg='white')
    z_deg_V.grid(row=3, column=4,columnspan=1,sticky="W")
    LF2.pack(fill="x", expand="yes")


    LF4 = tk.LabelFrame(win, width=100, height=100, text="UWB定位資訊", font=dfont)
        #UWB直標題
    A1_T = tk.Label(LF4, text="Anchor1:",font=dfont2,  width=w, pady=5, padx=10, bg='lightpink')
    A1_T.grid(row=1, column=0, columnspan=1, sticky="W")
    A2_T = tk.Label(LF4, text="Anchor2:",font=dfont2,  width=w, pady=5, padx=10, bg='PaleGreen')
    A2_T.grid(row=2, column=0, columnspan=1, sticky="W")
    A3_T = tk.Label(LF4, text="Anchor3:",font=dfont2,  width=w, pady=5, padx=10, bg='lightpink')
    A3_T.grid(row=3, column=0, columnspan=1, sticky="W")
    A4_T = tk.Label(LF4, text="Anchor4:",font=dfont2,  width=w, pady=5, padx=10, bg='PaleGreen')
    A4_T.grid(row=4, column=0, columnspan=1, sticky="W")
    #UWB橫標題
    Ax_T = tk.Label(LF4, text="X座標",font=dfont2,  width=w, pady=5, padx=10, bg='lightpink')
    Ax_T.grid(row=0, column=1, columnspan=1, sticky="W")
    Ay_T = tk.Label(LF4, text="Y座標",font=dfont2,  width=w, pady=5, padx=10, bg='PAleGreen')
    Ay_T.grid(row=0, column=2, columnspan=1, sticky="W")
    Az_T = tk.Label(LF4, text="Z座標",font=dfont2,  width=w, pady=5, padx=10, bg='lightpink')
    Az_T.grid(row=0, column=3, columnspan=1, sticky="W")
    Ad_T = tk.Label(LF4, text="距離",font=dfont2,  width=w, pady=5 ,padx=10, bg='PaleGreen')
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
    LF4.pack(fill="x", expand="yes")
    
 
    
    while True:

        
        if data['mode']=='navigation':
            data['mode']='導航'
        elif data['mode']=='avoidance':
            data['mode']='避障'
        if data['status']=='Rotate right':
            data['status']='右旋轉'
        elif data['status']=='Rotate left':
            data['status']='左旋轉'
        elif data['status']=='Traverse left':
            data['status']='左平移'
        elif data['status']=='Traverse right':
            data['status']='右平移'
        elif data['status']=='forward':
            data['status']='前進'
        
        data['lld']=data['lld']/10
        data['rrd']=data['rrd']/10
        data['l1d']=data['l1d']/10
        data['r1d']=data['r1d']/10
        print(data['rrd'])
        mode.set(data['mode'])
        status.set(data['status'])
        ulf.set(data['ulf'])
        urf.set(data['urf'])
        umf.set(data['umf'])
        ull.set(data['ull'])
        urr.set(data['urr'])
        ubb.set(data['ubb'])
        ul2.set(data['ul2'])
        ur2.set(data['ur2'])
        lld.set(data['lld'])
        rrd.set(data['rrd'])
        l1d.set(data['l1d'])
        r1d.set(data['r1d'])
        ur2.set(data['ur2'])
        ul2.set(data['ul2'])
        imur.set(data['imur']-360)
        
        imuc.set(int(data['imuc'])-360)
        a.set(a1)
        b.set(b1)
        
        Ax1.set(data['posan']['Ax'][0])
        Ax2.set(data['posan']['Ax'][1])
        Ax3.set(data['posan']['Ax'][2])
        Ax4.set(data['posan']['Ax'][3])
        Ay1.set(data['posan']['Ay'][0])
        Ay2.set(data['posan']['Ay'][1])
        Ay3.set(data['posan']['Ay'][2])
        Ay4.set(data['posan']['Ay'][3])
        
        Az1.set(data['posan']['Az'][0])
        Az2.set(data['posan']['Az'][1])
        Az3.set(data['posan']['Az'][2])
        Az4.set(data['posan']['Az'][3])
        Ad1.set(data['posan']['ADist'][0])
        Ad2.set(data['posan']['ADist'][1])
        Ad3.set(data['posan']['ADist'][2])
        Ad4.set(data['posan']['ADist'][3])
        
        imudeg.set(imude)
        
        x.set(data['pos']['x'])
        y.set(data['pos']['y'])
        z.set(data['pos']['z'])
               
        anchor=np.array([[float(data['posan']['Ax'][0]),float(data['posan']['Ay'][0])],
                 [float(data['posan']['Ax'][1]),float(data['posan']['Ay'][1])], 
                 [float(data['posan']['Ax'][2]),float(data['posan']['Ay'][2])], 
                 [float(data['posan']['Ax'][3]),float(data['posan']['Ay'][3])]])
        
        
        mat_1=np.array([[1,0],[0,-1]])    #座標轉換矩陣
        trans=np.array([[X0,Y0]])     # 1-by-u2 translation array
        
        an2=np.ones((4,1))*trans + scale*anchor.dot(mat_1)
         
        rect_color='#00BFFF'
        for i in range(4):
            cvs.create_rectangle(an2[i][0]-dx, an2[i][1]-dy, an2[i][0]+dx, an2[i][1]+dy, fill=rect_color, width=5,outline=rect_color)
          
        
    
        kpt=np.array([[1,6],[4,1]])
        kp=np.ones((2,1))*trans + scale*kpt.dot(mat_1)
            #畫當前路徑

        print(an2[3][0]-dx, an2[3][1]-dy)
        line_0 = cvs.create_line(data['oldx']*scale+X0,-data['oldy']*scale+Y0,data['a']*scale+X0,-data['b']*scale+Y0,fill='Orange', width=4)
        r=10  # radius
        spoint=[]
        
        oval_2=cvs.create_oval(data['a']*scale-r+X0,-data['b']*scale-r+Y0,data['a']*scale+r+X0,-data['b']*scale+r+Y0, fill='blue',width=2)
        for i in range(len(data['setx'])):
            spoint.append(cvs.create_oval(data['setx'][i]*scale+X0-r,-data['sety'][i]*scale-r+Y0,data['setx'][i]*scale+r+X0,-data['sety'][i]*scale+r+Y0, fill='green', width=2))    
        oval_1=cvs.create_oval(data['oldx']*scale+X0-r,-data['oldy']*scale-r+Y0,data['oldx']*scale+r+X0,-data['oldy']*scale+r+Y0, fill='blue', width=2)     
        print(spoint)
        #==============================
        #===============畫車子===============
        
        pngImage = Image.open("car arrow_6.png")
        photo = ImageTk.PhotoImage(pngImage.rotate(30))   # rotate image by 30 degrees
        car_x2=(float(data['pos']['x']))  #車子座標
        car_y2=(float(data['pos']['y']))
        
        
        try:
            
            car_x1+1  #此句用於測試car_x1是否存在，不存在即是第一次運行，則例外處理car1先設為car2
            
        except:
            car_x1 = car_x2
            car_y1 = car_y2
        imag_1=cvs.create_image(car_x1,car_y1, anchor = tk.CENTER, image=photo)
        car=np.array([[car_x1,car_y1],[car_x2,car_y2]])
        car2=np.ones((2,1))*trans + scale*car.dot(mat_1)
            #車的貼圖
        photo = ImageTk.PhotoImage(pngImage.rotate(data['imur']))
        imag_1=cvs.create_image(car2[1][0],car2[1][1], anchor = tk.CENTER, image=photo)
            #畫軌跡
        cvs.create_line(car2[0][0], car2[0][1], car2[1][0], car2[1][1], fill="DarkBlue", width=2)
        #==============================
        '''
        cvs.create_polygon (2.3*scale+X0, -3.9*scale+Y0, 1.45*scale+X0,  -4.65*scale+Y0, 2.15*scale+X0, -6*scale+Y0, 2.9*scale+X0, -5.6*scale+Y0,  fill='yellow')
        cvs.create_polygon (1.25*scale+X0, -6.9*scale+Y0, 0.8*scale+X0,  -6.85*scale+Y0, 0.7*scale+X0, -7.2*scale+Y0, 0.55*scale+X0, -7.4*scale+Y0,1.2*scale+X0, -8.5*scale+Y0,1.6*scale+X0, -7.65*scale+Y0,1.75*scale+X0, -7.65*scale+Y0,1.75*scale+X0, -7.25*scale+Y0,1.25*scale+X0, -7.25*scale+Y0,  fill='yellow')
        cvs.create_polygon (1.8*scale+X0, -9.1*scale+Y0, 1.2*scale+X0,  -9.65*scale+Y0, 1.95*scale+X0, -10*scale+Y0, 2.4*scale+X0, -9.65*scale+Y0,  fill='yellow')
        cvs.create_polygon (4.25*scale+X0, -7.6*scale+Y0, 3.8*scale+X0,  -7.6*scale+Y0, 4.5*scale+X0, -7.75*scale+Y0, 4.7*scale+X0, -7.6*scale+Y0,  fill='yellow')
        cvs.create_polygon (3.6*scale+X0, -1.8*scale+Y0, 3.6*scale+X0,  -2.6*scale+Y0, 4.4*scale+X0, -2.6*scale+Y0, 4.4*scale+X0, -1.8*scale+Y0,  fill='yellow')
        cvs.create_polygon (7.8*scale+X0, -2.6*scale+Y0, 7.9*scale+X0,  -2.5*scale+Y0, 8.3*scale+X0, -2.5*scale+Y0, 8.25*scale+X0, -2.45*scale+Y0,  fill='yellow')
        cvs.create_polygon (3.6*scale+X0, -9.85*scale+Y0, 3.6*scale+X0,  -10.65*scale+Y0, 4.4*scale+X0, -10.65*scale+Y0, 4.4*scale+X0, -9.85*scale+Y0,  fill='yellow')
        cvs.create_polygon (7.1*scale+X0, -9.35*scale+Y0, 7.3*scale+X0,  -9.6*scale+Y0, 7.85*scale+X0, -9.35*scale+Y0, 7.7*scale+X0, -9.15*scale+Y0,  fill='yellow')
        cvs.create_line(10.2*scale+X0,-5.5*scale+Y0,9.9*scale+X0,-5.9*scale+Y0, fill="yellow",width=10)
        cvs.create_polygon (10.4*scale+X0, -4.5*scale+Y0, 10.25*scale+X0,  -4.65*scale+Y0, 10.6*scale+X0, -4.95*scale+Y0, 10.75*scale+X0, -4.95*scale+Y0,  fill='yellow')
        cvs.create_polygon (11.8*scale+X0, -5.9*scale+Y0, 11.4*scale+X0,  -5.9*scale+Y0, 12.1*scale+X0, -6.05*scale+Y0, 12.15*scale+X0, -5.65*scale+Y0,  fill='yellow')
        cvs.create_line(11.7*scale+X0,-3.85*scale+Y0,13.0*scale+X0,-3.85*scale+Y0, fill="yellow",width=10)
        cvs.create_line(13.0*scale+X0,-5.4*scale+Y0,13.0*scale+X0,-3.85*scale+Y0, fill="yellow",width=10)
        cvs.create_polygon(5.25*scale+X0, -4.5*scale+Y0, 5.25*scale+X0,  -7*scale+Y0, 8.6*scale+X0, -7.3*scale+Y0, 8.6*scale+X0, -5.3*scale+Y0,8.4*scale+X0, -5.3*scale+Y0,8.4*scale+X0, -6.8*scale+Y0,5.5*scale+X0, -6.85*scale+Y0,5.5*scale+X0, -5.5*scale+Y0,6.1*scale+X0, -5*scale+Y0,6.1*scale+X0, -4.5*scale+Y0,  fill='yellow')
        cvs.create_line(10.55*scale+X0,-9.3*scale+Y0,10.55*scale+X0,-7.7*scale+Y0, fill="yellow",width=5)
        cvs.create_line(10.55*scale+X0,-7.7*scale+Y0,12.5*scale+X0,-7.7*scale+Y0, fill="yellow",width=5)
        cvs.create_line(12.5*scale+X0,-7.7*scale+Y0,12.5*scale+X0,-9.3*scale+Y0, fill="yellow",width=5)
        cvs.create_polygon (8.6*scale+X0, -1.8*scale+Y0, 8.6*scale+X0,  -2.6*scale+Y0, 9.4*scale+X0, -2.6*scale+Y0, 9.4*scale+X0, -1.8*scale+Y0,  fill='yellow')
        cvs.create_polygon (8.6*scale+X0, -9.85*scale+Y0, 8.6*scale+X0,  -10.65*scale+Y0, 9.4*scale+X0, -10.65*scale+Y0, 9.4*scale+X0, -9.85*scale+Y0,  fill='yellow')
        cvs.create_polygon (3.6*scale+X0, -1.8*scale+Y0, 3.6*scale+X0,  -2.6*scale+Y0, 4.6*scale+X0, -2.6*scale+Y0, 4.6*scale+X0, -1.8*scale+Y0,  fill='yellow')
        '''
        
        car_anchor_line_color='red'
        
        
        line_1=cvs.create_line(car2[1][0], car2[1][1], an2[0][0], an2[0][1], fill=car_anchor_line_color, width=3,dash = (2, 2))
        line_2=cvs.create_line(car2[1][0], car2[1][1], an2[1][0], an2[1][1], fill=car_anchor_line_color, width=3,dash = (2, 2))
        line_3=cvs.create_line(car2[1][0], car2[1][1], an2[2][0], an2[2][1], fill=car_anchor_line_color, width=3,dash = (2, 2))
        line_4=cvs.create_line(car2[1][0], car2[1][1], an2[3][0], an2[3][1], fill=car_anchor_line_color, width=3,dash = (2, 2))
        
        
        global angle
        rota=data['imur']
        angle=rota
        angle=math.radians(-angle)
        
        Imacar = Image.open("car1.png")            
        photo2=ImageTk.PhotoImage(Imacar.rotate(rota))        
        
        imag2=cvs.create_image(90,160,anchor=tk.NW,image=photo2)#中心點220,300
        

        
        pointxc=220
        pointyc=300
        
    
        w,h=Imacar.size
        print(w,h)
      
        
        
        if data['umf']<=40 and data['umf']>0:
            #cumf=cvs.create_oval(495, 160, 555, 220, fill="red")#umf
            umfx,umfy,umfx1,umfy1=chan(185,150,235,150)
            lineumf = cvs.create_line(umfx, umfy, umfx1, umfy1, fill="purple",width=10)#umf
            
        if data['ulf']<=40 and data['ulf']>1 or data['lld']<=40:
            #culf=cvs.create_oval(400, 160, 460, 220, fill="red")#ulf
            ulfx,ulfy,ulfx1,ulfy1=chan(130,150,185,150)
            lineulf = cvs.create_line(ulfx, ulfy,ulfx1, ulfy1, fill="purple",width=10)#ulf

        if data['urf']<=40 and data['urf']>1 or data['rrd']<=40:
            
            #curf=cvs.create_oval(590, 160, 650, 220, fill="red")#urf
            urx,ury,ur1x,ur1y=chan(235,150,295,150)
            lineurf = cvs.create_line(urx, ury, ur1x, ur1y, fill="purple",width=10)#urf
            
            
        if data['l1d']<=130:
            l1x,l1y,l11x,l11y=chan(130,150,80,200)
            linel1d = cvs.create_line(l1x,l1y,l11x,l11y, fill="purple",width=10)#l1d
            #l1cx,l1cy,l11cx,l11cy=chan(250,160,310,220)
            #cl11d=cvs.create_oval(l1cx,l1cy,l11cx,l11cy, fill="red")#l1d
            
        if data['r1d']<=130:
            #cr1d=cvs.create_oval(690, 160, 750, 220, fill="red")#r1d
            r1dx,r1dy,r11dx,r11dy=chan(295,150,345,200)
            liner1d = cvs.create_line(r1dx, r1dy, r11dx, r11dy, fill="purple",width=10)#r1d
            
        if data['ull']<=30 and data['ull']>=1:
            ullx,ully,ull1x,ull1y=chan(80,200,80,310)
            lineull = cvs.create_line(ullx,ully,ull1x,ull1y, fill="purple",width=10)#rll
            #cull=cvs.create_oval(300, 300, 360, 360, fill="red")#ull
        if data['ul2']<=30 and data['ul2']>=1:
            ul2x,ul2y,ul21x,ul21y=chan(80,310,80,420)
            lineul2 = cvs.create_line(ul2x,ul2y,ul21x,ul21y, fill="purple",width=10)#rl2
            #cul2=cvs.create_oval(300, 440, 360, 500, fill="red")#ul2
        if data['urr']<=30 and data['urr']>=1:
            urrx,urry,urr1x,urr1y=chan(345,200,345,300)
            lineurr = cvs.create_line(urrx, urry, urr1x, urr1y, fill="purple",width=10)#urr
            #curr=cvs.create_oval(295, 150, 295, 250, fill="red")#urr
        if data['ur2']<=30 and data['ur2']>=1:
            ur2x,ur2y,ur21x,ur21y=chan(345,300,345,420)
            lineur2 = cvs.create_line(ur2x,ur2y,ur21x,ur21y, fill="purple",width=10)#ur2
            #cur2=cvs.create_oval(690, 440, 750, 500, fill="red")#ur2
            
            
        if data['ubb']<=40 and data['ubb']>=1:
            #cubb=cvs.create_oval(495, 600, 555, 660, fill="red")#rbb
            ubbx,ubby,ubb1x,ubb1y=chan(80,420,345,420)
            lineubb = cvs.create_line(ubbx,ubby,ubb1x,ubb1y, fill="purple",width=10)#ubb


        dfont4 = tkFont.Font(family="Helvetica",size=16,weight='normal')
        dfont5 = tkFont.Font(family="Helvetica",size=16,weight='normal')
        cvs.create_text(600, 50, text='Obstacle avoidance and UWB navigation animation',font=dfont0)
        #cvs.create_text(220, 750, text='animation',font=dfont0)
        cvs.create_text(60,1000,text='legend',font=dfont4)        
        cvs.create_oval(10,1040,30,1060, fill='green', width=2)
        cvs.create_text(100,1050,text='set point',font=dfont4)
        cvs.create_rectangle(10,1080, 30, 1100, fill=rect_color, width=5,outline=rect_color)
        cvs.create_text(130,1090,text='anchor point',font=dfont4)
        cvs.create_line(10,1125,30,1125,fill='Orange', width=4)
        cvs.create_text(125,1125,text='target path',font=dfont4)
        cvs.create_line(10, 1165, 30, 1165, fill=car_anchor_line_color, width=3,dash = (2, 2))
        cvs.create_text(155,1165,text='anchor distance',font=dfont4)
        cvs.create_rectangle(10,1195, 30, 1215, fill='yellow', width=5,outline='yellow')
        cvs.create_text(105,1200,text='obstacle',font=dfont4)
        if data['mode']=='避障':
            
            red=Image.open('red.png')
            photo3=ImageTk.PhotoImage(red.rotate(0))
            imag3=cvs.create_image(165,600,anchor=tk.NW,image=photo3)
            avo=cvs.create_text(220,700,text='avoid mode',font=dfont4)
        
        
        cvs.update()
                
        car_x1=car_x2
        car_y1=car_y2
        
        
      
        if data['mode']=='避障':
            cvs.delete(imag3,avo)
        
        if data['umf']<=40 and data['umf']>0:
            cvs.delete(lineumf)
        if data['ulf']<=40 and data['ulf']>1 or data['lld']<=40:
            cvs.delete(lineulf)
        if data['urf']<=40 and data['urf']>1 or data['rrd']<=40:
            cvs.delete(lineurf)
        if data['l1d']<=130:
            cvs.delete(linel1d)
        if data['r1d']<=130:
            cvs.delete(liner1d)
        if data['ull']<=30 and data['ull']>=1:
            cvs.delete(lineull)
        if data['ul2']<=30 and data['ul2']>=1:
            cvs.delete(lineul2)
        if data['urr']<=30 and data['urr']>=1:
            cvs.delete(lineurr)
        if data['ur2']<=30 and data['ur2']>=1:
            cvs.delete(lineur2)
        if data['ubb']<=40 and data['ubb']>=1:
            cvs.delete(lineubb)
        cvs.delete(line_0,line_1,line_2,line_3,line_4,oval_1,)        
        for i in range(len(data['setx'])):
            cvs.delete(spoint[i])
        
        spoint.clear()
        '''
        while True:
         
            r=0
            client = mqtt.Client("ddg") #create new instance要記得更改，隨便一個id都可以
            datam=client.on_message=on_message #attach function to callback
            client.connect(broker_address) #connect to broker
            client.subscribe("ulcar/toby")
            client.loop_start() #start the loop
            time.sleep(0.5)
            client.loop_stop()
            if r==5 :
                f=open('小小5.txt','a')
                f.write(datam)
                f.write('\n')
                f.close()
                data=eval(datam)
                print(data)
                break
        '''
        data=givedataul.getdata()
        #刪除要重繪的東西
      #刪除!!
    #data=givedataul.getdata()   
    win.mainloop()
    win.bind("<Destroy>", _destroy)        


def animate(win):
    tk.Canvas.cvs.update()
    
if __name__ == "__main__":
    #sort_data.Open()
    
    #先讀取幾次把剛開機不完整的資料讀取掉
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