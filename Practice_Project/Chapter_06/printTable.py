# Practice Projects - Table Printer

def print_table(inp):
    col_width = [0] * len(inp)
    temp =''
    for k in range(len(inp)):
        for l in range(len(inp[k])):
            if col_width[k] <= len(inp[k][l]):
                col_width[k] = len(inp[k][l]) + 1

    for k in range(len(inp[0])):
        for l in range(len(inp)):
            temp += inp[l][k].rjust(col_width[l])
        print(temp)
        temp=''
    return

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

print_table(tableData)
