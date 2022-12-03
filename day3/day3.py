import string

input = open("input.txt", "r").readlines()

def get_matching_item_type(input):
  firstpart, secondpart = input[:len(input)//2], input[len(input)//2:]
  for char1 in firstpart:
    if char1 in secondpart:
      return char1

def get_group_type(group):
  for char1 in group[0]:
    if (char1 in group[1]) and (char1 in group[2]):
      return char1


def get_points_for_type(type):
  p = ord(type.lower()) - 96
  return p if type.islower() else p + 26

result = 0
result_two = 0
group = []
for line in input:
  group.append(line)
  if len(group) == 3:
    type_two = get_group_type(group)
    result_two += get_points_for_type(type_two)
    group.clear()
  type = get_matching_item_type(line)
  result += get_points_for_type(type)
print(result)
print(result_two)
  