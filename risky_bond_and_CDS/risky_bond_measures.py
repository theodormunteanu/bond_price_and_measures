# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 23:08:34 2018

@author: theod
"""

import sys
sys.path.append(r'C:\Users\theod\OneDrive\Documents\python army of functions2\bond_price_project\bond_measures')
#%%
def bond_yield_spread(FV,c,T,rate,intensities,R,freq=4,t=0,freq2=0,y0=0.0,**options):
    r"""
    
    Parameters:
    ----------
    
    `FV` : float,int
         face value of the (risky) bond
    
    `c`  : float
         annual coupon rate
    `rate`: float, int or tuple of lists
            Represents the zero-rate curve 
    
    Returns:
    --------
    
    `y2`: the non-risky bond yield
    
    `y1`: the risky bond yield
    
    `y2` - `y1`: the credit spread (`s`)
    """
    from risky_bond_prices2 import risky_bond_price
    from bond_duration import bond_yield
    price1 = risky_bond_price(FV,c,T,rate,intensities,R,freq,t,freq2)
    price2 = risky_bond_price(FV,c,T,rate,0,R,freq,t,freq2)
    y1 = bond_yield(FV,c,T,rate,freq,t,freq2,price1,y0)
    y2 = bond_yield(FV,c,T,rate,freq,t,freq2,price2,y0)
    return y2,y1,y1-y2
    