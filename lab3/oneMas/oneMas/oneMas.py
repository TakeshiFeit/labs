# Написать программу, которая читая символы из бесконечной последовательности 
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
        cond = False
        if Max < int(num[i],16):
            Max = int(num[i],16)
            cond = True
        txt2 = "".join(num2word.get(j, j) for j in num[i])
        num[i] = txt2
        if cond:
            print (num[i])
    num = check()
