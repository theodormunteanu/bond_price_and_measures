# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 09:55:39 2018

@author: theod
"""
import sys
sys.path.append(r'C:\Users\theod\OneDrive\Documents\python army of functions2\bond_price_project\bond_measures')
from bond_portfolio import bond_portfolio_price,\
     bond_portfolio_price_change as bpp_chg,bond_portfolio_duration as bpd
#%%
def bpp_change_test():
    r""" I am testing first the change in a portfolio value when initial 
    yield curve is flat.  Then I change this assumption.
    below I have 2e xamples 
    1. 2 bonds with the same yield 10%
    2. 2 bonds with yields 8% and 11% 
    """
    face_values,times,rate = [2000,6000],[1,10],0.1
    print(bond_portfolio_price(face_values,[0,0],times,[1,1],0,0,rate))
    print(bpp_chg(face_values,[0,0],times,[1,1],0.001,rate))
    print(bpp_chg(face_values,[0,0],times,[1,1],0.05,rate))
    rate2 = [0.08,0.11]
    #prc = bpp_chg(face_values,[0.02,0.04],times,[1,1],0.001,rate2)
    prc2 = bpd(face_values,[0.02,0.09],times,[1,1],0,None,0,0,rate2)
    print(bpp_chg(face_values,[0.02,0.09],times,[1,1],0.005,rate2))
    print(prc2 * 0.005)
bpp_change_test()
#%%
