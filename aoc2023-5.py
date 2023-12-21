import re


def part1(f):
    lines = getFullInput(f)

    # get seeds then remove from data
    seeds = list(map(int, lines[0][7:].split(" ")))
    del lines[0:2]

    # make list of conversion ranges
    # format [[(source1lower, source1upper), (destination1lower, destination2lower),...],...]
    conversionList = []
    tempConversion = []
    for line in lines:
        if not line:
            conversionList.append(tempConversion)
            tempConversion.clear()
        elif line[0].isalpha():
            continue
        else:
            nums = list(map(lambda x: int(x), line.split(" ")))
            tempConversion.append((nums[1], nums[1]+nums[2]-1))
            tempConversion.append((nums[0], nums[0]+nums[2]-1))
        lowestLocation = 0
        for seed in seeds:


    return None

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
