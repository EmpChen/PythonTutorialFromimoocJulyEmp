'''
4-3 元组  tuple
 
元租用小括号表示 用逗号将元素隔开 元组中的元素可以为不同类型    (元素,元素,元素,元素,元素)

访问元组 元组相加 元祖乘数字 与列表相同

(0,1,2,3,4)[0]   ====>  0
(0,1,2,3,4)[0:2] ====>  (0, 1)
(0,1,2) + (3,4,5) ====> (0,1,2,3,4,5)
(0,1,2) * 3 ====>  (0, 1, 2, 0, 1, 2, 0, 1, 2)

如果元组中只有一个元素  则不会认为是元组类型  而是会认定为元素的类型
type((1)) ====>  <class 'int'>

=================================================================================
因为在python中 () 也可以表示一种数学的运算  如 (1+1)*2  
()就叫做运算优先级括号 这就会和元组产生冲突 
当有歧义的时候 Python中规定 当有一个括号并且其中只有一个元素 就当做运算符号来进行计算
=================================================================================
但是这在list中就不会有这样的顾虑
=================================================================================
但如何定义只有一个元素的元组呢？  (1,) 加一个都好加装后面有一个元素
  如何定义一个元素都没有的元组呢？  ( )    type(( ))   ====>   <class 'tuple'>

'''
