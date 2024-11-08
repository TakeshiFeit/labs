file = open('text.txt', 'r')

num2points = {'A': '.' * 10, 'B': '.' * 11, 'C': '.' * 12, 'D': '.' * 13, 'E': '.' * 14, 'F': '.' * 15, '-': '-'} 
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

while txt != []:
    Max = int(txt[0],16) - 1
    for i in range(len(txt)):
        a = 0
        for j in (txt[i]):
            if str(j) not in (num2word):
                a += 1
                continue
        if a > 0:
            continue
        cond = False
        if Max < int(txt[i],16):
            Max = int(txt[i],16)
            cond = True; index = i
        txt2 = "".join(num2points.get(j, j) for j in txt[i])
        txt[i] = txt2
        if cond:
            txt[index] = "".join(num2word.get(j, j) for j in str(txt2))
            print (txt[index])
    txt = file.readline().split()
