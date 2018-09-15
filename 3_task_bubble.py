import time

def buble(li):
    n = 1 
    while n < len(li):
         for i in range(len(li)-n):
              if li[i] > li[i+1]:
                   li[i],li[i+1] = li[i+1],li[i] # проходим по множеству, наибольший элемент поднимаем в конец массива
         n += 1 # увеличиваем n, чтобы пройти по массиву еще раз, исключив наибольший элемент
    print(li)

li = [int(i) for i in input('Введите натуральные числа через пробел ').split()] # ввод массива
start_time = time.time()
buble(li) # вызов функции
print("--- %s seconds ---" % (time.time() - start_time)) # вывод времени работы программы