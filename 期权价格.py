# -*- coding: utf-8 -*-
import tushare as ts
from math import log,sqrt,exp
from scipy.stats import norm

def call_option_pricer(share_num, strike, maturity, r, vol):
    spot = ts.get_realtime_quotes(str(share_num))['price'][0]
    spot = float(spot)
    d1 = (log(spot/strike)+(r+0.5*vol*vol)*maturity)/vol/sqrt(maturity)
    d2 = d1-vol*sqrt(maturity)
    price = spot*norm.cdf(d1)-strike*exp(-r*maturity)*norm.cdf(d2)
    return price


#share_num 股票代码
#strike 行权价
#maturity 有效期
#r 无风险利率
#vol 波动率

print('期权价格:%.4f'%call_option_pricer(600848,
                                        strike=2,
                                        maturity=0.25,
                                        r=0.05,
                                        vol=0.25))



