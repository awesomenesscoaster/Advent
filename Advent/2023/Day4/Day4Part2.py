with open('Day4\Day4InfoFile.txt', 'r') as fhand:
    matches = 0
    scratchcards = 0
    for line in fhand:
        matches = 0
        line = line.split()
        line[1] = line[1].rstrip(':')
        for i in range(2,line.index('|')):  
            for j in range(line.index('|')+1,len(line)):
                if line[i] == line[j]:
                    matches += 1
        
        #Adds the new line to the end of the file
        for i in range(matches):
            for line2 in fhand:
                line2 = line2.split()
                line2[1] = line2[1].rstrip(':')
                print(line2)
                if int(line2[1]) == (int(line[1]) + 1 + i):
                    line2 = ' '.join(line2)
                    fhand.write(line2)
                    scratchcards += 1
    print(fhand)