# Задание № 1

# Вычислите определитель:
#
# a)begin{vmatrix}
# sinx -cosx\\
# cosx sinx
# \end{vmatrix};
#
# б)begin{vmatrix}
# 4  2  3\\
# 0  5  1\\
# 0  0  9
# \end{vmatrix};
#
# в)begin{vmatrix}
# 1  2  3\\
# 4  5  6\\
# 7  8  9
# \end{vmatrix}.

# Решение

# Будем решать с подклбючением модуля numpy
import numpy as np

# det=sinx*sinx-(cosx*-cosx)=sin^{2}x+cos^{2}x=1

# Вариант б;

list1_2 = np.array([[4, 2, 3], [0, 5, 1], [0, 0, 9]])
det1_2 = np.linalg.det(list1_2)
print(det1_2)

# Вариант в;

list1_3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
det1_3 = np.linalg.det(list1_3)
print(det1_3)

# Задание № 2

# Определитель
# матрицы A равен 4.Найдите:

# а) det(A ^ {2});
# б) det(A ^ {T});
# в) det(2A)

# Вариант а;
# det(A ^ {2})=det(AA)=det(A)*det(a)=4*4=16

# Вариант б;

# det(A ^ {T})=det(A)=4

# Вариант в;

# det(2 ^ {A})=det(A)*2 ^ {n}=4*2^ {n}, n кол-во строк в матрице

# Задание № 3

# Докажите, что матрица:
#
# \begin{pmatrix}
# -2  7  -3\\
# 4  -14  6\\
# -3  7  13
# \end{pmatrix}

# Решение

# Выраженная

list3 = np.array([[-2, 7, -3], [4, -14, 6], [-3, 7, 13]])
det3 = np.linalg.det(list3)
print(det3)

# определитель матрицы равен нулю, следовательно, матрица вырожденная

# Задание № 4

# Найдите ранг матрицы:
# а) \begin{pmatrix}
# 1  2  3\\
# 1  1  1\\
# 2  3  4
# \end{pmatrix};

# б) \begin{pmatrix}
# 0  0  2  1\\
# 0  0  2  2\\
# 0  0  4  3\\
# 2  3  5  6
# \end{pmatrix}.

# Решение

# Вычислим вариант а;
list4_1 = np.array([[1, 2, 3], [1, 1, 1], [2, 3, 4]])
result4_1 = np.linalg.matrix_rank(list4_1)
print(result4_1)
# Получаем 2

# Теперь вычислим вариант б;
list4_2 = np.array([[0, 0, 2, 1], [0, 0, 2, 2], [0, 0, 4, 3], [2, 3, 5, 6]])
result4_2 = np.linalg.matrix_rank(list4_2)
print(result4_2)
# Получаем 3