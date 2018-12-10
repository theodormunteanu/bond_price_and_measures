# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:05:56 2018

@author: theod
"""
import sys
sys.path.append(r'C:\Users\theod\OneDrive\Documents\python army of functions2\bond_price_project\bond_measures')
sys.path.append(r'C:\Users\theod\OneDrive\Documents\python army of functions2\bond_price_project\risky_bond_and_CDS')

#%%
def test1():
    from risky_bond_prices import risky_bond_price
    FV,c,T,r,lbd,R,freq = 100,0.045,10,0.05,0.02,0.4,1
    rate = ([0.5,1,1.5,2],[0.05,0.05,0.05,0.05])
    intensities = ([1,2,3],[0.02,0.02,0.02,0.02])
    print(risky_bond_price(FV,c,T,rate,intensities,R,freq))
    print(risky_bond_price(FV,c,T,r,intensities,R,freq))
    print(risky_bond_price(FV,c,T,rate,lbd,R,freq))
    print(risky_bond_price(FV,c,T,r,lbd,R,freq))
test1()
#%%
def test2():
    from risky_bond_prices import risky_bond_price
    from bond_prices import bond_price
    FV,c,T,lbd,R,freq = 100,0.045,10,0,0.4,1
    rate = ([0.5,1,1.5,2],[0.05,0.05,0.05,0.05])
    print(risky_bond_price(FV,c,T,rate,lbd,R,freq))
    print(bond_price(FV,c,T,rate,freq))
test2()
#%%
def test3():
    from risky_bond_prices import risky_bond_price
    from nelson_siegel_curve import nelson_siegel_rate
    theta1,theta2,theta3,theta4 = 0.05,-0.05,0.06,10
    rates = [nelson_siegel_rate(theta1,theta2,theta3,theta4,x) for x in range(1,6)]
    lbd1,lbd2 = 0.02,0.1
    rates = (list(range(1,6)),rates)
    FV,c,T,freq,R = 100,0.045,10,1,0.4
    print(risky_bond_price(FV,c,T,0,0,R,freq))
    print(risky_bond_price(FV,c,T,0.05,0,R,freq))
    print(risky_bond_price(FV,c,T,0.05,lbd1,R,freq))
    print(risky_bond_price(FV,c,T,0.05,lbd2,R,freq))
    print(risky_bond_price(FV,c,T,rates,0,R,freq))
    print(risky_bond_price(FV,c,T,rates,lbd1,R,freq))
    print(risky_bond_price(FV,c,T,rates,lbd2,R,freq))
test3()
#%%
def test4():
    from risky_bond_prices2 import risky_bond_price
    from nelson_siegel_curve import nelson_siegel_rate
    theta1,theta2,theta3,theta4 = 0.05,-0.05,0.06,10
    rates = [nelson_siegel_rate(theta1,theta2,theta3,theta4,x) for x in range(1,11)]
    print(rates)
    lbd1,lbd2 = 0.02,0.1
    rates = (list(range(1,11)),rates)
    FV,c,T,freq,R = 100,0.045,10,1,0.4
    print(risky_bond_price(FV,c,T,0,0,R,freq))
    print(risky_bond_price(FV,c,T,0.05,0,R,freq))
    print(risky_bond_price(FV,c,T,0.05,lbd1,R,freq))
    print(risky_bond_price(FV,c,T,0.05,lbd2,R,freq))
    print(risky_bond_price(FV,c,T,rates,0,R,freq))
    print(risky_bond_price(FV,c,T,rates,lbd1,R,freq))
    print(risky_bond_price(FV,c,T,rates,lbd2,R,freq))
test4()
#%%
def test5():
    from risky_bond_measures import bond_yield_spread
    