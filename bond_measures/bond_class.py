# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 09:40:50 2018

@author: theod
"""

from bond_prices import bond_price
from bond_duration import bond_duration, bond_yield,par_yield,bond_convexity
#%%
class bond:
    r"""
    any bond is characterized by a face value FV, c = coupon rate (yearly rate)
    T = lifetime of the bond, freq = frequency of payments
    """
    def __init__(self,FV_,c_,T_,freq_):
        self.FV = FV_
        self.c = c_
        self.T = T_
        self.freq = freq_
    def price(self,rate,t=0,freq2=0,**options):
        return bond_price(self.FV,self.c,self.T,rate,self.freq,t,freq2,\
                          option = options.get("option"))
    def YTM(self,rate = None,t=0,freq2=0,mkt_price = None,y0 = 0.0,**options):
        return bond_yield(self.FV,self.c,self.T,rate,self.freq,t,freq2,\
                          mkt_price,y0,option = options.get("option"))
    def par_yield(self,rate,t = 0,freq2 = 0,y0 = 0.0,**options):
        return par_yield(self.FV,self.T,rate,self.freq,t,freq2,y0,\
                         option = options.get("option"))
    def duration(self,mkt_price=None,freq2 = 0,t = 0,y0 = 0.0,rate = None,**options):
        return bond_duration(self.FV,self.c,self.T,mkt_price,self.freq,t,\
               freq2,y0,rate,option = options.get("option"),Modified = options.get("Modified")) 
    def convexity(self,mkt_price,t = 0,freq2 = 0,y0 = 0,rate = None,**options):
        return bond_convexity(self.FV,self.c,self.T,mkt_price,self.freq,t,freq2,y0,\
                              option = options.get("option"))


