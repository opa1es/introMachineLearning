import copy
import random


class NQPosition:

    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.queens = [-1] * boardSize
        self.board = [['_' for x in range(boardSize)] for y in range(boardSize)]

        self.generateQueensOnBoard(boardSize)

        for e in range(boardSize):
            print(self.board[e])

    def generateQueensOnBoard(self, boardSize):
        for e in range(boardSize):
            self.queens[e] = random.randint(0, boardSize - 1)
        i = 0

        for u in range(boardSize):
            self.board[self.queens[i]][u] = "O"
            i += 1

    def conflictsValue(self):
        value = 0
        for i in range(len(self.queens)):
            for j in range(i + 1, len(self.queens)):
                if self.queens[i] == self.queens[j] or \
                        self.queens[i] == self.queens[j] + (j - i) or \
                        self.queens[i] == self.queens[j] - (j - i):
                    value += 1
        return value

    def makeMove(self, move):
        self.board[move[1]][move[0]] = 'O'
        self.board[self.queens[move[0]]][move[0]] = '_'
        self.queens[move[0]] = move[1]

    def generateFreeXY(self):
        i = random.randint(0, self.boardSize - 1)
        j = random.randint(0, self.boardSize - 1)
        while self.queens[i] == j:
            i = random.randint(0, self.boardSize - 1)
            j = random.randint(0, self.boardSize - 1)
        return i, j

    def bestMove(self):
        potentialMoves = {}
        for g in range(self.boardSize):
            i, j = self.generateFreeXY()
            copiedObject = copy.deepcopy(self)
            copiedObject.makeMove((i, j))
            potentialMoves[(i, j)] = copiedObject.conflictsValue()

        move = min(potentialMoves, key=potentialMoves.get)
        return move, potentialMoves[move]


def hill_climbing(pos):
    curr_value = pos.conflictsValue()
    while True:
        move, new_value = pos.bestMove()
        if curr_value == 0:
            return pos, curr_value
        else:
            curr_value = new_value
            pos.makeMove(move)


pos = NQPosition(8)  # test with the tiny 4x4 board first
print("Initial position value", pos.conflictsValue())
best_pos, best_value = hill_climbing(pos)
print("Final value", best_value)
for e in pos.board:
    print(e)
# if best_value is 0, we solved the problem
