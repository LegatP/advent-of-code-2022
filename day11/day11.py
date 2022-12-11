import math

input = open('input.txt', 'r').readlines()

class Monkey:
  
  def __init__(self, items, operation, operation_number, test_division, assignments):
    self.items = items
    self.operation = operation
    self.operation_number = operation_number
    self.test_division = test_division
    self.assignments = assignments
    self.inspected = 0

  def print(self):
    print('Monkey')
    print(self.items)
    print(self.operation)
    print(self.operation_number)
    print(self.test_division)
    print(self.assignments)

  def play_turn(self, monkeys):
    self.inspected += len(self.items)

    while self.items:
      worry_level = self.items.pop(0)
      number = worry_level if self.operation_number == 'old' else int(self.operation_number)

      if self.operation == '+':
        worry_level += number
      else:
        worry_level *= number
      # uncomment next line for part 1
      # worry_level = math.floor(worry_level / 3) 

      # part 2 optimization
      worry_level = worry_level % math.lcm(*[m.test_division for m in monkeys])

      assign_to = self.assignments[0] if worry_level % self.test_division == 0 else self.assignments[1]
      monkeys[assign_to].items.append(worry_level)



monkeys = []

for index, line in enumerate(input[::7]):
  items = list(map(int, input[index * 7 + 1][18:].split(', ')))
  operation, operation_number = input[index * 7 + 2][23:].strip().split(' ')
  test_division = int(input[index * 7 + 3][21:])
  a1 = int(input[index * 7 + 4][29:])
  a2 = int(input[index * 7 + 5][30:])
  monkeys.append(Monkey(items, operation, operation_number, test_division, [a1, a2]))
  

for round in range(10000):
  for monkey in monkeys:
    monkey.play_round(monkeys)

sorted = [monkey.inspected for monkey in monkeys]
sorted.sort(reverse=True)
print(sorted)
print(sorted[0] * sorted[1])
