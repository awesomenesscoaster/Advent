import re

c = 0
with open("Advent/2024/Day3/Day3.txt", "r") as fhand:
    txt = fhand.read()
    matches = re.findall(r"(do\(\))|(don't\(\))|mul\((\d+),(\d+)\)", txt)
    print(matches)
    add = True
    for match in matches:
        if match[0] == "do()":
            add = True
        elif match[1] == "don't()":
            add = False
        else:
            if add:
                c += int((match[2])) * int(float(match[3]))
print(c)