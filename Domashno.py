for x in range(2000, 5001):
	

	a = x//1000
	b = (x//100)%10
	c = (x//10)%10
	d = x%10

	if a % 2 == 0 and b % 2 == 0 and c % 2 == 0 and d % 2 == 0:
		print(x, end = ', ')
