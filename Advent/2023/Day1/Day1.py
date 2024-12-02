fhand = open('Day1\Day1InfoFile.txt')

newL = []
tot = 0
for line in fhand:
    line.split()
    for i in line:
        if i.isnumeric():
            newL.append(i)
    tot += int(str(newL[0])+str(newL[len(newL)-1]))
    newL.clear()

print(tot)