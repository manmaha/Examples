def fibonacci(number):
	if number == 0:
		return 0
	else :
		if number == 1:
			return 1
		else :
			return(fibonacci(number-1)+fibonacci(number-2))
				
print('Fibonacci Series Calculator')
print('this will print the first n fibonacci numbers')
n = input('input n ')
for index in  range(0 , n):
	print(' %d' % fibonacci(index))
	
