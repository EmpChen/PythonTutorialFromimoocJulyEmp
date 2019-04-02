'''



'''

import re

language = 'PythonC#JavaC#PHPC#'
# r = re.sub('C#','Go',language,2)
# print(r)
print('=================================')

# language = language.replace('C#','Go',2)
# print(language)


def convert(value):
    matched = value.group()
    return "11" + matched + "11"

r = re.sub('C#',convert,language,1)
print(r)
