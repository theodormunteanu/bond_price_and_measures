# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:48:55 2018

@author: theod
"""

import sys
sys.path.append(r'C:\Users\theod\OneDrive\Documents\python army of functions2\bond_price_project\bond_measures')
from bond_portfolio import bond_portfolio_price,bond_portfolio_duration as bpd
from bond_class import bond
from duration_hedging import duration_hedge,duration_convexity_hedge
from bond_portfolio import bond_portfolio_price_change as bpp_chg
#%%
def duration_hedge_test():
    face_values,coupons,maturities,frequences = [100,100],[0.04,0.06],[1,2],[1,1]
    rate = [0.09,0.11]
    b1 = bond(face_values[0],coupons[0],maturities[0],frequences[0])
    b2 = bond(face_values[1],coupons[1],maturities[1],frequences[1])
    price1 = b1.price(rate[0],0,0)
    price2 = b2.price(rate[1],0,0)
    print(price1,price2)
    dur1 = b1.duration(price1,0,0,0,rate[0]) 
    dur2 = b2.duration(price2,0,0,0,rate[1])
    print(dur1,dur2)
duration_hedge_test()
#%%
def duration_hedge_test2():
    face_values,coupons,maturities,frequences = [100,100],[0.04,0.06],[1,2],[1,1]
    rate = [0.09,0.11]
    print(duration_hedge(face_values,coupons,maturities,frequences,0,None,0,\
                         0,rate))
duration_hedge_test2()
#%%
def duration_hedge_test3():
    face_values,coupons,maturities,frequences = [100,100],[0.04,0.06],[1,2],[1,1]
    rate = [0.09,0.11]
    q = duration_hedge(face_values,coupons,maturities,frequences,0,None,0,\
                         0,rate)
    print(bpp_chg(face_values,coupons,maturities,frequences,0.001,rate,0,0,[1,q]))
duration_hedge_test3()
#%%
def duration_hedge_test4():
    face_values,coupons = [100,100,100],[0.04,0.06,0.08]
    maturities,frequences = [1,2,3],[1,1,1]
    rate = [0.09,0.11,0.12]
    [q1,q2]= duration_convexity_hedge(face_values,coupons,maturities,frequences,0,None,0,0,rate).tolist()
    print(bpp_chg(face_values,coupons,maturities,frequences,0.001,rate,0,0,[1,q1,q2]))
    print(bpp_chg(face_values,coupons,maturities,frequences,0.05,rate,0,0,[1,q1,q2]))
    print(q1,q2)
    print(bpd(face_values,coupons,maturities,frequences,0,None,0,0,rate))
    print(bpd(face_values,coupons,maturities,frequences,0,None,0,0,rate,[1,q1,q2]))
duration_hedge_test4()
#%%