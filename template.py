def part1(f):
    return None

def part2(f):
    return None


def main():
    with open("inputs/aoc{yearday}-input.txt") as f:
        print("Input results:")
        print(f"  Part 1: {part1(f)}")
        f.seek(0)
        print(f"  Part 2: {part2(f)}")


if __name__ == "__main__":
    main()
