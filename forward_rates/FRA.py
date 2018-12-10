# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 12:36:25 2018

@author: theod
"""

"""
In this file we are defining the price for an FRA (forward rate agreement)


"""
from forward_rate_curve import forward_rates2
#%%
def FRA_price(L,times,rates,RK,T1,T2,freq = 0,option = 'receiver'):
    import numpy as np
    r"""
    Parameters: 
    ----------
    
    `L`: float, int
       principal/notional/face value
    
    `times`,`rates`: the ensemble forming the zero-rate curve
    `RK`: the rate that is agreed to be received/payed
    `T1`,`T2`: the starting date and the end date of payment 
    
    The frequency is determined by the `freq` parameter
    """
    zero_curve = lambda u: np.interp(u,times,rates)
    curve = forward_rates2(times,rates,freq,1)
    fwd_rate = curve(T1,T2)
    print(fwd_rate)
    if option in {'receiver','Receiver',None}:
        return L*(RK - fwd_rate)*(T2-T1)*np.exp(-zero_curve(T2)*T2)
    else:
        return -L*(RK-fwd_rate)*(T2-T1)*np.exp(-zero_curve(T2)*T2)