import re

# returns true is a character is a symbol
# a character is a symbol if it is not a period "." or a digit 1-9
def checkSymbol(charIn):
    notSymbols = ".1234567890"
    return not charIn in notSymbols
def part1(f):
    line = f.readline().strip()
    # turn input into array
    schematic = []
    while line:
        schematic.append(line)
        line = f.readline().strip()
    schematicX = len(schematic[0])
    schematicY = len(schematic)

    # traverse each row of the schematic, look for numbers, check for adjacent symbols
    partNumTotal = 0
    for r, row in enumerate(schematic):
        numFinder = re.finditer(r'\d+', row)
        for num in numFinder:
            isNearSymbol = False
            for x in range(num.start()-1, num.end()+1):
                if x < 0 or x > schematicX-1:
                    continue
                for y in range(r - 1, r + 2):
                    if y < 0 or y > schematicY-1:
                        continue
                    if checkSymbol(schematic[y][x]):
                        isNearSymbol = True
            if isNearSymbol: partNumTotal += int(num.group())
            # print(f"{num.group()} near symbol? {isNearSymbol}",end="")
            # input()
    return partNumTotal

def part2(f):
    line = f.readline().strip()
    # turn input into array and create list of part numbers
    schematic = []
    partNums = []
    while line:
        schematic.append(line)

        rowNums = []
        for partNum in re.finditer(r'\d+', line):
            rowNums.append((int(partNum.group()), partNum.start(), partNum.end()-1))
        partNums.append(rowNums)

        line = f.readline().strip()
    schematicX = len(schematic[0])
    schematicY = len(schematic)


    # traverse each row of the schematic, look for "*", check for adjacent numbers
    gearRatioTotal = 0
    partNumBatch = [partNums[0]]
    for r, row in enumerate(schematic):
        if r > 1:
            del partNumBatch[0]
        if r+1 < schematicY:
            partNumBatch.append(partNums[r+1])

        for gear in re.finditer(r'\*', row):
            gearPos = int(gear.start())
            adjacentNumbers = []

            for partNumRow in partNumBatch:
                for partNum in partNumRow:
                    if partNum[1] <= gearPos+1 and partNum[2] >= gearPos-1: adjacentNumbers.append(partNum)

            if len(adjacentNumbers) == 2:
                gearRatioTotal += adjacentNumbers[0][0] * adjacentNumbers[1][0]

    return gearRatioTotal

def main():
    with open("inputs/aoc2023-3-input.txt") as f:
        print("Input results:")
        print(f"  Part 1: {part1(f)}")
        f.seek(0)
        print(f"  Part 2: {part2(f)}")


if __name__ == "__main__":
    main()
