'''
5-12  如何判断变量的值, 身份 与 类型

值 Value  身份 id  类型 type

type 类型的判断 
>>> a=1
>>> type(a)==int
True

如果这样做就太麻烦了

函数(Function) isinstance(变量名称要判断的对象,类型名称甚至可以为元组)  返回一个bool类型

isinstance(a,int) ====>   True

如果为元组: 
isinstance(a,(int,str,float))
a 是不是int str float 中的一种？  同样也会返回 一个bool类型 

>>> isinstance(a,(int,str,float))
True

'''
