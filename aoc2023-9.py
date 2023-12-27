def part1(f):
    output = 0
    for line in inputReader(f):
        # generate list of lists to operate on to find predicted number
        layers = [list(map(int, line.split()))]
        processing = True
        layerNum = 0
        while processing:
            # build next layer while checking for all 0 values
            nextLayer = []
            nonZeroValue = False
            for i in range(len(layers[layerNum])-1):
                nextLayer.append(layers[layerNum][i+1]-layers[layerNum][i])
                if nextLayer[-1] != 0:
                    nonZeroValue = True
            layers.append(nextLayer)
            if nonZeroValue:
                layerNum += 1
                continue
            else:
                processing = False

        # work backwards up the layers to find predicted value for current input line
        predictValue = 0
        for layer in reversed(layers[:-1]):
            predictValue = layer[-1]+predictValue
        output += predictValue

    return output

def part2(f):
    output = 0
    for line in inputReader(f):
        # generate list of lists to operate on to find predicted number
        layers = [list(map(int, line.split()))]
        processing = True
        layerNum = 0
        while processing:
            # build next layer while checking for all 0 values
            nextLayer = []
            nonZeroValue = False
            for i in range(len(layers[layerNum]) - 1):
                nextLayer.append(layers[layerNum][i + 1] - layers[layerNum][i])
                if nextLayer[-1] != 0:
                    nonZeroValue = True
            layers.append(nextLayer)
            if nonZeroValue:
                layerNum += 1
                continue
            else:
                processing = False

        # work backwards up the layers to find predicted value for current input line
        predictValue = 0
        for layer in reversed(layers[:-1]):
            predictValue = layer[0] - predictValue
        output += predictValue

    return output


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
    with open("inputs/aoc2023-9-input.txt") as f:
        print("Input results:")
        print(f"  Part 1: {part1(f)}")
        f.seek(0)
        print(f"  Part 2: {part2(f)}")


if __name__ == "__main__":
    main()
