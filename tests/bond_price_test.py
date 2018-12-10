# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 23:59:42 2018

@author: theod
"""
import sys
sys.path.append(r'C:\Users\theod\OneDrive\Documents\python army of functions2\bond_price_project\bond_measures')
from bond_prices import bond_price
from bond_duration import bond_yield, bond_duration,par_yield,bond_convexity
#%%
def bond_price_test1():
    FV,c,T,freq,r = 100,0.06,2,2,0.0676
    print(bond_price(FV,c,T,r,freq))
    print(bond_price(FV,c,T,r,freq,0,1))
    print(bond_price(FV,c,T,r,freq,0,2))
bond_price_test1()
#%%
def bond_price_test2():
    import matplotlib.pyplot as plt
    import numpy as np
    FV,c,T,freq = 100,0.06,2,2
    f = lambda r: bond_price(FV,c,T,r,freq)
    div = np.linspace(-0.02,0.1,61,endpoint = True)
    plt.plot(div*100,[f(x) for x in div],'b--')
    plt.xlabel('Flat interest rate (%)')
    plt.ylabel('Bond price')
    plt.title('Bond price evolution with interest rate')
    plt.grid(True)
    
bond_price_test2()
#%%
def bond_price_test3():
    import matplotlib.pyplot as plt
    import numpy as np
    FV,c,T,freq,rates = 100,0.06,2,2,([0.5,1,1.5,2],[0.05,0.058,0.064,0.068])
    prix = bond_price(FV,c,T,rates,freq)
    fct = lambda x:[z+x for z in rates[1]]
    div = np.linspace(0.001,0.02,20,endpoint = True)
    f = lambda x:bond_price(FV,c,T,(rates[0],fct(x)),freq)
    plt.figure(1)
    plt.plot(div*100,[(f(x)/prix-1)*100 for x in div])
    plt.xlabel('Parallel shift in curve (%)')
    plt.ylabel('Bond price (%) change')
    plt.title('Parallel shift')
    plt.grid(True)
    plt.show()
bond_price_test3()
#%%
def bond_price_test4():
    import matplotlib.pyplot as plt
    import numpy as np
    FV,c,T,freq,rate = 100,0.06,2,2,(np.array([0.5,1,1.5,2]),np.array([0.05,0.058,0.064,0.068]))
    e1,e2,e3,e4 = np.array([1,0,0,0]),np.array([0,1,0,0]),np.array([0,0,1,0]),\
                  np.array([0,0,0,1])
    g1 = lambda x:bond_price(FV,c,T,(rate[0].tolist(),(rate[1]+x*e1).tolist()),freq)
    g2 = lambda x:bond_price(FV,c,T,(rate[0].tolist(),(rate[1]+x*e2).tolist()),freq)
    g3 = lambda x:bond_price(FV,c,T,(rate[0].tolist(),(rate[1]+x*e3).tolist()),freq)
    g4 = lambda x:bond_price(FV,c,T,(rate[0].tolist(),(rate[1]+x*e4).tolist()),freq)
    prix = bond_price(FV,c,T,(rate[0].tolist(),rate[1].tolist()),freq)
    div = np.linspace(0.001,0.02,20,endpoint = True)
    plt.subplot(221)
    plt.suptitle('Influence of component-wise shifts')
    plt.plot(div*100,[(g1(x)/prix-1)*100 for x in div])
    plt.xlabel('change in r1 (%)')
    plt.ylabel('Bond price % change')
    plt.grid(True)
    plt.subplot(222)
    plt.plot(div*100,[(g2(x)/prix-1)*100 for x in div])
    plt.xlabel('change in r2 (%)')
    plt.ylabel('Bond price % change')
    plt.grid(True)
    plt.subplot(223)
    plt.plot(div*100,[(g3(x)/prix-1)*100 for x in div])
    plt.xlabel('change in r3 (%)')
    plt.ylabel('Bond price % change')
    plt.grid(True)
    plt.subplot(224)
    plt.plot(div*100,[(g4(x)/prix-1)*100 for x in div])
    plt.xlabel('change in r4 (%)')
    plt.ylabel('Bond price % change')
    plt.grid(True)
bond_price_test4()
#%%
def bond_price_test5():
    FV = 100
    rates = ([1/12,2/12,3/12,6/12,9/12,1,2,3],[x/100 for x in [0.5,0.7,1.2,\
             1.4,1.7,2.1,2.3,2.5]])
    coupons = [0,0,0,0.04,0.04,0.06,0.06,0.08]
    freqs = [1,1,1,2,2,4,4,2]
    times = rates[0]
    afp = [bond_price(FV,coupons[i],times[i],rates,freqs[i]) for i in range(len(freqs))]
    "arbitrage free price"
    mkt_prices = [98.5,99,99.5,100.5,101.7,102.5,104.5,105.5]
    yields = [bond_yield(FV,coupons[i],times[i],rates,freqs[i]) for i in range(len(freqs))]
    yields2 = [bond_yield(FV,coupons[i],times[i],rates,freqs[i],0,0,mkt_prices[i]\
                          ) for i in range(len(freqs))]
    print("Arbitrage free prices:",afp)
    print("Treasury yields:",yields)
    print("Realized yields:",yields2)
bond_price_test5()
#%%
def bond_price_test6():
    "Price sensitivities for two money market instruments"
    FV,T1,T2 = 100,0.25,10
    r,freq = 0.025,2
    c1,c2 = 0,0.08
    px1 = bond_price(FV,c1,T1,r,freq)
    px2 = bond_price(FV,c2,T2,r,freq)
    f1,f2 = lambda x:bond_price(FV,c1,T1,r+x,freq),lambda x:bond_price(FV,c2,T2,r+x,freq)
    import numpy as np
    import matplotlib.pyplot as plt
    div = np.linspace(0,0.1,51,endpoint = True)
    fig, ax1 = plt.subplots()
    color1,color2 = 'tab:red','tab:green'
    ax1.set_xlabel('$\Delta r$ (%)')
    ax1.set_ylabel('$\Delta$ price (%) 3M treasury bill')
    ln1 = ax1.plot(div*100,[(f1(x)/px1 - 1)*100 for x in div],\
                      label ='Treasury bill 3M % price change' ,color = color1)
    ax1.grid()
    ax2 = ax1.twinx()
    ax2.set_ylabel('$\Delta$ price (%) 10Y bond')
    ln2 = ax2.plot(div*100,[(f2(x)/px2 - 1)*100 for x in div],\
                      label = 'Bond 10Y % price change',color = color2)
    lns = ln1+ln2
    labs = [l.get_label() for l in lns]
    ax1.legend(lns,labs,loc = 0)
    plt.title('% change in instrument price')
    plt.grid(True)  
    fig.tight_layout()
    plt.show()
bond_price_test6()
#%%
def bond_price_test7():
    FV,T1,T2 = 100,0.25,10
    r,freq = 0.025,2
    c1,c2 = 0,0.08
    px1 = bond_price(FV,c1,T1,r,freq)
    px2 = bond_price(FV,c2,T2,r,freq)
    f1,f2 = lambda x:bond_price(FV,c1,T1,r+x,freq),lambda x:bond_price(FV,c2,T2,r+x,freq)
    import numpy as np
    import matplotlib.pyplot as plt
    div = np.linspace(0,0.1,51,endpoint = True)
    plt.plot(div*100,[(f1(x)/px1 - 1)*100 for x in div],label  = 'Treasury bill 3M % price change' )
    plt.plot(div*100,[(f2(x)/px2 - 1)*100 for x in div],label = 'Bond 10Y % price change')
    plt.title('% price change of instruments')
    plt.xlabel('$\Delta r$ (%)')
    plt.ylabel('$\Delta$ price (%)')
    plt.grid(True)
    plt.legend()
    plt.show()
bond_price_test7()
#%%