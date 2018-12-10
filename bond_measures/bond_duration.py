# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 23:48:28 2018

@author: theod
"""
from bond_prices import bond_price
def bond_yield(FV,c,T,rate = None,freq = 4,t=0,freq2=0,mkt_price=None,y0=0.0,**options):
    r"""
    
    Parameters:
    ----------
    `FV`  : (Required) face value (float/int)
    
    `c`   :  (Required) coupon rate (between 0 and 1)
    
    `T`  : (Required) time to maturity left
    
    `rate`   : (Optional) By default is not introduced, because it starts from the market 
               price. Otherwise, it is a tuple, as in the bond_price function
               representing the zero rate curve along with its maturities
    
    `freq`   : (Optional) frequency of payments per annum. Default set at 4, quarterly 
               payments
    
    `t`   :  (Optional) time of evaluation of the bond
    
    `freq2`   : (Optional) frequency of compounding. 
               Default set to 0 = continuous compounding
    
    `mkt_price`  : (Optional) by default is set to None. In that case, the bond yield is 
                    computed from its theoretical price, using the zero rates
    
    `y0`   : (Optional) initial guess of the bond yield. Default set to 0.0
             We use Newton approximation method
               
    `options`   : refers to clean/dirty price. 
                  It is written as option = "dirty price" / option = "clean price"
    
    Warning: If `mkt_price` is not introduced, then `rate` must be and viceversa.
    
    Examples:
    ---------
    
    1. Compute the yield of a 2-year bond if the zero-rates are 5%, 5.8%, 6.4% 
    and 6.8% corresponding to 6M, 12M, 18M and 24M, if the coupon is 6% per year 
    and the payment frequency is twice/year.
    
    >>>   bond_yield(100,0.06,2,([0.5,1,1.5,2],[0.05,0.058,0.064,0.068]),2)
    >>>   0.0676 (or 6.76%)
    
    2. Compute the yield of a 2-year bond if the market price is 96.65 and the 
       frequency and amount of coupon payment is the same. 
       
    >>>   bond_yield(100,0.06,2,None,2,0,0,96.65)
    >>>   0.0769 (or 7.69%)
    
    Source:
    ------
    
    John Hull (Options, Futures, and other derivatives), Section 4.4 (Bond yield)
    """
    import scipy.optimize as opt
    if mkt_price==None:
       theoretical_price = bond_price(FV,c,T,rate,freq,t,freq2,\
                                       option = options.get("option"))
       f = lambda x:bond_price(FV,c,T,x,freq,t,freq2,\
                               option = options.get("option"))-theoretical_price
    elif isinstance(mkt_price,(float,int)):
       f = lambda x:bond_price(FV,c,T,x,freq,t,freq2,\
                               option = options.get("option"))-mkt_price
    return opt.newton(f,y0)
#%%

def par_yield(FV,T,rate,freq=4,t=0,freq2=0,y0=0.0,**options):
    r"""
    
    Definition:
    ----------
    
    Par yield   : the coupon rate (`c`) that makes the bond price = `FV` (face value)
    
    Parameters:
    ---------
    
    Same as in the `bond_yield` function except the coupon rate `c`
    
    Example:
    -------
    
    We take as example the continuation example from yields.
    
    >>>  par_yield(100,2,([0.5,1,1.5,2],[0.05,0.058,0.064,0.068]),2)
    >>>  0.0687
    
    Source:
    -------
    
    The same book, chapter and section as in `bond_yield` function 
    """
    f = lambda x: bond_price(FV,x,T,rate,freq,t,freq2,option = options.get("option"))-FV
    import scipy.optimize as opt
    return opt.newton(f,y0)
#%%
def bond_duration(FV,c,T,mkt_price=None, freq=4, t = 0, freq2=0, y0 = 0, \
                  rate = None,**options):
    r"""
    This function returns the duration / modified duration of a bond.
    
    Parameters:
    ----------
    
    
    Besides from the already-presented parameters in the yield function,
    in options we have stored a new option, called `Modified`.
    
    `Modified` : By default is set to No. 
    
    Options: For yes one can choose between: `Yes` |`YES` | `Y` | `yes`.
    
    Also I have introduced in keyword-argument parameters, `rate` which behaves 
    the same as in `bond_price` function. 
    
    `rate`   : By default is None. We compute the implied yield and then its duration
            from the market price. If `rate` exists, the implied duration becomes 
            a tested duration, given a yield or a given treasury zero-rate curve.
            
    Can be of the following types: 
        1. `int` or `float`: a single discounted rate
        2. `tuple` of two elements: the first element is a list of maturities while 
        the second component is a list of interest rates
    
    REMARK:
    =========
    
    If chosen `yes` for `Modified` one must introduce also `t`, `freq2` and `y0` parameters
    
    EXAMPLES:
    ========
    
    1. For a zero-coupon 5-year bond, the duration is 5.
    
    >>> bond_duration(100,0,5,95)
    >>> 5.0000000000016644
    
    2. Consider a 3-year 10% coupon bearing bond with a face value of 100$. Suppose 
    that the yield is 12% per annum with continuous compounding. Also the payment frequency
    is considered twice a year. 
    
    The bond duration would be then given by:
        
    >>> bond_duration(100,0.1,3,None,2,0,0,0,0.12)
    >>> 2.653
    >>> bond_duration(100,0.1,3,0,2,0,0,0,0.12)
    >>> 2.653
    
    3. If we want to compute the modified duration, by changing the compounding from 
    continuous to annual, we can do it by writing:
    
    >>> bond_duration(100,0.1,3,0,2,0,1,0,0.12,Modified = 'Yes')
    >>> 2.3000
    
    REMARK2: 
    =======
    
    In the case of zero-coupon bonds, you can enter whatever market price you wish, 
    the result will depend only on the maturity.
    
    REMARK3:
    =======
    
    If `rate` is introduced, `mkt_price` is then set to the theoretical price, hence
    it is no longer needed, and the result is independent of `mkt_price`
    
    REMARK4:
    =======
    
    If `Modified` is used, then one must introduce a non-null parameter `freq2`
    otherwise it will give the same duration as in the continuous compounding. 
    """
    if rate==None:
       y = bond_yield(FV,c,T,None,freq,t,freq2,mkt_price, y0,option = options.get("option"))
    elif isinstance(rate,(int,float)):
        y = rate
        mkt_price = bond_price(FV,c,T,rate,freq)
    elif isinstance(rate,tuple) and len(rate)==2 and isinstance(rate[0],list) and isinstance(rate[1],list):
        y = bond_yield(FV,c,T,(rate[0],rate[1]),freq)
        mkt_price = bond_price(FV,c,T,(rate[0],rate[1]),freq)
    import numpy as np
    def times(t,T,freq = 4):
        if freq*(T-t)==int(freq*(T-t)):
            k = freq*(T-t)-1
        else:
            k = int(freq*(T-t))
        return np.linspace(T-k/freq,T,(k+1),endpoint = True)
    time_points = times(t,T,freq)
    k = len(time_points)
    cash_flows = [c/freq * FV]*k
    cash_flows[-1] = cash_flows[-1]+FV
    elapsed_time = [time_points[i]-t for i in range(k)]
    if options.get("Modified") in {'Not','No',None}:
        return np.dot(elapsed_time,np.array(cash_flows)*np.array([np.exp(-y*elapsed_time[i]) \
                                        for i in range(k)]))/mkt_price
    elif options.get("Modified") in {'YES','Y','yes','Yes'}:
        y = bond_yield(FV,c,T,0,freq,t,freq2,mkt_price)
        if freq2==0:
            return np.dot(elapsed_time,np.array(cash_flows)*np.array([np.exp(-y*elapsed_time[i]) \
                                        for i in range(k)]))/mkt_price
        else:
            return np.dot(elapsed_time,np.array(cash_flows)*np.array([np.exp(-y*elapsed_time[i]) \
                   for i in range(k)]))/mkt_price * 1/(1+y/freq2)
        
    
def bond_convexity(FV,c,T,mkt_price,freq = 4,t=0,freq2 = 0,y0 = 0,**options):
    y = bond_yield(FV,c,T,None,freq,t,freq2,mkt_price,y0,option = options.get("option"))
    import numpy as np
    def times(t,T,freq = 4):
        if freq*(T-t)==int(freq*(T-t)):
            k = freq*(T-t)-1
        else:
            k = int(freq*(T-t))
        return np.linspace(T-k/freq,T,(k+1),endpoint = True)
    time_points = times(t,T,freq)
    k = len(time_points)
    cash_flows = [c/freq * FV]*k
    cash_flows[-1] = cash_flows[-1]+FV
    elapsed_times = [(time_points[i]-t) for i in range(k)]
    elapsed_times2 = [(time_points[i]-t)**2 for i in range(k)]
    if freq2==0:
       return np.dot(elapsed_times2,np.array(cash_flows)*np.array([np.exp(-y*elapsed_times[i])\
                                          for i in range(k)]))/mkt_price
    else:
       a = np.dot(elapsed_times2,np.array(cash_flows)*np.array([(1+y/freq2)**\
                                          (-freq2*elapsed_times[i]-2) for i in range(k)]))
       b = np.dot(elapsed_times,np.array(cash_flows)*np.array([(1+y/freq2)**\
                                         (-freq2*elapsed_times[i]-2) for i in range(k)]))
       return a/mkt_price+b/(freq2*mkt_price)
    
def bond_error_check(FV,c,T,mkt_price1,mkt_price2,freq,freq2,t1,t2,**options):
    y1 = bond_yield(FV,c,T,0,freq,t1,mkt_price1,freq2,option = options.get("option"))
    y2 = bond_yield(FV,c,T,0,freq,t2,mkt_price2,freq2,option = options.get("option"))
    diff1 = (mkt_price2-mkt_price1)/mkt_price1
    dur = bond_duration(FV,c,T,mkt_price1,freq,t1,freq2,option = options.get("option"))
    conv = bond_convexity(FV,c,T,mkt_price1,freq,t1,freq2,option = options.get("option"))
    diff2 = -dur * (y2-y1) + 1/2 * conv * (y2 - y1)**2
    return diff1,diff2

