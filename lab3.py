import math 
x = 0.01
delim = 2 * math.log(x**2) + 3 * math.log(x**3)
delit = math.exp(2 + 2**x) + math.exp(3 + 3 ** x)
y = delim/delit
print(f"{y:.5}")