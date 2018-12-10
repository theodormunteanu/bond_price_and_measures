# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 09:25:38 2018

@author: theod
"""

import sys
sys.path.append(r'C:\Users\theod\OneDrive\Documents\python army of functions2\bond_price_project\bond_measures')
from bond_class import bond_portfolio_duration, bond_portfolio_price
#%%
r"""
    1. First I will measure the percentage of portfolio price change when a
    parallel shift in yields or zero-curve is assumed. 
"""

def bond_portfolio_price_change(face_values,coupons,maturities,frequences,chg,\
                                rate,t=0,freq2 = 0,**options):
    price0 = bond_portfolio_price(face_values,coupons,maturities,frequences,\
                                  t,freq2,rate,option = options.get("option"))
    if isinstance(rate,(int,float)):
       price1 = bond_portfolio_price(face_values,coupons,maturities,frequences,\
                                     t,freq2,rate+chg,option = options.get("option"))
       return price1/price0-1
    elif isinstance(rate,(tuple)) and len(rate)==2:
       aux = [rate[1][i]+chg for i in range(len(rate[1]))]
       price1 = bond_portfolio_price(face_values,coupons,maturities,frequences,\
                                     t,freq2,(rate[0],aux),option = options.get("option"))
       return price1/price0-1
    elif isinstance(rate,list):
       aux = [rate[i]+chg for i in range(len(rate))]
       return price1/price0-1


       
    
