import math

def checkReport(report):
  isSafe = True
  unsafeIndex = None

  diffs = [level - report[i] for i, level in enumerate(report[1:])]

  # sign of first item must be consistent for differences
  expectedSign = math.copysign(1, diffs[0])
  for i in range(len(diffs)):
    # diff i is edge between report[i] and report[i+1]
    current = diffs[i]
    safeRate = expectedSign == math.copysign(1, current)
    magnitued = abs(current)
    safeTrend = magnitued > 0 and magnitued <=3
    isSafe = isSafe and safeRate and safeTrend
    if not isSafe:
      unsafeIndex = i
      break

  return isSafe

safe = 0
with open('input.txt', 'r') as input:
  for line in input:
    report = []
    for level in line.split(' '):
      report.append(int(level))

    isSafe = checkReport(report)

    if isSafe:
      safe += 1


print(f'Safe reports: {safe}')
