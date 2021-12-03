increase_counter = 0
with open('day1.txt') as f:
    previous_line = None
    for line in f:
        if ((previous_line is not None) and (int(previous_line) < int(line))):
            increase_counter += 1
        previous_line = line
    print(increase_counter)