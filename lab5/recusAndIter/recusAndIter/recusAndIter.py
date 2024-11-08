import timeit
import math
import pandas as pd

def F_recursive(n):
    if n == 0 or n == 1:
        return 3
    else:
        return (-1)**n * (F_recursive(n-1) / math.factorial(n) - F_recursive(n-2) / math.factorial(2*n))


def F_iterative(n):
    if n == 0 or n == 1:
        return 3
    results = [3, 3]
    for i in range(2, n + 1):
        results.append((-1)**i * (results[i-1] / math.factorial(i) - results[i-2] / math.factorial(2*i)))
    return results[n]


results = []
choice = 1

while choice == 1:
    
    choice1 = int(input("1 = continue, 0 = break\n"))
    choice = choice1
    if choice == 1:
        n = int(input("enter n:\n"))
    else:
        break

    startTime = timeit.default_timer()
    F_recursive(n)
    endTime = timeit.default_timer()
    recursive_time = endTime - startTime

    startTime = timeit.default_timer()
    F_iterative(n)
    endTime = timeit.default_timer()
    iterative_time = endTime - startTime

    results.append((recursive_time, iterative_time))

    print (pd.DataFrame(results, columns=['Recursive Time (s)', 'Iterative Time (s)']))