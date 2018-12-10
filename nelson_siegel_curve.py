# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 16:28:15 2018

@author: theod
"""

class nelson_siegel_curve:
    r"""
    theta1: represents the level factor
    theta2: represents the rotation parameter
    theta3: controls the shape of the curve
    theta4: allows to localize the break of the curve / discontinuities
    
    If `tau` = 0 the result is `theta1` + `theta2` 
    
    If `tau` = infinity the result is `theta1`, the level factor
    """
    def __init__(self,theta1,theta2,theta3,theta4):
        self.theta1 = theta1
        self.theta2 = theta2
        self.theta3 = theta3
        self.theta4 = theta4
    def rate(self,tau):
        import numpy as np
        return self.theta1 + self.theta2 * (1-np.exp(-tau/self.theta4))/(tau/self.theta4) + self.theta3 * \
               ((1-np.exp(-tau/self.theta4))/(tau/self.theta4)-np.exp(-tau/self.theta4))
    
    