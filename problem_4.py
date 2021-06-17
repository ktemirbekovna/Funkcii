'''Напишите функцию которая принимает SET и рекурсивно удаляет оттуда 
по одному элементу при запуске.'''


def set_del(a):
    if a:
        a.pop()
        print(a)
        set_del(a)
c = { 10,17,"sumka",85,42,"okno","konder",}
print(c)
set_del(c)