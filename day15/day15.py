input = open('input.txt', 'r').readlines()

def manhatten(a, b):
  x1, y1 = a
  x2, y2 = b
  return abs(x1 - x2) + abs(y1 - y2)

bs_pairs = []

for line in input:
  sensor, beacon = line.strip()[10:].split(": ")

  s_x, s_y = map(lambda x: int(x[2:]), sensor.split(", "))
  b_x, b_y = map(lambda x: int(x[2:]), beacon[21:].split(", "))

  bs_pairs.append([(s_x, s_y), (b_x, b_y)])

bs_blocks = {}
target_y = 2000000

for pair in bs_pairs:
  s, b = pair
  s_x, s_y = s
  b_x, b_y = b
  manhatten_d = manhatten(s, b)
  queue = [(s_x , target_y)]
  visisted = {}

  while queue:
    current = queue.pop(0)
    if manhatten(s, current) >= manhatten_d:
      break
    for xChange in [-1, 1]:
      new = (current[0] + xChange, current[1])
      if new not in visisted:
        queue.append(new)
        visisted[new] = True
  for s in visisted.keys():
    bs_blocks[s] = True

print(len(bs_blocks) - 1)

# x_max = 20
# y_max = 20
x_max = 4000000
y_max = 4000000

posible_positions = []

# needs optimizing
for p in bs_pairs:
  s, b = p
  s_x, s_y = s
  b_x, b_y = b
  m = manhatten(s, b) + 1

  for x in range(-m,m):
    y1 = abs(m - x)
    y2 = -abs(m - x)
    for p in [(s_x + x,s_y + y1), (s_x + x,s_y + y2)]:
      pos_x, pos_y = p
      if pos_x < 0 or pos_y < 0 or pos_x > x_max or pos_y > y_max:
        continue
      if (pos_x, pos_y) in [b for (s, b) in bs_pairs]:
        continue
      else:
        posible_position = (pos_x, pos_y)
        reaches = []
        for p1 in bs_pairs:
          # print(p)
          s, b = p1
          m1 = manhatten(s, b)
          in_reach = m1 >= manhatten(posible_position, s)
          reaches.append(True) if in_reach else reaches.append(False)
        if True not in reaches:
          print(posible_position[0] * 4000000 + posible_position[1])
          exit(0) 