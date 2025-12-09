from operator import itemgetter


def readInput(filePath):
    with open(filePath, "r") as file:
        return [line.strip() for line in file.readlines()]


def parseFreshIngredientLine(line):
    idRangeStr = line.split("-")
    idRange = [int(id) for id in idRangeStr]
    return idRange


def main():
    inputLines = readInput("input.txt")

    freshIdRanges = []
    for line in inputLines:
        if line == "":
            break

        idRange = parseFreshIngredientLine(line)
        freshIdRanges.append(idRange)

    print(f"Lines parsed ({len(freshIdRanges)})")

    # sort fresh id ranges by start id
    freshIdRanges.sort(key=itemgetter(0))
    # print("Fresh ingredient ID ranges sorted.", freshIdRanges)

    # double for loop is way too slow

    # instead, consolidate ranges and use differences
    consolidatedFreshIdRanges = []
    prevStartId = None
    prevEndId = None
    for startId, endId in freshIdRanges:
        if prevStartId is None:
            prevStartId = startId
            prevEndId = endId
            consolidatedFreshIdRanges.append((startId, endId))
            continue

        # three cases: contained, overlapping, separate
        if startId <= prevEndId and endId <= prevEndId:
            # contained range, skip
            continue
        elif startId <= prevEndId and endId > prevEndId:
            # overlapping range, extend previous end id
            prevEndId = endId
            consolidatedFreshIdRanges[-1] = (prevStartId, endId)
        else:
            # separate range, add new range
            prevStartId = startId
            prevEndId = endId
            consolidatedFreshIdRanges.append((startId, endId))

    print(f"Consolidated to {len(consolidatedFreshIdRanges)} unique fresh ID ranges.")

    # now calculate total unique fresh ids
    countFreshIds = 0
    for startId, endId in consolidatedFreshIdRanges:
        idCount = endId - startId + 1
        # print(f"Range {startId}-{endId} -> {idCount}")
        countFreshIds += idCount

    print(f"Total unique fresh ingredients: {countFreshIds}")


if __name__ == "__main__":
    main()
