#  Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. 
#  Например, print(int_func(‘text’)) -> Text

def int_func(word):
    word = word.capitalize()
    return word

string_words = input("Введите строку из слов разделёнными запятыми: ")
list_words = list(string_words.split(','))

for i in range(0, len(list_words)):
    list_words.insert(i, int_func(list_words.pop(i)))  
print(list_words)
    
