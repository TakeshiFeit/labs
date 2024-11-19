﻿# Написать программу, которая читая символы из бесконечной последовательности 
# (эмулируется конечным файлом), распознает, преобразует и выводит на экран 
# объекты по определенному правилу. Объекты разделены пробелами. 
# Преобразование делать по возможности через словарь. Для упрощения под 
# выводом числа прописью подразумевается последовательный вывод всех цифр 
# числа. Регулярные выражения использовать нельзя.
# Шестнадцатеричные целые числа. Цифры от А до F менять на соответствующее количество точек. Максимальное число выводить прописью.

file = open('text.txt', encoding="utf8")

num2word = {'0': ' zero ', 
            '1': ' one ', 
            '2': ' two ', 
            '3': ' three ', 
            '4': ' four ', 
            '5': ' five ', 
            '6': ' six ', 
            '7': ' seven ', 
            '8': ' eight ', 
            '9': ' nine ',
            'A': '.' * 10,
            'B': '.' * 11,
            'C': '.' * 12,
            'D': '.' * 13,
            'E': '.' * 14,
            'F': '.' * 15,
            '-': '-'}

cond = False
while cond == False:
    txt = file.readline().split()
    for item in txt:
        try:
            Max = int(item, 16) - 1 
            cond = True
            break
        except ValueError:
            pass

while txt != []:
    for i in range(len(txt)):
        a = 0
        for j in (txt[i]):
            if str(j) not in (num2word):
                a += 1
        if a > 0:
            continue
        cond = False
        if Max < int(txt[i],16):
            Max = int(txt[i],16)
            cond = True
        txt2 = "".join(num2word.get(j, j) for j in txt[i])
        txt[i] = txt2
        if cond:
            print (txt[i])
    txt = file.readline().split()
