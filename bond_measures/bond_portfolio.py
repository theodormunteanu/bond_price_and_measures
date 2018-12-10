# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 10:40:42 2018

@author: theod
"""
from bond_class import bond
#%%
def bond_portfolio_duration(face_values,coupons,maturities,frequences,t = 0,\
                            mkt_prices = None,freq2 =0, y0 = 0,rate = None,positions=None,**options):
    r"""
    We compute the duration of the portfolio as the weighted average of separate durations.
    
    We consider as weights, the value occupied by each bond in the portfolio 
    divided by the value of the entire portfolio. 
    
    Warning:
    --------------
    This approach, however, works only as maturity average.
    
    The sensitivity approach is not working as weighted averages unless we have 
    an initial flat curve. 
    
    """
    import numpy as np
    bonds = [bond(face_values[i],coupons[i],maturities[i],frequences[i]) \
             for i in range(len(face_values))]
    if isinstance(rate,(int,float))==True or (isinstance(rate,tuple) and len(rate)==2) or rate==None:
        if mkt_prices == None:
           prices = [bonds[i].price(rate,t,freq2,option = options.get("option")) \
                     for i in range(len(face_values))]
           durations = [bonds[i].duration(prices[i],t,freq2,y0,rate,\
                        option = options.get("option"),Modified = options.get("Modified")) \
                        for i in range(len(face_values))]
           if positions==None:
               return np.dot(prices,durations)/sum(prices)
           else:
               return np.dot(np.array(positions)*np.array(prices),durations)/np.dot(positions,prices)
        else:
           durations = [bonds[i].duration(mkt_prices[i],t,freq2,y0,rate,\
                        option = options.get("option"),Modified = options.get("Modified"))\
                       for i in range(len(face_values))]
           if positions==None:
               return np.dot(mkt_prices,durations)/sum(mkt_prices)
           else:
               return np.dot(np.array(positions)*np.array(mkt_prices),durations)/np.dot(positions,mkt_prices)
    elif isinstance(rate,list):
        if mkt_prices == None:
           prices = [bonds[i].price(rate[i],t,freq2,option = options.get("option")) \
                     for i in range(len(face_values))]
           durations = [bonds[i].duration(prices[i],t,freq2,y0,rate[i],\
                        option = options.get("option"),Modified = options.get("Modified")) \
                        for i in range(len(face_values))]
           if positions==None:
               return np.dot(prices,durations)/sum(prices)
           else:
               return np.dot(np.array(positions)*np.array(prices),durations)/np.dot(positions,prices)
        else:
            durations = [bonds[i].duration(mkt_prices[i],t,freq2,y0,rate[i],\
                        option = options.get("option"),Modified = options.get("Modified"))\
                       for i in range(len(face_values))]
            if positions==None:
                return np.dot(mkt_prices,durations)/sum(mkt_prices)
            else:
                return np.dot(np.array(positions)*np.array(mkt_prices),durations)/np.dot(positions,mkt_prices)

def bond_portfolio_price(face_values,coupons,maturities,frequences,t=0,\
                         freq2=0, rate = None, positions = None,**options):
    r"""
    Price of a bond portfolio 
    """
    import numpy as np
    bonds = [bond(face_values[i],coupons[i],maturities[i],frequences[i])\
             for i in range(len(face_values))]
    if isinstance(rate,(int,float)) == True or (isinstance(rate,tuple) and len(rate)==2) or rate==None:
        if positions == None:
            return sum([bonds[i].price(rate,t,freq2,option = options.get("option"))\
                    for i in range(len(face_values))])
        elif isinstance(positions,list):
            return np.dot([bonds[i].price(rate,t,freq2,option = options.get("option"))\
                    for i in range(len(face_values))],positions)
    elif isinstance(rate,list):
        if positions == None:
            return sum([bonds[i].price(rate[i],t,freq2,option = options.get("option"))\
                      for i in range(len(face_values))])
        elif isinstance(positions,list):
            return np.dot([bonds[i].price(rate[i],t,freq2,option = options.get("option"))\
                      for i in range(len(face_values))],positions)
#%%
def bond_portfolio_price_change(face_values,coupons,maturities,frequences,chg,\
                                rate,t=0,freq2 = 0,positions = None,**options):
    r"""
    We search for the change in the portfolio bond price when a parallel shift 
    on the yield curve is assumed. 
    
    We do not use the duration-convexity approach.
    
    Parameters:
    ----------
    
    face_values: face value (nominal) of each bond
    
    coupons: coupon rate for each bond
    
    maturities: lifetime of each bond
    
    positions: number of long/short bonds existing in the portfolio 
    By default, the positions are [1,1,...,1] where the vector is as long is as 
    long as the vector of face values.
    """
    price0 = bond_portfolio_price(face_values,coupons,maturities,frequences,\
                                  t,freq2,rate,positions,option = options.get("option"))
    if isinstance(rate,(int,float)):
       price1 = bond_portfolio_price(face_values,coupons,maturities,frequences,\
                                     t,freq2,rate+chg,positions,option = options.get("option"))
       return price1/price0-1
    elif isinstance(rate,(tuple)) and len(rate)==2:
       aux = [rate[1][i]+chg for i in range(len(rate[1]))]
       price1 = bond_portfolio_price(face_values,coupons,maturities,frequences,\
                                     t,freq2,(rate[0],aux),positions,option = options.get("option"))
       return price1/price0-1
    elif isinstance(rate,list):
       aux = [rate[i]+chg for i in range(len(rate))]
       price1 = bond_portfolio_price(face_values,coupons,maturities,frequences,\
                                     t,freq2,aux,positions,option = options.get("option"))
       return price1/price0-1