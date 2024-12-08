# from multiprocessing import Pool

def getDiff(v1, v2):
  if v1 == None or v2 == None:
    return None
  return v1 - v2


def getDirection(diff):
  if diff == None:
    return None
  return 'asc' if diff >= 0 else 'desc'


def checkSafe(lastDirection, currentDirection, diff):
  safeTrend = lastDirection == None or currentDirection == None or lastDirection == currentDirection
  safeRate = diff == None or (abs(diff) > 0 and abs(diff) <=3)
  return safeTrend and safeRate


def checkReport(report):
  isSafe = True
  unsafeIndex = None
  size = len(report)

  for i in range(size):
    current = report[i]
    prev =  report[i-1] if i > 0 else None
    next = report[i+1] if i < size - 1 else None
    lastDiff = getDiff(current, prev)
    diff = getDiff(next, current)
    lastDirection = getDirection(lastDiff)
    currentDirection = getDirection(diff)
    isSafe = isSafe and checkSafe(lastDirection, currentDirection, diff)
    if not isSafe:
      unsafeIndex = i
      break

  return isSafe, unsafeIndex


def tryFixing(report, baseIndex):
  isSafe = False

  for i in range(baseIndex-1, baseIndex+1):
    testReport = report.copy()
    del testReport[i]
    madeSafe, _ = checkReport(testReport)
    isSafe = isSafe or madeSafe
    if madeSafe:
      print(f'made safe ({i}): {report} -> {testReport}')
    if not isSafe:
      break

  return isSafe


# safe rules
# - all increasing or all decreasing
# - differ by 1 - 3 inclusive
safe = 0
with open('input.txt', 'r') as input:
  for line in input:
    report = []
    for level in line.split(' '):
      report.append(int(level))

    isSafe, unsafeIndex = checkReport(report)

    if not isSafe:
      madeSafe = tryFixing(report, unsafeIndex)

    if not isSafe and not madeSafe:
      print(f'Still unsafe ({unsafeIndex}): {report}')

    if isSafe or madeSafe:
      safe += 1


print(f'Safe reports: {safe}')
