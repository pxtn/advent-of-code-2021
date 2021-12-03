with open('inputs/day_03.txt') as f:
    lines = [line.rstrip() for line in f]
    f.close()

def part1():
    gammaRate = ''
    epsilonRate = ''

    for i in range(len(lines[0])):
        columnValues = ''
        for line in lines:
            columnValues = columnValues + line[i]
        
        countCondition = columnValues.count('1') > columnValues.count('0')

        gammaRate = gammaRate + '1' if countCondition else gammaRate + '0'
        epsilonRate = epsilonRate + '0' if countCondition else epsilonRate + '1'
    
    return int(gammaRate, 2) * int(epsilonRate, 2)

print('Result Part 1:', part1())