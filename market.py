'''
Date: 2020-10-12 00:40:49
LastEditors: Yuchen ZHANG
LastEditTime: 2020-10-12 00:41:50
FilePath: /project/SpotMarket/market.py
'''
import numpy as np
import random
import pandas as pd

def output_data(particitant:list):
    name = particitant[0].kind
    print(name)
    print("name".ljust(15), "price".ljust(10), "quantities".ljust(10))
    for i in particitant:
        print(format(i.name, " <15"), format(i.price, " <10"), format(i.quantities, " <10"))
    print('\n')

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

