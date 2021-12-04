horizontal = 0
depth = 0
aim = 0

with open('day2.txt', 'r') as f:
    for line in f:
        l = line.split()
        if (l[0] == 'forward'):
            horizontal += int(l[1])
            depth = depth + (aim * int(l[1]))
        elif (l[0] == 'down'):
            aim += int(l[1])
        elif (l[0] == 'up'):
            aim -= int(l[1])
    