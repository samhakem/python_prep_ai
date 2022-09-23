EMPTY = '-'
PLAYER_X = 'X'
PLAYER_O = 'O'

N_FIELDS = 9


def print_board(board):
    """
    Prints the current board in readable form to the screen
    :param board: list of length N_FIELDS with all board elements representing the current game state
    :return: (No return value)
    """

    # TODO print the tictactoe board to console
    # Hint: You can access the first position of the board by "board[0]"

    # Manual method
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-----')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-----')
    print(board[6] + '|' + board[7] + '|' + board[8])


def perform_move(player, position, board):
    """
    Places the piece for a player on the given position of the board
    :param player: the player which performs the move
    :param position: the position where to place the stone (0-8)
    :param board: list of length N_FIELDS with all board elements representing the current game state
    :return: board after move was performed
    """

    # TODO place the piece on the given position of the board
    # Hint: assign "player" to the given position in the board
    board[position] = player


    # TODO return updated board
    return board


def board_full(board):
    """
    Checks if there is an empty spot on the board
    :param board: list with all board elements
    :return: True if there is no empty spot otherwise False
    """

    for i in board:
        if i == '-':
            return False
    return True

    # TODO return True if the board only contains "PLAYER_X" and "PLAYER_O" symbols else False
    # Hint: Look for the "EMPTY"-symbol in the list


def has_won(board, player):
    """
    Check if there are three equal pieces for this player in some row, column or one of the two diagonals

    :param board: list of length N_FIELDS with all board elements representing the current game state
    :param player: symbol of player that should be checked
    :return: True if three pieces in a row
    """

    # TODO check all rows for a winner
    if board[0:3] == [player] * 3:
        return True
    if board[3:6] == [player] * 3:
        return True
    if board[6:9] == [player] * 3:
        return True
    if board[0::3] == [player] * 3:
        return True
    if board[1::3] == [player] * 3:
        return True
    if board[2::3] == [player] * 3:
        return True
    if board[0::4] == [player] * 3:
        return True
    if board[2:7:2] == [player] * 3:
        return True

    # TODO check all columns for a winner

    # TODO check both diagonals for a winner

    # TODO return True if somebody has won, otherwise False
    return False

def game_over(board):
    """
    Checks if the game is over, i.e., no more moves are possible
    :param board: list of length N_FIELDS with all board elements representing the current game state
    :return: True if the game is over (no more empty pieces left or one of the players won the game otherwise False
    """

    # TODO return True if the game is over else False
    # Hint: You need to check if the board is full or if PLAYER_X or PLAYER_O has won.
    # Try to reuse some functions from above.
    if has_won(board, PLAYER_X):
        return True
    if has_won(board, PLAYER_O):
        return True

    if board_full(board):
        return True

def valid_move(user_in, board):
    """
    Checks whether the input of the user is a valid move.
    A move is valid if it is a number between 0 and 8 (inclusive) and if the position on the board is empty.
    :param user_in: string input of the user
    :param board: list of length N_FIELDS with all board elements representing the current game state
    :return: integer between 0-8 indicating a valid position where the piece should be placed otherwise -1
    """

    # TODO optional check if the input is a valid integer number
    # Hint: Checkout the isnumeric() function https://www.programiz.com/python-programming/methods/string/isnumeric
    if user_in.isnumeric():
        # TODO cast the user input to an integer number
        p_move = int(user_in)
        # TODO check if the move is valid
        # Hint: A move is valid if the input is between 0 and 8 and if the position on the board contains the "EMPTY"-symbol
        if p_move >= 0 and p_move <= 8:
            if board[p_move] == '-':
                return p_move

    return -1

    # TODO return the number indicating the valid move or -1 if the move is not valid


def init_board():
    """
    Initializes the game board
    :return: list of length N_FIELDS filled with the EMPTY symbol representing the board
    """
    board = []
    for x in range(N_FIELDS):
        board.append(EMPTY)
    return board


def winner(board):
    """
    Prints the outcome of the game to the console. Either PLAYER_X or PLAYER_O has won or it is a tie.
    :param board: list of length N_FIELDS with all board elements representing the current game state
    :return: (no return value)
    """
    if has_won(board, PLAYER_X):
        print('Player X won!')
    elif has_won(board, PLAYER_O):
        print('Player O won!')
    elif board_full(board):
        print('Tie!')


def get_valid_moves(board):
    """
    Get all valid moves for the current game state
    :param board: list of length N_FIELDS with all board elements representing the current game state
    :return: list off all possible moves, i.e., all position of the board that are filled with EMPTY
    """

    valid_moves = []
    for i in range(N_FIELDS):
        if board[i] == EMPTY:
            valid_moves.append(i)

    return valid_moves

