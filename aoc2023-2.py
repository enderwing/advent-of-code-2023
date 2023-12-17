import re


def part1(f):
    colorLimits = {"red": 12, "green": 13, "blue": 14}

    getNum = re.compile(r'\d+')
    getColor = re.compile(r'[a-z]+$')

    gameIDSum = 0
    while True:
        line = f.readline().strip().lower()
        if not line:
            break

        split1 = line.split(":")
        gameID = int(getNum.findall(split1[0])[0])
        rounds = split1[1].split(";")
        for i, game in enumerate(rounds):
            rounds[i] = game.split(",")

        possible = True
        for singleRound in rounds:
            for colorInfo in singleRound:
                amount = int(getNum.findall(colorInfo)[0])
                color = getColor.findall(colorInfo)[0]
                if amount > colorLimits.get(color):
                    possible = False
                    break
            else:
                continue
            break
        if possible:
            gameIDSum += gameID

    return gameIDSum

def part2(f):
    getNum = re.compile(r'\d+')
    getColor = re.compile(r'[a-z]+$')

    gamePowerSum = 0
    while True:
        line = f.readline().strip().lower()
        if not line:
            break

        split1 = line.split(":")
        gameID = int(getNum.findall(split1[0])[0])
        rounds = split1[1].split(";")
        for i, game in enumerate(rounds):
            rounds[i] = game.split(",")

        colorMaxes = {"red": 0, "green": 0, "blue": 0}
        for singleRound in rounds:
            for colorInfo in singleRound:
                amount = int(getNum.findall(colorInfo)[0])
                color = getColor.findall(colorInfo)[0]
                if amount > colorMaxes.get(color):
                    colorMaxes.update({color: amount})
        gamePower = 1
        for num in colorMaxes.items():
            gamePower *= num[1]
        gamePowerSum += gamePower

    return gamePowerSum


def main():
    with open("inputs/aoc2023-2-input.txt") as f:
        print("Input results:")
        print(f"  Part 1: {part1(f)}")
        f.seek(0)
        print(f"  Part 2: {part2(f)}")

if __name__ == "__main__":
    main()
