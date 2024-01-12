def part1(f):
    # create the expanded universe, initially handling all row expansion
    rowExpandedUniverse = []
    for line in inputReader(f):
        rowExpandedUniverse.append(list(line))
        if "#" not in line:
            rowExpandedUniverse.append(list(line))
    expandedSize = len(rowExpandedUniverse)
    # handle column expansion
    rowExpandedUniverse = list(map(list, zip(*rowExpandedUniverse)))
    expandedUniverse = []
    for column in rowExpandedUniverse:
        expandedUniverse.append(column)
        if "#" not in column:
            expandedUniverse.append(column)
    expandedUniverse = list(map(list, zip(*expandedUniverse)))

    # list of row, col positions [(r1,c1), (r2,c2) ...]
    galaxies = []
    for r, row in enumerate(expandedUniverse):
        for c, col in enumerate(row):
            if col == "#":
                galaxies.append((r,c))

    pathSum = 0
    for g, galaxy in enumerate(galaxies[:-1]):
        for compGalaxy in galaxies[g+1:]:
            pathSum += abs(galaxy[0]-compGalaxy[0]) + abs(galaxy[1]-compGalaxy[1])

    return pathSum

def part2(f):
    expansionFactor = 1000000
    rowIsExpanded = []
    colIsExpanded = []

    originalUniverse = []
    for line in inputReader(f):
        originalUniverse.append(list(line))
        if "#" in line:
            rowIsExpanded.append(False)
        else:
            rowIsExpanded.append(True)

    for column in zip(*originalUniverse):
        if "#" in column:
            colIsExpanded.append(False)
        else:
            colIsExpanded.append(True)

    # list of row, col positions [(r1,c1), (r2,c2) ...]
    galaxies = []
    for r, row in enumerate(originalUniverse):
        for c, col in enumerate(row):
            if col == "#":
                galaxies.append((r, c))

    pathSum = 0
    for g, galaxy in enumerate(galaxies[:-1]):
        for compGalaxy in galaxies[g + 1:]:
            pathSum += abs(galaxy[0] - compGalaxy[0]) + abs(galaxy[1] - compGalaxy[1])
            if compGalaxy[0] >= galaxy[0]:
                pathSum += rowIsExpanded[galaxy[0] + 1:compGalaxy[0]].count(True) * (expansionFactor-1)
            else:
                pathSum += rowIsExpanded[compGalaxy[0] + 1:galaxy[0]].count(True) * (expansionFactor-1)

            if compGalaxy[1] >= galaxy[1]:
                pathSum += colIsExpanded[galaxy[1] + 1:compGalaxy[1]].count(True) * (expansionFactor-1)
            else:
                pathSum += colIsExpanded[compGalaxy[1] + 1:galaxy[1]].count(True) * (expansionFactor - 1)

    return pathSum


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
    with open("inputs/aoc2023-11-input.txt") as f:
        print("Input results:")
        print(f"  Part 1: {part1(f)}")
        f.seek(0)
        print(f"  Part 2: {part2(f)}")


if __name__ == "__main__":
    main()
