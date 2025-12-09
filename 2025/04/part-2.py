import copy


def readInput(filePath):
    with open(filePath, "r") as file:
        return [line.strip() for line in file.readlines()]


def parseLine(line):
    valueLine = line.replace("@", "1").replace(".", "0")
    grid = [int(char) for char in valueLine]
    return grid


def getAdjacentPositions(x, y, maxX, maxY):
    positions = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            newX, newY = x + dx, y + dy
            if newX == x and newY == y:
                continue
            if 0 <= newX < maxX and 0 <= newY < maxY:
                positions.append((newX, newY))
    return positions


def getRollsForPosition(x, y, grid):
    width = len(grid[0])
    height = len(grid)

    adjacent = getAdjacentPositions(x, y, width, height)

    rollCount = sum(grid[ay][ax] for ax, ay in adjacent)
    return rollCount


def process(grid):
    newGrid = copy.deepcopy(grid)
    rollCount = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 0:
                continue

            rollsNearCell = getRollsForPosition(x, y, grid)
            if rollsNearCell is None:
                continue
            if rollsNearCell < 4:
                rollCount += 1
                newGrid[y][x] = 0

    return rollCount, newGrid


def main():
    inputLines = readInput("input.txt")
    currentGrid = [parseLine(line) for line in inputLines]

    testCount, testGrid = process(currentGrid)
    print(f"Test process rolls: {testCount}")
    totalRolls = None
    rollCount = None
    process_count = 0
    while totalRolls is None or rollCount > 0:
        rollCount, currentGrid = process(currentGrid)
        totalRolls = rollCount + totalRolls if totalRolls is not None else rollCount
        process_count += 1
        print(
            f"After process {process_count}, rolls this round: {rollCount}, total rolls: {totalRolls}"
        )

    print(f"Total rolls: {totalRolls}")


if __name__ == "__main__":
    main()
