# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 23:22:24 2021

@author: willy

give_data
"""

with open("202106251126避障測試7.txt", "r", encoding="utf8") as fp:
    datastrlist = fp.readlines()
a=0

def getdata():
    global a
    a=a+1
    data = eval(datastrlist[a])
    return(data)
    


