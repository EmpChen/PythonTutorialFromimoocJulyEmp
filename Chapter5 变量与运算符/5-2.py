'''
5-2 变量的命名规则

1. 变量名不能以数字开头

2. 变量名可以由字母、数字、下划线 组成

3. 变量名不可以为系统关键字(Python 系统关键字)
    比如说：and if import 等等
    得到Python3中所有的关键字 可以百度搜索 Python保留关键字 
    或者
    在Python3 的IDLE中执行代码 
        >>> import keyword
        >>> keyword.kwlist
    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def',
     'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
      'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

    type 可以用于变量名 但是 强烈建议不要使用 不要使用！
    因为: 
    >>> type = 1
    >>> type(1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'int' object is not callable

    在这种情况就会报错  当type作为一个变量名 把整型赋给了 type 然后你把int当做一个方法来调用 就大错特错了 
    所以 type print 等这类的虽然可以用作变量名 但是不要用 never

4. Python 变量名要区分大小写
    a=1  print(A)  这是没有用的 
    apple 不等于 Apple

5. 变量本身是没有类型的 字符串、整形、元组都可以复制给变量 
   变量是没有类型减值的


情况1：
>>> a=1
>>> b=a
>>> a=3
>>> print(b)
1

情况2：
>>> a = [1,2,3,4]
>>> b = a
>>> a[0]
1
>>> type(a[0])
<class 'int'>

在这里a[0] 的情况 与 [1,2,3,4][0]的情况是一样的 

当我们对a 进行一下修改 

>>> a[0] = '1'
这个 1 是字符串的1 
>>> print(a)
['1', 2, 3, 4]
>>> print(b)
['1', 2, 3, 4]

我们可以看到 a 与 b 同时修改了





'''


