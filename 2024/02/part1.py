# from multiprocessing import Pool

def getDiff(v1, v2):
  if v1 == None or v2 == None:
    return None
  return v1 - v2


def getDirection(diff):
  if diff == None:
    return None
  return 'asc' if diff >= 0 else 'desc'


# safe rules
# - all increasing or all decreasing
# - differ by 1 - 3 inclusive
safe = 0
with open('input.txt', 'r') as input:
  for line in input:
    report = []
    for level in line.split(' '):
      report.append(int(level))

    size = len(report)
    isSafe = True

    for i in range(size):
      current = report[i]
      prev =  report[i-1] if i > 0 else None
      next = report[i+1] if i < size - 1 else None
      lastDiff = getDiff(current, prev)
      diff = getDiff(next, current)
      lastDirection = getDirection(lastDiff)
      currentDirection = getDirection(diff)
      safeTrend = lastDirection == None or currentDirection == None or lastDirection == currentDirection
      safeRate = diff == None or (abs(diff) > 0 and abs(diff) <=3)
      isSafe = isSafe and safeTrend and safeRate
      if not isSafe:
        break

    if isSafe:
      safe += 1


print(f'Safe reports: {safe}')
