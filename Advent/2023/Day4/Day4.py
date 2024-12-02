with open('Day4\Day4InfoFile.txt', 'r') as fhand:
    pointPerCard = 0
    matches = 0
    cardSum = 0 
    for line in fhand:
        line = line.split()
        matches = 0
        pointPerCard = 0
        for i in range(2,line.index('|')):  
            for j in range(line.index('|')+1,len(line)):
                if line[i] == line[j]:
                    if matches == 0:
                        pointPerCard = 1
                    else:
                        pointPerCard = 2*pointPerCard
                    matches += 1
        cardSum += pointPerCard            
        print(cardSum)