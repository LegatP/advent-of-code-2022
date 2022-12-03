input = open("input.txt", "r").readlines()
top_three_calories = [0,0,0]
current_calories = 0
for line in input:
  if len(line.strip()) == 0:
    if current_calories > min(top_three_calories):
      min_value_index = top_three_calories.index(min(top_three_calories))
      top_three_calories[min_value_index] = current_calories
    current_calories = 0
  else:
    current_calories += int(line)

print("part1: " + str(max(top_three_calories)))
print("part2: " + str(sum(top_three_calories)))
  