'''
    Напишите генератор, используя регулярное выражение,
    для поиска всех email-адресов в текстовом файле Напишите программу,
    которая использует, написанный генератор для копирования в другой файл. 
'''

import re


def find_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    matches = re.finditer(email_pattern, text)
    return [match.group() for match in matches]


def copy_emails(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
        emails = find_emails(content)

    with open(output_file, 'w', encoding='utf-8') as file:
        for email in emails:
            file.write(email + '\n')



input_file_path = 'input.txt'
output_file_path = 'output.txt'

copy_emails(input_file_path, output_file_path)

