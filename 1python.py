import math

x = float(input("Enter x:")) 
print("x is: ", round(x), "\n")


print ("1 part")

if x > 0:
    print("ln x: ", math.log(x,10))
else:
    print("ln x: Error")

print("sin x:", math.sin(x))
print("cos x:", math.cos(x))
print("\n")

print ("2 part")

if x <= 2:
    F = (x**2 + 4*x + 5)  
else:
    F = (1/(x**2 + 4*x + 5))
    
print("F(x) = ", F, "\n")