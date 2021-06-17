'''Спросите у пользователя имя файла. Создайте функцию которая создаёт 
файл с именем которое передал пользователь. Присвойте 
ИМЯ функции к переменной и вызывайте функцию через переменную.'''

a = input("Введите название файла: ")

def open_file( ):
	b = open('/home/karlygach/Desktop/{a}.txt', 'w')
	f.close
    a = open_file()
    print(a)
open_file()



# a = input('Имя файла')
# def main():
#  f = open (f'/users/mac/Desktop/{a}.txt', 'w')
#  f.close
# a = main()
# print(a)