import re

def part1(f):
    line = f.readline()
    total = 0
    numFilter = re.compile(r'\d')
    while line:
        numbers = numFilter.findall(line)
        if len(numbers) == 0:
            line = f.readline()
            continue
        out = numbers[0]+numbers[-1]
        total += int(out)
        line = f.readline()
    return total


def part2(f):
    line = f.readline().strip().lower()
    total = 0
    numFilter = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))')
    digitConversion = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    while line:
        numbers = numFilter.findall(line)
        out1 = numbers[0]
        if out1 in digitConversion:
            out1 = digitConversion.get(out1)
        out2 = numbers[-1]
        if out2 in digitConversion:
            out2 = digitConversion.get(out2)

        total += int(out1 + out2)
        line = f.readline().strip().lower()
    return total


def main():
    with open("inputs/aoc2023-1-input.txt") as f:
        print("Input results:")
        print(f"  Part 1: {part1(f)}")
        f.seek(0)
        print(f"  Part 2: {part2(f)}")


if __name__ == "__main__":
    main()
