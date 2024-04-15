def part1(f):
    sumArrangements = 0
    rowData = []
    for row in inputReader(f):
        a = row.split()
        springs = list(a[0])
        nonogram = a[1].split(",")

        for i in range(len(springs)-1, 0, -1):
            if springs[i] == '.' and springs[i-1] == '.': springs.pop(i)


    return sumArrangements

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
    with open("inputs/aoc2023-12-input.txt") as f:
        print("Input results:")
        print(f"  Part 1: {part1(f)}")
        f.seek(0)
        print(f"  Part 2: {part2(f)}")


if __name__ == "__main__":
    main()
