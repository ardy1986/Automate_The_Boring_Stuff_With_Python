#!python 3
print('regexStrip.py, using regex to does the same thing as the strip()')

import re

def regStrip(inp,cha):
    print('Strip result are below... \n')
    if cha == '':
        cha = ' '
    return re.compile('(^%s*)(.+?)(%s*$)' % (cha,cha)).search(inp).group(2)

while True:
    testStrip = input('Please type the string (enter blank for exit) ...\n')
    if testStrip == '':
        break
    chaStrip = input('Please type the character for strip ....\n')
    print(regStrip(testStrip,chaStrip))
    print()


