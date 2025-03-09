# python3 -i v2.TicTacToe.GHU.py

board = [['-'] * 3 for i in range(3)]
space = """


        """

def tic_tac_toe():
    # clears board, begins a new game of tic tac toe
    print(space)
    global board
    board = [['-'] * 3 for i in range(3)]
    print('Game Begin!')
    print('rows can only be top, middle, or bottom')
    print('columns can only be left, middle, or right')
    print_board(board)
    player_row('x')

def player_row(x_o):
    # Prompts player for valid row index
    row_entry = input(f"Player {x_o}, which row? ")
    if row_entry not in ['top','middle','bottom']:
        print(space)
        print("ERROR: row entries may only be top, middle, or bottom!")
        print_board(board)
        return player_row(x_o)
    else:
        return player_col(x_o, row_entry)

def player_col(x_o, row_entry):
    # Prompts player for valid column index
    column_entry = input(f"Player {x_o}, which column? ")
    if column_entry not in ['left','middle','right']:
        print(space)
        print("ERROR: column entries may only be left, middle, or right!")
        print_board(board)
        print(f"Player {x_o}, which row? " + row_entry)
        return player_col(x_o, row_entry)
    else:
        return play(x_o, row_entry, column_entry)

def play(x_o, row_entry, column_entry):
    # makes a tic tac toe play
    row, column = row_sort(row_entry), column_sort(column_entry)
    global board
    if board[row][column] != '-':
        # checks whether index is already occupied
        print(space)
        print('ERROR: cannot override an entry. choose again!')
        print_board(board)
        return player_row(x_o)
    board[row][column] = x_o
    # index is set to x_o
    if win_check(board, x_o) == True or board_full(board):
        print(space)
        if win_check(board, x_o) == True:
            print(f'Player {x_o} wins!')
        elif board_full(board):
            print('Tie!')
        print_board(board)
        input('Press Enter to start another game! ')
        tic_tac_toe()
    else: 
        print(space)
        print('Next Player\'s turn!')
    print_board(board)
    # switches players
    if x_o == 'x':
        x_o = 'o'
    elif x_o == 'o':
        x_o = 'x'
    player_row(x_o)

def board_full(board):
    # checks whether board is full
    for row in board:
        if '-' in row:
            return False
    return True

def win_check(board, x_o):
    # checks whether a player has won the tic tac toe game
    board_dim = range(len(board))
    for row in board:
        # checks for row win
        if all(entry == x_o for entry in row):
            return True 
    for col_num in board_dim:
        # checks for column win
        if all(row[col_num] == x_o for row in board):
            return True
    if all(board[diagonal_entry][diagonal_entry] == x_o for diagonal_entry in board_dim):
        # checks for diagonal win \
        return True
    if all(board[diagonal_entry][2-diagonal_entry] == x_o for diagonal_entry in board_dim):
        # checks for reverse diagonal win /
        return True

def row_sort(row_entry):
    # assigns row entry to respective row index
    if row_entry == 'top':
        return 0
    elif row_entry == 'middle':
        return 1
    elif row_entry == 'bottom':
        return 2

def column_sort(column_entry):
    # assigns column entry to respective column index
    if column_entry == 'left':
        return 0
    elif column_entry == 'middle':
        return 1
    elif column_entry == 'right':
        return 2

def print_board(board):
    # prints the board out in readable format
    for rows in board:
        line = ""
        for entry in rows:
            line += f" {entry}"
        print(line)

input("Press Enter to start Tic Tac Toe! ")
tic_tac_toe()