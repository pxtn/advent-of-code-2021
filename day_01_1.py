with open('inputs/day_01.txt') as f:
    lines = [int(line.rstrip()) for line in f]
    f.close()

counter = 0

for i in range(1, len(lines)):
    if lines[i] > lines[i - 1]:
        counter += 1

print('Result:', counter)