class constants:
	NONE = 0
	X = 1
	O = 2

# function to check if there is a winner in the current board setting 
def game_status(board):
	#diagonals
	if (board[0]==constants.X and board[4]==constants.X and board[8]==constants.X):
		return constants.X
	if (board[2]==constants.X and board[4]==constants.X and board[6]==constants.X):
		return constants.X

	#horizontal
	if (board[0]==constants.X and board[1]==constants.X and board[2]==constants.X):
		return constants.X
	if (board[3]==constants.X and board[4]==constants.X and board[5]==constants.X):
		return constants.X
	if (board[6]==constants.X and board[7]==constants.X and board[8]==constants.X):
		return constants.X
	
	#vertical
	if (board[0]==constants.X and board[3]==constants.X and board[6]==constants.X):
		return constants.X
	if (board[1]==constants.X and board[4]==constants.X and board[7]==constants.X):
		return constants.X
	if (board[2]==constants.X and board[5]==constants.X and board[8]==constants.X):
		return constants.X

	#diagonals
	if (board[0]==constants.O and board[4]==constants.O and board[8]==constants.O):
		return constants.O
	if (board[2]==constants.O and board[4]==constants.O and board[6]==constants.O):
		return constants.O

	#horizontal
	if (board[0]==constants.O and board[1]==constants.O and board[2]==constants.O):
		return constants.O
	if (board[3]==constants.O and board[4]==constants.O and board[5]==constants.O):
		return constants.O
	if (board[6]==constants.O and board[7]==constants.O and board[8]==constants.O):
		return constants.O
	
	#vertical
	if (board[0]==constants.O and board[3]==constants.O and board[6]==constants.O):
		return constants.O
	if (board[1]==constants.O and board[4]==constants.O and board[7]==constants.O):
		return constants.O
	if (board[2]==constants.O and board[5]==constants.O and board[8]==constants.O):
		return constants.O

	return constants.NONE #tie or unfinished

# function to find outcome of the game by exploring all possibilities in the solution space using min-max
def minmax_tictactoe(board, turn):
    infinity = 100000000000

    def prun(board, turn):

        result = game_status(board)

        if result == 0 and check_terminal(board): return 0
        if result == 1: return 10
        if result == 2: return -10

        # if turn is X, maximising case 
        if turn == 1:
            v = 0 - infinity
            for i in range(len(board)):
                if board[i] == 0:
                    board[i] = turn
                    R_value = prun(board, 2)
                    board[i] = 0
                    if R_value > v:
                        v = R_value

        # if turn is O, minimising case
        if turn == 2:
            v = infinity
            for i in range(len(board)):
                if board[i] == 0:
                    board[i] = turn
                    R_value = prun(board, 1)
                    board[i] = 0
                    if R_value < v:
                        v = R_value
        return v 
    
    winner = prun(board, turn)
    if winner == -10: return constants.O
    if winner == 0: return constants.NONE
    if winner == 10: return constants.X

# function using alpha beta pruning to trim the solution space while using min-max 
def abprun_tictactoe(board, turn):
    infinity = 100000000000

    def prun(board, turn, alpha = -infinity, beta = infinity):

        result = game_status(board)
        
        if result == 0 and check_terminal(board): return 0
        if result == 1: return 10
        if result == 2: return -10

        # if turn is X, maximising case 
        if turn == 1:
            v = 0 - infinity
            for i in range(len(board)):
                if board[i] == 0:
                    board[i] = turn
                    R_value = prun(board, 2, alpha, beta)
                    board[i] = 0
                    if R_value > v:
                        v = R_value
                    if v >= beta:
                        return v
                    if v > alpha:
                        alpha = v

        # if turn is O, minimising case
        if turn == 2:
            v = infinity
            for i in range(len(board)):
                if board[i] == 0:
                    board[i] = turn
                    R_value = prun(board, 1, alpha, beta)
                    board[i] = 0
                    if R_value < v:
                        v = R_value
                    if v <= alpha:
                        return v
                    if v < beta:
                        beta = v  
        return v 
    
    winner = prun(board, turn)
    if winner == -10: return constants.O
    if winner == 0: return constants.NONE
    if winner == 10: return constants.X

# function to check if the board is a terminal case
def check_terminal(board):
	for i in range(len(board)):
		if board[i] == 0: return False
	return True