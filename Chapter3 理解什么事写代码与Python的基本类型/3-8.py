'''
3-8 转义字符

转义字符 ---->  特殊的字符{表示无法"看到"的字符 换行 等，与语言本身语法有冲突的字符}

转义字符 
    \n  换行
    \`  单引号
    \t  横向制表符
    etc  还有很多 可以自行百度

    \n \r 容易搞混 不是同一个概念 可以找一下 百度 google 
    \n 换行   \r  回车 

    print 输出 hello \n world
    
    print('hello \\n world')  这与let\'s go 同理
    这个可以再输出文件夹路径的时候用到
    >>> print('C:\\fatherfoldername\\childfoldername')
    C:\fatherfoldername\childfoldername

    但是要是有太多的 \\ 这样做也是真的很麻烦  
    
    所以在路径前面加一个 r  表示r后面的字符串不是一个普通字符串 而是一个原始字符串
                        r 的大小写不影响
        这个原始字符串  所见即所得
        print(r'C:\fatherfoldername\childfoldername')
        
        注意 这种情况不是普遍适用的 
        如果字符串里面有单引号就不能用
        print(r'let's go')          这种情况就会报错  因为出现了三个单引号
        所以换成双引号就没问题了啊
        print(r"let's go")



    



'''