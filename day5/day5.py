import re

input = open("input.txt", "r").readlines()

stacks = [[] for i in range(int(len(input[0])/4))]
read_all_stacks = False
# Defines which part of the puzzle will be solved
is_part_two = True

for line in input:
  if len(line.strip()) == 0 or line[1] == '1':  
    read_all_stacks = True
    continue
  if not read_all_stacks:
    boxes = [line[i:i+4] for i in range(0, len(line), 4)]
    for index, box in enumerate(boxes):
      if not len(box[1].strip()) == 0:
        stacks[index].append(box[1])
  else:
    _, move, move_from, to = re.split('move | from | to ', line)
    move_from, to = map(lambda x: int(x) - 1, [move_from, to])
    move = int(move)
    to_add = stacks[move_from][:min(move, len(stacks[move_from]))]
    if not is_part_two:
      to_add.reverse()
    stacks[to] = to_add + stacks[to]
    del stacks[move_from][:min(move, len(stacks[move_from]))]

result = map(lambda s: s[0], stacks)
print(''.join(list(result)))    