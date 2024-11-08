import re

file = open('text.txt', 'r')
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
            '.' * 15,  #F
            '-')

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

txt = file.readline().split()
Max = int(txt[0],16) - 1

while txt != []:
    for i in range(len(txt)):
        a = 0
        for j in (txt[i]):
            if  str(j) not in (num2word):
                print(j)
                a += 1
                continue
        if a > 0:
            continue
        cond = False
        replaced = ""
        if int(txt[i], 16) > 0:
            txt[i] = "+"+ txt[i]
            sign = ""
        else:
            sign = "-"
        if Max < int(txt[i],16):
            Max = int(txt[i],16)
            cond = True; index = i
        txt2 = re.sub("(.)", r'\1 ', str(txt[i]))
        txt2 = [int(txt2[x], 16) for x in range(2, len(txt2), 2)]
        replaced += num.sub(lambda x: num2some[int(x.group())], str(txt2))
        txt[i] = replaced
        print (sign + txt[index]) if (cond == True) else()
    txt = file.readline().split()

