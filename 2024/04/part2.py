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
    print(f'{"".join(printLine)}')


def checkValue(potentialMatch):
  # match for each direction
  leftMatch = 'MSAMS'
  rightMatch = 'SMASM'
  topMatch = 'MMASS'
  bottomMatch = 'SSAMM'
  return potentialMatch in [leftMatch, rightMatch, topMatch, bottomMatch]

def getValue(matrix, center):
  # get characters in specific order: top, middle, bottom -> left to right
  value = ""
  x, y = center
  coordinates = [(x-1, y-1),(x+1,y-1),(x,y),(x-1, y+1),(x+1, y+1)]
  for location in coordinates:
    x, y = location
    value += matrix[y][x]
  return value

def findMatches(matrix, location):
  x, y = location
  width = len(matrix[0])
  height = len(matrix)

  totalFound = 0

  # four directions: left, right, up and down
  # search character (the location) needs to be
  # surrounded by one row/col on each side
  validLocation = x > 0 and x < width - 1 and y > 0 and y < height - 1

  if validLocation:
    value = getValue(matrix, (x,y))
    if checkValue(value):
      totalFound += 1


  return totalFound


def solve(matrix):
  searchValue = 'A'
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

print(f'Total Matches: {matchCount}')