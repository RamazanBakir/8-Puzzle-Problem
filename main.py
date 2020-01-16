def move(tab_original):
    """
    Tree durumlarını kontrol etmek için
    """
    movements = []
    tab = eval(tab_original)
    i = 0
    j = 0
    while 0 not in tab[i]: i += 1
    j = tab[i].index(0)
    

    if i<2:         #0 aşağı git
        tab[i][j], tab[i+1][j] = tab[i+1][j], tab[i][j] 
        movements.append(str(tab))
        tab[i][j], tab[i+1][j] = tab[i+1][j], tab[i][j]

    if i>0:         #0 yukarı git
        tab[i][j], tab[i-1][j] = tab[i-1][j], tab[i][j]  
        movements.append(str(tab))
        tab[i][j], tab[i-1][j] = tab[i-1][j], tab[i][j]  

    if j<2:         #0'ı sağa hareket ettir
        tab[i][j], tab[i][j+1] = tab[i][j+1], tab[i][j] 
        movements.append(str(tab))
        tab[i][j], tab[i][j+1] = tab[i][j+1], tab[i][j]
    
    if j>0:         #0'ı sola taşı
        tab[i][j], tab[i][j-1] = tab[i][j-1], tab[i][j] 
        movements.append(str(tab))
        tab[i][j], tab[i][j-1] = tab[i][j-1], tab[i][j]

    return movements

def h_misplaced(board):
    misplaced = 0
    compare = 1
    tab = eval(board)
    for i in range(0,3):
        for j in range(0,3):
            if tab[i][j] != compare:
                misplaced += 1
            compare += 1
    return misplaced

def a_star(start,end):
    exploid = []
    store = [[h_misplaced(start),start]]
    while store:
        i = 0
        for j in range(1,len(store)):
            if (store[i][0]) > (store[j][0]):
               i = j
        path = store[i]
        store = store[:i] + store[i+1:]
        final = path[-1]
        if final in exploid: continue
        for movement in move(final):
            if movement in exploid: continue
            novo = [path[0] + h_misplaced(movement) + h_misplaced(final)] + path[1:] + [movement] 
            store.append(novo)
        exploid.append(final)
        if final == end: break
    return path


board = str([
                [1,2,3],
                [8,0,4],
                [7,6,5]
            ])

obj_final = str([
                [2,8,1],
                [0,4,3],
                [7,6,5]
            ])



print("A*:")
for i in a_star(board,obj_final):
    print(i, end="\n")