# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой

class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    dividend = float(input('Введите делимое: '))
    divider = float(input('Введите делитель: '))
        
    if divider == 0:
        raise MyZeroDivisionError("Вы ввели 0! Делить на ноль нельзя!")
    else:
       print(f"Результат деления: {dividend / divider}")
except MyZeroDivisionError as err:
    print(err) 
