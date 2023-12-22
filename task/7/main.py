'''
    Наполните текстовый файл рандомными значениями (побольше),
    можете использовать сторонние библиотеки (faker).
    Напишите декоратор timeit который принимает значение N для измерения времени работы функции и примените к прошлому заданию.
    Если время превышает заданное N выводить дополнительное уведомление.
'''

import time
from faker import Faker


def timeit_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' took {elapsed_time:.6f} seconds.")
        return result, elapsed_time
    return wrapper


@timeit_decorator
def fill_text_file_with_random_values(file_path, num_values):
    fake = Faker()
    with open(file_path, 'w') as file:
        for _ in range(num_values):
            file.write(f"{fake.name()}, {fake.address()}, {fake.email()}\n")

file_path = 'random_data.txt'
num_values = 10000

max_allowed_time = 5.0 

try:
    _, elapsed_time = fill_text_file_with_random_values(file_path, num_values)
except Exception as e:
    print(f"Error: {e}")
    exit(1)


if elapsed_time > max_allowed_time:
    print(f"Warning: Execution time exceeded {max_allowed_time} seconds.")
