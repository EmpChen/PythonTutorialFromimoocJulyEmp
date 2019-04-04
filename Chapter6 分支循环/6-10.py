'''
6-10 流程控制语句之条件控制 四 elif的优点

问题：
    a=x 当a=1 ----> 吃苹果
        当a=2 ----> 吃orange
        当a=3 ----> 吃banana
        当a=其他 ----> go shopping
如何表达这个条件？

笨方法：

a=input()
if a==1:
    print('Eat Apple.')
else:
    if a==2:
        print('Eat Orange.')
    else:
        if a==3:
            print('Eat banana')
        else:
            print('go shopping')

并且 这种方法是错的 因为无论你输入什么都会返回 go shopping  
原因是在 terminal中输入的是String  而循环中对比的是int  用string和int 对比一定会一直返回False 

我们可以进行验证一下 在 a=input() 下面一行 加一行代码看看输入的类型是什么

print(type(a))    =========>    <class 'str'>
返回结果是 str     这是因为 input() 函数 默认把所有用户输入的都认为是 str

所以我们先要把 str 转换成 int  然后在进行比较 所以代码完整版如下


a=input()
a=int(a)
if a==1:
    print('Eat Apple.')
else:
    if a==2:
        print('Eat Orange.')
    else:
        if a==3:
            print('Eat banana')
        else:
            print('go shopping')


这个代码使用了三个if else 语句进行层层嵌套 非常的难以阅读 所以不推荐！！
一般一层嵌套就可以了 再多的就不要用了 




'''

# 问题：
#     a=x 当a=1 ----> 吃苹果
#         当a=2 ----> 吃orange
#         当a=3 ----> 吃banana
#         当a=其他 ----> go shopping
# 如何表达这个条件？

# 笨方法：

# a=input()
# print(type(a))
# if a==1:
#     print('Eat Apple.')
# else:
#     if a==2:
#         print('Eat Orange.')
#     else:
#         if a==3:
#             print('Eat banana')
#         else:
#             print('go shopping')


a=input()
a=int(a)
if a==1:
    print('Eat Apple.')
else:
    if a==2:
        print('Eat Orange.')
    else:
        if a==3:
            print('Eat banana')
        else:
            print('go shopping')

print('=============================================')
if a==1:
    print("Eat Apple")
elif a==2:
    print("Eat Orange")
elif a==3:
    print("Eat Banana")
else:
    print("Go Shopping")
    
