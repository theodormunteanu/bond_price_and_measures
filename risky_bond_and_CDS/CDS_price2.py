# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 20:16:45 2018

@author: theod
"""
from piecewise_expo import piecewise_exponential
#%%
def price_CDS2(FV,c,T,rate,intensities,R,freq=4,t=0,freq2=0,**options):
    import numpy as np
    import scipy.integrate as integrate
    def times(t,T,freq):
        if freq*(T-t)==int(freq*(T-t)):
            k = freq*(T-t)-1
        else:
            k = int(freq*(T-t))
        return np.linspace(T-k/freq,T,(k+1),endpoint = True)
    h = 1/freq
    time_points = times(t,T,freq)
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
    def RPV01():
        if options.get("option") in {None,"dirty"}:
            survivs = [surv(u) for u in time_points]
            discounts = [discount(u) for u in time_points]
            return h*np.dot(survivs,discounts)
        elif options.get("option") in {"clean","Clean"}:
            survivs = [surv(u) for u in time_points]
            discounts = [discount(u) for u in time_points]
            accruals = [integrate.quad(lambda u:(u-time_points[i])*discount(u)*pdf_exp(u),\
                        time_points[i],time_points[i+1])[0] for i in range(len(time_points)-1)]
            accruals.insert(0,integrate.quad(lambda u:(u-time_points[0]+h)*discount(u)\
                                             *pdf_exp(u),time_points[0]-h,time_points[0])[0])
            return h*np.dot(survivs,discounts)+sum(accruals)
    fct = lambda u: discount(u)*pdf_exp(u)
    discounted_leg = FV * (1-R)*integrate.quad(fct,t,T)[0]
    premium_leg = FV * c * RPV01()
    return discounted_leg - premium_leg