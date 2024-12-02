def is_safe(level):
    is_increasing = all(i < j for i,j in zip(level, level[1:]))
    is_decreasing = all(i > j for i,j in zip(level, level[1:]))
    if not(is_increasing or is_decreasing):
        return False
    return all(1 <= abs(level[i +1 ] - level[i]) <= 3 for i in range(len(level)-1))

with open("Advent/2024/Day2/Day2.txt", "r") as fhand:
    c = 0
    for line in fhand.read().split('\n'):
        level = line.split()
        level = [int(x) for x in level]
        
        if is_safe(level):
            c +=1 
            continue
        
        for i in range(len(level)):
            newWin = level[:i] + level[i+1:]
            if is_safe(newWin):
                c+=1
                break
    print(c)
        