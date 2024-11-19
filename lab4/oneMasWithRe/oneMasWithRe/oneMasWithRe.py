# Написать программу, которая читая символы из файла, распознает, преобразует и 
# выводит на экран объекты по определенному правилу. Объекты разделены 
# пробелами. Распознавание и преобразование делать по возможности через 
# регулярные выражения. Для упрощения под выводом числа прописью 
# подразумевается последовательный вывод всех цифр числа.
# Шестнадцатеричные целые числа. Цифры от А до F менять на соответствующее количество точек. Максимальное число выводить прописью.

import re

file = open('text.txt', encoding="utf8")
q = re.compile(r"\d+")

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

def check():
    cond = False
    while cond == False:
        txt = file.readline().split()
        num = []
        for item in txt:
            try:
                q = int(item, 16)
                num.append(item)
                cond = True
            except ValueError:
                pass
    return num

num = check()
Max = int(num[0], 16) - 1

while num != []:
    for i in range(len(num)):
        if int(num[i], 16) > 0:
            num[i] = "+" + num[i]
            sign = ""
        else:
            sign = "-"
        cond = False
        if Max < int(num[i],16):
            Max = int(num[i],16)
            cond = True
        replaced = ""
        txt2 = re.sub("(.)", r'\1 ', str(num[i]))
        txt2 = [int(txt2[x], 16) for x in range(2, len(txt2), 2)]
        replaced += q.sub(lambda x: num2some[int(x.group())], str(txt2))
        num[i] = replaced[:1] + sign + replaced[1:]
        print (num[i]) if (cond == True) else()
    num = check()
