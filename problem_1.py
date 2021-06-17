'''Создайте функцию которая которая берёт лист делит его пополам и обе стороны разворачивает в 
противоположную сторону. Пример:

Оригинальный Лист:

list_1 = ['name', 'age', '1', '19']

Изменённый Лист:

list_1 = ['age', 'name', '19', '1']'''



a = ['name', 'age', '1', '19']

def my_func_rev():
	b = int(len(a)) // 2
	c = list(reversed(a[:b])) + list(reversed(a[b::]))
	
	print(c)
	
my_func_rev()

def delitel():
	a = input().split()
	print((list(reversed(a[:(int(len(a)) // 2)])))+(list(reversed(a[(int(len(a)) // 2)::]))))
delitel()