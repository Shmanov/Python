#  Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
#  Последний атрибут должен быть защищенным и ссылаться на словарь, 
#  содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
#  В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
#  Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
#  проверить значения атрибутов, вызвать методы экземпляров)

class Worker:
    name = " "
    surname = " "
    position = " "
    _income = {"wage": 0, "bonus": 0}

    


class Position(Worker):

    def __init__(self):
        self._income = self._income.copy()
        self.name = input("Введите имя сотрудника: ")
        self.surname = input("Введите фамилию сотрудника: ")
        self.position = input("Введите должность сотрудника: ")
        self._income["wage"] = float(input("Введите оклад сотрудника: "))
        self._income["bonus"] = float(input("Введите премию сотрудника: "))

    def get_full_name(self):
        return("Имя " + self.name + " Фамилия " + self.surname + " Должность " + self.position)
    def get_total_income(self):
        income = sum(self._income.values())
        return("Совокупный доход " + str(income))

w1 = Position()

print(w1.get_full_name())
print(w1.get_total_income())

w2 = Position()

print(w2.get_full_name())
print(w2.get_total_income())

print(w1.name, w1.surname, w1.position, w1._income)
print(w2.name, w2.surname, w2.position, w2._income)