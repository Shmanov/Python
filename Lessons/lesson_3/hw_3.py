# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов

def my_func(arg_1, arg_2, arg_3):
    list_args = list()
    list_args.append(float(arg_1))
    list_args.append(float(arg_2))
    list_args.append(float(arg_3))
    list_args.sort()
    return(list_args[1] + list_args[2])
    
print(f"Сумма наибольших двух: {my_func(input('Введите первый аргумент: '), input('Введите второй аргумент: '), input('Введите третий аргумент: '))}")

