'''
7-2  for 与 for-else 循环

for loop    for 循环  主要是用来遍历/循环序列,集合和字典

=====================================================
for target_list in expression_list:
    pass

for 变量 in 集合,序列,字典
    pass

fruit=['apple','orange','banana','grape']
for x in fruit:
    print(x)

结果就是:   apple 
          orange
          banana
          grape
=====================================================

for loop可以嵌套    类似于 2维列表

fruitNumber=[['apple','orange','banana'],(1,2,3)]
for x in fruitNumber:
    for y in x:
        print(y)

结果就是:   apple 
          orange
          banana
          grape
          1
          2
          3
=====================================================
print 会以列的形式打印 如果想把结果打印在同一行 则在print语句中加上 end='\n'
print(y,end=' ')  #这是如果想打印在一行中 需要改写的end
print(y,end='\n') #这是默认情况下的end

for else    else在所有列表中的元素都遍历之后 才会执行     for else 不常用                                                            

强行终止    使用 break 语句 强行终止一个维度的循环 loop







'''

fruit=['apple','orange','banana','grape']
for x in fruit:
    print(x)

print("=====================================================")

fruitNumber=[['apple','orange','banana'],(1,2,3)]
for x in fruitNumber:
    for y in x:
        print(y,end=' ')  #这是如果想打印在一行中 需要改写的end
        print(y,end='\n') #这是默认情况下的end

print("=====================================================")

a=[1,2,3]
for x in a:
        

