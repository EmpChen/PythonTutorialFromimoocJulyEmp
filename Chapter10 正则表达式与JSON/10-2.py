'''
10-2 元字符与普通字符

更改一下   a = 'c0c++7Java8Python9Javascript0'
要求 把a字符串中的所有数字都提取出来

可以用for in 语句 但是 我觉得做不出来
可是 for in 这种情况的缺点很多 非常浪费脑力 而且 代码看上去与不会太简洁

所以这种情况依旧使用正则表达式来解决：
    正则表达式提供了0-9 的数字表示方法为 \d 
    代码写成: r = re.findall("\d", a)
        import re

        a = 'c0c++7Java8Python9Javascript0'
        r = re.findall('\d', a)
        print(r)  #打印结果 ['0', '7', '8', '9', '0']

对于类似‘Python’ 这样的字符 叫做普通字符 
对于类似‘\d’ 这样的字符 叫做元字符


经过百度
正则表达式语言由两种基本字符类型组成：原义（正常）文本字符和元字符。
元字符使正则表达式具有处理能力。
所谓元字符就是指那些在正则表达式中具有特殊意义的专用字符，可以用来规定其前导字符（即位于元字符前面的字符）在目标对象中的出现模式。

元字符有很多 可以通过百度 正则表达式 看到.

example:
    找到 a 中 所有非数字字符

    a = 'c0c++7Java8Python9Javascript0'
    r = re.findall('\D', a)
    print(r)  
    #['c', 'c', '+', '+', 'J', 'a', 'v', 'a', 'P', 'y', 't', 'h', 'o', 'n', 'J', 'a', 'v', 'a', 's', 'c', 'r', 'i', 'p', 't']


'''
import re

a = 'c0c++7Java8Python9Javascript0'
r = re.findall('\d', a)
print(r)  #打印结果 ['0', '7', '8', '9', '0']

r1 = re.findall('\D', a)
print(r1)  #打印结果 ['0', '7', '8', '9', '0']

