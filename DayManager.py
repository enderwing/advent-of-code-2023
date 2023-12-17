import importlib as imp
import importlib.util


def main():
    year = 2023
    # pressing enter without entering any input for the first prompt will automatically select quickDay and run it on
    # the test-input.txt file
    # if quickRun is true on program start, DayManager automatically selects quickDay and runs
    # the test-input.txt with no user input
    quickDay = 2
    quickRun = False
    skipTest = False

    day = None
    dayNum = -1
    while not day:
        if quickRun or quickDay > -1:
            userInput = quickDay
        else:
            userInput = input("Enter a number (#) to import that day, or (C) to create a new day: ").strip().lower()
        if not userInput:
            userInput = quickDay
            quickRun = True
        if userInput == "c":
            dayNum = int(input("Enter the day number (#): "))
            with open(f"aoc{year}-{dayNum}.py", "x") as f:
                templateData = ""
                with open(f"template.py") as template:
                    templateData = template.read()
                templateData = templateData.replace("{yearday}", f"{year}-{dayNum}")
                f.write(templateData)
            with open(f"inputs/aoc{year}-{dayNum}-input.txt", "x") as f:
                f.write("")
                f.close()
            return 0
        elif userInput == "q":
            return 0
        else:
            dayNum = int(userInput)
            day = imp.util.find_spec(f"aoc{year}-{dayNum}")
            if not day:
                if not quickRun:
                    print("Day not found")
                else:
                    print("Quick run selected with no valid day, please enter day manually")
                    quickRun = False
    day = imp.import_module(f"aoc{year}-{dayNum}")

    while True:
        if quickRun:
            userInput = "t" if not skipTest else "r"
            quickRun = False
        else:
            userInput = input(f"Day {dayNum}, enter (R) to run on input data, or (T) to run on test file data, (Q) to quit: ").strip().lower()

        if not userInput:
            userInput = "t"
        if userInput == "r":
            with open(f"inputs/aoc{year}-{dayNum}-input.txt") as f:
                print("Input results:")
                print(f"  Part 1: {day.part1(f)}")
                f.seek(0)
                print(f"  Part 2: {day.part2(f)}")
        elif userInput == "t":
            with open(f"inputs/test-input.txt") as f:
                print("Test results:")
                print(f"  Part 1: {day.part1(f)}")
                f.seek(0)
                print(f"  Part 2: {day.part2(f)}")
        elif userInput == "q":
            return 0


if __name__ == "__main__":
    main()
