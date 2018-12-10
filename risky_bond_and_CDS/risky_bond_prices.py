# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:03:40 2018

@author: theod
"""

from piecewise_expo import piecewise_exponential
#%%
def risky_bond_price(FV,c,T,rate,intensities,R,freq=4,t=0,freq2 = 0):
    r"""
    `FV` = face value;
    
    `c` = coupon rate;
    
    `rate` : can be tuple of two lists or a numerical value
          If it is tuple then the first component is the maturities and the second
          component is formed of the zero rates
    
          If it is numerical value, then it means all cash-flows are discounted 
          with the same interest rate
    """
    if isinstance(rate,(float,int)):
        if isinstance(intensities,(float,int)):
            return risky_bond_price1(FV,c,T,rate,intensities,R,freq,t,freq2)
        elif isinstance(intensities,tuple) and all(isinstance(x,list) for x in intensities):
            return risky_bond_price3(FV,c,T,rate,intensities,R,freq,t,freq2)
    elif isinstance(rate,tuple) and all(isinstance(x,list) for x in rate):
        if isinstance(intensities,(float,int)):
            return risky_bond_price2(FV,c,T,rate,intensities,R,freq,t,freq2)
        elif isinstance(intensities,tuple) and all(isinstance(x,list) for x in intensities):
            return risky_bond_price4(FV,c,T,rate,intensities,R,freq,t,freq2)
#%%
def risky_bond_price1(FV,c,T,r,lbd,R,freq=4,t=0,freq2 = 0):
    r"""
    `FV` : float
          Face Value/Nominal of the bond
    
    `c`: float 
         coupon rate (must be between 0 and 1)
    
    `R`: float
         Recovery rate
    
    `lbd`: float
           Default Intensity
           
    `r`: float
         flat term interest rate
    
    `T`: float/int
         Lifetime of the bond
         
    `t`: float/int (Default: 0)
        :current time of evaluation of the bond
    
    `freq`: int
           frequency of coupon payments
           
    `freq2`: int
             frequency of compounding the risk-free rate
    
    """
    def times(t,T,freq = 4):
        r"The above function gives the times of cash-flows posterior to time t"
        if freq*(T-t)==int(freq*(T-t)):
            k = freq*(T-t)-1
        else:
            k = int(freq*(T-t))
        import numpy as np
        return np.linspace(T-k/freq,T,(k+1),endpoint = True)
    import numpy as np
    if t==T:
        return FV + (c/freq+1)*FV
    elif t>T or t<0:
        raise TypeError('the time when you want to evaluate the bond surpasses\
                        the lifetime of the bond or it is negative')
    else:
        time_points = times(t,T,freq)
        k = len(time_points)
        if freq2==0:
            disc_rates = [np.exp(-r*(time_points[i]-t)) for i in range(k)]
        else:
            disc_rates = [1/(1+r/freq2)**(freq2*(time_points[i]-t)) for i in range(k)]
        cash_flows = [c/freq*FV]*k
        cash_flows[-1]=cash_flows[-1]+FV
        survivs = [np.exp(-lbd*(time_points[i]-t)) for i in range(k)]
        a = np.dot(np.array(disc_rates)*np.array(survivs),np.array(cash_flows))
        b = R*FV*lbd/(r+lbd)*(1-np.exp(-(r+lbd)*(T-t))) if (r!=0 or lbd!=0) else 0
        return a+b
#%%
        
def risky_bond_price2(FV,c,T,rates,lbd,R,freq = 4,t=0,freq2=0):
    r"""
    We assume zero-rate curve and constant exponential model for time of default
    """
    def times(t,T,freq = 4):
        r"The above function gives the times of cash-flows posterior to time t"
        if freq*(T-t)==int(freq*(T-t)):
            k = freq*(T-t)-1
        else:
            k = int(freq*(T-t))
        import numpy as np
        return np.linspace(T-k/freq,T,(k+1),endpoint = True)
    import numpy as np
    if t==T:
        return FV + (c/freq+1)*FV
    elif t>T or t<0:
        raise TypeError('the time when you want to evaluate the bond surpasses\
                        the lifetime of the bond or it is negative')
    else:
        import scipy.integrate as integrate
        time_points = times(t,T,freq)
        k = len(time_points)
        app_rates = [np.interp(time_points[i]-t,rates[0],rates[1])\
                         for i in range(k)]
        if freq2==0:
            disc_rates = [np.exp(-app_rates[i]*(time_points[i]-t)) for i in range(k)]
        else:
            disc_rates = [1/(1+app_rates[i]/freq2)**(freq2*(time_points[i]-t)) for i in range(k)]
        cash_flows = [c/freq*FV]*k
        cash_flows[-1]=cash_flows[-1]+FV
        survivs = [np.exp(-lbd*(time_points[i]-t)) for i in range(k)]
        a = np.dot(np.array(disc_rates)*np.array(survivs),np.array(cash_flows))
        f = lambda u: np.exp(-(u-t)*np.interp(u-t,rates[0],rates[1]))
        g = lambda u: lbd*np.exp(-lbd*(u-t))
        h = lambda u:f(u)*g(u)
        b = R*FV*integrate.quad(h,t,T)[0]
        return a+b
#%%
def risky_bond_price3(FV,c,T,r,intensities,R,freq=4,t=0,freq2 = 0):
    def times(t,T,freq = 4):
        r"The above function gives the times of cash-flows posterior to time t"
        if freq*(T-t)==int(freq*(T-t)):
            k = freq*(T-t)-1
        else:
            k = int(freq*(T-t))
        import numpy as np
        return np.linspace(T-k/freq,T,(k+1),endpoint = True)
    import numpy as np
    if t==T:
        return FV + (c/freq+1)*FV
    elif t>T or t<0:
        raise TypeError('the time when you want to evaluate the bond surpasses\
                        the lifetime of the bond or it is negative')
    else:
        import scipy.integrate as integrate
        time_points = times(t,T,freq)
        k = len(time_points)
        if freq2==0:
            disc_rates = [np.exp(-r*(time_points[i]-t)) for i in range(k)]
        else:
            disc_rates = [1/(1+r/freq2)**(freq2*(time_points[i]-t)) for i in range(k)]
        cash_flows = [c/freq*FV]*k
        cash_flows[-1]=cash_flows[-1]+FV
        model = piecewise_exponential(intensities[0],intensities[1])
        survivs = [model.survival2(time_points[i]-t) for i in range(len(time_points))]
        a = np.dot(np.array(disc_rates)*np.array(survivs),np.array(cash_flows))
        f = lambda u: np.exp(-r*(u-t))
        g = lambda u: model.pdf2(u-t)
        h = lambda u: f(u)*g(u)
        b = R*FV*integrate.quad(h,t,T,args=(),full_output = 1)[0]
        return a+b
#%%
def risky_bond_price4(FV,c,T,rates,intensities,R,freq=4,t=0,freq2=0):
    def times(t,T,freq = 4):
        r"The above function gives the times of cash-flows posterior to time t"
        if freq*(T-t)==int(freq*(T-t)):
            k = freq*(T-t)-1
        else:
            k = int(freq*(T-t))
        import numpy as np
        return np.linspace(T-k/freq,T,(k+1),endpoint = True)
    import numpy as np
    if t==T:
        return FV + (c/freq+1)*FV
    elif t>T or t<0:
        raise TypeError('the time when you want to evaluate the bond surpasses\
                        the lifetime of the bond or it is negative')
    else:
        import scipy.integrate as integrate
        time_points = times(t,T,freq)
        k = len(time_points)
        app_rates = [np.interp(time_points[i]-t,rates[0],rates[1])\
                         for i in range(k)]
        if freq2==0:
            disc_rates = [np.exp(-app_rates[i]*(time_points[i]-t)) for i in range(k)]
        else:
            disc_rates = [1/(1+app_rates[i]/freq2)**(freq2*(time_points[i]-t)) for i in range(k)]
        cash_flows = [c/freq*FV]*k
        cash_flows[-1]=cash_flows[-1]+FV
        model = piecewise_exponential(intensities[0],intensities[1])
        survivs = [model.survival(time_points[i]-t) for i in range(len(time_points))]
        a = np.dot(np.array(disc_rates)*np.array(survivs),np.array(cash_flows))
        f = lambda u: np.exp(-(u-t)*np.interp(u-t,rates[0],rates[1]))
        g = lambda u: model.pdf2(u-t)
        h = lambda u: f(u)*g(u)
        b = R*FV*integrate.quad(h,t,T,args=(),full_output = 1)[0]
        return a+b
