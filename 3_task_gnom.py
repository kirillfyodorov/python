import time

def gnom(li):
    i = 1 # начинаем с 1, т.к. будем сравнивать с предыдущим
    while i < len(li):
            if not i or li[i - 1] <= li[i]:
                i+=1
            else: # находим элементы стоящие в неправильном порядке и меняем местами
                li[i], li[i - 1] = li[i - 1], li[i]
                i-=1
    print(li)
    
li = [int(i) for i in input('Введите натуральные числа через пробел ').split()] # ввод массива
start_time = time.time() 
gnom(li) # вызов функции
print("--- %s seconds ---" % (time.time() - start_time)) # вывод времени работы программы