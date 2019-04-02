'''


'''

import re
s = 'A83B72C1D8E67'

def convert(value):
    print(value)
    matched = value.group()
    if int(matched) >= 50:
        return '100'
    else:
        return '0'
r = re.sub('\D\d\D','',s)
r1 = re.sub('\d{2}',convert,r)
print(r1)

