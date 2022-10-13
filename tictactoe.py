"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    x = 0;
    o = 0;
    for row in board:
        for item in row:
            if item == X:
                x += 1
            elif item == O:
                o += 1
    return O if x > o else X


def actions(board):
    tuples = [];
    for indexX, row in enumerate(board):
        for indexY, item in enumerate(row):
            if item == EMPTY:
                tuples.append([indexX, indexY])
    return tuples


class IllegalMoveExcepltion(Exception):
    """Requested move is not valid"""
    pass

def result(board, action):
    if (board[action[0]][action[1]] != EMPTY):
        raise IllegalMoveExcepltion
    currentPlayer = player(board)
    newBoard = [];
    for row in board:
        newBoard.append(row.copy())
    newBoard[action[0]][action[1]] = currentPlayer
    return newBoard

def winner(board):
    cols = len(board[0])
    rows = len(board)
    
    for row in range(rows):
        for col in range(cols):
            cell = board[row][col]
            if cell:
                # Checking row
                if (col < cols-2 and board[row][col+1] == cell and board[row][col+2] == cell):
                    return cell
                # Checking col
                if (row < rows-2 and board[row+1][col] == cell and board[row+2][col] == cell):
                    return cell
                # Checking forward diagonale
                if (col < cols-2 and row < rows-2 and board[row+1][col+1] == cell and board[row+2][col+2] == cell):
                    return cell
                # Checking back diagonale
                if (col > 1 and row < rows-2 and board[row+1][col-1] == cell and board[row+2][col-2] == cell):
                    return cell
    return EMPTY

def terminal(board):
    return bool(winner(board)) or len(actions(board)) == 0

def utility(board):
    theWinner = winner(board)
    return 1 if theWinner == X else (-1 if theWinner == O else 0)


def minimax(board):
    if (terminal(board)):
        return None
    currentPlayer = player(board)
    best = [0, None]
    for move in actions(board):
        newBoard = result(board, move)
        score = minimax_score(newBoard)
        if (best[1] is None) or (currentPlayer == X and score > best[0]) or (currentPlayer == O and score < best[0]):
            best = [score, move]
    return best[1]

def minimax_score(board):
    if terminal(board):
        theWinner = winner(board)
        if theWinner:
            return 1 if theWinner == X else -1
        else:
            return 0

    scores = []
    for move in actions(board):
        newBoard = result(board, move)
        scores.append(minimax_score(newBoard))

    return max(scores) if player(board) == X else min(scores)
  
