# Реализовать класс Stationery (канцелярская принадлежность). 
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” 
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
# В каждом из классов реализовать переопределение метода draw. 
# Для каждого из классов метод должен выводить уникальное сообщение. 
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра

class Stationery:
    title ="Канцелярская принадлежность"
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print("Выбран инструмент: ручка")
class Pencil(Stationery):
    def draw(self):
        print("Выбран инструмент: карандаш")
class Handle(Stationery):
    def draw(self):
        print("Выбран инструмент: маркер")

s = Stationery()
s.draw()

pen = Pen()
pen.draw()

penc = Pencil()
penc.draw()

han = Handle()
han.draw()


