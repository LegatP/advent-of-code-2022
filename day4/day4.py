input = open("input.txt", "r").readlines()

def is_subtask(a, b):
  a1 = int(a.split('-')[0])
  a2 = int(a.split('-')[1])
  b1 = int(b.split('-')[0])
  b2 = int(b.split('-')[1])
  if a1 <= b1 and a2 >= b2:
    return True
  return False


def overlaps(a,b):
  a1 = int(a.split('-')[0])
  a2 = int(a.split('-')[1])
  b1 = int(b.split('-')[0])
  b2 = int(b.split('-')[1])
  if a2 >= b1 and a1 <= b2:
    return True
  return False


result = 0
result_two = 0
for line in input:
  a = line.split(',')[0]
  b = line.split(',')[1]
  if overlaps(a,b):
    result_two += 1
    if is_subtask(a,b) or is_subtask(b,a):
      result += 1 

print(result)
print(result_two)