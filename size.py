import time

answer = int(input("Здравствуйте! Хотите измерить длину своего члена? \n[1]-да\n[2]-нет\n"))

def chlenSize():
	b = int(input("Введите Ваш размер обуви: "))
	c = int(input("Введите длину Вашего носа:  "))
	d = int(input("Введите Ваш вес: "))
	a = 35 * (b + 3 * c)/d
	print(round(a))

if answer == 1:
	chlenSize()
else:
	print("Всего доброго! Как надумаете - заходите)")
