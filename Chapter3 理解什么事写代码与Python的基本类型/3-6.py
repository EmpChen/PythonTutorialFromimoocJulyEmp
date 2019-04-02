'''
3-6 字符串:单引号 与 双引号

字符串 ---> 非常常用的基本类型
字符串  str  表示文字类型的数据

str{单引号 ''    双引号" "  三引号 }

>>> 'Helloworld'
'Helloworld'
>>> "helloworld"
'helloworld'
这两个都是可以的  但是区别就是在于 
单引号无法表示 字符串中的引号
    >>> 'let''s'
    'lets'
    >>> 'let''s go'
    'lets go'

如果想使用单引号表示 字符串中的引号 则需要用到转义字符 \ 
    >>> 'let\'s go'
    "let's go"

但是双引号可以表示 
    >>> "let's go"
    "let's go"
    
无论任何符号 在Python中都必须是英文符号

1 与 '1' 不同 因为 1 是 int 而 '1' 是 str







'''