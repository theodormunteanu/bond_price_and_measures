# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 08:48:00 2018

@author: theod
"""

from bond_prices import bond_price
from bond_duration import bond_yield,par_yield,bond_duration,bond_convexity
#%%
def test_bond_price1():
    "Flat interest rate"
    FV,c,T,freq = 100,0.04,2,2
    f = lambda x: bond_price(FV,c,T,x,freq)
    g = lambda x: bond_price(FV,c,T,x,4)
    import numpy as np
    div = np.linspace(0,0.2,21,endpoint = True)
    import matplotlib.pyplot as plt
    plt.suptitle('Bond price dependence on flat interest rate')
    plt.subplot(121)
    plt.plot(div*100,[f(x) for x in div],label = 'frequence: semi-annually')
    plt.plot(div*100,[g(x) for x in div],label = 'frequence: quarterly')
    plt.xlabel('interest rate (%)')
    plt.ylabel('bond price ')
    plt.legend()
    plt.grid(True)
    plt.subplot(122)
    plt.plot(div,[f(x)-g(x) for x in div])
    plt.xlabel('interest rate (%)')
    plt.ylabel('difference')
    plt.grid(True)
test_bond_price1()
#%%
def test_bond_price2():
    FV,T,freq = 100,2,2
    f = lambda x: bond_price(FV,0.04,T,x,freq)
    g = lambda x: bond_price(FV,0.08,T,x,freq)
    import numpy as np
    div = np.linspace(0,0.2,21,endpoint = True)
    import matplotlib.pyplot as plt
    plt.suptitle('Bond price dependence on flat interest rate')
    plt.subplot(121)
    plt.plot(div*100,[f(x) for x in div],label = 'coupon: 4%')
    plt.plot(div*100,[g(x) for x in div],label = 'coupon: 8%')
    plt.xlabel('interest rate (%)')
    plt.ylabel('bond price ')
    plt.legend()
    plt.grid(True)
    plt.subplot(122)
    plt.plot(div,[f(x)-g(x) for x in div])
    plt.xlabel('interest rate (%)')
    plt.ylabel('difference')
    plt.grid(True)
test_bond_price2()
#%%
def test_bond_price3():
    "evolution with lifetime for two coupons"
    FV,freq,r = 100,2,0.04
    f = lambda T:bond_price(FV,0.06,T,r,freq)
    g = lambda T:bond_price(FV,0.08,T,r,freq)
    import numpy as np
    div = np.linspace(0.5,30,60,endpoint = True)
    import matplotlib.pyplot as plt
    plt.plot(div,[f(x) for x in div],label = 'coupon: 6%')
    plt.plot(div,[g(x) for x in div],label = 'coupon: 8%')
    plt.xlabel('Lifetime (years)')
    plt.ylabel('Bond price')
    plt.title('Bond price dependence on lifetime')
    plt.legend()
    plt.grid(True)
test_bond_price3()
#%%
def test_bond_price4():
    FV,c,T,freq = 100,0.06,2,2
    import numpy as np
    import matplotlib.pyplot as plt
    rate = (np.array([0.5,1,1.5,2]),np.array([0.03,0.04,0.05,0.06]))
    f = lambda x:bond_price(FV,c,T,(rate[0].tolist(),(rate[1]+x).tolist()),freq)
    div = np.linspace(0.001,0.02,20,endpoint = True)
    plt.figure(1)
    plt.plot(div*100,[f(x) for x in div])
    plt.xlabel('Parallel shift in curve (%)')
    plt.ylabel('Bond price')
    plt.title('Parallel shift')
    plt.grid(True)
    plt.show()
test_bond_price4()
#%%
def test_bond_price5():
    FV,c,T,freq = 100,0.06,2,2
    import numpy as np
    import matplotlib.pyplot as plt
    e1,e2,e3,e4 = np.array([1,0,0,0]),np.array([0,1,0,0]),np.array([0,0,1,0]),\
                  np.array([0,0,0,1])
    rate = (np.array([0.5,1,1.5,2]),np.array([0.03,0.04,0.05,0.06]))
    g1 = lambda x:bond_price(FV,c,T,(rate[0].tolist(),(rate[1]+x*e1).tolist()),freq)
    g2 = lambda x:bond_price(FV,c,T,(rate[0].tolist(),(rate[1]+x*e2).tolist()),freq)
    g3 = lambda x:bond_price(FV,c,T,(rate[0].tolist(),(rate[1]+x*e3).tolist()),freq)
    g4 = lambda x:bond_price(FV,c,T,(rate[0].tolist(),(rate[1]+x*e4).tolist()),freq)
    div = np.linspace(0.001,0.02,20,endpoint = True)
    plt.subplot(221)
    plt.suptitle('Influence of component-wise shifts')
    plt.plot(div*100,[g1(x) for x in div])
    plt.xlabel('change in r1 (%)')
    plt.ylabel('Bond price')
    plt.grid(True)
    plt.subplot(222)
    plt.plot(div*100,[g2(x) for x in div])
    plt.xlabel('change in r2 (%)')
    plt.ylabel('Bond price')
    plt.grid(True)
    plt.subplot(223)
    plt.plot(div*100,[g3(x) for x in div])
    plt.xlabel('change in r3 (%)')
    plt.ylabel('Bond price')
    plt.grid(True)
    plt.subplot(224)
    plt.plot(div*100,[g4(x) for x in div])
    plt.xlabel('change in r4 (%)')
    plt.ylabel('Bond price')
    plt.grid(True)
           
test_bond_price5()
#%%
def test_pricing_bond():
    import numpy as np
    FV,c,freq = 100,0.1,4
    print(bond_price(FV,c,1,0.05,freq))
    print(bond_yield(FV,c,1,([0.25,0.5,0.75,1],[0.02,0.03,0.04,0.05]),freq))
test_pricing_bond()
#%%
"Yield curve test now" 
def test_yield_zero_curve():
    rates = ([x/12 for x in [1,2,3,6,9,12]],[x/100 for x in [0.5,1,1.5,2,2.5,3]])
    FV,c,freq = 100,0.24,12
    yields = [bond_yield(FV,c,rates[0][i],rates,freq) for i in range(len(rates[1]))]
    print(rates[0])
    import numpy as np
    f1 = lambda x:np.interp(x,rates[0],rates[1])
    f2 = lambda x:np.interp(x,rates[0],yields)
    import matplotlib.pyplot as plt
    div = np.linspace(0,2,21,endpoint = True)
    plt.plot(div,[f1(x)*100 for x in div],label = 'zero-rate curve')
    plt.plot(div,[f2(x)*100 for x in div],label = 'treasury yield curve')
    plt.xlabel('time (years)')
    plt.ylabel('zero/yield curve (%)')
    plt.title('Treasury yield curve vs. zero-rate curve')
    plt.grid(True)
    plt.legend()
test_yield_zero_curve()
#%%
def test_bond_yield():
    FV,c,T,freq = 100,0.06,2,2
    import numpy as np
    import matplotlib.pyplot as plt
    e1,e2,e3,e4 = np.array([1,0.5,0.2,0]),np.array([0,1,0.5,0.2]),np.array([0.2,0,1,0.5]),\
                  np.array([1,0,0,0.2])
    rate = (np.array([0.5,1,1.5,2]),np.array([0.035,0.04,0.055,0.06]))
    g1 = lambda x:bond_yield(FV,c,T,(rate[0].tolist(),(rate[1]+x*e1).tolist()),freq)
    g2 = lambda x:bond_yield(FV,c,T,(rate[0].tolist(),(rate[1]+x*e2).tolist()),freq)
    g3 = lambda x:bond_yield(FV,c,T,(rate[0].tolist(),(rate[1]+x*e3).tolist()),freq)
    g4 = lambda x:bond_yield(FV,c,T,(rate[0].tolist(),(rate[1]+x*e4).tolist()),freq)
    div = np.linspace(0.001,0.05,50,endpoint = True)
    plt.subplot(221)
    plt.suptitle('Influence of component-wise shifts')
    plt.plot(div*100,[g1(x)*100 for x in div])
    plt.xlabel('change in r1 (%)')
    plt.ylabel('Bond yield(%)')
    plt.grid(True)
    plt.subplot(222)
    plt.plot(div*100,[g2(x)*100 for x in div])
    plt.xlabel('change in r2 (%)')
    plt.ylabel('Bond yield(%)')
    plt.grid(True)
    plt.subplot(223)
    plt.plot(div*100,[g3(x)*100 for x in div])
    plt.xlabel('change in r3 (%)')
    plt.ylabel('Bond yield(%)')
    plt.grid(True)
    plt.subplot(224)
    plt.plot(div*100,[g4(x)*100 for x in div])
    plt.xlabel('change in r4 (%)')
    plt.ylabel('Bond yield(%)')
    plt.grid(True)
test_bond_yield()
#%%
def test_yield():
    FV,c,freq = 100,0.05,4
    import numpy as np
    mkt_prices = np.linspace(98,105,15,endpoint = True)
    lifetimes = np.linspace(0.25,3.75,15,endpoint = True)
    yields = [bond_yield(FV,c,lifetimes[i],0,freq,0,mkt_prices[i])\
              for i in range(len(lifetimes))]
    import matplotlib.pyplot as plt
    plt.plot(lifetimes,[yields[i] for i in range(len(lifetimes))])
    plt.xlabel('Maturity')
    plt.ylabel('Yield')
    plt.title('Yield curve from Market prices')
    plt.grid(True)
    print(yields)
test_yield()
#%%
def test_par_yield():
    FV,freq,T = 100,2,2
    import numpy as np
    rates = (np.array([0.5,1,1.5,2]),np.array([0.05,0.058,0.064,0.068]))
    import matplotlib.pyplot as plt
    e1,e2,e3,e4 = np.array([1,0,0,0]),np.array([0,1,0,0]),np.array([0,0,1,0]),\
                  np.array([0,0,0,1])
    g1 = lambda x:par_yield(FV,T,(rates[0].tolist(),(rates[1]+x*e1).tolist()),freq)
    g2 = lambda x:par_yield(FV,T,(rates[0].tolist(),(rates[1]+x*e2).tolist()),freq)
    g3 = lambda x:par_yield(FV,T,(rates[0].tolist(),(rates[1]+x*e3).tolist()),freq)
    g4 = lambda x:par_yield(FV,T,(rates[0].tolist(),(rates[1]+x*e4).tolist()),freq)
    div = np.linspace(0,0.02,21,endpoint = True)
    plt.figure(1)
    plt.plot(div*100,[g1(x)*100 for x in div])
    plt.title('Par yield evolution when $r_1$ changes')
    plt.xlabel('$\Delta r_1 $ (in %)')
    plt.ylabel('$\Delta y$ (in %)')
    plt.grid(True)
    plt.figure(2)
    plt.plot(div*100,[g2(x)*100 for x in div])
    plt.title('Par yield evolution when $r_2$ changes')
    plt.xlabel('$\Delta r_2 $ (in %)')
    plt.ylabel('$\Delta y$ (in %)')
    plt.grid(True)
    plt.figure(3)
    plt.plot(div*100,[g3(x)*100 for x in div])
    plt.title('Par yield evolution when $r_3$ changes')
    plt.xlabel('$\Delta r_3 $ (in %)')
    plt.ylabel('$\Delta y$ (in %)')
    plt.grid(True)
    plt.figure(4)
    plt.plot(div*100,[g4(x)*100 for x in div])
    plt.title('Par yield evolution when $r_4$ changes')
    plt.xlabel('$\Delta r_4 $ (in %)')
    plt.ylabel('$\Delta y$ (in %)')
    plt.grid(True)
test_par_yield()