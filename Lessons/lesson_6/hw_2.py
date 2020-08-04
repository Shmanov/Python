# Реализовать класс Road (дорога), в котором определить атрибуты: 
# length (длина), width (ширина). 
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    _length = 0
    _width = 0

    def __init__(self):
        Road._length = float(input("Введите длину дороги в метрах: "))
        Road._width = float(input("Введите ширину дороги в метрах: "))

    def weight_asphalt(self, weight, thickness):
        self.weight = weight
        self.thickness = thickness
        return(Road._length * Road._width * self.weight * (self.thickness / 100)) 

r = Road()
print(r.weight_asphalt(float(input("Введите вес: ")), float(input("Введите толщину в см: "))))
print("Вариант 2 (другой вес и толщина) ")
print(r.weight_asphalt(float(input("Введите вес: ")), float(input("Введите толщину в см: "))))




