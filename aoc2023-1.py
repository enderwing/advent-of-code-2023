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
    numFilter = re.compile(r'one|two|three|four|five|six|seven|eight|nine|\d')
    words = ("one","two","three","four","five","six","seven","eight","nine")
    digits = ["1","2","3","4","5","6","7","8","9"]
    while line:
        numbers = numFilter.findall(line)
        out1 = numbers[0]
        if out1 in words:
            index1 = words.index(out1)
            out1 = digits[index1]
        out2 = numbers[-1]
        if out2 in words:
            index2 = words.index(out2)
            out2 = digits[index2]

        total += int(out1+out2)
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
