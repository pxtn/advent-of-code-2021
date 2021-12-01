with open('inputs/day_01.txt') as f:
    lines = [int(line.rstrip()) for line in f]
    f.close()

counter = 0

for i in range(len(lines)):
    if sum(lines[i+1 : i+4]) > sum(lines[i : i+3]):
        counter += 1

print('Result:', counter)