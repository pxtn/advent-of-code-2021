with open('inputs/day_01.txt') as f:
    lines = [int(line.rstrip()) for line in f]
    f.close()

def part1():
    counter = 0

    for i in range(1, len(lines)):
        if lines[i] > lines[i - 1]:
            counter += 1
    
    return counter

def part2():
    counter = 0

    for i in range(1, len(lines)):
        if sum(lines[i+1 : i+4]) > sum(lines[i : i+3]):
            counter += 1
    
    return counter

print('Result Part 1:', part1())
print('Result Part 2:', part2())