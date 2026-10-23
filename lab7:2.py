def spiral_order(matrix):
    if not matrix or not matrix[0]:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # 1. Проход по верхней границе (слева направо)
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # 2. Проход по правой границе (сверху вниз)
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # 3. Проход по нижней границе (справа налево), если строка ещё есть
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # 4. Проход по левой границе (снизу вверх), если столбец ещё есть
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result


m1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

m2 = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12]]

print(spiral_order(m1))  # [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(spiral_order(m2))  # [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
