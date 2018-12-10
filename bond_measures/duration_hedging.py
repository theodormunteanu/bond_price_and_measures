# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:25:12 2018

@author: theod
"""

import sys
sys.path.append(r'C:\Users\theod\OneDrive\Documents\python army of functions2\bond_price_project\bond_measures')
from bond_portfolio import bond_portfolio_price,\
     bond_portfolio_price_change as bpp_chg,bond_portfolio_duration as bpd
from bond_class import bond
#%%
def duration_hedge(face_values,coupons,maturities,frequences,t=0,\
                     mkt_prices = None,freq2 = 0, y0 = 0,rate = None,**options):
    r"""
    You must have 1 hedging instrument so: face_values, coupons, maturities,
    frequences, and mkt_prices will be lists of length 2
    
    """
    b1 = bond(face_values[0],coupons[0],maturities[0],frequences[0])
    b2 = bond(face_values[1],coupons[1],maturities[1],frequences[1])
    if mkt_prices == None:
        if (isinstance(rate,tuple) and len(rate)==2 and isinstance(rate[0],\
                       list)) or isinstance(rate,(int,float)) :
            price1 = b1.price(rate,t,freq2,option = options.get("option"))
            price2 = b2.price(rate,t,freq2,option = options.get("option"))
            dur1 = b1.duration(price1,freq2,t,y0,rate,option = options.get("option"),\
                                Modified = options.get("Modified"))
            dur2 = b2.duration(price2,freq2,t,y0,rate,option = options.get("option"),\
                               Modified = options.get("Modified"))
        elif isinstance(rate,list) and len(rate)==2 and isinstance(rate[0],(float,int)):
            price1 = b1.price(rate[0],t,freq2,option = options.get("option"))
            price2 = b2.price(rate[1],t,freq2,option = options.get("option"))
            dur1 = b1.duration(price1,freq2,t,y0,rate[0],option = options.get("option"),\
                                Modified = options.get("Modified"))
            dur2 = b2.duration(price2,freq2,t,y0,rate[1],option = options.get("option"),\
                               Modified = options.get("Modified"))
        return -price1*dur1/(price2*dur2)
    elif isinstance(mkt_prices,list):
        if (isinstance(rate,tuple) and len(rate)==2 and isinstance(rate[0],\
                     list)) or isinstance(rate,(int,float)):
            dur1 = b1.duration(mkt_prices[0],freq2,t,y0,rate,option = options.get("option"),\
                                Modified = options.get("Modified"))
            dur2 = b2.duration(mkt_prices[1],freq2,t,y0,rate,option = options.get("option"),\
                               Modified = options.get("Modified"))
        elif isinstance(rate,list) and len(rate)==2 and isinstance(rate[0],(float,int)):
            dur1 = b1.duration(mkt_prices[0],freq2,t,y0,rate[0],option = options.get("option"),\
                                Modified = options.get("Modified"))
            dur2 = b2.duration(mkt_prices[1],freq2,t,y0,rate[1],option = options.get("option"),\
                               Modified = options.get("Modified"))
        return -mkt_prices[0]*dur1/(mkt_prices[1]*dur2)

#%%        
def duration_convexity_hedge(face_values,coupons,maturities,frequences,t=0,\
                             mkt_prices = None,freq2 = 0, y0 = 0, rate = None,**options):
    r"""
    This functions computes the quantities of bonds necessary to hedge a single bond
    against a parallel shift (small/large) of the yield curve
    
    You must have two hedging instruments. 
    
    Therefore each variable (face_values, coupons, maturities, frequences) 
    must be a list of length 3
    
    """
    import numpy as np
    b1 = bond(face_values[0],coupons[0],maturities[0],frequences[0])
    b2 = bond(face_values[1],coupons[1],maturities[1],frequences[1])
    b3 = bond(face_values[2],coupons[2],maturities[2],frequences[2])
    if mkt_prices == None:
        if (isinstance(rate,tuple) and len(rate)==2 and isinstance(rate[0],\
                       list)) or isinstance(rate,(int,float)) :
            price1 = b1.price(rate,t,freq2,option = options.get("option"))
            price2 = b2.price(rate,t,freq2,option = options.get("option"))
            price3 = b3.price(rate,t,freq2,option = options.get("option"))
            dur1 = b1.duration(price1,freq2,t,y0,rate,option = options.get("option"),\
                                Modified = 'Yes')
            dur2 = b2.duration(price2,freq2,t,y0,rate,option = options.get("option"),\
                               Modified = 'Yes')
            dur3 = b3.duration(price3,freq2,t,y0,rate,option = options.get("option"),\
                               Modified = 'Yes')
            conv1 = b1.convexity(price1,t,freq2,y0,rate,option = options.get("option"))
            conv2 = b2.convexity(price2,t,freq2,y0,rate,option = options.get("option"))
            conv3 = b3.convexity(price3,t,freq2,y0,rate,option = options.get("option"))
        elif isinstance(rate,list) and len(rate)==3 and isinstance(rate[0],(float,int)):
            price1 = b1.price(rate[0],t,freq2,option = options.get("option"))
            price2 = b2.price(rate[1],t,freq2,option = options.get("option"))
            price3 = b3.price(rate[2],t,freq2,option = options.get("option"))
            dur1 = b1.duration(price1,freq2,t,y0,rate[0],option = options.get("option"),\
                                Modified = 'Yes')
            dur2 = b2.duration(price2,freq2,t,y0,rate[1],option = options.get("option"),\
                               Modified = 'Yes')
            dur3 = b3.duration(price3,freq2,t,y0,rate[2],option = options.get("option"),\
                               Modified = 'Yes')
            conv1 = b1.convexity(price1,t,freq2,y0,rate[0],option = options.get("option"))
            conv2 = b2.convexity(price2,t,freq2,y0,rate[1],option = options.get("option"))
            conv3 = b3.convexity(price3,t,freq2,y0,rate[2],option = options.get("option"))
        a = np.array([[price2*dur2,price3*dur3],[price2*conv2,price3*conv3]])
        b = np.array([-price1*dur1,-price1*conv1])
    elif isinstance(mkt_prices,list):
        if (isinstance(rate,tuple) and len(rate)==2 and isinstance(rate[0],\
                     list)) or isinstance(rate,(int,float)):
            dur1 = b1.duration(mkt_prices[0],freq2,t,y0,rate,option = options.get("option"),\
                                Modified = 'Yes')
            dur2 = b2.duration(mkt_prices[1],freq2,t,y0,rate,option = options.get("option"),\
                               Modified = 'Yes')
            dur3 = b3.duration(mkt_prices[2],freq2,t,y0,rate,option = options.get("option"),\
                               Modified = 'Yes')
            conv1 = b1.convexity(mkt_prices[0],t,freq2,y0,rate,option = options.get("option"))
            conv2 = b2.convexity(mkt_prices[1],t,freq2,y0,rate,option = options.get("option"))
            conv3 = b3.convexity(mkt_prices[2],t,freq2,y0,rate,option = options.get("option"))
        elif isinstance(rate,list) and len(rate)==3 and isinstance(rate[0],(float,int)):
            dur1 = b1.duration(mkt_prices[0],freq2,t,y0,rate[0],option = options.get("option"),\
                                Modified = 'Yes')
            dur2 = b2.duration(mkt_prices[1],freq2,t,y0,rate[1],option = options.get("option"),\
                               Modified = 'Yes')
            dur3 = b3.duration(mkt_prices[2],freq2,t,y0,rate[2],option = options.get("option"),\
                               Modified = 'Yes')
            conv1 = b1.convexity(mkt_prices[0],t,freq2,y0,rate[0],option = options.get("option"))
            conv2 = b2.convexity(mkt_prices[1],t,freq2,y0,rate[1],option = options.get("option"))
            conv3 = b3.convexity(mkt_prices[2],t,freq2,y0,rate[2],option = options.get("option"))
        a = np.array([[mkt_prices[1]*dur2,mkt_prices[2]*dur3],[mkt_prices[1]*conv2,mkt_prices[2]*conv3]])  
        b = np.array([mkt_prices[0]*dur1,mkt_prices[0]*conv1])
    return np.linalg.solve(a,b)