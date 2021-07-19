#這是數字遊戲
import random
r = random.randint(1, 500)
count = 0
count = int(count)
while True:
	a = input('please type a number :')
	a = int(a)
	count += 1 # 
	print('這是第', count, '次')
	if a > r:
		print('less')
	elif a < r:
		print('more')
	elif a == r:
		print('your right!!Good job.')
		break

