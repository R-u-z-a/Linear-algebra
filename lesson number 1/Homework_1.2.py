# Задание № 1 часть 2
# Найдите скалярное произведение векторов x, y \in \mathbb{R}
# а) x=(0,-3, 6), y=(-4, 7, 9);
# б) x=(7, -4, 0, 1), y=(-3, 1, 11, 2).

# Решение

import numpy as np

result_1 = np.dot([0, -3, 6], [-4, 7, 9])
print(result_1)

result_2 = np.dot([7, -4, 0, 1], [-3, 1, 11, 2])
print(result_2)

# Задание № 2

# Найдите нормы векторов (4, 2, 4) и (12, 3, 4) и угол между ними

# Решение

list_1 = [4, 2, 4]
result_1 = np.linalg.norm(list_1)
print(result_1)

# норма вектора (12,3,4)

list_2 = [12, 3, 4]
result_2 = np.linalg.norm(list_2)
print(result_2)

# угол между векторами list_1 и list_2

result_3 = np.arccos(np.dot(list_1, list_2) / (result_1 * result_2)) / np.pi * 180
print(result_3)

# Задание № 3

# Определите, будет ли линейное пространство евклидовым, если за скалярное произведение принять:
# а) произведение длин векторов;
# б) утроенное обычное скалярное произведение векторов?

# Решение

# a) не будет

# б) будет

# Задание № 4

# Выясните, какие из нижеперечисленных векторов образуют ортонормированный базис в линейном пространстве $\mathbb{R}^{3}$:<br>
# а) (1,0,0),(0,0,1);
# б) (1/\sqrt{2},-1/\sqrt{2},0),(1/\sqrt{2},1/\sqrt{2},0), (0,0,1);
# в) (1/2, -1/2, 0), (0, 1/2, 1/2), (0,0,1);
# г) (1,0,0),(0,1,0),(0,0,1)?

# а) нет

# б) да

# в) нет

# г) да