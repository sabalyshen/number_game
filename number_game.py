#這是數字遊戲
import random
b = input('請輸入最小值')
c = input('請輸入最大值')
b = int(b)
c = int(c)
r = random.randint(b, c)
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

