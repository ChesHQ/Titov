n = int(input("Введите количество чисел N"))
numbers = list(map(int, input("Введите N чисел через пробел").split()))
if len (numbers) != n:
    print("Количество чисел не совпадае с N")
else:
    paircount = 0
    for i in range(len(numbers) - 2):
        if (numbers[i] + numbers[i + 2]) == (numbers[i + 1])*2 :
            paircount += 1
print(f"Количество пар: {paircount}")
