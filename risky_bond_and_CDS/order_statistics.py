# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 13:24:54 2018

@author: theod
"""

class order_statistics:
    r"""
    "This class is devised for 2 random variables
    
    Methods:
    -----------
    
    cumulative distribution function of the first order statistics
    cumulative distribution function of the second order statistics
    survival function of the first order statistics
    survival function of the second order statistics
    """
    def __init__(self,intensities):
        r"""
        Intensities: (list or tuple of 2 floats: in that case we are talking
        about simple exponential models)
                     list of two tuples: each tuple containing the piecewise 
                     exponential model
        """
        
        self.intensities = intensities
    