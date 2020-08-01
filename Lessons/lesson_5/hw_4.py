# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.


en_rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре" }
new_text = ""
try:
    with open("textfile4.txt", 'r+') as f_obj:
                
        text = f_obj.readlines()
        print(text)
        
        for i in text:
           word = i.split(' ')
           new_text += (en_rus_dict[word[0]] + " " + word[1] + " " + word[2])
    with open("new_textfile4.txt", 'w') as f_obj:
        f_obj.write(new_text)
        
        
except IOError:
    print("Произошла ошибка ввода-вывода!")