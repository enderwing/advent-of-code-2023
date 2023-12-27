import math


def part1(f):
    puzzleInput = getFullInput(f)
    raceTimes = list(map(int, filter(lambda x: x, puzzleInput[0][10:].split(" "))))
    records = list(map(int, filter(lambda x: x, puzzleInput[1][10:].split(" "))))

    output = 1
    for i in range(len(raceTimes)):
        currentRecordButtonTime = math.trunc((-math.sqrt(raceTimes[i]**2 - 4*records[i]) + raceTimes[i])/2)
        winningCardinality = (raceTimes[i]/2 - currentRecordButtonTime)*2 - 1
        print(f"race {i}: current {currentRecordButtonTime}, winning {winningCardinality}")
        output *= winningCardinality

    return int(output)

def part2(f):
    puzzleInput = getFullInput(f)
    raceTime = int(puzzleInput[0][10:].replace(" ", ""))
    record = int(puzzleInput[1][10:].replace(" ", ""))

    output = 1
    currentRecordButtonTime = math.trunc((-math.sqrt(raceTime ** 2 - 4 * record) + raceTime) / 2)
    winningCardinality = (raceTime / 2 - currentRecordButtonTime) * 2 - 1
    print(f"race: current {currentRecordButtonTime}, winning {winningCardinality}")
    output *= winningCardinality

    return int(output)


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
    with open("inputs/aoc2023-6-input.txt") as f:
        print("Input results:")
        print(f"  Part 1: {part1(f)}")
        f.seek(0)
        print(f"  Part 2: {part2(f)}")


if __name__ == "__main__":
    main()
