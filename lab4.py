import math
S = 0
a = math.pi/3
for n in range(1,51):
    b = a**(2*n+1)
    c = math.factorial(n+1)
    S = (b / c) * math.cos(n)
print(S)
