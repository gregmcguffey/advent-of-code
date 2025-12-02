def parseInput(filePath):
    with open(filePath, "r") as file:
        input = file.read()

    # Each range is separated by a comma and represented as "start-end"
    ranges = []
    for part in input.strip().split(","):
        start, end = map(int, part.split("-"))
        ranges.append((start, end))

    return ranges


def checkInvalid(value):
    # Invalid if it's a number repeated twice.
    # So, values with an odd number of digits are valid.
    strValue = str(value)
    length = len(strValue)
    if length % 2 != 0:
        return False

    halfLength = length // 2
    firstHalf = strValue[0:halfLength]
    secondHalf = strValue[halfLength:length]
    return firstHalf == secondHalf


def main():
    ranges = parseInput("input.txt")
    invalidCount = 0
    invalidSum = 0
    for start, end in ranges:
        for value in range(start, end + 1):
            if checkInvalid(value):
                invalidCount += 1
                invalidSum += value

    print(f"Invalid count: {invalidCount}\nInvalid sum: {invalidSum}")


if __name__ == "__main__":
    main()
