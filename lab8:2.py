def is_latin_square(matrix):
    n = len(matrix)
    
    # Проверка, что матрица квадратная и не пустая
    if n == 0:
        return False
    for row in matrix:
        if len(row) != n:
            return False

    expected_set = set(range(1, n + 1))

    # Проверка всех строк
    for row in matrix:
        if set(row) != expected_set:
            return False

    # Проверка всех столбцов
    for col_idx in range(n):
        column = [matrix[row_idx][col_idx] for row_idx in range(n)]
        if set(column) != expected_set:
            return False

    return True


# Ввод данных
try:
    n = int(input("Введите порядок квадрата (n): "))
    matrix = []
    print(f"Введите {n} строк матрицы, в каждой строке по {n} целых чисел через пробел:")
    for _ in range(n):
        row = list(map(int, input().split()))
        if len(row) != n:
            raise ValueError("Количество чисел в строке не соответствует n.")
        matrix.append(row)

    if is_latin_square(matrix):
        print("Да, это латинский квадрат.")
    else:
        print("Нет, это не латинский квадрат.")

except ValueError as e:
    print(f"Ошибка ввода: {e}")
