# Создать текстовый файл (не программно), 
# сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

try:
    with open("text.txt", 'a+') as f_obj:
        while True:
            content = input("Введите строку:")
            if not content:
                print("Ввод данных завершён!")
                break
            
            print(content, file =  f_obj)
        
        f_obj.seek(0,0)
        text = f_obj.read()
        count = text.count('\n')
        print(f"Строк в тексте:  {count}")
        text = text.split('\n')
        num_words =[len(sentence.split()) for sentence in text]
        
        word_in_str = [(el , num_words[el - 1]) for el in range(1, count+1)]
        print(f"(Строка, Слов): {word_in_str}")
        
        
except IOError:
    print("Произошла ошибка ввода-вывода!")


    
