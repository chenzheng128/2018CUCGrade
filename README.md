# 功能说明

读入2017年高考数据， 计算分数差， 并生成可视化效果 

# 运行环境信息
```
import sys, matplotlib
# 生成运行环境信息
print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)
print('Pyecharts version ' + pyecharts.__version__)

Python version 3.6.0 |Anaconda 4.3.1 (x86_64)| (default, Dec 23 2016, 13:19:00) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)]
Pandas version 0.19.2
Matplotlib version 2.0.0
Pyecharts version 0.5.11
```

# 运行方法 

`python last.py` # 可视化效果生成为 `12-24-bar.html`

# 文件说明

* `first.py`  定义读入文件函数
* `second.py` 定义分数差处理函数
* `last.py`   定义绘图函数
* `2017CUCGrade.xlsx` 2017高考数据 http://zhaosheng.cuc.edu.cn/zs/Inquiry/Score.aspx
