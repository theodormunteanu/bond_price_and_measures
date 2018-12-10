# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 20:38:18 2018

@author: theod
"""

import sys
sys.path.append(r'C:\Users\theod\OneDrive\Documents\python army of functions2\bond_price_project\bond_measures')
from bond_prices import bond_price
from bond_duration import bond_yield
#%%
def test_yield():
    FV,c,T,freq = 100,0.06,2,2
    rates = ([0.5,1,1.5,2],[0.05,0.058,0.064,0.068])
    print(bond_yield(FV,c,T,rates,freq))
    print(bond_yield(FV,c,1.5,rates,freq))
    print(bond_yield(FV,c,1,rates,freq))
    print(bond_yield(FV,c,0.5,rates,freq))
test_yield()
#%%
def test_yield2():
    import numpy as np
    import matplotlib.pyplot as plt
    rates = ([x/12 for x in range(1,25)],[x/100 for x in np.linspace(5,11,24)])
    FV,c,freq = 100,0.08,12
    yields = [bond_yield(FV,c,rates[0][i],rates,freq) for i in range(len(rates[1]))]
    print(yields)
    f1 = lambda x:np.interp(x,rates[0],rates[1])
    f2 = lambda x:np.interp(x,rates[0],yields)
    print([f1(x) for x in rates[0]])
    print([f2(x) for x in rates[0]])
    div = np.linspace(0,2,41,endpoint = True)
    plt.plot(div,[f1(x)*100 for x in div],label = 'zero-rate curve')
    plt.plot(div,[f2(x)*100 for x in div],label = 'treasury yield curve')
    plt.xlabel('time (years)')
    plt.ylabel('zero/yield curve (%)')
    plt.title('Treasury yield curve vs. zero-rate curve')
    plt.grid(True)
    plt.legend()
test_yield2()
#%%    
def bond_yield_test3():
    FV = 100
    rates = ([1/12,2/12,3/12,6/12,9/12,1,2,3],[x/100 for x in [0.5,0.7,1.2,\
             1.4,1.7,2.1,2.3,2.5]])
    coupons = [0,0,0,0.04,0.04,0.06,0.06,0.08]
    freqs = [1,1,1,2,2,4,4,2]
    times = rates[0]
    afp = [bond_price(FV,coupons[i],times[i],rates,freqs[i]) for i in range(len(freqs))]
    "afp = arbitrage free prices"
    mkt_prices = [98.5,99,99.5,100.5,101.7,102.5,104.5,105.5]
    yields = [bond_yield(FV,coupons[i],times[i],rates,freqs[i]) for i in range(len(freqs))]
    yields2 = [bond_yield(FV,coupons[i],times[i],rates,freqs[i],0,0,mkt_prices[i]\
                          ) for i in range(len(freqs))]
    d = {'Zero rates':rates[1],'No-arb prices':afp,'Market price':mkt_prices,\
         'Treasury yields':yields,'Implied yields':yields2}
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    #new_index = pd.DataFrame.set_index(['1M','2M','3M','6M','9M','1Y','2Y','3Y'])
    indexes = ['1M','2M','3M','6M','9M','1Y','2Y','3Y']
    df = pd.DataFrame(data = d)
    df.index = indexes
    print(df)
    writer = pd.ExcelWriter('output.xlsx')
    df.to_excel(writer,'Sheet1')
    writer.save()
    my_xticks = ['1','2','3','6','9','12','24','36']
    plt.figure(1)
    plt.xticks(rates[0],my_xticks)
    plt.plot(rates[0],np.array(yields)*100,'go--',label = 'Treasury yield curve')
    plt.plot(rates[0],np.array(yields2)*100,'ro--',label = 'Implied yield curve')
    plt.xlabel('Maturity (months)')
    plt.ylabel('Yield rate (%)')
    plt.title('Yield curves')
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.figure(2)
    plt.xticks(rates[0],my_xticks)
    plt.plot(rates[0],(np.array(yields2)-np.array(yields))*100,'go--',\
             label = 'Spread curve')
    plt.xlabel('Maturity (months)')
    plt.ylabel('Yield rate (%)')
    plt.title('Yield curves')
    plt.legend()
    plt.grid(True)
    plt.show()
bond_yield_test3()