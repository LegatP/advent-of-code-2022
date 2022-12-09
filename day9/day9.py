input = open('input.txt', 'r').readlines()

visited = {'0': {'0': True}}

# part 1
# knots = [
#   [0, 0], 
#   [0, 0],
# ]

# part 2
knots = [
  [0, 0], 
  [0, 0],
  [0, 0],
  [0, 0],
  [0, 0],
  [0, 0],
  [0, 0],
  [0, 0],
  [0, 0],
  [0, 0],
]

def make_move(x, d):
  if d == 'R':
    x[0] += 1
  if d == 'L':
    x[0] -= 1
  if d == 'U':
    x[1] += 1
  if d == 'D':
    x[1] -= 1 

def follow(head, tail):
  distanceX = head[0] - tail[0]
  distanceY = head[1] - tail[1]
  if abs(distanceX) > 1 or abs(distanceY) > 1:
    if distanceX == 2:
      make_move(tail, 'R')
      # print('R')
    if distanceX == -2:
      make_move(tail, 'L')
      # print('L')
    if distanceY == 2:
      make_move(tail, 'U')
      # print('U')
    if distanceY == -2:
      make_move(tail, 'D')
      # print('D')
    if abs(distanceX) + abs(distanceY) == 3:
      if abs(distanceX) == 2:
        if distanceY == -1:
          make_move(tail, 'D')
          # print('D')
        else:
          make_move(tail, 'U')
          # print('U')
      if abs(distanceY) == 2:
        if distanceX == -1:
          make_move(tail, 'L')
          # print('L')
        else:
          make_move(tail, 'R')
          # print('R') 


for line in input:
  direction, moves = line.strip().split(' ')

  for move in range(int(moves)):
    make_move(knots[0], direction)

    for index, knot in enumerate(knots[1:]):
      head = knots[index]
      tail = knot
      follow(head, tail)

      if index == len(knots[1:]) - 1:
        if str(tail[0]) not in visited:
          visited[str(tail[0])] = {}
        visited[str(tail[0])][str(tail[1])] = True

print(sum([len(visited[x]) for x in visited]))