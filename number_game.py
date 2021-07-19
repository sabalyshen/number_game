#這是數字遊戲
import random
r = random.randint(1, 500)
while True:
	a = input('please type a number :')
	a = int(a)
	if a > r:
		print('less')
	elif a < r:
		print('more')
	elif a == r:
		print('your right!!Good job.')
		break

