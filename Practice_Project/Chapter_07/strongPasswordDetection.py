# Practice Project; Strong Password Detection

import re

while True:
    pwd = input("Input your designated password:\nPlease use a strong password\n")
    if len(pwd) < 8:
        print("Password is less then 8 character, please use a strong password\n")

    # password have to have mininum uppercase and lower case character
    elif re.compile(r'[a-z]').search(pwd) == None:

        print("Password doesn't have lowercase character, please use a strong password\n")

    elif re.compile(r'[A-Z]').search(pwd) == None:

        print("Password doesn't have lowercase character, please use a strong password\n")


    #  password have to have at least one digit
    elif re.compile(r'[0-9]').search(pwd) == None:

        print("Password doesn't have numeric character, please use a strong password\n")

    else:
        print("Password inputed is a strong password")
        break
