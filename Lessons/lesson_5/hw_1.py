#  Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. 
#  Об окончании ввода данных свидетельствует пустая строка

text = list()
i = 1 
while True:
    content = input("Введите строку " + str(i) + ": ")
    
    if not content:
        print("Ввод данных завершён!")
        break
    
    text.append(content + '\n')
    i += 1


try:
    with open("text.txt", 'w') as f_obj:
        f_obj.writelines(text)
        print("Файл сохранён!")
except IOError:
    print("Произошла ошибка ввода-вывода!")
