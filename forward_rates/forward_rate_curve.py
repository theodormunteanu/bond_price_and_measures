# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 11:41:37 2018

@author: theod
"""

def forward_rates(times,rates,freq=0,option = 0):
    r"""
    This function computes for a given set of knots (times) and for a given set 
    of zero-rates the forward rates seen at time 0.
    
    Parameters:
    ---------
    
    `times`: list
             the knots for the zero-rate curve
    
    `rates`: list
             the zero rates
    
    `freq`: float/int
            frequency of compounding
    
    `option`: default = 0
              If set to 0, the function returns a list of forward rates
              Otherwise, it returns a function of two variables, R(t1,t2)
    
    """
    import numpy as np
    if option==0:
        if freq==0:
            return [(rates[i+1]*times[i+1]-rates[i]*times[i])/(times[i+1]-times[i])\
                for i in range(len(times)-1)]
        else:
            return [freq*((1+rates[i+1]/freq)**(2*times[i+1])/\
                          (1+rates[i]/freq)**(2*times[i])**1/(freq*(times[i+1]-times[i]))-1) \
                    for i in range(len(times))]
    else:
        zero_rate_curve = lambda x:np.interp(x,times,rates)
        f = zero_rate_curve
        if freq==0:
            return lambda t1,t2:(f(t2)*t2-f(t1)*t1)/(t2-t1) * (t2>t1)
        else:
            return lambda t1,t2: freq*(((1+f(t2)/freq)**(freq*t2)/\
                                (1+f(t1)/freq)**(freq*t1))**1/(freq*(t2-t1))-1)
            
def forward_rates2(times,rates,freq=0,option = 0):
    r"""
    This function computes for a given set of knots (times) and for a given set 
    of zero-rates the forward rates seen at time 0.
    
    Parameters:
    ---------
    
    `times`: list
             the knots for the zero-rate curve
    
    `rates`: list
             the zero rates
    
    `freq`: float/int
            frequency of compounding
    
    `option`: default = 0
              If set to 0, the function returns a list of forward rates
              Otherwise, it returns a function of two variables, R(t1,t2)
    
    """
    import numpy as np
    if option == 0:
        fwd_rates = [(rates[i+1]*times[i+1]-rates[i]*times[i])/(times[i+1]-times[i])\
                for i in range(len(times)-1)]
        if freq==0:
            return fwd_rates
        else:
            return [freq*(np.exp(x/freq)-1) for x in fwd_rates]
    else:
        zero_curve = lambda x: np.interp(x,times,rates)
        f = zero_curve
        param_curve = lambda t1,t2:(f(t2)*t2-f(t1)*t1)/(t2-t1) * (t2>t1)
        if freq==0:
            return param_curve
        else:
            return lambda t1,t2: freq*(np.exp(param_curve(t1,t2)/freq) - 1)