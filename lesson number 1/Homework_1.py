# Задание № 1
# Исследуйте на линейную зависимость:
# f_{1}(x)=e^{x}, f_{2}(x)=1, f_{3}(x)=x+1, f_{4}(x)=x-e^{x}.

# Решение

# Мы можем выразить одну функцию, через другую:
# f_{4}(x)=f_{3}(x)-f_{2}(x)-f_{1}(x)

# Таким образом мы видим линейную зависимость.

# Задание № 2

# Исследуйте на линейную зависимость:
# f_{1}(x)=2, f_{2}(x)=x, f_{3}(x)=x^{2}, f_{4}(x)=(x+1)^{2}

# Решение

# Сдесь мы видем, что в данном примере мы можем так же как и в первом примере выразить одну функцию через другую.
# f_{4}(x)=f_{3}(x)+2f_{2}(x)+f_{1}(x)

# наблюдается линейная зависимость

# Задание № 3
# Найдите координаты вектора $x = (2, 3, 5)\in \mathbb{R}^{3}$ в базисе $b_{1}=(0, 0, 10)$, $b_{2}=(2, 0, 0)$, $b_{3}=(0, 1, 0)

# Найдем координаты векторов по методичке, аналогично решению в примере 4
# Стандартный базис линейного пространства $\mathbb{R}^{3}$ образует векторы
# e_{1}=(1, 0, 0)$, $e_{2}=(0, 1, 0)$, $e_{3}=(0, 0, 1)

# Решение

# x=(2,3,5)=(2,0,0)+(0,3,0)+(0,0,5)=1*(2,0,0)+3*(0,1,0)+0.5*(0,0,10)=0.5b1+1*b2+3*b3=(0.5,1,3)

# координаты вектора x в стандартном базисе - 0.5,1,3.

# Задача № 4

# Найдите координаты вектора 3x^{2}-2x+2\in\mathbb{R}^{3}[x]:

# а) в базисе $1$, $x$, $x^{2}$;
# б) в базисе $x^{2}$, $x-1$, $1$

# Решение

# Для базиса 1,x,x^{2}  координаты (2, -2,3)
# Для базиса x^{2},x-1,1  приведем вектор к нужному виду: 3x^{2}-2x+2=3x^{2}-2(x-1)
# тогда координаты для базиса x^{2},x-1,1 будут (3,-2,0)

# Задание № 5
# а) совокупность всех векторов трёхмерного пространства, у которых по крайней мере одна из первых двух координат равна нулю;
# б) все векторы, считающиеся линейными комбинациями данных векторов $\{u_{1}, u_{2} \ldots, u_{n}\}$.

# Решение

# а) Возьмем два вектора для примера a=(0,a2,a3) и b=(b1,0,b3)
# Сумма данных векторов a+b=(b1,a2,a3+b3).
# Ни одна из двух первых координат не равна нулю, следовательно, данная совокупность векторов не является линейным подпространством.

# б) Возьмем два вектора для примера a=3u1+5u2+7u3 и b=2u4+6u5+8u6
# Сумма данных векторов a+b=(3u1+5u2+7u3+2u4+6u5+8u6)
# Конец