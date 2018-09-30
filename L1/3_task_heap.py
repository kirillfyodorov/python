import time

def heapSort(li):
    def downHeap(li, k, n): # построение пирамиды(восстановление пирамиды после удаления элемента)
        new_elem = li[k]
        while 2*k+1 < n:
            child = 2*k+1
            if child+1 < n and li[child] < li[child+1]: # основное условие дерева
                child += 1
            if new_elem >= li[child]:
                break
            li[k] = li[child]
            k = child
        li[k] = new_elem
  
    size = len(li)
    for i in range(size//2-1,-1,-1):    # создание изначальной пирамиды
        downHeap(li, i, size)
    for i in range(size-1,0,-1): # сортировка пирамиды
        temp = li[i] # перемещаем верхушку в начало отсортированного списка
        li[i] = li[0]
        li[0] = temp
        downHeap(li, 0, i) # находим нужное место в пирамиде для нового элемента
    print(li)
    
li = [int(i) for i in input('Введите натуральные числа через пробел ').split()] # ввод массива
start_time = time.time()    
heapSort(li) # вызов функции
print("--- %s seconds ---" % (time.time() - start_time)) # вывод времени работы программы