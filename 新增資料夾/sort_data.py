# -*- coding: utf-8 -*-
"""
sort_data
20210109 pm0731

讀取巡航車socket回傳的資料
並整理

修改0109
增加if __name__=='__main__':
    的try以自動嘗試連線10次 間隔5S
修改0110 1418
增加if __name__=='__main__':
    的檔名功能自訂


"""

import socketreaddata
import time
import pprint

#rpiIP = '192.168.0.146' #車載rpi3b+於R303_24E-01GHz
#rpiIP = '192.168.100.2' #車載rpi3b+於IDSLab-307
rpiIP = '192.168.100.3' #車載rpi3b+於IDSLab-307

fpname = time.strftime('%Y%m%d%H%M', time.localtime())#以日期時間做存檔名稱
fpnamemark = ''  #可額外輸入的標記
datastr = ""

#(下)馬達-mega-座標-rpi
#data_dict = {'Tem': 0.0, 'Hum': 0.0, 'Pressure': 0.0, 'v': 0.0, 'WindSpeed': 0.0, 'CO2': 0, 'mgt': 0, 'OfA1': 0, 'OfB1': 0, 'dir1': 0, 'TfA1': 0, 'TfB1': 0, 'FA1': 0, 'FB1': 0, 'pwmA1': 0, 'pwmB1': 0, 'over1': 0, 'pM1': 0, 'OfA2': 0, 'OfB2': 0, 'dir2': 0, 'TfA2': 0, 'TfB2': 0, 'FA2': 0, 'FB2': 0, 'pwmA2': 0, 'pwmB2': 0, 'over2': 0, 'pM2': 0, 'roll_eul': 0.00, 'pitch_eul': 0.00, 'yaw_eul': 0.00, 'rpitime': 0.00, 'x': '0', 'y': '0', 'z': '0', 'rem_dist': 0.00, 'vv_norm': 0.00, 'angle_vv': 0.00, 'angle_1': 0.00, 'Yaw_deg': 0.00, 'stage': -2, 'message': '無', 'a': -1, 'round': 0}
#(下)不預設

data_dict = {'a':-1}

a = -1
data = b''
olddata = b''
datastr_list = []

def setIP(IP):
    socketreaddata.setIP(IP)

def getdata():
    global a
    global datastr
    global data_dict
    global datastr_list
    global olddata
    global fpnamemark
    data = socketreaddata.readdata()
    data = olddata+data
    if data != b'':
        #print(data)
        flag = 1 if data[-1]=='\n' else 0  #判斷有沒有傳完整一句話
        try:
            dast = data.decode()  #bytes轉str，因為有時遇到中文編碼不在ascii之內，一句話沒傳完整就無法解析，所以要用try
            olddata = b''  #成功解析則清空
            #print('data:\n',data)
            #print('dast:\n',dast)
            #with open(fpname, "a", encoding="utf8") as fp:
            #    fp.write(dast)
            datastr = datastr + dast  #上次剩下的字串與這次的串起來
            datastr_list = datastr.split('\r\n'or'\n')  #根據換行符切段(以list儲存)
            datastr='' if flag else datastr_list.pop()  #沒傳完整的話，最後一個字串要留下
            #字串資料轉成字典，並以後來的覆蓋先前的
        except:
            olddata=data  #解析失敗則保存(中文字可能被切段)，等待與下次的資料串起來
            
        for dst in datastr_list:
            try:
                dsd = eval(dst)  #表達式轉字典(因為發來的應該是字典)
                data_dict = {**data_dict,**dsd}
            except:
                pass
        #print(data_dict)
        if data_dict['a'] > a:
            a=data_dict['a']
            with open(fpname+fpnamemark+'.txt', "a", encoding="utf8") as fp:
                fp.write(repr(data_dict)+'\n')
                print("寫入")
        return(data_dict)
    
def Open():
    global fpnamemark
    fpnamemark = input('請輸入檔名標記\n')
    for n in range(0,20):
        try:
            socketreaddata.setIP(rpiIP)
            break
        except:
            time.sleep(5)
    
if __name__=='__main__':
    Open()
    while True:
        datar = getdata()
        #print(datar['x'],datar['y'],datar['yaw_eul'])
        pprint.pprint(datar,sort_dicts=False)
        print()

"""
完整的資料範例 1100323

{'a': 169,    迴圈計數
 'OfA2': 15,  要求頻率 A指馬達 1指馬驅
 'OfB2': 15,  要求頻率 A指馬達 1指馬驅
 'dir': 0,  
 'pwmB2': 65,  B馬達2馬驅的PWM
 'over2': 14,  馬驅2過電流計數
 'pM2': 6011097,  馬驅2的時鐘
 'rpitime': 6014.71,  RPI的時間
 'x': '3.32',  座標
 'y': '1.44',  座標
 'z': '-0.01',  座標
 'Anchor No': ['AN0', 'AN1', 'AN2', 'AN3'],  Anchor編號
 'AID': ['1D33', '4090', '4097', '86AE'],  Anchor ID
 'Ax': ['4.04', '0.00', '0.00', '8.08'],  Anchor 座標
 'Ay': ['0.00', '0.00', '4.04', '4.04'],  Anchor 座標
 'Az': ['1.00', '1.00', '1.00', '1.00'],  Anchor 座標
 'ADist': ['1.91', '3.72', '4.35', '5.33'],   Anchor 距離
 'roll_eul': 1.27,  滾轉角
 'pitch_eul': -0.51,  俯仰角
 'yaw_eul': -86.1,  方向角
 'P0': [3.5, 1.5],  當下起點
 'P1': [5.5, 1.5],  當下終點
 'Pcar': [3.32, 1.44],  車座標
 'Ppro': [3.32, 1.5],  投影點座標
 'Vgo': [0.99, 0.12],  當前目標移動方向的單位向量
 'ADeviation': -17.89,  與目標方向的偏差角
 'reviseLv': 1,  方向修正等級 0無須 1行進間 2原地
 'reviseFlag': 1,  原地修正標記
 'spL': 15,  左輪速度
 'spR': -15,  右輪速度
 'stage': 3,  階段(KP切換)
 'round_count': 0,  繞圈回合技術
 'OfA1': 15,  指令 A指馬達 1指馬驅
 'OfB1': 15,  指令 B指馬達 1指馬驅
 'dir1': 3,  方向
 'TfA1': 315,  目標頻率
 'TfB1': 315,  目標頻率
 'FA1': 360,  當前頻率
 'FB1': 280,  當前頻率
 'pwmA1': 60,  馬達A馬驅1的PWM
 'pwmB1': 40,  馬達B馬驅1的PWM
 'over1': 0,  馬驅1過流計數
 'pM1': 6011181,  馬驅1計時
 'dir2': 3,  馬驅2方向
 'TfA2': 315,  目標頻率馬達A馬驅2
 'TfB2': 315,  目標頻率馬達B馬驅2
 'FA2': 390,  當前頻率馬達A馬驅2
 'FB2': 330,  當前頻率馬達B馬驅2
 'pwmA2': 60}  A馬達2馬驅PWM

"""
    
