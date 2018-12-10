# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 12:19:16 2018

@author: theod
"""

import sys
sys.path.append(r'C:\Users\theod\OneDrive\Documents\python army of functions2\bond_price_project\forward_rates')
from forward_rate_curve import forward_rates,forward_rates2
from FRA import FRA_price
#%%
def test_fwd_rates():
    r"""
    Description:
    -----------
    
    Given the zero_rates and maturities represented by `rates` and `times` 
    we find a list of forward rates and then the `curve` interpolated from them. 
    
    We use the forward_rates function from forward_rate_curve package. 
    """
    import numpy as np
    times = range(1,6)
    rates = np.array([3.0,4.0,4.6,5.0,5.3])/100
    freq = 1
    print(forward_rates(times,rates))
    curve = forward_rates(times,rates,freq,1)
    curve2 = forward_rates(times,rates,0,1)
    print(curve(1,2),curve2(1,2))
    print(forward_rates2(times,rates))
    print(forward_rates2(times,rates,1))
test_fwd_rates()
#%%
def test_fwd_price():
    import numpy as np
    times = range(1,6)
    rates = np.array([3.0,4.0,4.6,5.0,5.3])/100
    L,RK,T1,T2,freq = 10**8,0.06,1,2,1
    print(FRA_price(L,times,rates,RK,T1,T2,freq))
test_fwd_price()
#%%