# Задана рекуррентная функция. Область определения функции – натуральные числа. 
# Написать программу сравнительного вычисления данной функции рекурсивно и 
# итерационно. Определить границы применимости рекурсивного и итерационного подхода. 
# Результаты сравнительного исследования времени вычисления представить в табличной
# форме. Обязательное требование – минимизация времени выполнения и объема памяти.
# F(0) = F(1) = 3; F(n) = (-1)** n *(F(n-1)/n!- F(n-2) /(2n)!)

import timeit
import math
import pandas as pd
from functools import lru_cache

@lru_cache(maxsize=None)
def F_recursive(n):
    if n == 1 or n == 0:
        return 3
    else:
        return (-1) ** n * (F_recursive(n - 1) / math.factorial(n) - F_recursive(n - 2) / math.factorial(2 * n))

def F_iterative(n):
    if n == 0 or n == 1:
        return 3
    results = [3, 3]
    for i in range(2, n + 1):
        results.append((-1)**(i * (results[i - 1] / math.factorial(i) - results[i - 2] / math.factorial(2 * i))))
    return results[n]

results = []

print("Введите натуральное число от 1 ")
n = int(input())
num = list(range(n + 1))

for i in num:
    startTime = timeit.default_timer()
    F_recursive(i)
    endTime = timeit.default_timer()
    recursive_time = endTime - startTime

    startTime = timeit.default_timer()
    F_iterative(i)
    endTime = timeit.default_timer()
    iterative_time = endTime - startTime

    results.append((recursive_time, iterative_time))

print (pd.DataFrame(results, columns=['Recursive Time (s)', 'Iterative Time (s)']))