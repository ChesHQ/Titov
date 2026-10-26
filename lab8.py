n = int(input("Введите числа"))
read = [float(input()) for _ in range(n)]

read.sort()#Сортировка показаний для хронологии

cons = [read[i] - read[i] for i in range( , n)]
total_cons = sum(cons) #разница между соседними показаниями и суммы всех расходов

aver_month = total_cons #среднее потребление за месяц

print(f"среднее потребление газа за месяц: {average_month:.2f} куб.м")
