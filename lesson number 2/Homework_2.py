#  Установите, какие произведения матриц AB и BA определены, и найдите размерности полученных матриц:
#
#    а) A — матрица 4\times 2, B — матрица 4\times 2;
#
#    б) A — матрица 2\times 5, B — матрица 5\times 3;
#
#    в) A — матрица 8\times 3, B — матрица 3\times 8;
#
#    г) A — квадратная матрица 4\times 4, B — квадратная матрица 4\times 4.

import numpy as np

# Вариант а:

# A*B=4*2 и 4*2
# B*A=4*2 и 4*2

# Произведение не определены

# Вариант b:

# A*B=2*5 и 5*3, произведение определено, размерность полученной матрицы 2*3
# B*A=5*3 и 2*5, произведение не определено

# Вариант v:

# A*B=8*3 и 3*8, произведение определено, размерность полученной матрицы 8*8
# B*A=3*8 и 8*3, произведение определено, размерность полученной матрицы 3*3

# Вариант г:

# A*B,B*A - оба произведение определены, размерность полученной матрицы 4*4

# Задание № 2

# Найдите сумму и произведение матриц A=\begin{pmatrix}
# 1  -2\\
# 3  0
# \end{pmatrix} и B=\begin{pmatrix}
# 4  -1\\
# 0  5
# \end{pmatrix}.

# Решение

a = np.array([[1, -2], [3, 0]])
b = np.array([[4, -1], [0, 5]])
result1 = a + b
print(result1)

result2 = np.dot(a, b)
print(result2)

# Задание № 3

# Из закономерностей сложения и умножения матриц на число можно сделать вывод, что матрицы одного размера образуют линейное пространство. Вычислите линейную комбинацию 3A-2B+4C для матриц A=\begin{pmatrix}
# 1  7\\
# 3  -6
# \end{pmatrix}, B=\begin{pmatrix}
# 0  5\\
# 2  -1
# \end{pmatrix}, C=\begin{pmatrix}
# 2  -4\\
# 1  1
# \end{pmatrix}.

# Решение

a = np.array([[1, 7], [3, -6]])
b = np.array([[0, 5], [2, -1]])
c = np.array([[2, -4], [1, 1]])
result3 = (3 * a) + (-2 * b) + (4 * c)
print(result3)

# Задание № 4

# Дана матрица A=\begin{pmatrix}
# 4  1\\
# 5  -2\\
# 2  3
# \end{pmatrix}.
# Вычислите AA^{T} и A^{T}A.

# Решение

list = np.array([[4, 1], [5, -2], [2, 3]])
aT = list.T
print(aT)

result4 = np.dot(list, aT)
print(result4)

result4_2 = np.dot(aT, list)
print(result4_2)


# Задание № 5
# Напишите на Python функцию для перемножения двух произвольных матриц, не используя NumPy.

def multiply_matrix(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return ValueError('произведение не определено')
    result = [[0 for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


# Проверка работы

x = np.array([[1, -2], [3, 0], [5, 7]])
y = np.array([[4, -1], [0, 5]])
print(f'Матрица Х:\n {x}')
print(f'Матрица Y:\n {y}')
print(f'Результат метода NumPy:\n {np.dot(x, y)}')
print(f'Результат собственного метода: \n {multiply_matrix(x, y)}')
