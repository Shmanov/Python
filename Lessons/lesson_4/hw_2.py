#  Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
#  Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
#  Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
#  Результат: [12, 44, 4, 10, 78, 123].


from random import randint

list_after = list()
list_random = [randint(0, 100) for i in range(20)]
print(list_random)

for i in range(0, len(list_random)-1):
    if(list_random[i + 1] > list_random[i]):
        list_after.append(list_random[i + 1])    
print(list_after)