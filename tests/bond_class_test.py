# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 10:10:20 2018

@author: theod
"""

import sys
sys.path.append(r'C:\Users\theod\OneDrive\Documents\python army of functions2\bond_price_project\bond_measures')
from bond_class import bond
from bond_portfolio import bond_portfolio_duration,bond_portfolio_price
from bond_prices import bond_price
from bond_duration import bond_duration,bond_convexity,bond_yield,par_yield
#%%
def test_bond_class():
    b1 = bond(100,0.06,2,2)
    rate = ([0.5,1,1.5,2],[0.05,0.058,0.064,0.068])
    print(b1.price(rate))
    print(bond_price(100,0.06,2,rate,2))
    print(b1.YTM(rate,0,0))
    print(b1.duration(None,0,0,0,rate))
    b2 = bond(100,0,2,2)
    print(b2.duration(None,0,0,0,rate))
    b3 = bond(100,0.1,3,2)
    print(b3.duration(None,0,0,0,0.12))
test_bond_class()
#%%
def bond_portfolio_test():
    face_values,times,rate = [2000,6000],[1,10],0.1
    print(bond_portfolio_duration(face_values,[0,0],times,[1,1],0,None,0,0,rate))
    print(bond_portfolio_duration(face_values,[0,0],times,[1,1],0,None,0,0,[0.1,0.11]))
bond_portfolio_test()
#%%
def bond_portfolio_test3():
    face_values,times,rate = [2000,6000],[1,10],0.1
    print(bond_portfolio_price(face_values,[0,0],times,[1,1],0,0,rate))
    print(bond_portfolio_price(face_values,[0,0],times,[1,1],0,0,rate,[-1,1]))
bond_portfolio_test3()