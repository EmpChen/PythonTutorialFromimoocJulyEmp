'''
5-11  身份运算符
(这里需要理解对象的定义)(现在只是一个简单的了解)

身份运算符:  is     is not      并且返回一个bool值  用于比较两个对象的存储单元(内存地址)

is  是判断2个表示符是不是引用子一个对象

x is y 类似于 id(x) == id(y)
如果引用的是同一对象 则返回 True 否则(两个表示符不是同一对象) 则返回 False

x is not y 类似于 id(x) != id(y)
如果引用的不是同一对象 则返回 True  否则(两个表示符引用的是同一对象) 则返回 False

>>> a=1
>>> b=2
>>> a is b
False

>>> a=1
>>> b=1
>>> a is b
True

>>> a='hello'
>>> b='world'
>>> a is b
False

>>> c='hello'
>>> a is c
True

>>> a=1
>>> b=1.0
>>> a==b
True            # 这是单纯比较 a 和 b 的值  就是 1==1 True 
>>> a is b
False           # 这是比较 a 和 b 的内存地址 所以会返回 False

>>> id(a)
271112368
>>> id(b)
55816320


>>> a={1,2,3}
>>> b={2,1,3}
>>> a==b
True
>>> a is b
False
>>> c=(1,2,3)
>>> d=(2,1,3)
>>> c==d
False
>>> c is d
False

集合 set 是无序的 所以只比较值  a==b ==> True  id(a) != id(b)  a is b ==> False

c 与 d 是元组tuple 是有序的 要按照顺序来 所以 c != d ==> False  id(c) != id(d) ==> False


'''
