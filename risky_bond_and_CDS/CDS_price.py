# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 17:13:49 2018

@author: theod
"""

from risky_bond_prices import risky_bond_price
from piecewise_expo import piecewise_exponential
#%%
def price_CDS(FV,c,T,rate,intensities,R,freq=4,t=0,freq2=0):
    import numpy as np
    import scipy.integrate as integrate
    if isinstance(rate,(float,int)):
        discount = np.exp(-rate*(T-t))
        f = lambda u:np.exp(-rate*(u-t))
        if isinstance(intensities,(float,int)):
            surv = np.exp(-intensities*(T-t))
            g = lambda u:np.exp(-intensities*(u-t))*intensities
            h = lambda u:f(u)*g(u)
        elif isinstance(intensities,tuple) and all(isinstance(x,list) for x in intensities):
            model = piecewise_exponential(intensities[0],intensities[1])
            surv = model.survival2(T-t)
            g = lambda u: model.pdf2(u-t)
            h = lambda u: f(u)*g(u)
    elif isinstance(rate,tuple) and all(isinstance(x,list) for x in rate):
        app_rate = np.interp(T-t,rate[0],rate[1])
        discount = np.exp(-app_rate*(T-t))
        f = lambda u:np.exp(-np.interp(u-t,rate[0],rate[1])*(u-t))
        if isinstance(intensities,(float,int)):
            surv = np.exp(-intensities*(T-t))
            g = lambda u:np.exp(-(u-t)*intensities)*intensities
            h = lambda u:f(u)*g(u)
        elif isinstance(intensities,tuple) and all(isinstance(x,list) for x in intensities):
            model = piecewise_exponential(intensities[0],intensities[1])
            surv = model.survival2(T-t)
            g = lambda u: model.pdf2(u-t)
            h = lambda u:f(u)*g(u)
    return FV*(discount*surv + integrate.quad(h,t,T)[0]) - \
                   risky_bond_price(FV,c,T,rate,intensities,R,freq,t,freq2)
            