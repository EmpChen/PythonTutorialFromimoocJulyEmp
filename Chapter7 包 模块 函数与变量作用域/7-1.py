'''
第七章  包 模块 函数与变量作用域

7-1 while循环与使用场景

循环 loop: while循环(While loop) for循环(for loop)

while loop:

    while expression:
        pass

While loop 的计算步骤:
     while expression =====>  True  ====> do something ====> back to while expression check again
                      =====>  False ====>执行 while loop 外的语句
While 循环很容易造成无限循环的情况 所以在无限循环的时候 使用 control + c 强制终止
为了避免造成无限循环 while expression 不应该为一个变量 应该是一个表达式

count = 0
while count <= 10:
    print("现在的数字是：" + str(count))
    count+=1

count1 = 0
while count1 <= 10:
    print(count1)
    count1+=1
=====================================================================================

while expression:       expression=True ====> run Pass1
    pass1
else:                   expression=False ====> run Pass2
    pass1

count2 = 0
while count2<=10:
    print(count2)
    count2+=1
else:
    print("EOF")
=====================================================================================
递归算法用while合适 其他情况用for loop更多一点

'''

count = 0
while count <= 10:
    print("现在的数字是：" + str(count))
    count+=1

count1 = 0
while count1 <= 10:
    print(count1)
    count1+=1


count2 = 0
while count2<=10:
    print(count2)
    count2+=1
else:
    print("EOF")


