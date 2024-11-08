import timeit

def algo_without_func(num):
    numbers = []
    for i in range(num + 1):
        counter1 = 0; counter2 = 0 
        for symbol in str(i):
            if symbol == '1':
                counter1 += 1
            elif symbol == '2':
                counter2 += 1
        if ((counter1 and counter2) == 1):
            numbers.append(i)
    return numbers


def algo_with_func(num):
    numbers = []
    for i in range(num + 1):
        if str(i).count('1') == 1 and str(i).count('2') == 1:
            numbers.append(i)
    return numbers


def compare_perfomance(n):
    start_time = timeit.default_timer()
    numbers = algo_without_func(n)
    end_time = timeit.default_timer()
    without_func_time = end_time - start_time

    start_time = timeit.default_timer()
    numbers = algo_with_func(n)
    end_time = timeit.default_timer()
    with_func_time = end_time - start_time

    return without_func_time, with_func_time, numbers

n = int(input("enter N = "))

without_func_time, with_func_time, numbers = compare_perfomance(n)

print ('time required to execute algo_without_func =', without_func_time)
print('time required to execute algo_with_func =', with_func_time)

print(numbers)

