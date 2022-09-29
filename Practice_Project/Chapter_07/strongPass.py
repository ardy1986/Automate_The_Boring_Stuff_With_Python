#! python3
print('strongPass.py - Strong password detection using regex')

import re

def sPass(inp):
    if re.compile(r'\w{8,}').search(inp) == None:
        return 'Password have less then 8 character, please input a new one\n'
    elif re.compile(r'[A-Z]+').search(inp) == None:
        return 'Password doesn\'t have at least one uppercase letter, please input a new one\n'
    elif re.compile(r'[a-z]+').search(inp) == None:
        return 'Password doesn\'t have at least one lowercase letter, please input a new one\n'
    elif re.compile(r'[0-9]+').search(inp) == None:
        return 'Password doesn\'t have at least one number, please input a new one\n'
    else:
        return 'Password is strong\n'

while True:
    testPass = input('Please type the password (enter blank for exit) ...\n')
    if testPass == '':
        break
    print(sPass(testPass))

