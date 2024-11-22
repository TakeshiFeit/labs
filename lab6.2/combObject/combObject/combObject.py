import timeit

def algo_without_func(num):
    numbers = []
    for i in range(0, num + 1, 2):
        counter1 = 0
        for symbol in str(i):
            if symbol == '1' and counter1 < 2: 
                counter1 += 1
            else:
                counter1 = 2
                break 
            numbers.append(i) if (counter1 == 1) else ()
    return numbers

def algo_with_func(num):
    return list(filter(lambda num: (str(num).count('1') == 1 and num % 2 == 0), range(0, num + 1, 2)))

def compare_perfomance(n):

    start_time = timeit.default_timer()
    algo_without_func(n)
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

print(numbers[-1])

