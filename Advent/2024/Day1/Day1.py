with open("Advent/2024/Day1/Day1.txt", "r") as fhand:
    l = []
    r = []
    for i in fhand.read().split("\n"):
        nl,nr = i.split()
        l.append(int(nl))
        r.append(int(nr))
    l.sort(), r.sort()
    s = 0
    for i in l:
        s += i * r.count(i)
    print(s)
        
        