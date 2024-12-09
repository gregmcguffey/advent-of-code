import re

inputFile = 'input.txt'


def getInput():
  mulPattern = r'(mul\((?P<lhs>\d{1,3}),(?P<rhs>\d{1,3})\))'

  doPattern=r"(^.+?(?=don't\(\)))|(do\(\).+?(?=don't\(\)))|(do\(\).+?$)"

  enabledSets = 0
  enabledCommands = 0
  sum = 0
  full = ''
  with open(inputFile, 'r') as input:
    mulEnabled = True
    for line in input:
      # make into one big file, not ideal
      full += line[:-1]

    for match in re.finditer(doPattern, full):
      enabledSets += 1
      doCommands = match.group()
      for mulMatch in re.finditer(mulPattern, doCommands):
        enabledCommands += 1
        values = mulMatch.groupdict()
        lhs = int(values["lhs"])
        rhs = int(values["rhs"] )
        value = lhs * rhs
        sum += value

  return [enabledSets, enabledCommands, sum]


enabledSets, enabledCommands, sum = getInput()

print(f'Total enabled command sets: {enabledSets}')
print(f'Total enabled command: {enabledCommands}')
print(f'Sum: {sum}')

