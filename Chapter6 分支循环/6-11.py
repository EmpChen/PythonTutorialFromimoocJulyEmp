'''
6-11  思考题解答与改变定势思维

a=1 b=0     #两个变量一个为True 一个为False  但是要返回为True的值
if else 可行 但是 我们也可以用 or 
===============================================================
a=1
b=0

if a==1:
    print("a is True")
else:
    print("a is False")
===============================================================

print(a or b)
这会返回 1 ， 一真一假  使用 or 运算符来计算 则会返回为真的元素 
然后判断哪个value 等于1 就返回哪个variable 就可以了 


'''
a=1
b=0

if a==1:
    print("a is True")
else:
    print("a is False")


print(a or b) 
