class Node:
  def __init__(self, parent, name, size):
    self.parent = parent
    self.name = name
    self.children = None
    self.size = size

  def add_child(self, child):
    if self.children is None:
      self.children = []
    self.children.append(child)

  def print(self):
    for x in range(self.depth()):
      print(' ' , end="")
    print(self.name)
    if self.children: 
      for c in self.children:
        c.print()

  def depth(self):
    if self.parent == None:
      return 0
    return 1 + self.parent.depth()

  def get_size(self):
    if self.size in None:
      sum = 0
      for c in self.children:
        sum += c.size
      return sum
    return self.size

input = open("input.txt", "r").readlines()
root = Node(None, '/', None) 
current = root
for l in input:
  line = l.strip()
  if line == '$ ls' or line == '$ cd /':
    continue
  elif line == '$ cd ..':
    current = current.parent
  elif line[:4] == '$ cd':
    child = list(filter(lambda x: x.name == line[5:], current.children))[0]
    current = child
  elif line[:3] == 'dir':
    dir = Node(current, line[4:], None)
    current.add_child(dir)
  else:
    size = line.split(' ')[0]
    name = line.split(' ')[1]
    file = Node(current, name, int(size))
    current.add_child(file)

# root.print()

result = 0
result_two = float("inf")
needed_space = None

def recursive_size(current_node, size):
  if current_node.children is None:
    return current_node.size
  size = 0
  for c in current_node.children:
    size += recursive_size(c, size)
  if size <= 100000:
    global result
    result += size
  global result_two
  if needed_space is not None and size >= needed_space and size < result_two:
    result_two = size
  return size

total_used_space = recursive_size(root, 0)
available_space = 70000000 - total_used
needed_space = 30000000 - available_space
recursive_size(root, 0)
print(result)
print(result_two)
    

  

  
  
  











