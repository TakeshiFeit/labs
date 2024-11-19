# Написать программу, которая читая символы из файла, распознает, преобразует и 
# выводит на экран объекты по определенному правилу. Объекты разделены 
# пробелами. Распознавание и преобразование делать по возможности через 
# регулярные выражения. Для упрощения под выводом числа прописью 
# подразумевается последовательный вывод всех цифр числа.
# Шестнадцатеричные целые числа. Цифры от А до F менять на соответствующее количество точек. Максимальное число выводить прописью.

import re

file = open('text.txt', encoding="utf8")
num = re.compile(r"\d+")

num2some = ('zero', 
            'one', 
            'two', 
            'three', 
            'four', 
            'five', 
            'six', 
            'seven', 
            'eight', 
            'nine',
            '.' * 10,  #A
            '.' * 11,  #B
            '.' * 12,  #C
            '.' * 13,  #D
            '.' * 14,  #E
            '.' * 15)  #F

something = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', '-') 

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
            if  str(j) not in (something):
                a += 1
                continue
        if a != 0:
            continue
        if int(txt[i], 16) > 0:
            txt[i] = "+" + txt[i]
            sign = ""
        else:
            sign = "-"
        cond = False
        if Max < int(txt[i],16):
            Max = int(txt[i],16)
            cond = True
        replaced = ""
        txt2 = re.sub("(.)", r'\1 ', str(txt[i]))
        txt2 = [int(txt2[x], 16) for x in range(2, len(txt2), 2)]
        replaced += num.sub(lambda x: num2some[int(x.group())], str(txt2))
        txt[i] = replaced[:1] + sign + replaced[1:]
        print (txt[i]) if (cond == True) else()
    txt = file.readline().split()

