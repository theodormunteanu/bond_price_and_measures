# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 07:54:03 2018

@author: theod
"""
import sys
sys.path.append(r'C:\Users\theod\OneDrive\Documents\python army of functions2\bond_price_project\risky_bond_and_CDS')
sys.path.append(r'C:\Users\theod\OneDrive\Documents\python army of functions2\bond_price_project')
sys.path.append(r'C:\Users\theod\OneDrive\Documents\python army of functions2\bond_price_project\bond_measures')
#%%
def test1():
    from risky_bond_measures import bond_yield_spread as bys
    from nelson_siegel_curve import nelson_siegel_curve
    curve = nelson_siegel_curve(0.05,-0.05,0.06,10)
    rates = [curve.rate(x) for x in range(1,11)]
    rates = (list(range(1,11)),rates)
    FV,c,T,R,freq = 100,0.045,10,0.4,1
    print(bys(FV,c,T,rates,0.02,R,freq))
    print(bys(FV,c,T,rates,0.02,0.8,freq))
test1()
    
    
    
