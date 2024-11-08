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
            '.' * 15)  #F

txt = file.readline().split()
Max = int(txt[0],16) - 1

while txt != []:
    for i in range(len(txt)):
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

