'''
Date: 2020-10-08 19:29:58
LastEditors: Yuchen ZHANG
LastEditTime: 2020-10-08 21:03:08
FilePath: /project/SpotMarket/deal_market.py
'''
import torch
import torch.nn as nn
import numpy as np
import random
import pandas as pd
import MarketSimulator as ms
import matplotlib.pyplot as plt
from time import sleep

df = pd.read_csv('avg.csv', sep=',',header=None)
a = df.values
a = a.astype(np.float64)

def print_time(num):
    if num < 10:
        time = '0' + str(int(num)) + ":00"
    else:
        time = str(int(num)) + ":00"
    print('\n', time)

def plot_step(time:list, price:list, generators:list, retailers:list):
    plt.plot(time, price, c='r',ls='-', lw=1.5, marker='*')
    plt.plot(time, generators,c='g', ls='-', lw=0.1,  alpha=0.7)
    plt.plot(time, retailers, c='b', ls='-', lw=0.1, alpha=0.7)
    plt.pause(0.5)

#loc_g_q=600, scale_g_q=31, loc_g_p=12.5, scale_g_p=0.07, loc_r_q=600, scale_r_q=31, loc_r_p=11.5, scale_r_p=0.07
time_list = []
price_list = []
generators_list = []
retailers_list = []
plt.ion()
fig = plt.figure(1)
plt.style.use("dark_background") # 设置使用的样式
plt.xlim(0,23)
plt.ylim(9.5, 13)
plt.pause(5)
for i in a:
    print_time(i[0])
    step_price, generators, retailers = ms.run_step(loc_g_q=i[1], loc_g_p=i[2])
    time_list.append(i[0])
    price_list.append(step_price)
    generators_list.append(generators)
    retailers_list.append(retailers)
    plot_step(time_list, price_list, generators_list, retailers_list)
    #sleep(1)
plt.pause(0)
