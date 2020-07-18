#Спортсмен занимается ежедневными пробежками. 
#В первый день его результат составил a километров. 
#Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. 
#Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. 
#Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня
#Например: a = 2, b = 3.
#Результат:
#1-й день: 2
#2-й день: 2,2
#3-й день: 2,42
#4-й день: 2,66
#5-й день: 2,93
#6-й день: 3,22
#Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

day = 1
result_first_day = float(input("Введите значение результата первой пробежки: "))
result_total = float(input("Введите значение которое необходимо достигнуть: "))

result = result_first_day

while(result <= result_total):
    print(f"{day}-й день: {result:.2f}")
    result += result * 0.1
    day += 1
print(f"{day}-й день: {result:.2f}")
