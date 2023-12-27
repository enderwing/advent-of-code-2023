import math


def part1(f):
    puzzleInput = getFullInput(f)

    instructions = puzzleInput[0]

    mappings = {}
    for line in puzzleInput[2:]:
        mappings.update({line[:3]: (line[7:10], line[12:15])})

    steps = 1
    currentLocation = 'AAA'
    searching = True
    while searching:
        for direction in instructions:
            currentLocation = mappings.get(currentLocation)[0 if direction == 'L' else 1]
            if currentLocation == 'ZZZ':
                searching = False
                break
            steps += 1

    return steps

def part2(f):
    puzzleInput = getFullInput(f)
    instructions = puzzleInput[0]
    mappings = {}
    startNodes = set()
    endNodes = set()
    for line in puzzleInput[2:]:
        mappings.update({line[:3]: (line[7:10], line[12:15])})
        if line[2] == 'A':
            startNodes.add(line[:3])
        elif line[2] == 'Z':
            endNodes.add(line[:3])

    loopDistances = []
    for searchingNode in startNodes:
        steps = 1
        currentLocation = searchingNode
        searching = True
        while searching:
            for direction in instructions:
                currentLocation = mappings.get(currentLocation)[0 if direction == 'L' else 1]
                if currentLocation in endNodes:
                    if searching:
                        searching = False
                        loopDistances.append(steps)
                        break
                steps += 1

    lcmSteps = math.lcm(*loopDistances)

    return lcmSteps


def inputReader(f, strip=True, lower=False):
    line = f.readline()
    while line:
        if strip: line = line.strip()
        if lower: line = line.lower()
        yield line
        line = f.readline()

def getFullInput(f, strip=True, lower=False):
    lines = []
    for line in inputReader(f, strip, lower):
        lines.append(line)
    return lines

def main():
    with open("inputs/aoc2023-8-input.txt") as f:
        print("Input results:")
        print(f"  Part 1: {part1(f)}")
        f.seek(0)
        print(f"  Part 2: {part2(f)}")


if __name__ == "__main__":
    main()
