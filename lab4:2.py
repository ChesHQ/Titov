import math
P = 1
for n in range(1, 16):
    a = (n ** (0.75 * n))
    b = math.factorial(n + 1)
    c = math.log(n + 1)
    P = ((a / b) * c)
print(P)