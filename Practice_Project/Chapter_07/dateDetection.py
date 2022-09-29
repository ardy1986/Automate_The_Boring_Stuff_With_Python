# Pratice projects : Date detection

# exp 31/02/2020 31/04/2021 01/01/2001 30/06/1001 15/03/800 25/09/3000 9/12/2000 31/1/2200
import re

test_string = '''31/02/2019 31/04/2021 01/01/2001 30/06/1001
15/03/800 25/09/3000 9/12/2000 31/1/2200 29/02/2020'''
print(test_string)
date_reg = re.compile(r'''
([0-2]\d|3[0-1])
\/
(0\d|1[0-2])
\/
([1-2]\d{3})''', re.VERBOSE)

result = date_reg.findall(test_string)
date =[]
month = []
year = []
valid_date=[]
for k in result:
#    date.append(k[0])
#    month.append(k[1])
#    year.append(k[2])
    if int(k[2])%4 == 0 and int(k[1]) == 2 and int(k[0])<30:
        valid_date.append(k[0]+'/'+k[1]+'/'+k[2])
    elif int(k[1]) == 2 and int(k[0])<29:
        valid_date.append(k[0]+'/'+k[1]+'/'+k[2])
    elif int(k[1])%2 == 1 and int(k[0])<32:
        valid_date.append(k[0]+'/'+k[1]+'/'+k[2])
    elif int(k[1]) > 2 and int(k[1])%2 == 0 and int(k[0])<31:
        valid_date.append(k[0]+'/'+k[1]+'/'+k[2])

print('below are the valid date\n',valid_date)
