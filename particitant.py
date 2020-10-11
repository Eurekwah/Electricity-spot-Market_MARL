'''
Date: 2020-10-12 00:38:10
LastEditors: Yuchen ZHANG
LastEditTime: 2020-10-12 00:40:04
FilePath: /project/SpotMarket/particitant.py
'''
import numpy as np
import random
import pandas as pd

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
            
