# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 12:25:01 2018

@author: theod
"""
import sys
sys.path.append(r'C:\Users\theod\OneDrive\Documents\python army of functions2\bond_price_project\risky_bond_and_CDS')
from piecewise_expo import piecewise_exponential
import scipy.stats as stats
#%%
def expo_test():
    import scipy.stats as stats
    import numpy as np
    f = stats.expon
    print(f.cdf(1,loc = 0,scale = 1/0.4))
    print(1-np.exp(-0.4))
    print(f.pdf(1,loc = 0,scale = 1/0.4))
    print(0.4 * np.exp(-0.4))
    print(f.logpdf(1,loc = 0,scale = 1/0.4))
    print(-0.4 * 1 + np.log(0.4))
expo_test()
#%%
def test_class_piece():
    b1 = piecewise_exponential([0.2,0.3,0.4],[1,2])
    x = b1.rvs2(10000)
    count = sum([(x[i]<2)*1 for i in range(len(x))  ])/len(x)
    count2 = sum([(x[i]<1)*1 for i in range(len(x))] )/len(x)
    print(count)
    import numpy as np
    print(1-np.exp(-0.5))
    print(count2,1-np.exp(-0.2))
test_class_piece()
#%%
def test_class_piece2():
    b1 = piecewise_exponential([1,2,3,4],[0.2,0.3,0.4,0.7,0.9])
    print(b1.survival(1),b1.survival(2))
    print(b1.survival2(1),b1.survival2(2))
    print(b1.survival(4.1))
    print(b1.survival2(4.1))
test_class_piece2()
#%%
def test_expo_dist():
    f = stats.expon
    print(f.cdf(1,loc = 0,scale = 1/1.1))
    g = piecewise_exponential([0.5,1],[0.2,0.3,0.4])
    print(g.cdf(1))
test_expo_dist()