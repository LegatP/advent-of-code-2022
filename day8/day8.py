from functools import reduce

input = open("input.txt", "r").readlines()

forest = []
visible_map = {}

for line in input:
  forest.append([*line.strip()])

visible = 0
max_scenic_score = 0

for row_index, row in enumerate(forest[1:-1]):
  inner_row = row[1:-1]
  for col_index, tree in enumerate(inner_row):
    left = row[:col_index + 1]
    right = row[col_index + 2:]

    left.reverse()

    col = [row[col_index + 1] for row in forest]
    bot = col[row_index + 2:]
    top = col[:row_index + 1]

    top.reverse()

    direction_not_visible_count = 0
    scenic_scores = [1, 1, 1, 1]
    for i, direction in enumerate([left, right, top, bot]):
      for x, compare_tree in enumerate(direction):
        if int(compare_tree) >= int(tree):
          scenic_scores[i] = x + 1
          direction_not_visible_count += 1
          break
        scenic_scores[i] = x + 1
    product = reduce(lambda x,y: x*y, scenic_scores)
    if product > max_scenic_score:
      max_scenic_score = product 
      
    if direction_not_visible_count < 4:
      visible +=1

visible += 4 * (len(forest) - 1)
print(visible)
print(max_scenic_score)