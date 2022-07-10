# Задание № 1

# Найдите посредством NumPy SVD для матрицы:
#
# \begin{pmatrix}
# 1 & 2 & 0\\
# 0 & 0 & 5\\
# 3 & -4 & 2\\
# 1 & 6 & 5\\
# 0 & 1 & 0
# \end{pmatrix}.

import math
import numpy as np

np.set_printoptions(precision=2, suppress=True)

A = np.array([[1, 2, 0],
              [0, 0, 5],
              [3, -4, 2],
              [1, 6, 5],
              [0, 1, 0]])
print(f'Матрица A:\n{A}')

U, s, W = np.linalg.svd(A)

# Транспонируем матрицу W
V = W.T

# s - список диагональных элементов, его нужно привести к виду диагональной матрицы для наглядности
D = np.zeros_like(A, dtype=float)
D[np.diag_indices(min(A.shape))] = s

print(f'Матрица D:\n{D}')
print(f'Матрица U:\n{U}')
print(f'Матрица V:\n{V}')

# Проверка
print(np.dot(np.dot(U, D), V.T))

# Задача № 2

# Для матрицы из предыдущего задания найдите:
#
#     а) евклидову норму;
#
#     б) норму Фробениуса.

print(f'Сингулярные числа: {s}')
print(f'Евклидова норма: {max(s)}')

sum_kv = 0
for num in s:
    sum_kv += num ** 2
print(f'норма Фробениуса: {math.sqrt(sum_kv)}')
