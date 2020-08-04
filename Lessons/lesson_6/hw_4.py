# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, 
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. 
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
# Выполните вызов методов и также покажите результат

import keyboard
import os


class Car:
    speed = 0
    color = ""
    name = ""
    is_police = False
    
    def show_speed(self):
        return Car.speed if Car.speed >= 0 else 0
      

    def go(self):
        
        if Car.speed < 250:
            print("Ускоряемся")
            Car.speed += 1
        else:
            print("Максимальная скорость")
            
        
    def stop(self):
        
        if self.speed > 0:
            print("Тормозим")
            Car.speed -= 1
        else:
            print("Остановились")

    def turn(self, direction):
        if direction == 'L':
            print("Поворачиваем влево")
        if direction == 'R':
            print("Поворачиваем вправо")
class TownCar(Car):
    name = "TownCar"
    def show_speed(self):
        if Car.speed > 60:
            return ("Превышена максимальная скорость")
        else:
            return Car.speed if Car.speed >= 0 else 0
class SportCar(Car):
    name = "SportCar"
    def go(self):
        if Car.speed < 250:
            print("Ускоряемся")
            Car.speed += 10
        else:
            print("Максимальная скорость")
    def stop(self):
        if self.speed > 0:
            print("Тормозим")
            Car.speed -= 10
        else:
            print("Остановились")

class WorkCar(Car):
    name = "TownCar"
    def show_speed(self):
        if Car.speed > 40:
            return ("Превышена максимальная скорость")
        else:
            return Car.speed if Car.speed >= 0 else 0
class PoliceCar(Car):
    name = "PoliceCar"
    pass

car = TownCar()
clear = lambda: os.system('cls')


while True:  
    try:  
        
        
        clear()
        print("Выбор автомобиля клавиши F1-F4, управление клавиши стрелок, выход ESC")
        print(f"Автомобиль: {car.name}")
        print(f"Скорость: {car.show_speed()}")
        
        if keyboard.is_pressed('F1'):   
            car = TownCar()
        if keyboard.is_pressed('F2'):   
            car = SportCar()
        if keyboard.is_pressed('F3'):   
            car = WorkCar()
        if keyboard.is_pressed('F4'):   
            car = PoliceCar()
        if keyboard.is_pressed('Up'):   
            car.go()
        if keyboard.is_pressed('Down'): 
            car.stop()
        if keyboard.is_pressed('Left'):  
            car.turn('L')
        if keyboard.is_pressed('Right'):  
            car.turn('R')   
        if keyboard.is_pressed('Esc'):  
            break  
        else:
            
            pass
    except:
        break 
