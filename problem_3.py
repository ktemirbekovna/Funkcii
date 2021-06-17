'''Напишите программу которая выводит только нечётные числа с помощью 
рекурсии.'''

from random import randint

def rec_even(num):
    rand_even = randint(0, 499) * 2 + 1
    if num > 0:
        print(rand_even, end=' ')
        rec_even(num-1)
    else:
        pass

rec_even(10)
