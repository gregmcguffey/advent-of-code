from functools import partial

inputFile = 'input.txt'
# inputFile = 'input-test.txt'


def loadMatrix():
  matrix = []
  with open(inputFile, 'r') as input:
    for line in input:
      matrix.append(list(line))

  return matrix


def printPuzzle(matrix):
  for line in matrix:
    printLine = line[:-1] if line[-1] == '\n' else line


def checkValue(potentialMatch):
  matchValue = 'XMAS'
  return potentialMatch == matchValue or potentialMatch[::-1] == 'XMAS'


def getValue(matrix, coordinates):
  value = ""
  for location in coordinates:
    x, y = location
    value += matrix[y][x]
  return value

def findMatches(matrix, location):
  x, y = location
  width = len(matrix[0])
  height = len(matrix)

  # Possible 8 directions, edges will have fewer
  searchWest = x >= 3
  searchEast = x + 3 < width
  searchNorth = y >= 3
  searchSouth = y + 3 < height

  searchNorthWest = searchWest and searchNorth
  searchNorthEast = searchEast and searchNorth
  searchSouthEast = searchEast and searchSouth
  searchSouthWest = searchWest and searchSouth

  # define coordinates for 4 cells (array of tuples) for each direction
  directions = [
    {
      "isUsed": searchWest,
      "coordinates": [(x - 3, y),(x - 2, y),(x - 1, y),(x, y)]
    },
    {
      "isUsed": searchNorthWest,
      "coordinates": [(x - 3, y - 3),(x - 2, y - 2),(x - 1, y - 1),(x, y)]
    },
    {
      "isUsed": searchNorth,
      "coordinates": [(x, y - 3),(x, y - 2),(x, y - 1),(x, y)]
    },
    {
      "isUsed": searchNorthEast,
      "coordinates": [(x + 3, y - 3),(x + 2, y - 2),(x + 1, y - 1),(x, y)]
    },
    {
      "isUsed": searchEast,
      "coordinates": [(x, y),(x + 1, y),(x + 2, y),(x + 3, y)]
    },
    {
      "isUsed": searchSouthEast,
      "coordinates": [(x + 3, y + 3),(x + 2, y + 2),(x + 1, y + 1),(x, y)]
    },
    {
      "isUsed": searchSouth,
      "coordinates": [(x, y + 3),(x, y + 2),(x, y + 1),(x, y)]
    },
    {
      "isUsed": searchSouthWest,
      "coordinates": [(x - 3, y + 3),(x - 2, y + 2),(x - 1, y + 1),(x, y)]
    }
  ]

  searchDirections = list(filter(lambda direction: direction["isUsed"], directions ))

  totalFound = 0
  for direction in searchDirections:
    value = getValue(matrix, direction["coordinates"])
    if checkValue(value):
      totalFound += 1

  return totalFound


def solve(matrix):
  searchValue = 'X'
  # find = partial(findMatches, matrix=matrix)
  matchCount = 0
  for y, row in enumerate(matrix):
    for x, value in enumerate(row):
      if value == searchValue:
        matchCount += findMatches(matrix, (x,y))

  return matchCount


puzzleMatrix = loadMatrix()
matchCount = solve(puzzleMatrix)

# printPuzzle(puzzleMatrix)

print(f'Total "XMAS" Matches: {matchCount}')