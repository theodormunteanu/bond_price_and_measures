# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 03:07:58 2018

@author: theod
"""
#%%
def bond_price_bis(FV,c,T,rate,freq = 4,t=0,**opt):
    if isinstance(rate,tuple) and isinstance(rate[0],list) and isinstance(rate[1],list):
       if opt.get("option") in {"dirty price",None}:
          return bond_price3(FV,c,T,rate,freq,t,discounting = opt.get("discounting"))
       elif opt.get("option") == "clean price":
          return bond_price3(FV,c,T,rate,freq,t,discounting = opt.get("discounting"))-\
                 accrued_coupon(FV,c,t,T,freq)
    elif isinstance(rate,(int,float)):
       if opt.get("option") in {"dirty price",None}:
          return bond_price2(FV,c,T,rate,freq,t,discounting=opt.get("discounting"))
       elif opt.get("option")=="clean price":
          return bond_price2(FV,c,T,rate,freq,t,discounting = opt.get("discounting"))-\
                 accrued_coupon(FV,c,t,T,freq)
#%%
def bond_price1(FV,c,T,r,freq = 4,**opt):
    import numpy as np
    k = int(T*freq)
    times = np.linspace(1/freq,T,k,endpoint = True)
    cash_flows = [c/freq * FV] * k
    cash_flows[-1] = cash_flows[-1]+FV
    d = opt.get("discounting")
    if d in {"continuous",None}:
        disc_rates = [np.exp(-r*times[i]) for i in range(k)]
    elif d=="yearly":
        disc_rates = [1/(1+r)**(i/freq) for i in range(1,k+1)]
    elif d=="semi-annually":
        disc_rates = [1/(1+r/2)**(2*i/freq) for i in range(1,k+1)]
    elif d == "quarterly":
        disc_rates = [1/(1+r/4)**(4*i/freq) for i in range(1,k+1)]
    elif d=="monthly":
        disc_rates = [1/(1+r/12)**(12*i/freq) for i in range(1,k+1)]
    return np.dot(disc_rates,np.array(cash_flows))

#%%
def bond_price2(FV,c,T,r,freq=4,t=0,**opt):
    def times(t,T,freq = 4):
        if freq*(T-t)==int(freq*(T-t)):
            k = freq*(T-t)-1
        else:
            k = int(freq*(T-t))
        import numpy as np
        return np.linspace(T-k/freq,T,(k+1),endpoint = True)
    'The above function gives the times of cash-flows posterior to time t'
    import numpy as np
    if t==T:
        return FV + (c/freq+1)*FV
    elif t>T or t<0:
        raise TypeError('the time when you want to evaluate the bond surpasses\
                        the lifetime of the bond or it is negative')
    else:
        time_points = times(t,T,freq)
        k = len(time_points)
        d = opt.get("discounting")
        if d in {"continuous",None}:
            disc_rates = [np.exp(-r*(time_points[i]-t)) for i in range(k)]
        elif d=="yearly":
            disc_rates = [1/(1+r)**(time_points[i]-t) for i in range(k)]
        elif d=="semi-annually":
            disc_rates = [1/(1+r/2)**(2*(time_points[i]-t)) for i in range(k)]
        elif d=="quarterly":
            disc_rates = [1/(1+r/4)**(4*(time_points[i]-t)) for i in range(k)]
        elif d=="monthly":
            disc_rates = [1/(1+r/12)**(12*(time_points[i]-t)) for i in range(k)]
        cash_flows = [c/freq*FV]*k
        cash_flows[-1]=cash_flows[-1]+FV
        return np.dot(disc_rates,np.array(cash_flows))

"This function makes useless the other function bond_price1 because it is a \
particular case of the 2nd function"
#%%
def bond_price3(FV,c,T,rates,freq=4,t=0,**opt):
    import numpy as np
    def times(t,T,freq = 4):
        if freq*(T-t)==int(freq*(T-t)):
            k = freq*(T-t)-1
        else:
            k = int(freq*(T-t))
        return np.linspace(T-k/freq,T,(k+1),endpoint = True)
    if t==T:
        return FV + (c/freq+1)*FV
    elif t>T or t<0:
        raise TypeError('the time when you want to evaluate the bond surpasses\
                        the lifetime of the bond or it is negative')
    else:
        time_points = times(t,T,freq)
        k = len(time_points)
        app_rates = [np.interp(time_points[i],rates[0],rates[1])\
                         for i in range(k)]
        d = opt.get("discounting")
        if d in {"continuous",None}:
            disc_rates = [np.exp(-app_rates[i]*(time_points[i]-t)) for i in range(k)]
        elif d=="yearly":
            disc_rates = [1/(1+app_rates[i])**(time_points[i]-t) for i in range(k)]
        elif d=="semi-annually":
            disc_rates = [1/(1+app_rates[i]/2)**(2*(time_points[i]-t)) for i in range(k)]
        elif d=="quarterly":
            disc_rates = [1/(1+app_rates[i]/4)**(4*(time_points[i]-t)) for i in range(k)]
        elif d=="monthly":
            disc_rates = [1/(1+app_rates[i]/12)**(12*(time_points[i]-t)) for i in range(k)]
        cash_flows = [c/freq*FV]*k
        cash_flows[-1]=cash_flows[-1]+FV
        return np.dot(disc_rates,np.array(cash_flows))
#%%
def accrued_coupon(FV,c,t,T,freq=4):
    def last_time(t,T,freq = 4):
        if freq*(T-t)==int(freq*(T-t)):
            k = freq*(T-t)-1
        else:
            k = int(freq*(T-t))
        return T-(k+1)/freq
    return FV*c/freq * (t-last_time(t,T,freq))
#%%
