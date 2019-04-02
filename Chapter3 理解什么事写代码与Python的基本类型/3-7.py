'''
3-7 多行字符串 
三引号  超长的字符串 不适宜阅读  
    所以 Python 中规定(建议) 每行的宽度为 79 个字符

三引号 可以使三个单引号 或者 三个双引号  要成对出现  可以回车
但是    IDLE中会在你每一次回车的时候 加上 \n

还是使用三个双引号吧 虽然在IDLE中可以使用三个单引号 但是三个单引号代表多行注释


    >>> """ helloworld
            helloworld
            helloworld"""
' helloworld\nhelloworld\nhelloworld'

为什么在IDLE中会有\n 出现？
    因为在Python 中 >>>  表示要接收一个输入  无论是可见的 abcd 或者 是不可见的tab enter等 
    IDLE要把所有的输入都要显示出来，所以会用转义字符 来表示无法显示的字符

    但是  >>> """helloworld\nhelloworld\nhelloworld"""
              'helloworld\nhelloworld\nhelloworld'
            如果这样收入 同时也会输出一样的字符 

            print() 可以吧\n 等转义字符解析并实现 
            >>> print("""hello world\nhelloworld\nhelloworld\n""")
            hello world
            hello world
            hello world

IDLE  单引号换行
    >>> 'hello\
        world'
    'helloworld'
    >>> "hello\
        world"
    'helloworld'




'''

print ("""hello world\nhello world\nhello world\n""")