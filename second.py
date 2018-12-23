import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from first import get_data

def comput_data(df):
    """
    计算分数差
    """
    
    df2 = df.reindex(columns=df.columns.insert(0, '分数差'))
    #df.columns
    return df2

df = get_data()
df2 = comput_data(df)