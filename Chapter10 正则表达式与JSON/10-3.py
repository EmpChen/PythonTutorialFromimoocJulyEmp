'''







'''

import re

a = 'c0c++7Java8Python9Javascript0'
r = re.findall('\d', a)
print(r)  #打印结果 ['0', '7', '8', '9', '0']

r1 = re.findall('\D', a)
print(r1)  #打印结果 ['0', '7', '8', '9', '0']



