'''
3-5 数字: 布尔类型 与 复数

Number   除 int 和 float 外 还有两种数据类型   bool  和 complex 

bool 布尔类型 表示真假  
complex  表示复数

bool: True 表示为真 T为大写
      False 表示为假 F为大写

bool 是Number的一个类型  为什么呢？

>>> int(True)
1
>>> int(False)
0
==========================================
>>> bool(1)
True
>>> bool(0)
False
>>> bool(2)
True
>>> bool(2.2)
True
>>> bool(-1.1)
True
>>> bool(0b10)
True

bool 只有是非0 就是True  如果是 0 或者 None 就是 False
Python中任何空值 都是False 非空值 都为 True

>>> bool(0)
False
>>> bool(None)
False

None类型
None类型 表示一个Null对象(没有值得对象)。 Python提供了一个Null对象，在程序中表示为None。
如果一个函数没有显式的返回值，则会返回该对象。None经常用作可选参数的默认值，以便让函数检测调用者是否为该参数实际传递了值。
None 没有任何属性，在布尔表达式中求值时为False。

不只是整数类型可以与bool互换，字符串也可以。
>>> bool('abc')
True
>>> bool(' ')
True
>>> bool('')
False
>>> bool()
False
>>> bool([1,2,3])
True
>>> bool([])
False
>>> bool({})
False
>>> bool({1,2,3})
True


复数 ---- complex 
用 j 表示复数    一般不会经常用  以后可以研究一下

'''