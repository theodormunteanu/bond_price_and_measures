# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 22:24:02 2018

@author: theod
"""

import sys
sys.path.append(r'C:\Users\theod\OneDrive\Documents\python army of functions2\bond_price_project\bond_measures')
import numpy as np
import scipy.optimize as optim
#%%
def bootstrap1(face_values,coupons,lifetimes,times,freqs,bond_prix,t=0,freq2=0,y0 = None):
    r"""
    
    Description:
    --------------
    
    Complete bootstrapping.
    
    
    This function finds the zero rates when the number of unknowns is exactly 
    the number of market prices we have at disposal. 
    
    Parameters:
    ----------
    
    `face_values`: list
                   Face values for the bonds whose prices are given
    
    `coupons`: list
               Annual coupon rates for the bonds whose prices are given
              
    `lifetimes`: list
               The lifetimes of the existing bonds/Money Market Instruments
               existing
    
    `times`: list
             Represents the times for which we find the corresponding zero rates
    
    `freqs`: list
             frequences of payments
    
    `bond_prix`: list
                 Market bond prices from where the bootstrapping is started
    
    For the case when the number of available data is bigger than the parameters
    to be found, please refer to bootstrap2 function. 
    """
    from bond_prices import bond_price
    f = lambda r:[bond_price(face_values[i],coupons[i],lifetimes[i],\
                    (times,r.tolist()),freqs[i],t,freq2) - bond_prix[i] \
        for i in range(len(face_values))]
    if y0==None:
        y0 = np.zeros((1,len(face_values)))
        return optim.fsolve(f,y0)
    else:
        return optim.solve(f,np.array(y0))

#%%
def bootstrap2(face_values,coupons,lifetimes,times,freqs,bond_prix,t=0,freq2 = 0,y0 = None):
    r"""
    Description:
    ---------------------
    Fitting the zero-curve to bond market prices.
    This is not bootstrapping. 
    
    Details:
    ---------------------
    The number of available bond prices is greater than the parameters to be calibrated   
    
    The entire zero-curve is to be determined.
    
    Remarks:
    --------
    For partial bootstrapping, please refer to bootstrap3 function. 
    """
    from bond_prices import bond_price
    f = lambda r:[bond_price(face_values[i],coupons[i],lifetimes[i],\
                    (times,r.tolist()),freqs[i],t,freq2) - bond_prix[i] for i in range(len(face_values))]
    if y0 == None:
        y0 = np.array([0]*len(times))
        res = optim.least_squares(f,y0)        
        return res.x,res.cost
    else:
        res = optim.least_squares(f,y0)
        return res.x,res.cost
#%%
def bootstrap3(face_values,coupons,lifetimes,rates,times,freqs,bond_prix,t=0,freq2 = 0,y0 = None):
    r"""
    Description:
    ---------------
    
    Partial bootstrapping.
    
    Some zero rates are given (represented by `rates`) but these are fewer than the zero rates
    necessary to fully price the bonds (due to the coupon payment frequencies.)
    
    Remark:
    ---------
    
    The number of rates + the number of rates to be found from `bond_prix` will 
    design the extended zero-rate curve. 
    
    
    """