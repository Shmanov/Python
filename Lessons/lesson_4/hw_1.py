# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами

from sys import argv

par_1, par_2, par_3 = argv

def calculation(output_in_hours,rate_in_hours,premium):
    
    """Функция расчета заработной платы сотрудника """
    try:
        result = float(output_in_hours) * float(rate_in_hours) + float(premium)
    except:
        print("Не корретный ввод параметров")
    return(result)

print(f"Заработная плата составляет {calculation(par_1, par_2, par_3)}")