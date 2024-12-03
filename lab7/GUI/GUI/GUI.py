# Требуется для своего варианта второй части л.р. №6 (усложненной программы) разработать реализацию с
# использованием графического интерфейса. Допускается использовать любую графическую библиотеку
# питона. Рекомендуется использовать внутреннюю библиотеку питона tkinter.
# В программе должны быть реализованы минимум одно окно ввода, одно окно вывода (со скролингом), одно текстовое поле, одна кнопка.

import timeit
from tkinter import *
from tkinter import ttk

def algo_without_func(num):
    numbers = []
    for i in range(0, num + 1, 2):
        counter1 = 0
        for symbol in str(i):
            if symbol == '1' and counter1 == 0:
                counter1 += 1
            else:
                counter1 = 2
                break 
            numbers.append(i) if (counter1 == 1) else ()
    return numbers

def algo_with_func(num):
    return list(filter(lambda num: (str(num).count('1') == 1), range(0, num + 1, 2)))

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

def center_screen(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - window.winfo_reqwidth()) // 2 - 320
    y = (screen_height - window.winfo_reqheight()) // 2 - 240

    window.geometry(f"640x480+{x}+{y}")

def show_res():
    try:
        number = int(entry.get())
    except ValueError:
        return
    if int(entry.get()) > 9:
        without_func_time, with_func_time, numbers = compare_perfomance(number)
        res = [0] * 3
        res[0] = "without_func_time = " + str(without_func_time); res[1] = "with_func_time = " + str(with_func_time); res[2] = "Max numbers = " + str(numbers[-1]); res += numbers
        listbox.delete(0,'end')
        for i in res:
            listbox.insert(len(res), i)
        scrollbar = ttk.Scrollbar(orient="vertical", command=listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        listbox["yscrollcommand"]=scrollbar.set

root = Tk()
root.title("Programm")
center_screen(root)

text = ttk.Label(root, text = "Enter number (number > 9)")
text.pack()

entry = ttk.Entry(root)
entry.pack()

btn = ttk.Button(root, text = "calculate", command=show_res)
btn.pack()

listbox = Listbox()
listbox.pack(side = LEFT, fill = BOTH, expand = 1)

root.mainloop()