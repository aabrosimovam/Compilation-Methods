# LL(1) - анализатор
# LL(1) - грамматика: 
rules = {
    1:
    {
        'left': 'A',
        'right': '!B!'
    },
    2: 
    {
        'left': 'B',
        'right': 'TB\''
    },
    3: 
    {
        'left': 'B\'',
        'right': 'e'
    },
    4: 
    {
        'left': 'B\'',
        'right': '+TB\''
    },
    5: 
    {
        'left': 'T',
        'right': 'MT\''
    },
    6: 
    {
        'left': 'T\'',
        'right': 'e'
    },
    7: 
    {
        'left': 'T\'',
        'right': '*MT\''
    },
    8: 
    {
        'left': 'M',
        'right': 'a'
    },
    9: 
    {
        'left': 'M',
        'right': 'b'
    },
    10: 
    {
        'left': 'M',
        'right': '(B)'
    }
}

T = ['!', '+', '*', '(', ')', 'a', 'b']
N = ['A', 'B', 'B\'', 'T', 'T\'', 'M']

cols = len(T) + 1 # число столбцов
rows = len(N) + len(T) + 1  # число строк

def form_table():
    table = [[0]*cols for _ in range(rows)]

    for i in range(1, cols):
        table[0][i] = T[i - 1]
    
    j = 0
    for i in range(1, rows):
        if (i < len(N) + 1):
            table[i][0] = N[i - 1]
        elif (i < rows):
            table[i][0] = T[j]
            j += 1 

    j = 1
    for i in range (len(N) + 1, rows):
        table[i][j] += -1
        j += 1
    
    table[1][1] = 1
    table[2][4] = 2; table[2][6] = 2; table[2][7] = 2
    table[3][1] = 3; table[3][2] = 4; table[3][5] = 3
    table[4][4] = 5; table[4][6] = 5; table[4][7] = 5
    table[5][1] = 6; table[5][2] = 6; table[5][3] = 7; table[5][5] = 6
    table[6][4] = 10; table[6][6] = 8; table[6][7] = 9

    return table

# table = form_table()
# for row in table:
#     print(row)
