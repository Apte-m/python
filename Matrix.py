import random

# Создание первой матрицы 10x10
matrix_1 = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(random.randint(-100, 100))
    matrix_1.append(row)

# Создание второй матрицы 10x10
matrix_2 = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(random.randint(-100, 100))
    matrix_2.append(row)

# Сложение двух матриц и создание третьей матрицы
matrix_3 = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(matrix_1[i][j] + matrix_2[i][j])
    matrix_3.append(row)

# Вывод результатов
print("Матрица 1:")
for row in matrix_1:
    print(row)

print("\nМатрица 2:")
for row in matrix_2:
    print(row)

print("\nМатрица 3 после сложения:")
for row in matrix_3:
    print(row)