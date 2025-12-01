def readInput(filePath):
    with open(filePath, "r") as file:
        return [line.strip() for line in file.readlines()]


def rotate(currentValue, direction, clickCount, debug=False):
    incValue = 1 if direction == "R" else -1
    newValue = currentValue
    if debug:
        print(f"\nRotating {direction}{clickCount} from {currentValue}")

    for click in range(1, clickCount + 1):
        rawValue = newValue + incValue
        if rawValue > 99:
            newValue = 0
        elif rawValue < 0:
            newValue = 99
        else:
            newValue = rawValue
        if debug:
            print(f"  Click #({click}): {newValue}")

    return newValue


def main():
    inputLines = readInput("input.txt")
    currentValue = 50  # Starting point
    zeroCount = 0

    for line in inputLines:
        direction = line[0]
        rotation = int(line[1:])

        debug = False  # rotation > 200 and rotation < 250

        if direction == "L":
            newValue = rotate(currentValue, direction, rotation, debug)
        elif direction == "R":
            newValue = rotate(currentValue, direction, rotation, debug)

        currentValue = newValue
        zeroCount = zeroCount + 1 if currentValue == 0 else zeroCount

    print(f"Final value: {zeroCount}")


if __name__ == "__main__":
    main()
