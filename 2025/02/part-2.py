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
    # Invalid the number is a sequence of digits repeated at least twice.
    strValue = str(value)
    length = len(strValue)

    # check sets of digits from size 1 up to half the length of the string
    for size in range(1, (length // 2) + 1):
        if length % size != 0:
            continue  # size must evenly divide length

        segment = strValue[0:size]
        repetitions = length // size
        if segment * repetitions == strValue:
            return True

    return False


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
