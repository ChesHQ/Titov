# Считываем количество показаний
n = int(input("Введите количество показаний (N): "))

# Считываем сами показания (можно через пробел в одной строке)
readings = list(map(float, input(f"Введите {n} показаний счётчика через пробел: ").split()))

if len(readings) != n:
    print("Ошибка: введено неверное количество чисел.")
else:
    # Сортируем показания — так восстанавливаем хронологию (счётчик только растёт)
    readings.sort()

    if n < 2:
        print("Недостаточно данных: нужно минимум 2 показания, чтобы посчитать расход.")
    else:
        # Считаем месячные расходы как разности соседних показаний
        total_consumption = readings[-1] - readings[0]          # общий расход
        months = n - 1                                           # количество месяцев (интервалов)
        average_consumption = total_consumption / months        # средний расход

        # Если хочется видеть ещё и отдельные месячные расходы:
        monthly_consumptions = [readings[i] - readings[i-1] for i in range(1, n)]

        print("\nОтсортированные показания:", readings)
        print("Месячные расходы (м³):", monthly_consumptions)
        print(f"Средний месячный расход газа: {average_consumption:.3f} м³")


