# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 16:12:22 2018

@author: theod
"""

import sys
sys.path.append(r'C:\Users\theod\OneDrive\Documents\python army of functions2\bond_price_project\bond_measures')
from bond_prices import bond_price
from bond_duration import bond_yield,bond_duration,bond_convexity
#%%
def test_yield_bond1():
    import numpy as np
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
    f = lambda x,i:(np.array(rates[1])+x*np.eye(1,8,i)).tolist()[0]
    g = lambda x:(np.array(rates[1])+x*np.ones((1,8))).tolist()[0]
    yields3 = [bond_yield(FV,coupons[i],times[i],(rates[0],g(0.001)),freqs[i]\
                          ) for i in range(len(freqs))]
    yields4 = [bond_yield(FV,coupons[i],times[i],(rates[0],f(0.005,0)),freqs[i]\
                          ) for i in range(len(freqs))]
    yields5 = [bond_yield(FV,coupons[i],times[i],(rates[0],f(0.005,7)),freqs[i]\
                          ) for i in range(len(freqs))]
    import matplotlib.pyplot as plt
    my_xticks = ['1','2','3','6','9','12','24','36']
    plt.figure(1)
    plt.xticks(rates[0],my_xticks)
    plt.plot(rates[0],np.array(yields)*100,'go--',label = 'Treasury yield curve')
    plt.plot(rates[0],np.array(yields3)*100,'ro--',label = 'Treasury yield curve: + 10bs')
    plt.title('Parallel shift of the treasury curve')
    plt.xlabel('Maturity (months)')
    plt.ylabel('Yield (treasury)')
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.figure(2)
    plt.xticks(rates[0],my_xticks)
    plt.plot(rates[0],np.array(yields)*100,'go--',label = 'Treasury yield curve')
    plt.plot(rates[0],np.array(yields4)*100,'ro--',label = 'Treasury yield curve: + 50bs')
    plt.title('1M rate increase with 50 bps')
    plt.xlabel('Maturity (months)')
    plt.ylabel('Yield (treasury)')
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.figure(3)
    plt.xticks(rates[0],my_xticks)
    plt.plot(rates[0],np.array(yields)*100,'go--',label = 'Treasury yield curve')
    plt.plot(rates[0],np.array(yields5)*100,'ro--',label = 'Treasury yield curve: + 50bs')
    plt.title('3Y rate increase with 50 bps')
    plt.xlabel('Maturity (months)')
    plt.ylabel('Yield (treasury)')
    plt.legend()
    plt.grid(True)
    plt.show()
test_yield_bond1()
#%%
def test_yield_bond2():
    import numpy as np
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
    durations = [bond_duration(FV,coupons[i],times[i],mkt_prices[i],freqs[i]) \
                 for i in range(len(freqs))]
    durations2 = [bond_duration(FV,coupons[i],times[i],afp[i],freqs[i])\
                 for i in range(len(freqs))]
    modified_durations = [bond_duration(FV,coupons[i],times[i],mkt_prices[i],freqs[i],\
                                        0,1,Modified = 'YES') for i in range(len(freqs))]
    modified_durations2 = [bond_duration(FV,coupons[i],times[i],afp[i],freqs[i],\
                                         0,1,Modified = 'YES') for i in range(len(freqs))]
    print(durations)
    print(durations2)
    print(modified_durations)
    print(modified_durations2)
test_yield_bond2()
#%%s
def test_yield_bond3():
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
    durations = [bond_duration(FV,coupons[i],times[i],mkt_prices[i],freqs[i]) \
                 for i in range(len(freqs))]
    durations2 = [bond_duration(FV,coupons[i],times[i],afp[i],freqs[i])\
                 for i in range(len(freqs))]
    modified_durations = [bond_duration(FV,coupons[i],times[i],mkt_prices[i],freqs[i],\
                                        0,1,Modified = 'YES') for i in range(len(freqs))]
    modified_durations2 = [bond_duration(FV,coupons[i],times[i],afp[i],freqs[i],\
                                         0,1,Modified = 'YES') for i in range(len(freqs))]
    d = {'Zero rates':rates[1],'No-arb prices':afp,'Market price':mkt_prices,\
         'Treasury yields':yields,'Implied yields':yields2}
    d2 = {'No-arb prices':afp,'Duration':durations2,'Modified duration':modified_durations2,\
          'Market price':mkt_prices,'Implied duration':durations,\
          'Implied modified duration':modified_durations}
    import pandas as pd
    #new_index = pd.DataFrame.set_index(['1M','2M','3M','6M','9M','1Y','2Y','3Y'])
    indexes = ['1M','2M','3M','6M','9M','1Y','2Y','3Y']
    df = pd.DataFrame(data = d)
    df.index = indexes
    df2 = pd.DataFrame(data=d2)
    df2.index = indexes
    print(df)
    writer = pd.ExcelWriter('output.xlsx')
    df.to_excel(writer,'Sheet1')
    df2.to_excel(writer,'Sheet2')
    writer.save()
test_yield_bond3()
