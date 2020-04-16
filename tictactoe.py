def printing(cells):
    print('---------')
    print('|', cells[0], cells[1], cells[2], '|')
    print('|', cells[3], cells[4], cells[5], '|')
    print('|', cells[6], cells[7], cells[8], '|')
    print('---------')


def cells_situation(cells):
    wining_tuples = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    count = 0
    winner_exist = True
    exist=False
    for i in range(len(wining_tuples)):
        a, b, c = wining_tuples[i]
        if cells[a] == cells[b] == cells[c] and cells[a] != '_':
            winner = cells[a]
            exist = True
    if exist:
        print(winner, 'wins')
        winner_exist = False
    else:
        if '_' not in cells:
            print('Draw')
            winner_exist = False
        else:
            pass
    return winner_exist


def reflecting(cells):
    d = 0
    dic = dict()
    for i in range(3,0,-1):
        for j in range(1,4,1):
            dic[str(j)+' '+str(i)]=cells[d]
            d += 1
    return dic


def change_inputs():
    g=False
    while not g:
        g = False
        inp = input('enter coordinates ')
        x = list(inp)
        if len(x)==3:
            enters = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
            if x[1] == ' ':
                if x[0] in enters and x[2] in enters:
                    if 0 < int(x[0]) < 4 and 0 < int(x[2]) < 4:
                        print(inp)
                        g = True
                        return inp
                    else:
                        print('Coordinates should be from 1 to 3!')
                else:
                    print('You should enter numbers!')

            else:
                print('please leave space between numbers ')

i=True
cells = ['_']*9
printing(cells)
dic = reflecting(cells)
winner_exist=True
while winner_exist:
    inp=change_inputs()
    while True:
        if dic[inp] != '_':
            print('This cell is occupied! Choose another one!')
            inp = change_inputs()
        else:
            break
    if i:
        dic[inp] = 'X'
    else:
        dic[inp] = 'O'
    i = not i

    cells = list(dic.values())
    printing(cells)
    winner_exist = cells_situation(cells)
