import math

#Task 1 

a = float(input("Enter a: "))
b = float(input("Enter b: "))
h = float(input("Enter h: "))

x = a

while x <= b:
    y = math.sin(x) + 0.5*math.cos(x)
    
    print("x: ", x, "y: ", y )
    x += h



