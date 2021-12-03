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

def part2():
    oxygenGeneratorRate = lines
    co2ScrubberRate = lines

    for i in range(len(oxygenGeneratorRate[0])):
        columnValues = ''
        for line in oxygenGeneratorRate:
            columnValues = columnValues + line[i]
        
        moreOf = '1' if columnValues.count('1') >= columnValues.count('0') else '0'
        oxygenGeneratorRate = [line for line in oxygenGeneratorRate if moreOf == line[i]]
        if len(oxygenGeneratorRate) == 1:
            break

    for i in range(len(co2ScrubberRate[0])):
        columnValues = ''
        for line in co2ScrubberRate:
            columnValues = columnValues + line[i]
        
        lessOf = '0' if columnValues.count('0') <= columnValues.count('1') else '1'
        co2ScrubberRate = [line for line in co2ScrubberRate if lessOf == line[i]]
        if len(co2ScrubberRate) == 1:
            break

    return int(oxygenGeneratorRate[0], 2) * int(co2ScrubberRate[0], 2)

print('Result Part 1:', part1())
print('Result Part 2:', part2())