# Uses recursion to calculate factorial of input integer
from os import system

def say(sayString):
	system('say "%s"' % sayString)

def factorial (n):
	if n == 0:
		return 1
	else :
		return(n*factorial(n-1))


say('Hello, Please Tell me your name')
name = raw_input('Please Tell me your name? ')
say("Hello")
say(name)
system('say factorial calculation')
system('say please input an integer')
n = input('Please Input an Integer ')
Factorial = factorial(n)
Question = 'Factorial of %d' % n
Answer = 'is %d' % Factorial
say(Question)
say(Answer)
 
		
