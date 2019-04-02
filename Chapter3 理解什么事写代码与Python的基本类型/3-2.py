'''
3-2 数字：整形与浮点型

Number 数字{int 整数型，float 浮点型，complex 复数，bool 布尔值(True 或 False)}
    Python 2 中还有一个类型为Long 任何精度的整数 只在 Python2 中

int 整数型  正 负都行
float 浮点数 就是带小数点的数
    (其他语言中有分 单精度 float 和 双精度 double)
    (在Python3 中没有单双精度的区分！)
    (其他语言 在整数型中 有分short int long)
    (在 Python3 中都没有 在 Python 2 中有 long)

type() 函数
type() 函数 如果只有一个参数返回对象的类型

type(1)     <class 'int'>
type(1+1.0) <class 'float'>   1+1.0 = 2.0 ---->  float
type(1*1.0) <class 'float'>
type(1.1)   <class 'float'>
type(1+1)   <class 'int'>
type(1*1)   <class 'int'>

type(2/2)   <class 'float'>
    2/2 ---->  1.0 ----> float
    2//2 ---->  1 ----> int     // 整除  只留整数部分

    int / int 如果能整除 结果就是int  不能整除 结果就是float
    int // int 就算不能整除 也只保留整数部分
    

'''



print(type(1))
print(type(1+1.0))
print(type(1*1.0))
print(type(1.1))
print(type(1+1))
print(type(1*1))
print(type(2/2))

