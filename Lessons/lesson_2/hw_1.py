# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. 
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе

ls = [45, "String",["R134", "R410a" ], {23: 34, 77: 45}, (2, "you"), {11, 3234}]

for l in ls:
    print(f"{l} тип {type(l)}")
