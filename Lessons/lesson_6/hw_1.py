# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). 
# Атрибут реализовать как приватный. 
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). 
# Проверить работу примера, создав экземпляр и вызвав описанный метод
import time
import os


class TrafficLight:
    __color = ("красный", "желтый", "зеленый")
    def runnung(self, red_time = 7, yellow_time = 2, green_time = 5, cycle = 2 ):
        clear = lambda: os.system('cls')
        while cycle > 0:
            print(TrafficLight.__color[0])
            time.sleep(red_time) 
            clear()
            print(TrafficLight.__color[1])
            time.sleep(yellow_time) 
            clear()
            print(TrafficLight.__color[2])
            time.sleep(green_time) 
            clear()
            cycle -=1

trlf = TrafficLight()
trlf.runnung()


