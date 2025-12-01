def readInput(filePath):
    with open(filePath, "r") as file:
        return [line.strip() for line in file.readlines()]


def rotate(currentValue, direction, clickCount):
    # work in range of 1 to 100 as 0 % 99 = 0 AND 99 % 99 = 0
    workingValue = currentValue + 1

    rotation = clickCount if direction == "R" else -clickCount
    calcValue = workingValue + rotation

    newValue = calcValue % 100

    # adjust back to 0-99 range
    if newValue == 0:
        newValue = 99
    else:
        newValue = newValue - 1

    return newValue


def main():
    inputLines = readInput("input.txt")
    currentValue = 50  # Starting point
    zeroCount = 0

    for line in inputLines:
        direction = line[0]
        rotation = int(line[1:])

        if direction == "L":
            newValue = rotate(currentValue, direction, rotation)
        elif direction == "R":
            newValue = rotate(currentValue, direction, rotation)

        currentValue = newValue
        zeroCount = zeroCount + 1 if currentValue == 0 else zeroCount

    print(f"Final value: {zeroCount}")


if __name__ == "__main__":
    main()
