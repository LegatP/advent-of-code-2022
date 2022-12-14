input = open ('input.txt', 'r').readlines()

rocks = {}

for line in input:
  ranges = line.strip().split(' -> ')
  for i, r in enumerate(ranges[1:]):
    fromTo = [list(map(int, ranges[i].split(','))), list(map(int, r.split(',')))]
    if fromTo[0][0] != fromTo [1][0]:
      x1, x2 = fromTo[0][0], fromTo[1][0]
      x1, x2 = sorted([x1, x2])
      for i in range(x1,x2 + 1,1):
        rock = (i, fromTo[0][1])
        rocks[rock] = True
    else:
      y1, y2 = fromTo[0][1], fromTo[1][1]
      y1, y2 = sorted([y1, y2])
      for i in range(y1, y2 + 1, 1):
        rock = (fromTo[0][0], i)
        rocks[rock] = True

lowest_rock = None
for r in rocks.keys():
  if lowest_rock is None or lowest_rock[1] < r[1]:
    lowest_rock = r

sands = 0
add_more_sand = True
blocks = rocks.copy()

while add_more_sand:
  sand = (500, 0)
  sands += 1
  while True:
    x, y = sand
    if sand[1] > lowest_rock[1]:
      add_more_sand = False
      break
    elif (x,y+1) not in blocks:
      sand = (x, y + 1)
    elif (x-1, y+1) not in blocks:
      sand = (x-1, y+1)
    elif (x+1, y+1) not in blocks:
      sand = (x+1, y+1)
    else:
      blocks[sand] = True
      break

print(sands -1)

sands = 0
add_more_sand = True

while add_more_sand:
  sand = (500, 0)
  sands += 1
  while True:
    x, y = sand
    if sand[1] + 1 == lowest_rock[1] + 2:
      rocks[sand] = 1
      break
    elif (x, y+1) not in rocks:
      sand = (x, y + 1)
    elif (x-1, y+1) not in rocks:
      sand = (x-1, y+1)
    elif (x+1, y+1) not in rocks:
      sand = (x+1, y+1)
    elif sand == (500,0):
      add_more_sand = False
      break
    else:
      rocks[sand] = 1
      break

print(sands)


