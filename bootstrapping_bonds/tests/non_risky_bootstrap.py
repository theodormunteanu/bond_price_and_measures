# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 08:17:31 2018

@author: theod
"""
import sys
sys.path.append(r'C:\Users\theod\OneDrive\Documents\python army of functions2\bond_price_project\bootstrapping_bonds')
from bootstrap import bootstrap1,bootstrap2
#%%
def test_bootstrap():
    face_values,coupons,lifetimes,times,freqs,bond_prix = [100]*4,\
          [0,0,0.062,0.08],[0.5,1,1.5,2],[0.5,1,1.5,2],[2]*4,[98,95,101,104]
    face_values2,coupons2,lifetimes2,freqs2,bond_prix2 = [100]*5,\
          [0,0,0.062,0.08,0.09],[0.5,1,1.5,2,2.5],[2]*5,[98,95,101,104,106]
    print(bootstrap1(face_values,coupons,lifetimes,times,freqs,bond_prix))
    print(bootstrap2(face_values,coupons,lifetimes,times,freqs,bond_prix))
    print(bootstrap2(face_values2,coupons2,lifetimes2,times,freqs2,bond_prix2))
test_bootstrap()
#%%