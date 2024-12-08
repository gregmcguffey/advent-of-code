import math

inputFile = 'input.txt'
# inputFile = 'input-test.txt'

def checkReport(report):
  isSafe = True
  unsafeIndex = None

  diffs = [level - report[i] for i, level in enumerate(report[1:])]
  # print(diffs)

  # sign of first item must be consistent for differences
  expectedSign = math.copysign(1, diffs[0])
  for i in range(len(diffs)):
    # edge i is edge between report[i] and report[i+1]
    current = diffs[i]
    safeTrend = expectedSign == math.copysign(1, current)
    magnitude = abs(current)
    safeRate = magnitude > 0 and magnitude <=3
    isSafe = isSafe and safeRate and safeTrend
    # print(f'[{i}] isSafe: {isSafe}, safeTrend: {safeTrend}, safeRate: {safeRate} ')
    if not isSafe:
      unsafeIndex = i
      break

  return isSafe, unsafeIndex


def tryFixing(report, baseIndex):
  isSafe = False

  for i in range(baseIndex - 1, baseIndex+2):
    if i < 0:
      continue
    testReport = report.copy()
    del testReport[i]
    # print(f'Modified Report to Test Again ({baseIndex}:{i}): {testReport}')
    madeSafe, _ = checkReport(testReport)
    isSafe = isSafe or madeSafe
    # print(f'Safe after try? {isSafe}')
    if madeSafe:
      # print(f'made safe ({i}): {report} -> {testReport}')
      break

  return isSafe


# safe rules
# - all increasing or all decreasing
# - differ by 1 - 3 inclusive
total = 0
safe = 0
madeSafeCount = 0
with open(inputFile, 'r') as input:
  for line in input:
    total += 1
    report = []
    for level in line.split(' '):
      report.append(int(level))

    isSafe, unsafeIndex = checkReport(report)

    if not isSafe:
      madeSafe = tryFixing(report, unsafeIndex)
      if madeSafe:
        madeSafeCount += 1

    if not isSafe and not madeSafe:
      print(f'Still unsafe ({unsafeIndex}): {report}')

    if isSafe or madeSafe:
      safe += 1


print(f'Reports Made Safe: {madeSafeCount}')
print(f'Safe reports: {safe}')
print(f'Total Reports: {total}')
