import re
import sys


def part1(f):
    lines = getFullInput(f)

    # get seeds then remove from data
    seeds = list(map(int, lines[0][7:].split(" ")))
    del lines[0:2]

    # make list of conversion ranges
    conversionSources = []
    conversionDestinations = []
    tempSources = []
    tempDestinations = []
    for line in lines:
        if not line:
            conversionSources.append(tempSources.copy())
            conversionDestinations.append(tempDestinations.copy())
            tempSources.clear()
            tempDestinations.clear()
        elif line[0].isalpha():
            continue
        else:
            nums = list(map(int, line.split(" ")))
            tempSources.append((nums[1], nums[1]+nums[2]-1))
            tempDestinations.append(nums[0])
    conversionSources.append(tempSources.copy())
    conversionDestinations.append(tempDestinations.copy())
    tempSources.clear()
    tempDestinations.clear()

    lowestLocation = sys.maxsize
    for seed in seeds:
        currentVal = seed
        # trace through all conversions
        for s, source in enumerate(conversionSources):
            offset = 0
            mappingIndex = -1
            for m, mapping in enumerate(source):
                if mapping[0] <= currentVal <= mapping[1]:
                    offset = currentVal - mapping[0]
                    mappingIndex = m
                    break

            if mappingIndex > -1:
                currentVal = conversionDestinations[s][mappingIndex]
                currentVal += offset

        if currentVal < lowestLocation: lowestLocation = currentVal

    # already tried:
    # 144435049 - too low
    return lowestLocation

def part2(f):

    return None


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
    with open("inputs/aoc2023-5-input.txt") as f:
        print("Input results:")
        print(f"  Part 1: {part1(f)}")
        f.seek(0)
        print(f"  Part 2: {part2(f)}")


if __name__ == "__main__":
    main()
