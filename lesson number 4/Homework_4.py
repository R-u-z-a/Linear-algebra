# Практическое задание № 4

# Задача № 1
# Решите систему уравнений методом Гаусса:
#
# \begin{cases}
# x_{1}+x_{2}-x_{3}-2x_{4}=0, \\
# 2x_{1}+x_{2}-x_{3}+x_{4}=-2, \\
# x_{1}+x_{2}-3x_{3}+x_{4}=4.
# \end{cases}

# Преобразуем расширенную матрицу системы путем элементарных преобразований:

# \begin{pmatrix}
# \left.\begin{matrix}
# 1 & 2 & -1 & -2 \\
# 2 & 4 & -1 & 1 \\
# 1 & 1 & -3 & 1
# \end{matrix}\right|
# \begin{matrix}
# 0\\
# -2 \\
# 4
# \end{matrix}
# \end{pmatrix}

# Отнимем из второй строки первую, умноженную на 2:

# \begin{pmatrix}
# \left.\begin{matrix}
# 1 & 1 & -1 & -2 \\
# 0 & -1 & 1 & 5 \\
# 1 & 1 & -3 & 1
# \end{matrix}\right|
# \begin{matrix}
# 0\\
# -2 \\
# 4
# \end{matrix}
# \end{pmatrix}

# Отнимем из третьей строки первую:

# \begin{pmatrix}
# \left.\begin{matrix}
# 1 & 1 & -1 & -2 \\
# 0 & -1 & 1 & 5 \\
# 0 & 0 & -2 & 3
# \end{matrix}\right|
# \begin{matrix}
# 0\\
# -2 \\
# 4
# \end{matrix}
# \end{pmatrix}

# Система имеет бесконечное кол-во решений.
#
# Поделим третью строку на 3:

# \begin{pmatrix}
# \left.\begin{matrix}
# 1 & 1 & -1 & -2 \\
# 0 & -1 & 1 & 5 \\
# 0 & 0 & -\frac{2}{3} & 1
# \end{matrix}\right|
# \begin{matrix}
# 0\\
# -2 \\
# \frac{4}{3}\\
# \end{matrix}
# \end{pmatrix}

# Оставшаяся матрица соответствует системе:


# \begin{cases}
# x_{1}+x_{2}-x_{3}-2x_{4}=0, \\
# -x_{2}+x_{3}-5x_{4}=-2, \\
# -\frac{2}{3}+x_{3}-x_{4}=\frac{4}{3}.
# \end{cases}

# Бесконечное множество решений принято записывать в виде общего решения.
#
# Последнее уравнение содержит две неизвестных.
# В данном случае можно рассматривать в качестве свободного параметра.
# Тогда, выражая остальные переменные через , получим:

# x_{4}=C\\
# x_{3}=\frac{{4-3}_{c}}{-2}\\
# x_{2}=2+5\cdot c+\frac{{4-3}_{c}}{-2}\\
# x_{1}=-2-3\cdot c

# Таковым будет общее решение системы. Подставляя произвольные числа вместо , мы получим частное решение. Например, при c = 0

# x_{1}=-2, x_{2}=0, x_{3}=-2, x_{4}=0

# Параметр  может принимать бесконечное количество значений, при которых уравнения в системе будут обращаться в тождества.

# Задача № 2
# Проверьте на совместность и выясните, сколько решений будет иметь система линейных уравнений:
#
# а) \begin{cases}
# 3x_{1}-x_{2}+x_{3}=4, \\
# 2x_{1}-5x_{2}-3x_{3}=-17, \\
# x_{1}+x_{2}-x_{3}=0;
# \end{cases}
#
# б) \begin{cases}
# 2x_{1}-4x_{2}+6x_{3}=1, \\
# x_{1}-2x_{2}+3x_{3}=-2, \\
# 3x_{1}-6x_{2}+9x_{3}=5;
# \end{cases}
#
# в) \begin{cases}
# x_{1}+2x_{2}+5x_{3}=4, \\
# 3x_{1}+x_{2}-8x_{3}=-2.
# \end{cases}

# Решение 2а):

# \begin{pmatrix}
# \left.\begin{matrix}
# 3 & -1 & 1  \\
# 2 & -5 & -3 \\
# 1 & 1 & -1
# \end{matrix}\right|
# \begin{matrix}
# 4\\
# -17\\
# 0\\
# \end{matrix}
# \end{pmatrix}

# Поделим первую строку на 3:

# \begin{pmatrix}
# \left.\begin{matrix}
# 1 & -\frac{1}{3} & \frac{1}{3}  \\
# 2 & -5 & -3 \\
# 1 & 1 & -1
# \end{matrix}\right|
# \begin{matrix}
# \frac{4}{3}\\
# -17\\
# 0\\
# \end{matrix}
# \end{pmatrix}

# Отнимем из второй строки первую, умноженную на 2:

# \begin{pmatrix}
# \left.\begin{matrix}
# 1 & -\frac{1}{3} & \frac{1}{3}  \\
# 0 & -\frac{13}{3} & -\frac{11}{3} \\
# 1 & 1 & -1
# \end{matrix}\right|
# \begin{matrix}
# \frac{4}{3}\\
# --\frac{59}{3}\\
# 0\\
# \end{matrix}
# \end{pmatrix}

# Отнимем из третьей строки первую:

# \begin{pmatrix}
# \left.\begin{matrix}
# 1 & -\frac{1}{3} & \frac{1}{3}  \\
# 0 & -\frac{13}{3} & -\frac{11}{3} \\
# 0 & \frac{4}{3} & -\frac{4}{3}\\
# \end{matrix}\right|
# \begin{matrix}
# \frac{4}{3}\\
# -\frac{59}{3}\\
# -\frac{4}{3}\\
# \end{matrix}
# \end{pmatrix}

# Умножим вторую строку на
#
# Умножим вторую строку на  -\frac{3}{13}, и отнимем вторую строку из третьей:

# \begin{pmatrix}
# \left.\begin{matrix}
# 1 & -\frac{1}{3} & \frac{1}{3}  \\
# 0 & 1 & -\frac{11}{3} \\
# 0 & 0 & -\frac{24}{13}\\
# \end{matrix}\right|
# \begin{matrix}
# \frac{4}{3}\\
# -\frac{59}{13}\\
# -\frac{72}{13}\\
# \end{matrix}
# \end{pmatrix}

# Упростим третью строку, путем умножения на 13 и деления полученных значений на 24:

# \begin{pmatrix}
# \left.\begin{matrix}
# 1 & -\frac{1}{3} & \frac{1}{3}  \\
# 0 & 1 & -\frac{11}{3} \\
# 0 & 0 & 1\\
# \end{matrix}\right|
# \begin{matrix}
# \frac{4}{3}\\
# -\frac{59}{13}\\
# 3\\
# \end{matrix}
# \end{pmatrix}

# rangA=rang(A|B)=n, следовательно, система совместная и определенная

# б) \begin{cases}
# 2x_{1}4x_{2}+6x_{3}=1, \\
# x_{1}-2x_{2}+3x_{3}=-2, \\
# 3x_{1}-6x_{2}+9x_{3}=5
# \end{cases}

# Решение 2б):

# \begin{pmatrix}
# \left.\begin{matrix}
# 2 & -4 & 6 \\
# 1 & -2 & 3 \\
# 3 & 6 & -9 \\
# \end{matrix}\right|
# \begin{matrix}
# 1\\
# -2\\
# 5
# \end{matrix}
# \end{pmatrix}

# Поделим первую строку на 2:

# \begin{pmatrix}
# \left.\begin{matrix}
# 1 & -2 & 3 \\
# 1 & -2 & 3 \\
# 3 & 6 & -9 \\
# \end{matrix}\right|
# \begin{matrix}
# 0.5\\
# -2\\
# 5
# \end{matrix}
# \end{pmatrix}

# Отнимем из второй строки первую:

# \begin{pmatrix}
# \left.\begin{matrix}
# 1 & -2 & 3 \\
# 0 & 0 & 0 \\
# 3 & 6 & -9 \\
# \end{matrix}\right|
# \begin{matrix}
# 0.5\\
# -2.5\\
# 5
# \end{matrix}
# \end{pmatrix}

# Отнимем из третьей строки первую, умноженную на 3:

# \begin{pmatrix}
# \left.\begin{matrix}
# 1 & -2 & 3 \\
# 0 & 0 & 0 \\
# 0 & 0 & 0 \\
# \end{matrix}\right|
# \begin{matrix}
# 0.5\\
# -2.5\\
# 3.5
# \end{matrix}
# \end{pmatrix}

# Поделим вторую строку на -2.5:

# \begin{pmatrix}
# \left.\begin{matrix}
# 1 & -2 & 3 \\
# 0 & 0 & 0 \\
# 0 & 0 & 0 \\
# \end{matrix}\right|
# \begin{matrix}
# 0.5\\
# 1\\
# 3.5
# \end{matrix}
# \end{pmatrix}

# Отнимем из третьей строки вторую, умноженную на 3.5:

# \begin{pmatrix}
# \left.\begin{matrix}
# 1 & -2 & 3 \\
# 0 & 0 & 0 \\
# 0 & 0 & 0 \\
# \end{matrix}\right|
# \begin{matrix}
# 0.5\\
# 1\\
# 0
# \end{matrix}
# \end{pmatrix}

#  rangA не равен rang(A|b), следовательно, система несовместная

# B) \begin{cases}
# x_{1}+x_{2}+5x_{3}=4, \\
# 3x_{1}+x_{2}-8x_{3}=-2. \\
# \end{cases}

# Решение 2в):

# \begin{pmatrix}
# \left.\begin{matrix}
# 1 & 2 & 5 \\
# 3 & 1 & -8 \\
# \end{matrix}\right|
# \begin{matrix}
# 4\\
# -2
# \end{matrix}
# \end{pmatrix}

# Отнимем из второй строки первую, умноженную на 3:

# \begin{pmatrix}
# \left.\begin{matrix}
# 1 & 2 & 5 \\
# 0 & -5 & -23 \\
# \end{matrix}\right|
# \begin{matrix}
# 4\\
# -14
# \end{matrix}
# \end{pmatrix}

# Разделим вторую строку на -5

# \begin{pmatrix}
# \left.\begin{matrix}
# 1 & 2 & 5 \\
# 0 & 1 & \frac{23}{5} \\
# \end{matrix}\right|
# \begin{matrix}
# 4\\
# \frac{14}{5}
# \end{matrix}
# \end{pmatrix}

# rangA = rang(A|b) < n, следовательно, система совместная и неопределенная

# 3. Проверить на совместность и выяснить, сколько решений будет иметь система линейных уравнений, заданная расширенной матрицей

# \tilde{A}=\begin{pmatrix}
# \left.\begin{matrix}
# 1 & 3 & -2 & 4\\
# 0 & 5 & 0 & 1\\
# 0 & 0 & 3 & 0\\
# 0 & 0 & 0 & 2
# \end{matrix}\right|
# \begin{matrix}
# 3\\
# 2\\
# 4\\
# 1
# \end{matrix}
# \end{pmatrix}

#  rangA = rang(A|b) = n, следовательно, система совместная и определенная

# 4. Дана система линейных уравнений, заданная расширенной матрицей

# \tilde{A}=\begin{pmatrix}
# \left.\begin{matrix}
# 1 & 2 & 3\\
# 4 & 5 & 6\\
# 7 & 8 & 9
# \end{matrix}\right|
# \begin{matrix}
# a\\
# b\\
# c
# \end{matrix}
# \end{pmatrix}

# Найти соотношение между параметрами a, b и c, при которых система является несовместной.

# Решение:

# Отнимем из второй строки первую, умноженную на 4:

# \tilde{A}=\begin{pmatrix}
# \left.\begin{matrix}
# 1 & 2 & 3\\
# 0 & -3 & -6\\
# 7 & 8 & 9
# \end{matrix}\right|
# \begin{matrix}
# a\\
# b-4\cdot a\\
# c
# \end{matrix}
# \end{pmatrix}

# Отнимем из третьей строки первую, умноженную на 7:

# \tilde{A}=\begin{pmatrix}
# \left.\begin{matrix}
# 1 & 2 & 3\\
# 0 & -3 & -6\\
# 0 & -6 & -12
# \end{matrix}\right|
# \begin{matrix}
# a\\
# b-4\cdot a\\
# c-7\cdot a
# \end{matrix}
# \end{pmatrix}

# Отнимем из третьей строки вторую, умноженную на -2:

# \tilde{A}=\begin{pmatrix}
# \left.\begin{matrix}
# 1 & 2 & 3\\
# 0 & -3 & -6\\
# 0 & 0 & 0
# \end{matrix}\right|
# \begin{matrix}
# a\\
# b-4\cdot a\\
# c-7\cdot a + 2\cdot b-8\cdot a
# \end{matrix}
# \end{pmatrix}

# При (-15\cdot a+2\cdot b+c) не равняется 0 система является несовместной