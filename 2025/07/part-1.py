def readInput(filePath):
    with open(filePath, "r") as file:
        return [line.strip() for line in file.readlines()]


def findStart(line):
    return line.find("S")


def replaceCharAtIndex(line, idx, char):
    return line[:idx] + char + line[idx + 1 :]


def main():
    startLine, *inputLines = readInput("input.txt")
    outputLines = [startLine]
    print(startLine)

    startIdx = findStart(startLine)

    rayIdx = [startIdx]
    splits = 0

    for idx in range(len(inputLines)):
        line = inputLines[idx]
        lineSplits = 0
        newLine = line[:]
        newRayIdx = []
        # print("\n\n0. STarting line Rays")
        # print(newRayIdx)

        for rIdx in rayIdx:
            charAtPos = line[rIdx]
            # print(f"character at {rIdx}: {charAtPos}")
            if charAtPos == ".":
                if not rIdx in newRayIdx:
                    newRayIdx.append(rIdx)
                    newLine = replaceCharAtIndex(newLine, rIdx, "|")
            elif charAtPos == "^":
                lineSplits += 1
                leftSplitIdx = rIdx - 1
                if not leftSplitIdx in newRayIdx:
                    newRayIdx.append(leftSplitIdx)
                    newLine = replaceCharAtIndex(newLine, leftSplitIdx, "|")

                rightSplitIdx = rIdx + 1
                if not rightSplitIdx in newRayIdx:
                    newRayIdx.append(rightSplitIdx)
                    newLine = replaceCharAtIndex(newLine, rightSplitIdx, "|")

        splits += lineSplits
        newLine = newLine + "  " + str(lineSplits) if lineSplits > 0 else newLine
        newLine = (
            newLine + "   ^ #" + str(newLine.count("^")) if lineSplits > 0 else newLine
        )
        outputLines.append(newLine)
        print(newLine)

        # print("\n\n1. Current Rays")
        # print(rayIdx)
        # print("\n\n2. Line Rays")
        # print(newRayIdx)

        rayIdx = newRayIdx

        # print("\n\n3. New Rays")
        # print(rayIdx)

    print(f"Number of splits: {splits}")


if __name__ == "__main__":
    main()
