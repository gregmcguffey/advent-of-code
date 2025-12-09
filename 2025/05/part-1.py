def readInput(filePath):
    with open(filePath, "r") as file:
        return [line.strip() for line in file.readlines()]


def parseFreshIngredientLine(line):
    idRangeStr = line.split("-")
    idRange = [int(id) for id in idRangeStr]
    return idRange


def main():
    inputLines = readInput("input.txt")

    freshCount = 0

    isAvailableSection = False
    idRanges = []

    for line in inputLines:
        if line == "":
            isAvailableSection = True
            continue

        if not isAvailableSection:
            idRange = parseFreshIngredientLine(line)
            # track ranges of fresh ingredients
            idRanges.append(idRange)
        else:
            availableId = int(line)
            # determine if the ingredient is fresh and available
            for startId, endId in idRanges:
                if availableId >= startId and availableId <= endId:
                    freshCount += 1
                    break

    print(f"Total fresh available ingredients: {freshCount}")


if __name__ == "__main__":
    main()
