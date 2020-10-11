'''
Date: 2020-09-24 14:07:29
LastEditors: Yuchen ZHANG
LastEditTime: 2020-10-12 00:47:23
FilePath: /project/SpotMarket/MarketSimulator.py
'''
import numpy as np
import random
import pandas as pd
import particitant as pt
import market as mk
import create_data as cd
#import data 

def group(particitant:list):
    generators = []
    retailers = []
    for i in particitant:
        if i.kind == "Generator":
            generators.append(i)
        else:
            retailers.append(i)
    return generators, retailers

def run_step(loc_g_q=600, scale_g_q=31, loc_g_p=12.5, scale_g_p=0.07, loc_r_q=600, scale_r_q=31, loc_r_p=11.5, scale_r_p=0.07):
    #data = cd.create_test_data()
    data = cd.create_normal_data(loc_g_q=600, scale_g_q=31, loc_g_p=12.5, scale_g_p=0.07, loc_r_q=600, scale_r_q=31, loc_r_p=11.5, scale_r_p=0.07)
    generators, retailers = group(data)
    market = mk.Market(generators, retailers)
    prices = market.match()
    prices = np.array(prices).round(3)
    print(prices)
    final_price = (sum(prices)/len(prices)).round(3)
    print("final price:", final_price)
    generators_list = []
    retailers_list = []
    for i in generators:
        generators_list.append(i.price)
    for i in retailers:
        retailers_list.append(i.price)
    return final_price, generators_list, retailers_list

if __name__ == '__main__':
  run_step()











    