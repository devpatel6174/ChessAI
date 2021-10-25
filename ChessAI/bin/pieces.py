import copy
import pygame
from constants import WHITE, BLACK, SQUARESIZE
class MoveSquare:

    def __init__(self, destination, rect):
        self.rect = rect
        self.dest = destination

    def check_pressed(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())



class Pawn:

    def __init__(self, code, square):
        self.color = WHITE if code < 6 else BLACK
        white = (self.color == WHITE)
        self.firstmove = True
        self.code = code
        self.rect = pygame.Rect(square[0] * SQUARESIZE, square[1] * SQUARESIZE, SQUARESIZE, SQUARESIZE)
        self.pos = (square[0], square[1])
        self.MOVETWOFORWARD = (0, -2 if white else 2)
        self.MOVEONEFORWARD = (0,-1 if white else 1)
        self.attack_moves = [(1, -1 if white else 1), (-1, -1 if white else 1)]
        self.enpassantable = False


    def make_move(self, move, board):
        board[self.pos[0]][self.pos[1]] = None
        dest_x, dest_y = move.dest
        if move.dest == (self.pos[0] + self.MOVETWOFORWARD[0], self.pos[1] + self.MOVETWOFORWARD[1]):
            self.enpassantable = True

        self.firstmove = False
        if board[dest_x][dest_y] != None:
            #todo code add capture piece code
            pass
        self.pos = (dest_x, dest_y)
        self.rect = pygame.Rect(dest_x * SQUARESIZE, dest_y * SQUARESIZE, SQUARESIZE, SQUARESIZE)
        board[dest_x][dest_y] = self





    def check_pressed(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def get_valid_moves(self, board):
        moves = []
        king = board.whiteking if self.color == WHITE else board.blackking
        for move in self.get_possible_moves(board.board):
            pos = move.dest
            copied_board = copy.deepcopy(board.board)
            copied_board[pos[0]][pos[1]] = self
            copied_board[self.pos[0]][self.pos[1]] = None
            if king.is_check(copied_board, king.pos):
                continue
            else:
                moves.append(move)
        return moves

    def get_possible_moves(self, board):
        moves = []
        pos = self.pos

        dest_x, dest_y = (pos[0] + self.MOVEONEFORWARD[0], pos[1] + self.MOVEONEFORWARD[1])

        try:
            piece = board[dest_x][dest_y]
            if piece == None and dest_x > -1 and dest_y > -1:
                moves.append(MoveSquare((dest_x, dest_y), pygame.Rect(dest_x * SQUARESIZE, dest_y * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                try:
                    dest_x, dest_y = (pos[0] + self.MOVETWOFORWARD[0], pos[1] + self.MOVETWOFORWARD[1])
                    piece = board[dest_x][dest_y]

                    if piece == None and dest_x > -1 and dest_y > -1 and self.firstmove:

                        moves.append(MoveSquare((dest_x, dest_y), pygame.Rect(dest_x * SQUARESIZE, dest_y * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                except IndexError:
                    pass
        except IndexError:
            pass

        for move in self.attack_moves:
            try:
                dest_x, dest_y = (pos[0] + move[0], pos[1] + move[1])
                piece = board[dest_x][dest_y]
                if piece != None and piece.color != self.color and dest_x > -1 and dest_y > -1:
                    moves.append(MoveSquare((dest_x, dest_y), pygame.Rect(dest_x * SQUARESIZE, dest_y * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
            except IndexError:
                pass

        return moves

class Rook:
    def __init__(self, code, square):
        self.color = WHITE if code < 6 else BLACK
        white = (self.color == WHITE)
        self.firstmove = True
        self.code = code
        self.rect = pygame.Rect(square[0] * SQUARESIZE, square[1] * SQUARESIZE, SQUARESIZE, SQUARESIZE)
        self.pos = (square[0], square[1])

    def check_pressed(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def make_move(self, move, board):
        board[self.pos[0]][self.pos[1]] = None
        dest_x, dest_y = move.dest
        if board[dest_x][dest_y] != None:
            #todo code add capture piece code
            pass
        self.pos = (dest_x, dest_y)
        self.rect = pygame.Rect(dest_x * SQUARESIZE, dest_y * SQUARESIZE, SQUARESIZE, SQUARESIZE)
        board[dest_x][dest_y] = self


    def get_valid_moves(self, board):
        moves = []
        king = board.whiteking if self.color == WHITE else board.blackking
        for move in self.get_possible_moves(board.board):
            pos = move.dest
            copied_board = copy.deepcopy(board.board)
            copied_board[pos[0]][pos[1]] = self
            copied_board[self.pos[0]][self.pos[1]] = None
            if king.is_check(copied_board, king.pos):
                continue
            else:
                moves.append(move)
        return moves


    def get_possible_moves(self, board):
        moves = []
        pos = self.pos

        #going left and right
        for i in range(pos[0] - 1, -1, -1):
            piece = board[i][pos[1]]
            if piece == None:
                moves.append(MoveSquare((i, pos[1]), pygame.Rect(i * SQUARESIZE, pos[1] * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
            elif piece.color != self.color:
                moves.append(MoveSquare((i, pos[1]), pygame.Rect(i * SQUARESIZE, pos[1] * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                break
            else:
                break


        for i in range(pos[0] + 1, 8):
            piece = board[i][pos[1]]
            if piece == None and i != pos[0]:
                moves.append(MoveSquare((i, pos[1]), pygame.Rect(i * SQUARESIZE, pos[1] * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
            elif piece.color != self.color:
                moves.append(MoveSquare((i, pos[1]), pygame.Rect(i * SQUARESIZE, pos[1] * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                break
            else:
                break




        #going up and down

        for j in range(pos[1] - 1, -1, -1):
            piece = board[pos[0]][j]
            if piece == None:
                moves.append(MoveSquare((pos[0], j), pygame.Rect(pos[0] * SQUARESIZE, j * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
            elif piece.color != self.color:
                moves.append(MoveSquare((pos[0], j), pygame.Rect(pos[0] * SQUARESIZE, j * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                break
            else:
                break


        for j in range(pos[1] + 1, 8):
            piece = board[pos[0]][j]
            if piece == None:
                moves.append(MoveSquare((pos[0], j), pygame.Rect(pos[0] * SQUARESIZE, j * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
            elif piece.color != self.color:
                moves.append(MoveSquare((pos[0], j), pygame.Rect(pos[0] * SQUARESIZE, j * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                break
            else:
                break
        return moves


class Bishop:
    def __init__(self, code, square):
        self.color = WHITE if code < 6 else BLACK
        white = (self.color == WHITE)
        self.firstmove = True
        self.code = code
        self.rect = pygame.Rect(square[0] * SQUARESIZE, square[1] * SQUARESIZE, SQUARESIZE, SQUARESIZE)
        self.pos = (square[0], square[1])

    def check_pressed(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def make_move(self, move, board):
        board[self.pos[0]][self.pos[1]] = None
        dest_x, dest_y = move.dest
        if board[dest_x][dest_y] != None:
            #todo code add capture piece code
            pass
        self.pos = (dest_x, dest_y)
        self.rect = pygame.Rect(dest_x * SQUARESIZE, dest_y * SQUARESIZE, SQUARESIZE, SQUARESIZE)
        board[dest_x][dest_y] = self

    def get_valid_moves(self, board):
        moves = []
        king = board.whiteking if self.color == WHITE else board.blackking
        for move in self.get_possible_moves(board.board):
            pos = move.dest
            copied_board = copy.deepcopy(board.board)
            copied_board[pos[0]][pos[1]] = self
            copied_board[self.pos[0]][self.pos[1]] = None
            if king.is_check(copied_board, king.pos):
                continue
            else:
                moves.append(move)
        return moves


    def get_possible_moves(self, board):
        moves = []
        pos = self.pos

        #diagonals

        for i in range(1, 8):
            try:
                x, y = pos[0] + i, pos[1] - i
                piece = board[x][y]
                if not (x > -1 and y > -1):
                    continue
                if piece == None:

                    moves.append(MoveSquare((x, y), pygame.Rect(x * SQUARESIZE, y * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                elif piece.color != self.color:
                    moves.append(MoveSquare((x, y), pygame.Rect(x * SQUARESIZE, y * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                    break
                else:
                    break
            except IndexError:
                break

        for i in range(1, 8):
            try:
                x, y = pos[0] - i, pos[1] + i
                piece = board[x][y]
                if not (x > -1 and y > -1):
                    continue
                if piece == None:

                    moves.append(MoveSquare((x, y), pygame.Rect(x * SQUARESIZE, y * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                elif piece.color != self.color:
                    moves.append(MoveSquare((x, y), pygame.Rect(x * SQUARESIZE, y * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                    break
                else:
                    break
            except IndexError:
                break

        for i in range(1, 8):
            try:
                x, y = pos[0] + i, pos[1] + i
                piece = board[x][y]
                if not (x > -1 and y > -1):
                    continue
                if piece == None:
                    moves.append(MoveSquare((x, y), pygame.Rect(x * SQUARESIZE, y * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                elif piece.color != self.color:
                    moves.append(MoveSquare((x, y), pygame.Rect(x * SQUARESIZE, y * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                    break
                else:
                    break
            except IndexError:
                break

        for i in range(1, 8):
            try:
                x, y = pos[0] - i, pos[1] - i
                piece = board[x][y]
                if not (x > -1 and y > -1):
                    continue
                if piece == None:

                    moves.append(MoveSquare((x, y), pygame.Rect(x * SQUARESIZE, y * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                elif piece.color != self.color:
                    moves.append(MoveSquare((x, y), pygame.Rect(x * SQUARESIZE, y * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                    break
                else:
                    break

            except IndexError:
                break

        return moves


class Queen:
    def __init__(self, code, square):
        self.color = WHITE if code < 6 else BLACK
        white = (self.color == WHITE)
        self.firstmove = True
        self.code = code
        self.rect = pygame.Rect(square[0] * SQUARESIZE, square[1] * SQUARESIZE, SQUARESIZE, SQUARESIZE)
        self.pos = (square[0], square[1])

    def check_pressed(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def make_move(self, move, board):
        board[self.pos[0]][self.pos[1]] = None
        dest_x, dest_y = move.dest
        if board[dest_x][dest_y] != None:
            #todo code add capture piece code
            pass
        self.pos = (dest_x, dest_y)
        self.rect = pygame.Rect(dest_x * SQUARESIZE, dest_y * SQUARESIZE, SQUARESIZE, SQUARESIZE)
        board[dest_x][dest_y] = self

    def get_valid_moves(self, board):
        moves = []
        king = board.whiteking if self.color == WHITE else board.blackking
        for move in self.get_possible_moves(board.board):
            pos = move.dest
            copied_board = copy.deepcopy(board.board)
            copied_board[pos[0]][pos[1]] = self
            copied_board[self.pos[0]][self.pos[1]] = None
            if king.is_check(copied_board, king.pos):
                continue
            else:
                moves.append(move)
        return moves

    def get_possible_moves(self, board):
        moves = []
        pos = self.pos

        #diagonals

        for i in range(1, 8):
            try:
                x, y = pos[0] + i, pos[1] - i
                piece = board[x][y]
                if not (x > -1 and y > -1):
                    continue
                if piece == None:

                    moves.append(MoveSquare((x, y), pygame.Rect(x * SQUARESIZE, y * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                elif piece.color != self.color:
                    moves.append(MoveSquare((x, y), pygame.Rect(x * SQUARESIZE, y * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                    break
                else:
                    break
            except IndexError:
                break

        for i in range(1, 8):
            try:
                x, y = pos[0] - i, pos[1] + i
                piece = board[x][y]
                if not (x > -1 and y > -1):
                    continue
                if piece == None:

                    moves.append(MoveSquare((x, y), pygame.Rect(x * SQUARESIZE, y * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                elif piece.color != self.color:
                    moves.append(MoveSquare((x, y), pygame.Rect(x * SQUARESIZE, y * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                    break
                else:
                    break
            except IndexError:
                break

        for i in range(1, 8):
            try:
                x, y = pos[0] + i, pos[1] + i
                piece = board[x][y]
                if not (x > -1 and y > -1):
                    continue
                if piece == None:

                    moves.append(MoveSquare((x, y), pygame.Rect(x * SQUARESIZE, y * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                elif piece.color != self.color:
                    moves.append(MoveSquare((x, y), pygame.Rect(x * SQUARESIZE, y * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                    break
                else:
                    break
            except IndexError:
                break

        for i in range(1, 8):
            try:
                x, y = pos[0] - i, pos[1] - i
                piece = board[x][y]
                if not (x > -1 and y > -1):
                    continue
                if piece == None:

                    moves.append(MoveSquare((x, y), pygame.Rect(x * SQUARESIZE, y * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                elif piece.color != self.color:
                    moves.append(MoveSquare((x, y), pygame.Rect(x * SQUARESIZE, y * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                    break
                else:
                    break

            except IndexError:
                break

        #going left and right
        for i in range(pos[0] - 1, -1, -1):
            piece = board[i][pos[1]]
            if piece == None:
                moves.append(MoveSquare((i, pos[1]), pygame.Rect(i * SQUARESIZE, pos[1] * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
            elif piece.color != self.color:
                moves.append(MoveSquare((i, pos[1]), pygame.Rect(i * SQUARESIZE, pos[1] * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                break
            else:
                break


        for i in range(pos[0] + 1, 8):
            piece = board[i][pos[1]]
            if piece == None and i != pos[0]:
                moves.append(MoveSquare((i, pos[1]), pygame.Rect(i * SQUARESIZE, pos[1] * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
            elif piece.color != self.color:
                moves.append(MoveSquare((i, pos[1]), pygame.Rect(i * SQUARESIZE, pos[1] * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                break
            else:
                break




        #going up and down

        for j in range(pos[1] - 1, -1, -1):
            piece = board[pos[0]][j]
            if piece == None:
                moves.append(MoveSquare((pos[0], j), pygame.Rect(pos[0] * SQUARESIZE, j * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
            elif piece.color != self.color:
                moves.append(MoveSquare((pos[0], j), pygame.Rect(pos[0] * SQUARESIZE, j * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                break
            else:
                break


        for j in range(pos[1] + 1, 8):
            piece = board[pos[0]][j]
            if piece == None:
                moves.append(MoveSquare((pos[0], j), pygame.Rect(pos[0] * SQUARESIZE, j * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
            elif piece.color != self.color:
                moves.append(MoveSquare((pos[0], j), pygame.Rect(pos[0] * SQUARESIZE, j * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                break
            else:
                break
        return moves





class King:
    def __init__(self, code, square):
        self.color = WHITE if code < 6 else BLACK
        white = (self.color == WHITE)
        self.firstmove = True
        self.code = code
        self.rect = pygame.Rect(square[0] * SQUARESIZE, square[1] * SQUARESIZE, SQUARESIZE, SQUARESIZE)
        self.pos = (square[0], square[1])

    def check_pressed(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def is_check(self, board, pos):

        for row in board:
            for piece in row:
                if piece and piece.color != self.color:
                    for move in piece.get_possible_moves(board):

                        if move.dest == pos:

                            return True
        return False

    def is_checkmate(self, board):
        no_move = True

        for row in board.board:
            for piece in row:
                if piece and piece.color == self.color:
                    if piece.get_valid_moves(board) != []:

                        return False


        return self.is_check(board.board,self.pos) and no_move





    def make_move(self, move, board):
        board[self.pos[0]][self.pos[1]] = None
        dest_x, dest_y = move.dest
        if board[dest_x][dest_y] != None:
            #todo code add capture piece code
            pass
        self.pos = (dest_x, dest_y)
        self.rect = pygame.Rect(dest_x * SQUARESIZE, dest_y * SQUARESIZE, SQUARESIZE, SQUARESIZE)
        board[dest_x][dest_y] = self

    def get_possible_moves(self, board):
        moves = []
        pos = self.pos

        pos_moves = [(1, 1), (1, -1), (-1, -1), (-1, 1), (1, 0), (0, 1), (-1, 0), (0, -1)]

        for move in pos_moves:
            try:
                x, y = pos[0] + move[0], pos[1] + move[1]
                piece = board[x][y]
                if not (x > -1 and y > -1):
                    continue

                if piece == None:

                    moves.append(MoveSquare((x, y), pygame.Rect(x * SQUARESIZE, y * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                elif piece.color != self.color:
                    moves.append(MoveSquare((x, y), pygame.Rect(x * SQUARESIZE, y * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                    break

            except IndexError:
                pass
        return moves


    def get_valid_moves(self, board):
        moves = []
        for move in self.get_possible_moves(board.board):
            pos = move.dest
            copied_board = copy.deepcopy(board.board)
            copied_board[pos[0]][pos[1]] = self
            copied_board[self.pos[0]][self.pos[1]] = None
            if self.is_check(copied_board, pos):
                continue
            else:
                moves.append(move)
        return moves







class Knight:
    def __init__(self, code, square):
        self.color = WHITE if code < 6 else BLACK
        white = (self.color == WHITE)
        self.firstmove = True
        self.code = code
        self.rect = pygame.Rect(square[0] * SQUARESIZE, square[1] * SQUARESIZE, SQUARESIZE, SQUARESIZE)
        self.pos = (square[0], square[1])


    def check_pressed(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def make_move(self, move, board):
        board[self.pos[0]][self.pos[1]] = None
        dest_x, dest_y = move.dest
        if board[dest_x][dest_y] != None:
            #todo code add capture piece code
            pass
        self.pos = (dest_x, dest_y)
        self.rect = pygame.Rect(dest_x * SQUARESIZE, dest_y * SQUARESIZE, SQUARESIZE, SQUARESIZE)
        board[dest_x][dest_y] = self

    def get_valid_moves(self, board):
        moves = []
        king = board.whiteking if self.color == WHITE else board.blackking
        for move in self.get_possible_moves(board.board):
            pos = move.dest
            copied_board = copy.deepcopy(board.board)
            copied_board[pos[0]][pos[1]] = self
            copied_board[self.pos[0]][self.pos[1]] = None
            if king.is_check(copied_board, king.pos):
                continue
            else:
                moves.append(move)
        return moves



    def get_possible_moves(self, board):
        moves = []
        pos = self.pos

        pos_moves = [(1, 2), (2, 1), (-1, 2), (2, -1), (-2, -1), (-1, -2), (-2, 1), (1, -2)]

        for move in pos_moves:
            try:
                x, y = pos[0] + move[0], pos[1] + move[1]
                piece = board[x][y]
                if not (x > -1 and y > -1):
                    continue
                if piece == None:

                    moves.append(MoveSquare((x, y), pygame.Rect(x * SQUARESIZE, y * SQUARESIZE, SQUARESIZE, SQUARESIZE)))
                elif piece.color != self.color:
                    moves.append(MoveSquare((x, y), pygame.Rect(x * SQUARESIZE, y * SQUARESIZE, SQUARESIZE, SQUARESIZE)))

            except IndexError:
                pass


        return moves
