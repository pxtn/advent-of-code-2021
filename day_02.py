with open('inputs/day_02.txt') as f:
    lines = [line.rstrip().split(' ') for line in f]
    f.close()

def part1():
    horizontalPos = 0
    depthPos = 0

    for key, valueString in lines:
        value = int(valueString)
        match key:
            case 'forward':
                horizontalPos += value
            case 'up':
                depthPos -= value
            case 'down':
                depthPos += value
            
    return horizontalPos * depthPos

def part2():
    horizontalPos = 0
    depthPos = 0
    aim = 0

    for key, valueString in lines:
        value = int(valueString)
        match key:
            case 'forward':
                horizontalPos += value
                depthPos += (aim * value)
            case 'up':
                aim -= value
            case 'down':
                aim += value
            
    return horizontalPos * depthPos

print('Result Part 1:', part1())
print('Result Part 2:', part2())