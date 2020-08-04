# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. 
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

import datetime

class Data:
    def __init__(self, data):
        self.data = data    
    
    @classmethod
    def to_int(cls, data):
       print (int(data.replace('-','')))

    @staticmethod
    def valid(data):
        dmy = data.split('-')
        try:
            datetime.datetime(year = int(dmy[2]), month = int(dmy[1]), day  = int(dmy[0]))
            print("Дата корректная")
        except ValueError:
            print("Не корректная дата")
       

data = input("Введите дату в формате «день-месяц-год»: ")

Data.to_int(data)
Data.valid(data)

