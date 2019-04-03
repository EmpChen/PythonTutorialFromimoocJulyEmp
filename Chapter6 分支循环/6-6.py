'''
6-7  流程控制语句之条件控制 一，二

Python是根据缩进来区分 代码和代码块的

注释：
    单行注释  #     vscode 快捷键    ctrl+/   mac 里是 command+/
    多行注释  '''  '''注释内容'''  '''   只是一个三引号  但是是成对出现的    vscode 快捷键 alt+shift+a   



# 条件控制 能解决 现实生活中选择性问题  

if 条件控制

mood = True
if mood:
    print("go left")
print("go right")

结果 是两个print都会被打印出来 

mood = True
if mood:
    print("go left")
else:    
    print("go right")

这样 就只会打印 go left   同样的代码 如果设定 mood = False   打印结果就会是 go right

if后面不一定是一个变量 还可以是一个表达式 

a=1
b=2
if a>b:
    print("a>b")
else:
    print('a<b')

=========================================================================================
接下来制作一个login function 如果用户输入正确 返回 successful 如果用户输入错误 返回 Fail



'''

mood = True
if mood:
    print("go left")
print("go right")


mood = True
if mood:
    print("go left")
else:    
    print("go right")

mood = False
if mood:
    print("go left")
else:    
    print("go right")


a=1
b=2
if a>b:
    print("a>b")
else:
    print('a<b')

print("=====================用户登录系统==================================")

account = 'ZhanyuanChen'
password = '123456'

print('Enter your username:')
user_account = input()

print('Enter your Password:')
user_password = input()

# if user_account == account and user_password == password:
#     print("Successful")
# else:
#     print("Failed")

if user_account == account:
    if user_password == password:
        print("successful")
        print("you have entered correct username and password")
    else:
        print("Password Error")
else:
    print("Username Error")

print("you entered user name is: " + user_account)
print("you entered password is: " + user_password)

