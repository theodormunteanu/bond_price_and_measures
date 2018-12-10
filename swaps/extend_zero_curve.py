# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 13:52:02 2018

@author: theod
"""

r"""
This file focuses on extending the zero curve by using LIBOR rates and swap rates

"""
def zero_curve_ext(times,rates,times2,rates2,face_values,frequencies,compounding = 0):
    r"""
    Parameters:
    ----------
    
    `times`: (Required) list
             It is the list of knots of the zero/LIBOR curve
    
    `rates`: (Required) list
             the zero_rates
    
    `times2`:(Required) list 
             the lifetimes of the swaps available on the market
    
    `rates2`: (Required) list
              The swap rates (e.g. the par yields for the underlying fixed bonds)
    
    `face_values`: (Required) list
                   The nominals (face values ) of the swaps
    
    `frequencies`: (Required) list 
                  The payment frequencies for the swaps
    
    `compounding`: (optional) float,int
                   The frequency of discounting cash-flows
    """
    