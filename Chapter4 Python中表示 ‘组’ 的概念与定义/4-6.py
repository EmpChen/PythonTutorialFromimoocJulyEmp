'''

4-6 dict 字典

    dict 字典是Python的基本数据类型
    dict 一般会有两个值  key  value   
    key  就是 关键字   value 就是 相应的数据得值

    dict 可以有多个 key 和 多个value  

    定义一个dict：
    {key 1: value 1,key 2: value 2,key 3: value 3, ......}

    {1:1, 2:2, 3:3}
    {'Q':'kill','R':'kiss','w':'kim'}

    字典是无序的 所以字典无法使用下标进行访问  所以dict通过key来访问
    {'Q':'kill','R':'kiss','w':'kim'}{'Q'}  ====>  kill

    dict 字典不可以有两个相同的 key 
    {1:'kill','1':'kiss','E':'kim','R':'business'}
    这里面的 1 与 '1' 是不同的  虽然都是1 但是第一个是数字 int  第二个是字符 string

    字典dict中 valur所能选取的Python数据类型总结：
    Value： 任意Python基本数据类型
            str int float list set dict 
            
            字典中的value 可以使另外一个字典 
            type({1:'kill','1':'kiss','E':{1:1},'R':'business'})  ====>  dict

    key：必须是不可变的类型 eg: int  str
        列表不可以 列表是可变的 list        元组也是不可以的 元组也是可变的 tuple


    如何定义一个空的字典呢？
        一个空的字典 表示就是一个空的大括号 {}
        type({}) ====>  dict
        



'''
