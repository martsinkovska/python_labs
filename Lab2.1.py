import math

#Task 1 

a = float (input("Enter a: "))
b = float (input("Enter b: "))
h = float (input("Enter h: "))

x = a

sum_negative = 0
mult_negative = 1

while x <= b:
    y = math.sin(x) + 0.5*math.cos(x)
    
    if y < 0:
        sum_negative += y
        mult_negative *= y
        negative = True
    
    print("x: ", x, "y: ", y )
    x += h
    
if negative:
    print("Sum of all negative values of y: ", sum_negative)
    print("Product of all negative values of y: ", mult_negative)


