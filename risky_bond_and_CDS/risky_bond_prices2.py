# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 22:37:05 2018

@author: theod
"""
from piecewise_expo import piecewise_exponential
#%%
def risky_bond_price(FV,c,T,rate,intensities,R,freq=4,t=0,freq2=0,**options):
    import numpy as np
    import scipy.integrate as integrate
    def times(t,T,freq):
        if freq*(T-t)==int(freq*(T-t)):
            k = freq*(T-t)-1
        else:
            k = int(freq*(T-t))
        return np.linspace(T-k/freq,T,(k+1),endpoint = True)
    def surv(u):
        if isinstance(intensities,(float,int)):
            return np.exp(-intensities*(u-t))
        elif isinstance(intensities,tuple) and all(isinstance(x,list) for x in intensities):
            model = piecewise_exponential(intensities[0],intensities[1])
            return model.survival2(u-t)
    def pdf_exp(u):
        if isinstance(intensities,(float,int)):
            return intensities*np.exp(-intensities*(u-t))
        elif isinstance(intensities,tuple) and all(isinstance(x,list) for x in intensities):
            model = piecewise_exponential(intensities[0],intensities[1])
            return model.pdf2(u-t)
    def discount(u):
        if isinstance(rate,(float,int)):
            if freq2==0:
                return np.exp(-rate*(u-t))
            else:
                return 1/(1+rate/freq2)**(freq2*(u-t))
        elif isinstance(rate,tuple) and all(isinstance(x,list) for x in rate):
            app_rate = np.interp(u-t,rate[0],rate[1])
            if freq2==0:
                return np.exp(-app_rate*(u-t))
            else:
                return 1/(1+app_rate/freq2)**(freq2*(u-t))
    if t==T:
        return FV + (c/freq+1)*FV
    elif t>T or t<0:
        raise TypeError('the time when you want to evaluate the bond surpasses\
                        the lifetime of the bond or it is negative')
    else:
        time_points = times(t,T,freq)
        k = len(time_points)
        cash_flows = [c/freq*FV]*k
        survivs = [surv(u) for u in time_points]
        discounts = [discount(u) for u in time_points]
        q1  = np.dot(np.array(cash_flows)*np.array(discounts),np.array(survivs))
        q2 = FV * discount(T)*surv(T)
        fct = lambda u:discount(u)*pdf_exp(u)
        q3 = integrate.quad(fct,t,T)[0]
        return q1+q2+q3*R*FV