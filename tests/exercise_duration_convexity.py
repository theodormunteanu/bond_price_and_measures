# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 16:37:47 2018

@author: theod
"""
import sys
sys.path.append(r'C:\Users\theod\OneDrive\Documents\python army of functions2\bond_price_project\bond_measures')
from bond_prices import bond_price
from bond_duration import bond_yield,bond_duration,bond_convexity
#%%
def test_bond_price_comp():
    FV,c,T,freq,y,chg1,chg2 = 100,0.08,5,1,0.11,-0.002,-0.01
    prix = bond_price(FV,c,T,y,freq)
    dur = bond_duration(FV,c,T,prix,freq)
    prix2 = prix * (1-dur*chg1)
    conv = bond_convexity(FV,c,T,prix,freq)
    prix2bis = bond_price(FV,c,T,y+chg1,freq)
    print("==============")
    print("Continuous compounding:\n===============")
    print("The duration is",dur)
    print("The initial price is",prix)
    print("The duration price after a 0.2% decrease in yield",prix2)
    print("The actual price after a 0.2% decrease in yield",prix2bis)
    prix3 = prix*(1-dur*chg2)
    prix3bis = prix*(1-dur*chg2 + 1/2*conv * chg2**2)
    prix3bisbis = bond_price(FV,c,T,y+chg2,freq)
    print("After a 1% decrease in yield, the duration price is",prix3)
    print("After a 1% decrease in yield, the dur-conv price is",prix3bis)
    print("After a 1% decrease in yield, the actual price is",prix3bisbis)
    print("===============")
    prix_ann = bond_price(FV,c,T,y,freq,0,1)
    dur2 = bond_duration(FV,c,T,prix_ann,freq,0,1,Modified = 'Yes')
    prix_ann2 = prix_ann*(1-dur2*chg1)
    prix_ann2bis = bond_price(FV,c,T,y+chg1,freq,0,1)
    print("Yearly compounding:\n===============")
    print("The modified duration is:",dur2)
    print("The initial price is:",prix_ann)
    print("The duration price after a 0.2% decrease in yield",prix_ann2)
    print("The actual price after a 0.2% decrease in yield",prix_ann2bis)
    conv2 = bond_convexity(FV,c,T,prix_ann,freq,0,1)
    prix4 = prix_ann * (1-dur2*chg2)
    prix4bis = prix_ann*(1-dur2*chg2+1/2 * conv2 * chg2**2)
    prix4bisbis = bond_price(FV,c,T,y+chg2,freq,0,1)
    print("After a 1% decrease in yield, the duration price is",prix4)
    print("After a 1% decrease in yield, the dur-conv price is",prix4bis)
    print("After a 1% decrease in yield, the actual price is",prix4bisbis)
    
test_bond_price_comp()
#%%
    
    