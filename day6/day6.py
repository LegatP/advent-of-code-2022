input = open("input.txt", "r").readline()

# part one => 4
# part two => 14
unique_count=14

for x in range(len(input) - (unique_count-1)):
  differrent = input[x:x+unique_count]
  if len(set(list(differrent))) == unique_count:
    print(x + unique_count)
    break