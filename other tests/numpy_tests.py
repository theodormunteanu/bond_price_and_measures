# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 22:17:11 2018

@author: theod
"""
#%%
def test_numpy():
    import numpy as np
    a = np.array([2,3,4])
    b = np.array([2,4,5])
    x,y = a.T,b.T
    print(np.vstack((a,b)))
    print(np.hstack((x,y,x)))
    x,y = a.reshape(3,1),b.reshape(3,1)
    print(np.hstack((x,y,x)))
test_numpy()
#%%
def vector_basis_test():
    import numpy as np
    rate = [0.02,0.03,0.04,0.06]
    f = lambda x,i: (np.array(rate)+x*np.eye(1,4,i)).tolist()[0]
    print(f(0.1,0))
    print(np.ones((1,4)))
    g = lambda x:(np.array(rate)+x*np.ones((1,4))).tolist()[0]
    print(g(0.1))
vector_basis_test()