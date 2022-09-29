def comma_code(inp):
    comma = ""
    for i in range(len(inp) - 1):
        comma += inp[i] + ", "
    comma += 'and ' + inp[len(inp) - 1]
    print(comma)


spam = ["apples", "bananas", "tofu", "cats"]
comma_code(spam)
