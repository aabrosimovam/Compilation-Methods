from rules import rules

def step1(key, L1,L2):
    # применение первой альтернативы к нетерминалу
    
    L1.append([]) # создается пустой список L1
    L1[len(L1) - 1].append(L2[len(L2)-1]) # в этот список добавляется последний символ из L2
    L1[len(L1) - 1].append(1)  # вторым элементом в списке ставится номер альтернативы (1)
    L2.pop() # последний символ из L2 удаляется

    # обрабатывается правая часть правила, 
    # добавляя в L2 каждый симовл в обратном порядке
    right = rules[key]['right']
    for i in range(len(right)-1,-1,-1):
       L2.append(right[i])

def step2(i,L1,L2):
    # сравнение входного символа с порожденным
  
    L1.append([])  # создается пустой список L1 
    L1[len(L1) - 1].append(L2[len(L2)-1]) # в этот список добавляется последний символ из L2
    L2.pop() # последний символ из L2 удаляется
    i += 1 # указатель входной цепочки продвигается на символ вправо 
    return i

def step3(L1):
    # успешное завершение

    result = [] # создается пустой список, который будет содержать результаты вычислений 
    for i in range(0,len(L1)): # перебираем при помощи цикла элементы в стеке L1
        if len(L1[i]) == 2: # если в стеке два элемента 
            for key in rules: # перебор ключей из словаря rules
                if L1[i][0] == rules[key]['left'] and int(L1[i][1]) == rules[key]['alternative'] :
                    result.append(key) 
    return result

def step4():
    return 'b'
    
def step5(i,L1,L2):
    # возврат по терминалу

    # символ из стека L1 переносится в стек L2, 
    # а указатель входной цепочки возвращается на символ назад
    L2.append(f'{L1[len(L1) - 1][0]}')
    i -= 1
    L1.pop()
    return i

def step6a(key,L1,L2):
    # перебор альтернатив
    for i in range (len(rules[key-1]['right'])):  # удаление элементов из стека
        L2.pop()
    L1[len(L1) - 1][1] = L1[len(L1) - 1][1] + 1 # берем следующую альтернативу

    # обрабатывается правая часть правила, 
    # добавляя в L2 каждый симовл в обратном порядке
    right = rules[key]['right'] 
    for i in range(len(right)-1,-1,-1):
       L2.append(right[i])

def step6b():
    # Исключение
    return 'Ошибка'

def step6c(L1,L2):
    # возврат на более высокий уровень
    for key in rules: # перебор ключей из словаря rules
        if L1[len(L1) - 1][0] == rules[key]['left'] and L1[len(L1) - 1][1] == rules[key]['alternative']:
            for i in range(len(rules[key]['right'])):
                L2.pop()
            L1.pop() # звесь удаляем только последний элемент
            L2.append(rules[key]['left']) # добавляем левую часть текущего правила в список L2

def algorithm(string):
    L1 = [] # история проделанных подстановок
    L2 = ['A'] # текущая цепочка выводв 
    state = 'q' # состояние работы 
    i = 0 # текущее значение указателя входной цепочки 
    while True:
        if state == 'q': # состояние нормальной работы 
            for key in rules: # проверяем текущий символ на вершине стека L2 и сравниваем его с левыми частями правил грамматики
                if L2[-1] == rules[key]['left']:
                    step1(key,L1,L2)
                    break
            else:
                if L2[-1] == string[i]: # совпадает ли символ не вершине стека с текущим символом строки
                    i = step2(i,L1,L2) 
                    if len(string) == i: # если завершено чтение входной строки
                        if not L2: # и стек L2 пуст
                            return step3(L1) # успешное завершение
                        else:
                            state = step4() # иначе состояние возврата
                    elif not L2: # если не завершено чтение входной строки и стек Л2 пуст
                        state = step4()
                else: # если символ на вершине стека не совпадает с текущим символом строки 
                    state = step4()
        elif state == 'b': # состояние возврата 
            if len(L1[-1]) == 1: # если в Л1 только 1 символ, то 
                i = step5(i,L1,L2) # возврат в предыдущее состояние
            else:
                for key in rules:
                    # проверка соответствует ли текущее состояние стека Л1 левой части какого-либо правила 
                    if rules[key]['left'] == L1[-1][0] and rules[key]['alternative'] == L1[-1][1] + 1:
                        step6a(key,L1,L2)
                        state = 'q'
                        break
                else:
                    if L1[-1][0] == 'A':
                        return step6b()
                    else:
                        step6c(L1,L2)