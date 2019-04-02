'''
10-1 初识正则表达式

学习 正则表达式 是为了 原生爬虫
Json 是一种 轻量级的数据格式

什么是正则表达式？正则表达式有什么作用？
正则表达式 是一个特殊的 字符串序列。它可以检测一个字符串是否与我们所设定的字符序列相匹配。

匹配就可以实现 快速检索文本 实现一些替换文本的操作。
example：
    1. 检查一串数字是否是电话号码
    2. 检测一组字符串是否是个Email
    3.  把文本里指定的残次替换为另外一个单词

正则表达是用的6 就不太需要系统内置的 字符串处理函数 
        -----别听他的 系统内置的 字符串处理函数 也要好好用

正则表达式 是操作字符串的
example:
    a = 'c|c++|Java|Python|Javascript'
    #检测字符串a中是否有Python
    
    #第一种方法  Python内置函数 index
    a.index('Python')>-1
    print(a.index('Python')>-1)     #返回结果为 True   说明包含Python

    #第二种方法  用 in 关键字
    print('Python' in a)            #返回结果为 True   说明包含Python

    #正则表达式  Python提供了一个模块 叫做 re  专门操作正则表达式  记得要先import re
    #re.findall(pattern,String)
    re.findall('Python',a)

    返回结果:
        ['Python']

    返回了一个列表 包括了 Python字符串  
    之所以会返回一个列表是因为 findall 方法是找到全部，所以可能不止一个 就会以列表的形式 把所有找到的元素返回过来

    所以我们在加一个 if loop

    r = re.findall('Python',a)  #使用一个变量来接收一下结果  并且把结果打印出来
    print(r)
    if len(r) >0:
        print("字符串中包含Python")
    else:
        print("不包含")


以上就是 正则表达式的基础用法  但是 只是单单找了一个常量  没有什么意义 规则也比较简单 和具体 

正则表达式最重要的就是 规则 

下节会给正则表达式设定一个规则 比较抽象的规则 让正则表达式 有意义

how to install bash terminal on vscode
https://patrickbutlermonterde.com/2017/05/03/visual-studio-code-integrated-terminal/
'''
import re

a = 'c|c++|Java|Python|Javascript'
#检测字符串a中是否有Python
    
#第一种方法  Python内置函数 index
a.index('Python')>-1
print(a.index('Python')>-1)     #返回结果为 True   说明包含Python

#第二种方法  用 in 关键字
print('Python' in a)            #返回结果为 True   说明包含Python

#正则表达式  Python提供了一个模块 叫做 re  专门操作正则表达式
#re.findall(pattern,String)
r = re.findall('Python',a)  #使用一个变量来接收一下结果  并且把结果打印出来
print(r)
if len(r) >0:
    print("字符串中包含Python")
else:
    print("不包含")
