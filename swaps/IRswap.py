# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 09:40:18 2018

@author: theod
"""

import sys
sys.path.append(r'C:\Users\frup74094\Documents\python army of functions2\bond_price_project\bond_measures')
from bond_prices import bond_price
#%%
def IRS_price(FV,c,T,rate,libor,freq = 4, t = 0, freq2=0,option = 'floating payer'):
    r"""
    Description:
    -----------
    
    This function builds the price of an interest rate swap. 
    """
    p1 = bond_price(FV,c,T,rate,freq,t,freq2)
    def times(t,T,freq):
        if freq*(T-t)==int(freq*(T-t)):
            k = freq*(T-t)-1
        else:
            k = int(freq*(T-t))
        import numpy as np
        return np.linspace(T-k/freq,T,(k+1),endpoint = True)
    time_points = times(t,T,freq)
    p2 = bond_price(FV,libor,time_points[0]-t,rate,freq,0,freq2)
    return p1-p2

def swap_rate(FV,T,rate,libor,freq = 4, t=0,freq2 = 0):
    f = lambda c: IRS_price(FV,c,T,rate,libor,freq,t,freq2)
    import scipy.optimize as opt
    return opt.newton(f,0)

def test_IRS():
    FV,c,T,rate = 100,0.07,10/12,0.05
    libor,freq,freq2 = 0.046,2,0
    print(IRS_price(FV,c,T,rate,libor,freq,0,freq2))
    c2,T2,rate2 = 0.08,15/12,([3/12,9/12,15/12],[0.1,0.105,0.11])
    libor2 = 0.102
    print(IRS_price(FV,c2,T2,rate2,libor2,freq,0,freq2))
    print(swap_rate(FV,T2,rate2,libor2,freq,0,freq2))
test_IRS()
#%%