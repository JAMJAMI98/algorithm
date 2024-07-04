def poly(board):
  board = board.replace('XXXX', 'AAAA')
  board = board.replace('XX', 'BB')

  if 'X' in board:
    return -1  
  return board

board = input().strip()
result = poly(board)
print(result)