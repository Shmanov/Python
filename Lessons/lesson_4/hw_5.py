# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce()

from functools import reduce


def my_func(prev_el, el):

    """ Функция премножает два элемента """
    
    return prev_el * el


list_range = [i for i in range(99, 1001) if i%2 == 0]

print(list_range)

print(reduce(my_func, list_range))