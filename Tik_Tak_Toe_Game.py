"""
1 make board
2 display board
3 play game
4 check win
    check rows
    check columns
    check diagonals
5 check tie
6 flip player
"""

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-', ]
# ---------------GLOBAL VARIABLES-----------------

# if game is still going
game_is_going = True

# who's the winner
winner = None

# who's turn is now
current_player = 'X'


def display_board():
    print('    ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('    ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('    ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print()


def play_game():
    display_board()

    while game_is_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()
        # declare the result
        if winner == 'X' or winner == 'O':
            print(winner, 'won the match.')
        elif winner == 'No one':
            print('OOPS! Tie.')


def handle_turn(player):
    print(player + 's turn.')

    position = int(input('Enter a number from 1-9: '))
    # chek for valid input
    valid = False
    while not valid:
        while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            position = int(input('INVELID INPUT.Enter a number from 1-9: '))

        position = position - 1

        if board[position] == '-':
            valid = True
        else:
            print('you can not write here !')

    board[position] = player
    display_board()


def check_if_game_over():
    check_for_win()
    check_if_tie()


def check_for_win():
    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    return


def check_rows():
    global game_is_going
    # check if any row has same value
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'
    # if any row has same value, end the game and declare winner
    if row_1 or row_2 or row_3:
        game_is_going = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    global game_is_going
    # check if any column has same value
    col_1 = board[0] == board[3] == board[6] != '-'
    col_2 = board[1] == board[4] == board[7] != '-'
    col_3 = board[2] == board[5] == board[8] != '-'
    # if any row has same value, end the game and declare winner
    if col_1 or col_2 or col_3:
        game_is_going = False

    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return


def check_diagonals():
    global game_is_going
    # check if any row has same value
    dia_1 = board[0] == board[4] == board[8] != '-'
    dia_2 = board[2] == board[4] == board[6] != '-'
    # if any row has same value, end the game and declare winner
    if dia_1 or dia_2:
        game_is_going = False

    if dia_1:
        return board[0]
    elif dia_2:
        return board[2]
    return


def check_if_tie():
    global game_is_going
    global winner
    if '-' not in board:
        game_is_going = False
        winner = 'No one'
    return


def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return


play_game()
