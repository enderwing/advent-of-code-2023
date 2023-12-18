def part1(f):
    line = f.readline().strip()
    winningStartIndex = line.index(":") + 2
    winningEndIndex = line.index("|") - 2
    numStartIndex = line.index("|") + 2
    winnings = 0
    while line:
        winningNums = list(map(lambda x: int(x), filter(lambda x: x, line[winningStartIndex:winningEndIndex+1].split(" "))))
        myNums = list(map(lambda x: int(x), filter(lambda x: x, line[numStartIndex:].split(" "))))

        matchingNumCount = 0
        for num in myNums:
            if num in winningNums:
                matchingNumCount += 1
        if matchingNumCount > 0: winnings += 2**(matchingNumCount-1)

        line = f.readline().strip()
    return winnings

def part2(f):
    line = f.readline().strip()
    winningStartIndex = line.index(":") + 2
    winningEndIndex = line.index("|") - 2
    numStartIndex = line.index("|") + 2

    cardCounts = {}
    currentCard = 1
    while line:
        winningNums = list(
            map(lambda x: int(x), filter(lambda x: x, line[winningStartIndex:winningEndIndex + 1].split(" "))))
        myNums = list(map(lambda x: int(x), filter(lambda x: x, line[numStartIndex:].split(" "))))

        cardCounts.setdefault(currentCard, 1)
        matchingCountOffset = 1
        for num in myNums:
            if num in winningNums:
                cardCounts.update({currentCard + matchingCountOffset: cardCounts.get(currentCard) + cardCounts.get(currentCard + matchingCountOffset, 1)})
                matchingCountOffset += 1

        line = f.readline().strip()
        currentCard += 1

    return sum(cardCounts.values())


def main():
    with open("inputs/aoc2023-4-input.txt") as f:
        print("Input results:")
        print(f"  Part 1: {part1(f)}")
        f.seek(0)
        print(f"  Part 2: {part2(f)}")


if __name__ == "__main__":
    main()
