with open("Day2\Day2InfoFile.txt", 'r') as fhand:
    tot = 0
    fail = False
    rgbMax = [12,13,14]
    for line in fhand:
        fail = False
        line = line.split()
        for i in range(len(line)-1):
            line[i] = line[i].rstrip(';:,')
            if line[i].isnumeric() and line[i+1] == 'red':
                if int(line[i]) > rgbMax[0]:
                    fail = True
                    break
            elif line[i].isnumeric() and line[i+1] == 'green':
                if int(line[i]) > rgbMax[1]:
                    fail = True
                    break
            elif line[i].isnumeric() and line[i+1] == 'blue':
                if int(line[i]) > rgbMax[2]:
                    fail = True
                    break
        if fail:
            del line
        else:
            tot += int(line[1])
            print(line)
    print(tot)
    
        