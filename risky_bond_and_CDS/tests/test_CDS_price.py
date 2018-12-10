# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 18:01:40 2018

@author: theod
"""
import sys
sys.path.append(r'C:\Users\theod\OneDrive\Documents\python army of functions2\bond_price_project')
sys.path.append(r'C:\Users\theod\OneDrive\Documents\python army of functions2\bond_price_project\bond_measures')
sys.path.append(r'C:\Users\theod\OneDrive\Documents\python army of functions2\bond_price_project\risky_bond_and_CDS')
from CDS_price import price_CDS
from CDS_measures import CDS_spread
from bond_prices import bond_price
from bond_duration import bond_yield
from CDS_price2 import price_CDS2
#%%
def CDS_price_test1():
    rate = ([1,2,3,4,5],[0.0052,0.0099,0.0142,0.018,0.0215])
    FV = 1000000
    R,T  = 0.4,5
    freq = 4
    intensities = 0.005
    c = 0.001
    print(price_CDS(FV,c,T,rate,intensities,R,freq))
    s = CDS_spread(FV,T,rate,intensities,R,freq)
    print(s)
    print(price_CDS(FV,s,T,rate,intensities,R,freq))
CDS_price_test1()
#%%
def CDS_price_test2():
    from nelson_siegel_curve import nelson_siegel_curve
    theta1,theta2,theta3,theta4 = 0.05,-0.05,0.06,10
    curve = nelson_siegel_curve(theta1,theta2,theta3,theta4)
    c=0.05
    freq=1
    print(bond_price(100,c,1,curve.rate(1),freq))
CDS_price_test2()
#%%
def CDS_price_test3():
    r"""
    Source:
    --------
    
    Thierry Roncalli, Financial Risk Management, Example 25 chapter 3
    Credit Risk
    
    Problem:
    --------
    
    Find the CDS prices for two levels of coupon rate and an exponential default
    time given. 
    
    The fixed parameters: 
    --------------------
    
    `FV`: notional (set to 10 million)
    
    `T`: time to maturity (10 years)
    
    `rates`: given by the Nelson siegel curve model having parameters `theta1`=0.05
             `theta2`=-0.05, `theta3` = 0.06, `theta4` = 10
    
    `lbd`: the intensity of the default time which is 50bps or 0.005
    
    `R`: recovery rate
    
    Tests:
    -----------
    
    1. The CDS price when the coupon rate is 10bps, continuous compounding.
    
    2. The CDS price when the coupon rate is 100bps, continuous compounding.
    
    3. The CDS price when the coupon rate is 10bps, quarterly compounding.
    
    4. The CDS price when the coupon rate is 100bps, quarterly compounding.
    """
    from nelson_siegel_curve import nelson_siegel_curve
    theta1,theta2,theta3,theta4 = 0.05,-0.05,0.06,10
    curve = nelson_siegel_curve(theta1,theta2,theta3,theta4)
    rates = [curve.rate(t) for t in range(1,6)]
    times = list(range(1,6))
    rates = (times,rates)
    FV,c1,c2,T,lbd = 10**6,10**(-3),10**(-2),5,5*10**(-3)
    R,freq = 0.4,4
    print(price_CDS2(FV,c1,T,rates,lbd,R,freq))
    print(price_CDS2(FV,c2,T,rates,lbd,R,freq))
    print(price_CDS2(FV,c1,T,rates,lbd,R,freq,0,4,option = "clean"))
    print(price_CDS2(FV,c2,T,rates,lbd,R,freq,0,4,option = "clean"))
CDS_price_test3()
#%%
def CDS_price_test4():
    from nelson_siegel_curve import nelson_siegel_curve
    theta1,theta2,theta3,theta4 = 0.05,-0.05,0.06,10
    curve = nelson_siegel_curve(theta1,theta2,theta3,theta4)
    rates = [curve.rate(t) for t in range(1,6)]
    times = list(range(1,6))
    rates = (times,rates)
    FV,T,lbd = 10**6,5,5*10**(-3)
    R,freq = 0.4,4
    from CDS_measures import CDS_spread2
    s1 = CDS_spread2(FV,T,rates,lbd,R,freq,0,0,option = "clean")
    print(s1)
CDS_price_test4()
#%%
def CDS_price_test5():
    