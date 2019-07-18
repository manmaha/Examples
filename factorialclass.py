def factorial(n):
  if (n>0):
    return n*factorial(n-1)
  else:
  	return 1


n = input('Enter n:')
print factorial(n)

