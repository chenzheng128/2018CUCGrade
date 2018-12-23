# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 设置字体，解决中文乱码问题
from pylab import mpl
#mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


def get_data():
    """
    读入excel数据
    """
# In[2]:
    df = pd.read_excel("2017CUCGrade.xlsx")
    return df


df = get_data()