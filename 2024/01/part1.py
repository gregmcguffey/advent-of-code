
left = []
right = []
with open('input-original.txt', 'r') as input:
  for line in input:
    x, y = line.split('   ')
    left.append(int(x))
    right.append(int(y))

left.sort()
right.sort()
distance = 0

for i in range(len(left)):
  x = left[i]
  y = right[i]
  distance += abs(x - y)


print(f'Total distance: {distance}')