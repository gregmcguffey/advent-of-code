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
    # print(f"    Cell ({x}, {y}) has adjacent positions: {adjacent}")

    rollCount = sum(grid[ay][ax] for ax, ay in adjacent)
    return rollCount


def main():
    inputLines = readInput("input.txt")

    rollCount = 0

    grid = [parseLine(line) for line in inputLines]

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 0:
                continue

            # print(f"Checking cell ({x}, {y}) with value {cell}")

            rollsNearCell = getRollsForPosition(x, y, grid)
            # print(f"  Cell ({x}, {y}) has rolls: {rollsNearCell}")
            if rollsNearCell is None:
                continue
            if rollsNearCell < 4:
                # print(
                #     f"  Current total rolls: {rollCount} with cell rolls: {rollsNearCell}"
                # )
                rollCount += 1

    print(f"Total rolls: {rollCount}")


if __name__ == "__main__":
    # test_line = "..@@@@@@...@@@@@@..@@@@@@@.@@.@...@@.@@.@.@..@..@@@@@@@.@..@@@..@..@@....@@@@..@.@@..@.@@.@@.@...@@@..@@@.@.@.@.@.@@@..@.@@@@.@@.@.@..@@."
    # values_line = test_line.replace("@", "1").replace(".", "0")
    # print(f"compare:\n{test_line}\n{values_line}")
    main()
