# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 22:23:37 2018

@author: theod
"""

r"""

This is the case when the number of zero-rates to be found is equal to the number
of instruments whose data we have at disposition.
"""
import sys
sys.path.append(r'C:\Users\theod\OneDrive\Documents\python army of functions2\bond_price_project\bond_measures')
sys.path.append(r'C:\Users\theod\OneDrive\Documents\python army of functions2\bond_price_project\risky_bond_and_CDS')
import numpy as np
import scipy.optimize as optim
#%%
def bootstrap1_test():
    r"""
    This is an example of bootstrapping 2 zero rates from 2 bond prices
    """
    FV,c1,c2,rates,T,freq = 100,0.06,0.08,([0.5,1],[0.04,0.06]),1,2
    from bond_prices import bond_price
    prix1 = bond_price(FV,c1,T,rates,freq)
    prix2 = bond_price(FV,c2,T,rates,freq)
    print(prix1,prix2)
    f = lambda r:[3*np.exp(-r[0]/2)+103*np.exp(-r[1])-99.5,4*np.exp(-r[0]/2)+104*np.exp(-r[1])-101.5]
    g = [lambda r:bond_price(FV,c1,T,(rates[0],r.tolist()),freq), \
         lambda r:bond_price(FV,c2,T,(rates[0],r.tolist()),freq)]
    l = optim.fsolve(f,np.zeros((1,2)))
    l2 = optim.fsolve(g,np.array([0,0]))
    print(l,type(l))
    print(l2)
    print(bond_price(FV,c1,T,([0.5,1],l.tolist()),freq))
bootstrap1_test()
#%%
def bootstrap2_test():
    FV,c1,c2,rates,T,freq = 100,0.06,0.08,([0.5,1],[0.04,0.06]),1,2
    from bond_prices import bond_price
    g = lambda r: [bond_price(FV,c1,T,(rates[0],r),freq),bond_price(FV,c2,T,(rates[0],r),freq)]
    print(g([0.04,0.06]))
bootstrap2_test()