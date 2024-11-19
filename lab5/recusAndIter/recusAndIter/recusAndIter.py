# Задана рекуррентная функция. Область определения функции – натуральные числа. 
# Написать программу сравнительного вычисления данной функции рекурсивно и 
# итерационно. Определить границы применимости рекурсивного и итерационного подхода. 
# Результаты сравнительного исследования времени вычисления представить в табличной
# форме. Обязательное требование – минимизация времени выполнения и объема памяти.
# F(0) = F(1) = 3; F(n) = (-1)** n *(F(n-1)/n!- F(n-2) /(2n)!)

import timeit
import math
from functools import lru_cache

@lru_cache(maxsize=128)
def F_recursive(n):
    if n == 1 or n == 0:
        return 3
    else:
        return (-1) ** n * (F_recursive(n - 1) / math.factorial(n) - F_recursive(n - 2) / math.factorial(2 * n))

def F_iterative(n):
    if n == 0 or n == 1:
        return 3

    prev1, prev2 = 3, 3
    for i in range(2, n + 1):
        res = (-1)**i * (prev1 / math.factorial(i) - prev2 / math.factorial(2 * i))
        prev2 = prev1
        prev1 = res
    return res


print("Введите натуральное число от 1 ")
n = int(input())
num = list(range(n + 1))

for i in num:
    startTime = timeit.default_timer()
    res_rec = F_recursive(i)
    endTime = timeit.default_timer()
    recursive_time = endTime - startTime

    startTime = timeit.default_timer()
    res_it = F_iterative(i)
    endTime = timeit.default_timer()
    iterative_time = endTime - startTime

    print(i,
        " | Результат рекурсии ->", res_rec,
        " | результат итерации ->", res_it,
        " | время  рекурсии ->", recursive_time,
        " | время  итерации ->", iterative_time )
