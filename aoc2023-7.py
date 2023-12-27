def part1(f):
    plays = getFullInput(f)
    # sortedHands = [ [5oaK], [4oaK], [FH], [3oaK], [TP], [OP], [HC] ]
    sortedHands = [[], [], [], [], [], [], []]
    cardLetters = ['T','J','Q','K','A']
    mappedLetters = [':',';','<','=','>']
    for play in plays:
        rawCards = play[:5]
        cards = ""
        bid = int(play[6:])
        cardCounts = {}
        for i in range(5):
            if ord(rawCards[i]) > 57: cards += (mappedLetters[cardLetters.index(rawCards[i])])
            else: cards += rawCards[i]
            cardCounts.update({cards[i]: cardCounts.setdefault(cards[i], 0) + 1})

        play = (cards, bid)
        if len(cardCounts) == 1:
            sortedHands[0].append(play)
        elif len(cardCounts) == 2:
            if 4 in list(cardCounts.values()):
                sortedHands[1].append(play)
            else:
                sortedHands[2].append(play)
        elif len(cardCounts) == 3:
            if 3 in list(cardCounts.values()):
                sortedHands[3].append(play)
            else:
                sortedHands[4].append(play)
        elif len(cardCounts) == 4:
            sortedHands[5].append(play)
        else:
            sortedHands[6].append(play)

    for handType in sortedHands:
        handType.sort(key=lambda x: x[0])

    rank = 1
    winnings = 0
    for handType in reversed(sortedHands):
        for hand in handType:
            winnings += hand[1]*rank
            rank += 1
    return winnings

def part2(f):
    plays = getFullInput(f)
    # sortedHands = [ [5oaK], [4oaK], [FH], [3oaK], [TP], [OP], [HC] ]
    sortedHands = [[], [], [], [], [], [], []]
    # mapping to change some card letters into better ascii aligned characters
    # ':' comes after '9', '1' comes before '2', '<' comes after ':' etc.
    cardLetters = ['T', 'J', 'Q', 'K', 'A']
    mappedLetters = [':', '1', '<', '=', '>']
    for play in plays:
        # process each hand to map card letters and to sort into the right hand type
        rawCards = play[:5]
        cards = ""
        bid = int(play[6:])
        cardCounts = {}
        # map original card letters to modified symbols to make sorting the hands easier
        for i in range(5):
            if ord(rawCards[i]) > 57:
                cards += (mappedLetters[cardLetters.index(rawCards[i])])
            else:
                cards += rawCards[i]
            cardCounts.update({rawCards[i]: cardCounts.setdefault(rawCards[i], 0) + 1})

        # if there are any jokers, "transform" all jokers into a different card with the (next) highest card count
        if 'J' in cardCounts.keys() and len(cardCounts) > 1:
            transformTarget = list(filter(lambda x: x[0] != 'J', sorted(cardCounts.items(), key=lambda x: x[1], reverse=True)))[0][0]
            cardCounts.update({transformTarget: cardCounts.get(transformTarget) + cardCounts.get('J')})
            cardCounts.pop('J')

        play = (cards, bid)
        # determine hand type and add to corresponding sortedHand list
        if len(cardCounts) == 1:
            sortedHands[0].append(play)
        elif len(cardCounts) == 2:
            if 4 in list(cardCounts.values()):
                sortedHands[1].append(play)
            else:
                sortedHands[2].append(play)
        elif len(cardCounts) == 3:
            if 3 in list(cardCounts.values()):
                sortedHands[3].append(play)
            else:
                sortedHands[4].append(play)
        elif len(cardCounts) == 4:
            sortedHands[5].append(play)
        else:
            sortedHands[6].append(play)

    # sort each type by the cards in hand
    for handType in sortedHands:
        handType.sort(key=lambda x: x[0])

    # iterate through the hand types in worst to best order
    # then iterate through hands in the string sorted order (worst to best)
    # increment rank and tally winnings
    rank = 1
    winnings = 0
    for handType in reversed(sortedHands):
        for hand in handType:
            winnings += hand[1] * rank
            rank += 1

    return winnings


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
    with open("inputs/aoc2023-7-input.txt") as f:
        print("Input results:")
        print(f"  Part 1: {part1(f)}")
        f.seek(0)
        print(f"  Part 2: {part2(f)}")


if __name__ == "__main__":
    main()
