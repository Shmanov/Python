#  Программа запрашивает у пользователя строку чисел, разделенных пробелом.
#  При нажатии Enter должна выводиться сумма чисел.
#  Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
#  Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. 
#  Но если вместо числа вводится специальный символ, выполнение программы завершается. 
#  Если специальный символ введен после нескольких чисел, 
#  то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программ

sum_total = 0
#list_digits = list()
stop = True

while stop:
   
    string_digits = input("Введите строку чисел, разделенных пробелом. Для выхода нажмите 'q': ")
    string_digits.islower()
    
    if string_digits.find("q") != -1:
        string_digits = string_digits[:string_digits.find("q") - 1]
        stop = False
    string_digits = string_digits.split(',')
    
    list_digits = list()
    for s in string_digits:
        try:
            list_digits.append(float(s))
        except:
            list_digits.append(0)
    
    for i in list_digits:
        sum_total += i
    print(sum_total)
    
    
    
