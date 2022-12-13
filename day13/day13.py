from functools import cmp_to_key

input = open('input.txt', 'r').readlines()

pairs = []

def parse_line(line):
  current = []
  while line:
    char = line.pop(0)
    if char == ',':
      continue
    elif char == ']':
      return current
    elif char == '[':
      inner = parse_line(line)
      current.append(inner)
    else:
      while line and line[0] not in [',', '[', ']']:
        c = line.pop(0)
        char = char + c
      current.append(int(char))
  return current

def is_right(s1, s2):
  for i in range(max(len(s1), len(s2))):
    if i >= len(s1):
      return True
    if i >= len(s2):
      return False
    
    v1, v2 = s1[i], s2[i]

    if isinstance(v1, int) and isinstance(v2, int):
      if v1 != v2:
        return True if v2 > v1 else False
    elif not isinstance(v1, int) and not isinstance(v2, int):
      value = is_right(v1, v2)
      if value != None:
        return value
    else:
      value = is_right([v1], v2) if isinstance(v1, int) else is_right(v1, [v2])
      if value != None:
        return value
  return None


for i, _ in enumerate(input[::3]):
  p1 = parse_line([*input[i * 3].strip()])
  p2 = parse_line([*input[i * 3 + 1].strip()])
  pairs.append([p1[0], p2[0]])

indexes = []
for i, p in enumerate(pairs):
  if is_right(*p):
    indexes.append(i + 1)

print(sum(indexes))

pairs.append([[[2]], [[6]]])

s = sorted([y for x in pairs for y in x], key=cmp_to_key(lambda x1, x2: -1 if is_right(x1, x2) else 1))
print((s.index([[2]]) + 1) * (s.index([[6]]) + 1))