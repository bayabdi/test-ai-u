'''
    Создайте текстовый файл с несколькими строками текста.
    Напишите функцию, которая читает файл и выводит количество слов в каждой строке. 
'''

def count_words_in_each_line(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start = 1):
            words = line.split()
            num_words = len(words)
            print(f"Line {line_number}: {num_words} words")


count_words_in_each_line('input.txt')
