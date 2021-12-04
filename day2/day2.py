horizontal = 0
depth = 0

with open('day2.txt', 'r') as f:
    for line in f:
        l = line.split()
        if (l[0] == 'forward'):
            horizontal += int(l[1])
        elif (l[0] == 'down'):
            depth += int(l[1])
        elif (l[0] == 'up'):
            depth -= int(l[1])
