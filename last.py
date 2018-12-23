import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from first import get_data
from second import comput_data


def plot_data(df2):
    """
    绘制图形
    """
    
    from pyecharts import Bar, Page

    page = Page()   #实例化，同一网页按顺序展示多图

    df3 = df2.sort_values(["分数差"], axis=0, ascending=[False])


    attr = [x for x in df3.高考省份][:20]
    v1 = [x for x in df3.最高分][:20]
    v2 = [x for x in df3.平均分][:20]
    v3= [x for x in df3.最低分][:20]
    bar = Bar("柱状图数据堆叠示例")
    bar.add("最高分", attr, v1, is_datazoom_show=True, is_datazoom_extra_show=True, mark_point=["max", "min"], mark_line=["average"])
    bar.add("平均分", attr, v2, is_datazoom_show=True, is_datazoom_extra_show=True, mark_point=["max", "min"], mark_line=["average"])
    bar.add("最低分", attr, v3, is_datazoom_show=True, is_datazoom_extra_show=True, mark_point=["max", "min"], mark_line=["average"])

    bar
    page.add(bar)

    # In[11]:


    df3 = df2.sort_values(["分数差"], axis=0, ascending=[False])


    attr = [x for x in df3.高考省份][:20]
    v1 = [x for x in df3.分数差][:20]
    bar2 = Bar("分数差计算统计")
    bar2.add("分数差", attr, v1, is_datazoom_show=True, is_datazoom_extra_show=True, mark_point=["max", "min"], mark_line=["average"])
    page.add(bar2)

    print("render page to 12-24-bar.html")
    page.render("12-24-bar.html")

    # In[12]:

    df3.to_json("test.json")
    
    

df = get_data()
df2 = comput_data(df)
plot_data(df2)
