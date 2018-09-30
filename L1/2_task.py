print('Введите числа через запятую без пробелов, сколько угодно, потом нажмите Enter.\nКомплексные числа вводятся в виде "a+bj".')
p = input()
l = p.split(',')
comp = [] # Комплексные числа
fl = [] # Вещественные
nat = [] # Натуральные
cel = [] # Целые
smp = [] # Простые
chet = [] # Четные
nch = [] # Нечетные
k = 0


def func(c): # проверка комплексного (записывается через j)числа
    for j in range(len(c)):
        if c[j] == 'j':
            return True
        else:
            continue
    return False


def sfl(d): # проверка вещественного числа(записывается через точку)
    for j in range(len(d)):
        if d[j] == '.':
            return True
        else:
            continue
    return False


def prs(h): # проверка простого числа
    n = int(h)
    if n < 0:
        n *= -1
    if n == 1:
        return True
    elif n <= 3:
        return True
    elif (n % 2 == 0) or (n % 3 == 0):
        return False
    for j in range(2, n + 1): # перебор чисел, на которые может делиться проверяемое число
        if j*j <= n:
            if n % j == 0:
                return False
            else:
                continue
        else:
            return True
    return True


for i in range(len(l)):
    y = l[i]
    if y == '0': # подсчет нулей
        k += 1
        continue
    elif func(y) is True: # проверка комплексного числа
        comp.append(y)
        continue
    elif sfl(y) is True: # проверка вещественного числа
        fl.append(y)
        continue
    elif int(y) > 0: # проверка целого и натурального числа
        nat.append(y)
        cel.append(y) 
        if int(y) % 2 != 0:
            nch.append(y) # проверка нечетности
            if prs(y) is True:
                smp.append(y) # проверка простого числа
                continue
            else:
                continue
        else:
            chet.append(y)
            continue
    else:
        cel.append(y) # проверка нечетности и простое/не простое для отрицательных чисел
        if (int(y)*-1) % 2 != 0:
            nch.append(y)
            if prs(y) is True:
                smp.append(y)
                continue
            else:
                continue
        else:
            chet.append(y)
            continue

print('Комплексные числа', '\n', comp, '\nВещественные числа:', '\n', fl, '\nРациональные числа:', '\n', fl, '\nНатуральные числа:', '\n', nat, '\nЦелые числа', '\n', cel, '\nПростые числа:', '\n', smp, '\nЧетные числа:', '\n', chet, '\nНечетные числа:', '\n', nch, '\nИ ', k, ' нулей')
# вывод числел, распределенных по критериям