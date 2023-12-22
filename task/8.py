'''
    Напишите программу,
    которая создает два потока и выводит сообщения из них параллельно.
'''

import threading
import time

def thread_function_1():
    for i in range(5):
        print("Thread 1: Message {}".format(i))
        time.sleep(1)

def thread_function_2():
    for i in range(5):
        print("Thread 2: Message {}".format(i))
        time.sleep(1)

# Create two threads
thread1 = threading.Thread(target=thread_function_1)
thread2 = threading.Thread(target=thread_function_2)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both threads have finished.")
