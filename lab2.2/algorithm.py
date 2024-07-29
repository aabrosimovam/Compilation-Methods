from table import rules, form_table, T

table = form_table()

def addtostack(stack, new): # добавить в стек
    if 'T\'' in new:
        new = new.replace('T\'', 'Y')
    elif 'B\'' in new:
        new = new.replace('B\'', 'V')

    # stack.insert(0, new)
    # first_element = stack.pop(0)
    stack = stack[1:]
    stack = list(new) + stack

    # Замена символов в стеке после добавления нового элемента
    stack = [x.replace('Y', 'T\'') for x in stack]
    stack = [x.replace('V', 'B\'') for x in stack]

    return stack


def ejection(string, stack): # выброс
    string = string[1:]
    stack.pop(0)
    return string, stack
   

def algorithm(string):
    stack = ['A']
    pi = []
    while stack and string: # проверка, что стек и строка не пусты
        if string[0] not in T:  # проверка, что текущий символ входит в алфавит T
            return f'Ошибка: символ "{string[0]}" не принадлежит входному алфавиту'
        
        if stack[0] == 'e': #если 1 символ стека е, то его мы удаляем 
            stack.pop(0)
        else: # иначе находим ключ в таблице, который соответствует правилу, которое мы будем использовать
            for i in range(len(table)):
                if table[i][0] == stack[0]:
                    break
            for j in range(len(table[0])):
                if table[0][j] == string[0]:
                    break
            key = table[i][j]
            if key == 0:
                return 'Ошибка: отсутствует правило'
            elif key == -1:
                string, stack = ejection(string, stack)
            else:
                pi.append(key)
                stack = addtostack(stack, rules[key]['right'])
        # if stack and stack[0] == string[0]:
        #     string, stack = ejection(string, stack)
    
    if not stack and not string:  # Если и стек, и строка пусты
        return pi
    else:
        return 'Ошибка: неожиданный конец строки или стека'
