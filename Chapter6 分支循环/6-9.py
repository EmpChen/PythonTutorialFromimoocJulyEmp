'''
6-9  流程控制语句之条件控制  三  snippet 嵌套分支 代码块的概念

IDE 中的snippet  snippet意思是 片段 
        tab 到下一个可编写的代码行。
        回到上一个代码行 shift+tab

if 和 else 不用一定要合在一起使用 if 可以单独使用  但是 else 必须与if配对使用 

if condition:
    pass
else:
    pass

pass 是空语句 也叫占位语句   它的作用是保持代码结构的完整性 
在 API接口 里面 Pass 会经常出现的

if else 可以嵌套使用  但是不可过多的嵌套 阅读感会很差 如果需要有多个if else 或者过多的代码的时候可以把这些代码写成一个函数

==========一个结构体==========
if condition:
    if condition:
        pass
    else:
        pass                # pass 中的代码被称为一个代码块
else:                       # 同一个代码块 一行被执行 则全部被执行 
    pass
=============================

认清结构体非常重要 可以判断变量的作用域
=============================
    if condition:           # 这就是一个完成的结构体
        pass
=============================

Code 1          code 1,2,5 为一个代码块 
Code 2          
    Code 3      code 3,4 为另外一个代码块
    Code 4
Code 5

这个怎么判断是不是一个代码块呢？
 根据缩进来判断是否为一个代码块  缩进一样则为一个代码块
 
封装 就是把这些代码装进 Function 或者 modual 中。


'''

a=True
if a == True:
    pass

if a == True:
    if a == True:
        pass
    else:
        pass
else:
    pass

