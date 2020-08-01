# Создать текстовый файл (не программно), 
# построчно записать фамилии сотрудников и величину их окладов. 
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников


try:
    with open("Staff.txt", 'r') as f_obj:
                
        text = f_obj.readlines()
        #print(text)
        print("Сотрудники с окладом меньше 20000:" + '\n')
        summ = 0
        cout_pers = 0
        for i in text:
            pers = i.split(' ')
            if int(pers[1]) < 20000:
                summ += int(pers[1]);
                cout_pers += 1
                print(pers[0] , pers[1])
        print(f"Средняя величина дохода {summ / cout_pers:.2f}")
        
except IOError:
    print("Произошла ошибка ввода-вывода!")