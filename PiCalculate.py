import random as rnd
import matplotlib.pyplot as plt

#Calculates Numerical Value of Pi
# Generates N random coordinates:x,y
# Counts the number of co-ordinates in the Unit Quadrant (n) and Divides by N
# This gives the ratio of area of unit quadrant to area of unit square
# n/N = Area of Unit Quadrant/Area of unit Square 
# Area of Unit Quadrant = Pi/4 , Pi = 4 * Area of Unit Quadrant = 4 * n/N

# returns True if the x,y co-ordinates lie inside the unit quadrant (or circle)
in_circle = lambda x,y: x*x+y*y<= 1.0

N = input('Enter the Total Number of Points : ')

# N is total number of points
in_quadrant = 0 # 'n' = number of points in unit quadrant, initially 0

for _ in range(N): #iterate N times, find N random co-ordinates
  
  marker = 'r^' # marker for points outside the circle (red triangle)
  # generate x and y co-ordinates
  x = rnd.random() #generates a random number between 0.0 and 1.0
  y = rnd.random()

  if in_circle(x,y) :
    in_quadrant = in_quadrant + 1
    marker = 'ys' # marker for points inside the circle (blue square)
  
  plt.plot(x,y,marker)

pi_approximate = 4 * float(in_quadrant)/N  
answer = 'Approximate value of Pi : '+str(pi_approximate)
plt.text(0.5,0.3,answer)
print 'Approximate Value of Pi :', pi_approximate
plt.show()   

