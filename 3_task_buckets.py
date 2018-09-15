import time

def bucketSort(li):
    # Ищем наибольший и наименьший элемент массива
    min = li[0]
    max = li[0]
    for i in range(1,len(li)):
        if li[i] < min:
            min = li[i]
        if li[i] > max:
            max = li[i]
    dif = max - min
    if dif == 0: # Если разница равна наибольшего и наименьшего элемента равна нулю, то массив отсортирован
        return li
    print("MIN: " + str(min) + " MAX: " + str(max))
    print("DIFFERENCE BETWEEN MIN&MAX: " + str(dif))
    # Количество блоков(минимум 2)
    n = len(li)
    print("SIZE: " + str(n))
    
    buckets = [[] for i in range(n)]
    # Размещаем входной массив по блокам
    for i in range(len(li)):
        index = int((li[i]-min)/dif*(n-1))
        print("index: " + str(index))
        buckets[index].append(li[i])
    output = []
    # Сортируем блоки сортировкой вставками
    for i in range(n):
        insertionSort(buckets[i])
    # объединяем блоки
    for i in range(len(buckets)):
        while len(buckets[i]) > 0:
            output.append(buckets[i].pop(0))
    return output
# сортировка вставками    
def insertionSort(li):
    if len(li) > 1:
        for i in range(1, len(li)):
            x = li[i]
            index= i
            print("index : " + str(i))
            while ((index > 0) and (li[index-1] > x)):
                li[index] = li[index-1]
                index = index - 1
            li[index] = x
    return li
   
li = [int(i) for i in input('Введите натуральные числа через пробел ').split()] # ввод массива
start_time = time.time() 
li = bucketSort(li) # вызов функции
print(li)
print("--- %s seconds ---" % (time.time() - start_time)) # вывод времени работы программы
