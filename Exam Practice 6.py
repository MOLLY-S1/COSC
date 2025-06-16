"""Question 20"""


def num_rook_moves(board):
    """f"""
    width = len(board[0])
    height = len(board)

    # finding rook position
    rook = []
    for i in range(height):
        if 'R' in board[i]:
            x = board[i].index('R')
            y = i
            position = (x, y)
            rook.append(position)

    # Finding other pieces
    pieces = []
    for i in range(height):
        for j in range(width):
            if board[i][j] == 'X':
                x = j
                y = i
                position = (x, y)
                pieces.append(position)

    # Distance to piece
    moves = 0
    r_x, r_y = rook[0]

    # moves right
    for rx in range(r_x + 1, width):
        if (rx, r_y) in pieces:
            break
        moves += 1

    # moves left
    for lx in range(r_x - 1, -1, -1):
        if (lx, r_y) in pieces:
            break
        moves += 1

    # moves up
    for uy in range(r_y - 1, -1, -1):
        if (r_x, uy) in pieces:
            break
        moves += 1

    # moves down
    for dy in range(r_y + 1, height):
        if (r_x, dy) in pieces:
            break
        moves += 1

    return moves


board = [['-', '-', '-', '-', '-', 'X', '-', '-'],
         ['R', '-', '-', '-', '-', '-', 'X', '-'],
         ['-', '-', '-', 'X', 'X', '-', '-', '-'],
         ['X', '-', '-', '-', '-', '-', '-', '-'],
         ['-', 'X', '-', 'X', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', 'X', '-', '-'],
         ['-', '-', '-', 'X', '-', 'X', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-', '-']]

print(num_rook_moves(board))
