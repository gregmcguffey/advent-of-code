# Find number of nodes for each path, sum for all paths
# create binary tree from parsing
def readInput(filePath):
    with open(filePath, "r") as file:
        return [line.strip() for line in file.readlines()]


class TachyonManifoldNode:
    def __init__(self, id, lIdx, rIdx):
        self.data = id, (lIdx, rIdx)
        self.left = None
        self.right = None


def findStart(line):
    return line.find("S")


def replaceCharAtIndex(line, idx, char):
    return line[:idx] + char + line[idx + 1 :]


def main():
    nodeId = 1
    startLine, *inputLines = readInput("input.txt")

    startIdx = findStart(startLine)
    rootNode = TachyonManifoldNode(nodeId, 0, startIdx)

    rayIdx = [(startIdx, rootNode)]
    splits = 0

    for idx in range(len(inputLines)):
        line = inputLines[idx]
        lineSplits = 0
        newLine = line[:]
        newRayIdx = []
        # print("\n\n0. STarting line Rays")
        # print(newRayIdx)

        for rIdx, node in rayIdx:
            charAtPos = line[rIdx]
            # print(f"character at {rIdx}: {charAtPos}")
            if charAtPos == ".":
                if not (rIdx, node) in newRayIdx:
                    newRayIdx.append((rIdx, node))
                    newLine = replaceCharAtIndex(newLine, rIdx, "|")
            elif charAtPos == "^":
                # need to track paths here, create copies, append nodes to paths
                # look up via rIdx, but with lower line idx....but splitter will be
                # either left or right of ray...hmmmß
                lineSplits += 1
                leftSplitIdx = rIdx - 1

                # the split ray will eventually end up at a node
                nodeId += 1
                leftNode = TachyonManifoldNode(nodeId)
                node.left = leftNode
                if not (leftSplitIdx, leftNode) in newRayIdx:
                    newRayIdx.append((leftSplitIdx, leftNode))
                    newLine = replaceCharAtIndex(newLine, leftSplitIdx, "|")

                rightSplitIdx = rIdx + 1
                nodeId += 1
                rightNode = TachyonManifoldNode(nodeId)
                node.right = rightNode
                if not (rightSplitIdx, rightNode) in newRayIdx:
                    newRayIdx.append((rightSplitIdx, rightNode))
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

    pathCount = outputLines[-1].count("|")
    print(f"Number of splits: {splits}")
    print(f"Number of Paths: {pathCount}")


if __name__ == "__main__":
    main()
