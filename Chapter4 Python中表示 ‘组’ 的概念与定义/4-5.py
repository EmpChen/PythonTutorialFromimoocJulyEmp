'''
4-5  set 集合

除了 元组tuple ()   列表List[]  以外 另一种基本类型为 集合 set 

集合 set 的特性就是 无序

type({1,2,3,4,5,6})   ====>   <class 'set'>

集合 set 没有下标索引 所以不支持切片  也不支持用下表索引访问

集合set 内的元素不允许重复   
    {1,1,2,2,3,3,4,4,5,5}  ====>   {1,2,3,4,5}

集合支持的操作：

    1. 长度判断  len({1,2,3,4})  ====>   4

    2. 是否有其元素    1 in {1,2,3}  ====>  True
       是否没有其元素   1 not in {1,2,3}   ====>  False

集合的特殊操作:
    除掉元素  
        集合1 {1,2,3,4,5,6}     集合2 {3,4,7}   
        
        {1,2,3,4,5,6} - {3,4,7} ====> {1,2,5,6}  {1,2,5,6} 叫做差集 这就是两个集合的差集合

    1. 除掉两个集合共有的元素 
        集合1 - 集合2    大集合 - 小集合

    2. 保留两个集合共有的元素
        集合1 & 集合2  {1,2,3,4,5,6} & {3,4,7} ====> {3,4}  这是交集

    3. 合并集合    
        {1,2,3,4,5,6} | {3,4,7} ====> {1,2,3,4,5,6,7} 
        最后结尾的这个集合 叫做 合集 或 并集

如何定义一个空的集合？
    set() 

    验证是否为空  len(set()) = 0


'''
