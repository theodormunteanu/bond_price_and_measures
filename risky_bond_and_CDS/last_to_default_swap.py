# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 15:02:15 2018

@author: theod
"""

def price_LtD_swap1(FV1,FV2,c,T,rate,lbd1,lbd2,R1,R2,freq = 4,t=0,freq2 = 0):
    r"""
    We have 2 credit entities
    I will assume that the default times are exponentially distributed. 
    The credits can have two different notionals or recovery rates.
    
    """
    import numpy as np
    import scipy.integrate as integrate
    def times(t,T,freq = 4):
        r"The above function gives the times of cash-flows posterior to time t"
        if freq*(T-t)==int(freq*(T-t)):
            k = freq*(T-t)-1
        else:
            k = int(freq*(T-t))
        return np.linspace(T-k/freq,T,(k+1),endpoint = True)
    time_points = times(t,T,freq)
    k = len(time_points)
    cash_flows1 = [c/freq*FV1]*k
    cash_flows1[-1]=cash_flows1[-1]+FV1
    cash_flows2 = [c/freq*FV2]*k
    cash_flows2[-1]=cash_flows2[-1]+FV2
    f1,f2 = lambda u:lbd1 * np.exp(-lbd1 *u),lambda u:lbd2 * np.exp(-lbd2*u)
    F1,F2 = lambda u:1-np.exp(-lbd1*u),lambda u: 1-np.exp(-lbd2 *u)
    pdf_second = lambda u:f1(u)*F2(u)+F1(u)*f2(u)
    surv_std = lambda u:1-F1(u)*F2(u)
    if isinstance(rate,(int,float)):
        f = lambda u:np.exp(-rate*u)
        integrator = lambda u: f(u)*pdf_second(u)
        q1 = (1-R1)*FV1 * integrate.quad(integrator,t,T)[0]* lbd1/(lbd1+lbd2)
        q2 = (1-R2)*FV2 * integrate.quad(integrator,t,T)[1] * lbd2/(lbd1+lbd2)
        if freq2==0:
            disc_rates = [np.exp(-rate*(time_points[i]-t)) for i in range(k)]
        else:
            disc_rates = [1/(1+rate/freq2)**(freq2*(time_points[i]-t)) for i in range(k)]
        survivs = [surv_std(time_points[i]-t) for i in range(len(time_points))]
        q3a = np.dot(np.array(disc_rates)*np.array(survivs),np.array(cash_flows1))
        q3b = np.dot(np.array(disc_rates)*np.array(survivs),np.array(cash_flows2))
        return q1 + q2 - (q3a * lbd2/(lbd1+lbd2) +q3b * lbd1/(lbd1+lbd2))
    elif isinstance(rate,tuple) and all(isinstance(x,list) for x in rate):
        app_rates = np.interp(T-t,rate[0],rate[1])
        f = lambda u:np.exp(-(u-t)*np.interp(u-t,rate[0],rate[1]))
        integrator = lambda u: f(u)*pdf_second(u)
        app_rates = [np.interp(time_points[i]-t,rate[0],rate[1])\
                         for i in range(k)]
        if freq2==0:
            disc_rates = [np.exp(-app_rates[i]*(time_points[i]-t)) for i in range(k)]
        else:
            disc_rates = [1/(1+app_rates[i]/freq2)**(freq2*(time_points[i]-t)) for i in range(k)]
        survivs = [surv_std(time_points[i]-t) for i in range(len(time_points))]
        q3a = np.dot(np.array(disc_rates)*np.array(survivs),np.array(cash_flows1))
        q3b = np.dot(np.array(disc_rates)*np.array(survivs),np.array(cash_flows2))
        return q1 + q2 - (q3a * lbd2/(lbd1+lbd2) +q3b * lbd1/(lbd1+lbd2))

#%%
def price_LtD_swap2(FV1,FV2,c,T,rate,lbd1,lbd2,R1,R2,freq = 4,t=0,freq2 = 0):
    r"""
    We have 2 credit entitites
    
    I will assume that the default times are exponentially distributed. 
    
    The credits can have two different notionals or recovery rates.
    """
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
    def surv_ltd(u):
        return np.exp(-lbd1*(u-t))+np.exp(-lbd2*(u-t))-np.exp(-(lbd1+lbd2)*(u-t))
    def pdf_ltd(u):
        return lbd1 * np.exp(-lbd1*(u-t)) + lbd2*np.exp(-lbd2*(u-t)) - \
               (lbd1 + lbd2)*np.exp(-(lbd1+lbd2)*(u-t))
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
        survivs = [surv_ltd(u) for u in time_points]
        discounts = [discount(u) for u in time_points]
        return h*np.dot(survivs,discounts)
    fct = lambda u: discount(u)*pdf_ltd(u)
    discounted_leg = ((1-R1)*FV1 * lbd2/(lbd1+lbd2)+\
                      (1-R2)*FV2*lbd1/(lbd1+lbd2))*integrate.quad(fct,t,T)[0]
    premium_leg = c*(FV1*lbd1/(lbd1+lbd2)+FV2 * lbd2/(lbd1+lbd1))*RPV01()
    return discounted_leg - premium_leg

#%%
def price_LtD_swap3(FV1,FV2,c,T,rate,intensities1,intensities2,R1,R2,freq = 4,t=0,freq2 = 0):
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
    from piecewise_expo import piecewise_exponential
    model1 = piecewise_exponential(intensities1[0],intensities1[1])
    model2 = piecewise_exponential(intensities2[0],intensities2[1])
    def surv_ltd(u):
        return 1-model1.cdf2(u-t)*model2.cdf(u-t)
    def pdf_ltd(u):
        return model1.pdf2(u-t)*model2.cdf(u-t)+model1.cdf2(u-t)*model2.pdf2(u-t)
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
        survivs = [surv_ltd(u) for u in time_points]
        discounts = [discount(u) for u in time_points]
        return h*np.dot(survivs,discounts)
    fct1 = lambda y: model1.cdf2(y) * model1.pdf2(y)
    proba = integrate.quad(fct1,0,np.Inf)[0]
    fct2 = lambda u:discount(u)*pdf_ltd(u)
    discounted_leg = ((1-R2)*FV2*proba + (1-R1)*FV1*(1-proba))*integrate.quad(fct2,t,T)[0]
    premium_leg = c*(FV2*proba + FV1*(1-proba))*RPV01()
    return discounted_leg - premium_leg