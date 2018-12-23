
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


# In[2]:

df = pd.read_excel("2017CUCGrade.xlsx")
df


# In[3]:

#df.index
df.columns
#df.values
#type(df.ix[20])
df2 = df.reindex(columns=df.columns.insert(0, '分数差'))
#df.columns
df2


# In[4]:

#df.最高分 - df.最低分 < 10 
#plt.plot(df.最高分 * 2)
#plt.show()
#df.高考省份


# In[5]:

df2.分数差 = df.最高分 - df.最低分
df2


# In[6]:

df2.sort_values(["招生类别", "分数差"], axis=0, ascending=[False, False])
df3 = df2.sort_values(["最高分"], axis=0, ascending=[False])
#df2.sort_index(axis=0, ascending=False)
df3

df
#dfn = df [["最高分", "最低分"]]
#dfn.ix[3] - dfn.ix[2]
df [df.最高分 > 700]


# In[15]:

df2.describe()


# In[16]:

df2.boxplot()
#plt.show()  # used in box
print("save fig to 12-24-box.png")
plt.savefig("12-24-box.png")


# In[8]:

df3.columns


# In[9]:

# pandas 转换为 echart 数据
# REF: http://pyecharts.org/#/zh-cn/prepare?id=pandasampnumpy-%E7%AE%80%E5%8D%95%E7%A4%BA%E4%BE%8B

[x for x in df3.高考省份][:10]


# In[14]:




# In[10]:

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
# In[13]:
pd.read_csv("sort_v2_utf8.csv").to_json("test.json")

