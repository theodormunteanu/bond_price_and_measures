# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 21:37:13 2018

@author: theod
"""

def test_lsq1():
    import numpy as np
    x = np.array([0,1,2,3])
    print(np.ones(4))
    A = np.vstack([x,np.ones(len(x))]).T
    y = np.array([1,2,3,4])
    m,c = np.linalg.lstsq(A,y,rcond = None)[0]
    print(np.linalg.lstsq(A,y,rcond = None))
    print(m,c)
test_lsq1()
#%%
def test_lsq2():
    import numpy as np
    A1 = np.array([[2,2,2,102],[3,3,3,103]])
    y1 = np.array([100.5,101.5])
    a1,b1,c1,d1 = np.linalg.lstsq(A1,y1,rcond = None)[0]
    #print(np.linalg.lstsq(A1,y1,rcond = None))
    #print(a1,b1,c1,d1)
    A2 = np.array([[2,2,2,102],[3,3,3,103],[4,4,4,104],[5,5,5,105],[6,6,6,106]])
    y2 = np.array([106.5,108.5,111.5,114.5,117.5])
    #a2,b2,c2,d2 = np.linalg.lstsq(A2,y2,rcond = None)[0]
    print(np.linalg.lstsq(A2,y2,rcond = None))
    #print(a2,b2,c2,d2)
test_lsq2()
#%%
def test_lsq3():
    import scipy.optimize as optim
    import numpy as np
    A1 = np.array([[2,2,2,102],[3,3,3,103]])
    y1 = np.array([100.5,101.5])
    print(type(optim.lsq_linear(A1,y1,bounds = (np.ones(4)/4,np.ones(4)))))
test_lsq3()
#%%