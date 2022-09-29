def is_valid_chess_board(inp):
    # Create valid spaces and unit
    valid_spaces = []
    for i in range(1,9):
        for j in ('abcdefgh'):
            valid_spaces.append(str(i)+j)
    valid_unit = {'bking':1,'wking':1,'bqueen':1,'wqueen':1,'bbishop':2,'wbishop':2,'wknight':2,'bknight':2,
                  'brook':2,'wrook':2,'wpawn':8,'bpawn':8}

    # Check validity
    count ={}
    number_of_invalid = 0
    for i,j in inp.items():
        count.setdefault(j,0)
        count[j] = count[j] + 1
        if i not in valid_spaces:
            number_of_invalid += 1
        if count[j] > valid_unit[j]:
            number_of_invalid += 1
    print('Numbers of invalid space and unit in the chess_board are ' + str(number_of_invalid))
    if number_of_invalid > 0:
        print('Chess board is invalid')
    else:
        print('Chess board is valid')



chess_board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
inspect = is_valid_chess_board(chess_board)
