# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:47:15 2018

@author: theod
"""
import sys
sys.append(r'C:\Users\theod\OneDrive\Documents\python army of functions2\bond_price_project\risky_bond_and_CDS')
from first_to_default_swap import price_FtD_swap1
from last_to_default_swap import price_LtD_swap1
from CDS_price import price_CDS
#%%
def test_FtD_swap_price():
    FV1,FV2,c,T,rate,lbd1,lbd2,R1,R2,freq = 100,100,0.02,5,0.05,0.3,0.4,0.4,0.4,1
    print(price_FtD_swap1(FV1,FV2,c,T,rate,lbd1,lbd2,R1,R2,freq))
    print(price_LtD_swap1(FV1,FV2,c,T,rate,lbd1,lbd2,R1,R2,freq))
    print(price_CDS(FV1,c,T,rate,lbd1,R1,freq))
    print(price_CDS(FV2,c,T,rate,lbd2,R2,freq))
test_FtD_swap_price()
#%%
def test_FtD_LtD_CDS_prices():
    FV1,FV2,c,T,rate,lbd1,lbd2,R1,R2,freq = 100,100,0.02,5,0.05,0.3,0.4,0.4,0.4,1
    intensities1 = ([0.5],[0.3,0.3])
    intensities2 = ([0.5],[0.4,0.4])
    from first_to_default_swap import price_FtD_swap2
    from last_to_default_swap import price_LtD_swap2
    from CDS_price2 import price_CDS2
    x1 = price_FtD_swap2(FV1,FV2,c,T,rate,lbd1,lbd2,R1,R2,freq)
    x2 = price_LtD_swap2(FV1,FV2,c,T,rate,lbd1,lbd2,R1,R2,freq)
    x3 = price_CDS2(FV1,c,T,rate,lbd1,R1,freq,option = "clean")
    x4 = price_CDS2(FV2,c,T,rate,lbd2,R2,freq,option = "clean")
    print(x1,x2,x3,x4,x1+x2-x3-x4)
    from first_to_default_swap import price_FtD_swap3
    from last_to_default_swap import price_LtD_swap3
    x5 = price_FtD_swap3(FV1,FV2,c,T,rate,intensities1,intensities2,R1,R2,freq)
    x6 = price_LtD_swap3(FV1,FV2,c,T,rate,intensities1,intensities2,R1,R2,freq)
    x7 = price_CDS2(FV1,c,T,rate,intensities1,R1,freq)
    x8 = price_CDS2(FV2,c,T,rate,intensities2,R2,freq)
    print(x5,x6,x7,x8,x5+x6-x7-x8)
test_FtD_LtD_CDS_prices()
#%%