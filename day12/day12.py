input = open('input.txt', 'r').readlines()

map = []
start = [0,0]
goal = [0,0]
goalAs = []

def getElevation(position, map):
  x, y = position
  if x >= 0 and x < len(map) and y >= 0 and y < len(map[x]):
    return map[x][y]
  return '/'

def canMoveTo(current, next, map):
  x1, y1 = current
  x2, y2 = next
  startElevation = getElevation(current, map)
  goalElevation = getElevation(next, map)
  if startElevation == 'S':
    startElevation = 'a'
  if goalElevation == 'E':
    goalElevation = 'z'
  if startElevation != '/' and goalElevation != '/' and ord(startElevation) - ord(goalElevation) >= -1 and not(x1 == x2 and y1 == y2):
    return True

def find_shortest(start, goal, map):
  queue = [start]
  path_length = 0

  while queue:
    level = len(queue)
    for _ in range(level):
      current = queue.pop(0)
      x, y = current

      if map[x][y] == 'E':
        return path_length

      next_moves = []
      for xChange in [-1, 1]:
        next = [x + xChange, y]
        if canMoveTo(current, next, map):
          next_moves.append(next)

      for yChange in [-1, 1]:
        next = [x, y + yChange]
        if canMoveTo(current, next, map):
          next_moves.append(next)

      for next in next_moves:
        queue.append(next)
      map[x][y] = '/'
    path_length += 1

for lineIndex, line in enumerate(input):
  line = line.strip()
  row = [*line]
  for col,letter in enumerate(row):
    if letter == 'a':
      goalAs.append([lineIndex, col])
  if 'S' in row:
    start = [lineIndex, row.index('S')]
  if 'E' in row:
    goal = [lineIndex, row.index('E')]
  map.append(row)

print(find_shortest(start, goal, [row[:] for row in map]))

shortest_alt = []

for a in goalAs:
  path = find_shortest(a, goal, [row[:] for row in map])
  if path:
   shortest_alt.append(path)
shortest_alt.sort()
print(shortest_alt[:1][0])
