import importlib
import importlib.util
import sys


year = 2023
selectedDayNum = -1
selectedDay = None
curPrompt = "initial"
userInput = ""
def main():
    global userInput
    running = True
    while running:
        match curPrompt:
            case "initial":
                getInput("Enter a number (#) to select a day, or (C) to create a day. Enter (Q) anywhere else to return to this prompt. Enter (Q) here to quit.")
            case "createDay":
                getInput("Enter the day number (#)")
            case "dayMenu":
                getInput(f"Day {selectedDayNum}. Enter (R) to run on input data, (T) to run on test input data, or (S) to run on scratch file data. Enter (E) to reload the current day code.")
            case _:
                print("Not recognized.")
        process_input()

def getInput(prompt):
    global userInput
    print(prompt)
    userInput = input(">> ").strip().lower()

def process_input():
    global curPrompt, userInput, selectedDayNum, selectedDay, year
    if userInput == 'q':
        if curPrompt != "initial":
            curPrompt = "initial"
            return
        else:
            print("Goodbye!")
            sys.exit(0)

    if curPrompt == "initial":
        if userInput == 'c':
            curPrompt = "createDay"
            return
        try: numInput = int(userInput)
        except ValueError:
            pass
        else:
            selectedDayNum = numInput
            selectedDay = importDay(selectedDayNum)
            if selectedDay is None:
                getInput("Day not found. Enter (C) to create it now, or anything else to continue.")
                if userInput == 'c':
                    userInput = selectedDayNum
                    curPrompt = "createDay"
                    process_input()
                    return
                curPrompt = "initial"
                return
            else:
                curPrompt = "dayMenu"
                return

    if curPrompt == "createDay":
        try: numInput = int(userInput)
        except ValueError:
            pass
        else:
            createDay(numInput)
            print(f"Day {numInput} created.")
            curPrompt = "initial"
            return

    if curPrompt == "dayMenu":
        if userInput == 'e':
            selectedDay = importDay(selectedDayNum)
            print(f"Day {selectedDayNum} reloaded.")
            return
        if userInput == 'r':
            path = f"inputs/aoc{year}-{selectedDayNum}-input.txt"
            runDay(selectedDay, path, path,"Input")
            return
        if userInput == 's':
            path = f"inputs/scratch-input.txt"
            runDay(selectedDay, path, path, "Scratch input")
            return
        if userInput == 't':
            path1 = f"inputs/aoc{year}-{selectedDayNum}-test1.txt"
            path2 = f"inputs/aoc{year}-{selectedDayNum}-test2.txt"
            runDay(selectedDay, path1, path2, "Test")
            return
    print("Input not recognized.")


def createDay(dayNum):
    with open(f"aoc{year}-{dayNum}.py", "x") as f:
        templateData = ""
        with open(f"template.py") as template:
            templateData = template.read()
        templateData = templateData.replace("{yearday}", f"{year}-{dayNum}")
        f.write(templateData)
    with open(f"inputs/aoc{year}-{dayNum}-input.txt", "x") as f:
        f.write("")
    with open(f"inputs/aoc{year}-{dayNum}-test1.txt", "x") as f:
        f.write("")
    with open(f"inputs/aoc{year}-{dayNum}-test2.txt", "x") as f:
        f.write("")

def importDay(dayNum):
    path = f"aoc{year}-{dayNum}"
    day = importlib.util.find_spec(path)
    if not day:
        return None
    day = importlib.import_module(path)
    return day

def runDay(day, filePath1, filePath2, resultTitle):
    print(f"{resultTitle} results:")
    with open(filePath1) as f:
        print(f"  Part 1: {day.part1(f)}")
    with open(filePath2) as f:
        print(f"  Part 2: {day.part2(f)}")

if __name__ == "__main__":
    main()
