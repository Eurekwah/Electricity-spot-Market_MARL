'''
Date: 2020-09-24 14:07:29
LastEditors: Yuchen ZHANG
LastEditTime: 2020-10-08 20:36:05
FilePath: /project/SpotMarket/MarketSimulator.py
'''
import torch
import torch.nn as nn
import numpy as np
import random
import pandas as pd
#import data 


# kind = {Generator, Retailer}
class Particitant:
    def __init__(self, kind, price, quantities, name):
        self.kind = kind
        self.price = price
        self.quantities = quantities
        self.name = name
    

    def key(self):
        return self.price
    
    def if_zero(self):
        if self.quantities == 0:
            return True
        else:
            return False

    def sell(self, quantity):
            self.quantities -= quantity
            

class Market:
    def __init__(self, generators:list, retailers:list):
        self.generators = []
        self.retailers = []
        for i in generators:
            self.generators.append(i)
        for i in retailers:
            self.retailers.append(i)

    def sort(self):
        return sorted(self.generators, key=lambda x: x.key(), reverse=False), sorted(self.retailers, key=lambda x: x.key(), reverse=True)

    def match(self):
        np.set_printoptions(precision=3)
        prices = []
        self.generators, self.retailers = self.sort()
        output_data(self.generators)
        output_data(self.retailers)
        bid_ask_spread = (self.generators[0].price-self.retailers[0].price) * 3
        i = 0
        print("\nTransaction Details")
        while self.generators and self.retailers:
            
            if self.generators[0].if_zero():
                self.generators.pop(0)
                continue
            if self.retailers[0].if_zero():
                self.retailers.pop(0)
                continue
            if abs(self.generators[0].price-self.retailers[0].price > bid_ask_spread):
                break
            i += 1
            if self.generators[0].quantities >= self.retailers[0].quantities:
                temp = self.retailers[0].quantities
            else:
                temp = self.generators[0].quantities
            self.generators[0].sell(temp)
            self.retailers[0].sell(temp)
            temp_price = (self.generators[0].price + self.retailers[0].price)/2
            item = "deal" + str(i)
            print(format(item, " <10"), format(self.generators[0].name, " <11"), "------>".ljust(8), format(self.retailers[0].name, " <10"), "quantities:".ljust(10), format(temp.round(3), " <10"), "price:".ljust(10), format(temp_price.round(3), " <10"))
            prices.append(temp_price)
        return prices

def group(particitant:list):
    generators = []
    retailers = []
    for i in particitant:
        if i.kind == "Generator":
            generators.append(i)
        else:
            retailers.append(i)
    return generators, retailers

def create_test_data():
    group = []
    for i in range(1, 11):
        name = "Retailer" + str(i)
        temp_2 = Particitant("Retailer", i, i * 10, name)
        group.append(temp_2)
    for i in range(11, 21):
        name = "Generator" + str(i)
        temp_1 = Particitant("Generator", i, i * 10, name)
        group.append(temp_1)
    return group

def create_normal_data(loc_g_q=600, scale_g_q=31, loc_g_p=12.5, scale_g_p=0.07, loc_r_q=600, scale_r_q=31, loc_r_p=11.5, scale_r_p=0.07):
    group = []
    temp_r_q = np.random.normal(loc_r_q, scale_r_q, 10)
    temp_g_q = np.random.normal(loc_g_q, scale_g_q, 10)
    temp_r_p = np.random.normal(loc_r_p, scale_r_p, 10)
    temp_g_p = np.random.normal(loc_g_p, scale_g_p, 10)

    temp_r_q = np.around(temp_r_q, decimals=3)
    temp_r_p = np.around(temp_r_p, decimals=3)
    temp_g_q = np.around(temp_g_q, decimals=3)
    temp_g_p = np.around(temp_g_p, decimals=3)

    for i in range(10):
        name = "Retailer" + str(i + 1)
        temp_r = Particitant("Retailer", temp_r_p[i], temp_r_q[i], name)
        group.append(temp_r)

    for i in range(10):
        name = "Generator" + str(i + 1)
        temp_g = Particitant("Generator", temp_g_p[i], temp_g_q[i], name)
        group.append(temp_g)
    return group
    
def output_data(particitant:list):
    name = particitant[0].kind
    print(name)
    print("name".ljust(15), "price".ljust(10), "quantities".ljust(10))
    for i in particitant:
        print(format(i.name, " <15"), format(i.price, " <10"), format(i.quantities, " <10"))
    print('\n')


def run_step(loc_g_q=600, scale_g_q=31, loc_g_p=12.5, scale_g_p=0.07, loc_r_q=600, scale_r_q=31, loc_r_p=11.5, scale_r_p=0.07):
    #data = create_test_data()
    data = create_normal_data(loc_g_q=600, scale_g_q=31, loc_g_p=12.5, scale_g_p=0.07, loc_r_q=600, scale_r_q=31, loc_r_p=11.5, scale_r_p=0.07)
    generators, retailers = group(data)
    market = Market(generators, retailers)
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

run_step()










    