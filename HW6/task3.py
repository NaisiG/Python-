import random

def is_valid_position(row, col, n):
  for i in range(n):
    if row == i or col == i or abs(row - i) == abs(col - i):
      return False
    return True

board_list = []
for _ in range(4):
  board = []
  coordinates = []

n = 8

for _ in range(n): 
    while True: 
        row = random.randint(0, n - 1) 
        col = random.randint(0, n - 1) 
         
        if is_valid_position(row, col, n): 
            break 
    board.append([row, col]) 
     
board_list.append(board)
