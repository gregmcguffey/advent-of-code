
left = []
right = []
with open('input-original.txt', 'r') as input:
  for line in input:
    x, y = line.split('   ')
    left.append(int(x))
    right.append(int(y))

left.sort()
right.sort()

scores = {}

for i in range(len(left)):
  x = left[i]
  if x not in scores:
    leftCount = left.count(x)
    rightCount = right.count(x)
    score = x * leftCount * rightCount
    scores[x] = score


print(f'Total similarity score: {sum(scores.values())}')