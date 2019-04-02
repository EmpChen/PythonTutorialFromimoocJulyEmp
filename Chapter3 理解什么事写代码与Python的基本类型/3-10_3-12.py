'''
3-10 ---- 3-12  字符串运算
合并两个字符串 & 截取字符串

合并 拼接 用 + (加号)  * (乘号)

"Hello" + "world" =======>  "Helloworld"
"hello" * 3 =======>  "hellohellohello"
"hello" * "world" =======>  报错 字符不可以与字符相乘
            字符串只能与数字相乘

截取 获取字符串 中的单个字符
"Helloworld"[0] ==> H
"Helloworld"[3] ==> l

只要输入字符的字号就能得到该字符  字号从0开始

"H  e   l   l   o   w   o   r   l   d"
"0  1   2   3   4   5   6   7   8   9"

如果中间带空格 空格也算一位
"H  e   l   l   o       w   o   r   l   d"
 0  1   2   3   4   5   6   7   8   9   10      这是字号
-11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1      这是n次的字符

"hello world"[-3]  ====>  r
字符串后面的方括号[]中 如果是正数 代表字号  从0开始
字符串后面的方括号[]中 如果是负数 从该字符串最后向前数 多少个位的字符  
                            -n  就是从后往前数 第n个字符

如果要得到 w 在 "hello world" 中
"Hello world"[6]  ====> w
"Hello world"[-5] ====> w


截取 获取字符串 中的一组字符  要从截取字符串的起点 并且往后截取几个字符
"hello world"[0:5]   ====>  hello
"hello world"[0:-1]  ====>  hello worl  我们发现d消失了
        这里面的-1 代表了 "步长" 往回数1个字符
"hello world"[0:-3] ====> hello wo  

Question: 截取 world的两种不同的方法
"Hello world"[6:11]  ====> world   但是奇怪的是 这个字符串没有第11个字符 所以无论你写什么数字 只要大于10 就没问题
"Hello world"[6:]   ====> world   可以使用这个样子 系统就明白从第六个字符开始截取 一直截取到字符串结束

"hello python java c# javascript php ruby"
截取 编程语言 去掉 hello
"hello python java c# javascript php ruby"[6:]  ====>  python java c# javascript php ruby
这样就去掉了 hello

[6:] 从第6位向右截取到字符串结束
[:4] 从字符串 0位向后截取 4个字符
[:-4] 从字符串 0位向前截取 4个字符   字符串第一个字符永远是0号字符
[-4:] 从字符串 -4位向后截取到字符串结尾。  ====> ruby
'''
