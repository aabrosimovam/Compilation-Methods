rules = {
    1:
    {
        'left': 'A',
        'alternative': 1,
        'right': '!B!'
    },
    2: 
    {
        'left': 'B',
        'alternative': 1,
        'right': 'T'
    },
    3: 
    {
        'left': 'B',
        'alternative': 2,
        'right': 'T+B'
    },
    4: 
    {
        'left': 'T',
        'alternative': 1,
        'right': 'M'
    },
    5: 
    {
        'left': 'T',
        'alternative': 2,
        'right': 'M*T'
    },
    6: 
    {
        'left': 'M',
        'alternative': 1,
        'right': 'a'
    },
    7: 
    {
        'left': 'M',
        'alternative': 2,
        'right': 'b'
    },
    8: 
    {
        'left': 'M',
        'alternative': 3,
        'right': '(B)'
    }
}