import re

inputFile = 'input.txt'
# inputFile = 'input-test.txt'


def getInput():
  mulPattern = r'(mul\((?P<lhs>\d{1,3}),(?P<rhs>\d{1,3})\))'
  total = 0
  sum = 0
  with open(inputFile, 'r') as input:
    for line in input:
      for match in re.finditer(mulPattern, line):
        total += 1
        values = match.groupdict()
        lhs = int(values["lhs"])
        rhs = int(values["rhs"] )
        value = lhs * rhs
        sum += value

  return [total, sum]


total, sum = getInput()

print(f'Sum: {sum}')
print(f'Total commands: {total}')