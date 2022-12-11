input = open('input.txt', 'r').readlines()


result = 0
cycle = 0
register = 1
drawing = []

def should_add(cycle):
  return cycle - 20 == 0 or ((cycle - 20) % 40) == 0

def draw(cycle, register):
  if cycle % 40 in [register - 1, register, register + 1]:
    drawing.append('#')
  else:
    drawing.append('.')


for line in input:
  line = line.strip()
  instruction = line
  draw(cycle, register)
  cycle += 1
  if should_add(cycle):
    result += register * cycle
  if line != 'noop':
    draw(cycle, register)
    cycle += 1
    if should_add(cycle):
      result += register * cycle
    register += int(line.split(' ')[1])

print(result)
for row in [drawing[i:i + 40] for i in range(0, len(drawing), 40)]:
  print(''.join(row))