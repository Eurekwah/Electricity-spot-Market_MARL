'''
Date: 2020-10-12 00:44:46
LastEditors: Yuchen ZHANG
LastEditTime: 2020-10-12 00:45:15
FilePath: /project/SpotMarket/create_data.py
'''
import numpy as np
import random
import pandas as pd
import particitant as pt


def create_test_data():
    group = []
    for i in range(1, 11):
        name = "Retailer" + str(i)
        temp_2 = pt.Particitant("Retailer", i, i * 10, name)
        group.append(temp_2)
    for i in range(11, 21):
        name = "Generator" + str(i)
        temp_1 = pt.Particitant("Generator", i, i * 10, name)
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
        temp_r = pt.Particitant("Retailer", temp_r_p[i], temp_r_q[i], name)
        group.append(temp_r)

    for i in range(10):
        name = "Generator" + str(i + 1)
        temp_g = pt.Particitant("Generator", temp_g_p[i], temp_g_q[i], name)
        group.append(temp_g)
    return group