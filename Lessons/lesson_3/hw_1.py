# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль


def division(dividend, divider):
    try:
        return(dividend / divider)
    except ZeroDivisionError:
        return("На ноль делить нельзя!")

print(f"Частное: {division(float(input('Введите делимое: ')), float(input('Введите делитель: ')))}")
    


      