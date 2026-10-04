import math

# Task 2

a = float(input("Enter a: "))
n = int(input("Enter n: "))

P = a
for i in range(1, n):
    P = P*(a + i)

print("P = ", P)


