import random
n, m = [int(i) for i in input('Введите через пробел размер матрицы: ').split(' ')]
matrix = [[random.randint(0, 9) for j in range(m)] for i in range(n)]
for row in matrix:
    print(row)
number = int(input('Столбец с какой цифрой удалить: '))
index_column = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == number:
            index_column.append(j)
index_column = sorted(list(set(index_column)), reverse=True)
for i in range(n):
    for j in index_column:
        matrix[i].pop(j)
for row in matrix:
    print(row)