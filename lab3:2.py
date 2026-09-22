import math
a = 2
b = 3.4
hag = 0.05
steps =int((b - a) / hag + +1e-9) + 1
print(f"{"x":>8} | {"y":>12}")
print("-" *23)
for i in range(steps):
    x = a + i * hag
    if x > b:
        x = b
    t1 = math.sin(x**3)**2
    ln = math.log(x**2)**3
    t2 = math.cos(x**3)**2
    t3 = x**2 + x**3
    if t3 == 0:
        t4 = 0
    else:
        t4 = t2 / t3
    
    y = t1 + ln - t4
    print(f"{x:8.5f} | {y:12.5f}") 