# Practice project: Sandwich Maker
import pyinputplus as pyip
total_price=0

# bread type: wheat, white or sourdough
btype = pyip.inputMenu(['wheat $0.1','white $0.1','sourdough $0.2'], numbered=True)
btype_price = {'wheat $0.1': 0.1, 'white $0.1': 0.1, 'sourdough $0.2': 0.2}
total_price += btype_price[btype]

# protein type: chicken, turkey, ham, or tofu
ptype = pyip.inputMenu(['turkey $1','ham $2','tofu $0.5'], numbered=True)
ptype_price = {'turkey $1': 1, 'ham $2': 2, 'tofu $0.5': 0.5}
total_price += ptype_price[ptype]

# if they want cheese, yes or no
cheese = pyip.inputYesNo('Do you want cheese?\n')

# if cheese yes, chese type: cheddar, Swiss or mozarella
if cheese == 'Yes':
    ctype = pyip.inputMenu(['cheddar $0.3','Swiss $0.5','mozarella $0.8'], numbered=True)
    btype_price = {'cheddar $0.3': 0.3, 'Swiss $0.5': 0.5, 'mozarella $0.8': 0.8}
    total_price += ptype_price[ptype]

# if they want mayo, mustard, lettuce, or tomato, yes or no
mayo = pyip.inputYesNo('Do you want mayo?\n')
mustard = pyip.inputYesNo('Do you want mustard?\n')
lettuce = pyip.inputYesNo('Do you want lettuce?\n')
tomato = pyip.inputYesNo('Do you want tomato?\n')

# how many sandwhiches they want
total_sandwich = pyip.inputInt('how many sandwhiches you want?:\n', min=1)
print('Your total price is $'+ str(total_sandwich*total_price))
