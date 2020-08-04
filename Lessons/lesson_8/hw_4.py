# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники

class Warehouse:
    pass

class Office_equipment:
    manufacturer
    serial_number
    paper_size
    color

class Printer(Office_equipment):
    pass

class Scaner(Office_equipment):
    pass

class Copier(Office_equipment):
    pass

