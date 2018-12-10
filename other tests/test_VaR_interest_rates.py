# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 14:56:49 2018

@author: theod
"""

def read_data():
    import xlwings as xw
    import numpy as np
    wb = xw.Book('euribor_rates.xlsx')
    sht = wb.sheets['Sheet1']
    data = sht.range('E4:H203').value
    data2 = sht.range('E4:E203').value
    print(data)
    print(type(data))
    print(type(data2))
    print(data2)
    #print(np.array(data))
    x = np.array(data)
    print(type(x))
    y = np.diff(x,axis = 0)
    print(np.mean(y,axis = 0))
    print(np.cov(y,rowvar = 0))
read_data()
#%%