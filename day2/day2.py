input = open("input.txt", "r").readlines()
LOSE = 0
DRAW = 3
WIN = 6
ROCK = "R"
PAPER = "P"
SCISSORS = "S"

def get_move(input):
  if input in ["A", "X"]:
    return ROCK
  elif input in ["B", "Y"]:
    return PAPER
  return SCISSORS

def get_desired_result(input):
  if input == "X":
    return LOSE
  elif input == "Y":
    return DRAW
  return WIN
  
def get_move_for_result(result, opponent_move):
  if result == DRAW:
    return opponent_move
  if opponent_move == SCISSORS:
    return PAPER if result == LOSE else ROCK
  elif opponent_move == PAPER:
    return ROCK if result == LOSE else SCISSORS
  return SCISSORS if result == LOSE else PAPER
  
def get_move_points(move):
  if move == ROCK:
    return 1
  elif move == PAPER:
    return 2
  return 3

def get_game_result(opponent_move, move):
  if opponent_move == move:
    return DRAW
  elif (opponent_move == ROCK and move == SCISSORS) or (opponent_move == SCISSORS and move == PAPER) or (opponent_move == PAPER and move == ROCK):
    return LOSE
  return WIN

result = 0
result_two = 0
for line in input:
  opponent_move = get_move(line[0])
  move = get_move(line[2])
  move_two = get_move_for_result(get_desired_result(line[2]), opponent_move)
  result += get_move_points(move) + get_game_result(opponent_move, move)
  result_two += get_move_points(move_two) + get_game_result(opponent_move, move_two)


print("part1: " + str(result))
print("part2: " + str(result_two))
