import pygame
from constants import *
from pieces import *
class Gameboard:

    def __init__(self, screen):
        self.screen = screen
        load_pieces(screen)
        self.board = [[Rook(BLACK_ROOK, (0, 0)), Knight(BLACK_KNIGHT, (1, 0)), Bishop(BLACK_BISHOP, (2, 0)), Queen(BLACK_QUEEN, (3, 0)), King(BLACK_KING, (4, 0)), Bishop(BLACK_BISHOP, (5, 0)), Knight(BLACK_KNIGHT, (6, 0)), Rook(BLACK_ROOK, (7, 0))],
                      [Pawn(BLACK_PAWN, (i, 1)) for i in range(0, 8)],
                      *[[None for i in range(8)] for j in range(4)],
                      [Pawn(WHITE_PAWN, (i, 6)) for i in range(0, 8)],
                      [Rook(WHITE_ROOK, (0, 7)), Knight(WHITE_KNIGHT, (1, 7)), Bishop(WHITE_BISHOP, (2, 7)), Queen(WHITE_QUEEN, (3, 7)), King(WHITE_KING, (4, 7)), Bishop(WHITE_BISHOP, (5, 7)), Knight(WHITE_KNIGHT, (6, 7)), Rook(WHITE_ROOK, (7, 7))]]

        self.board = list(map(list,zip(*self.board)))

        self.selections = []
        self.turn = WHITE
        self.clicked_piece = None
        self.whiteking = self.board[4][7]
        self.blackking = self.board[4][0]







    def draw_board(self):
        divisor = SQUARESIZE * 2
        for i in range(0, SQUARESIZE * 8, SQUARESIZE):
            for j in range(0, SQUARESIZE * 8, SQUARESIZE):
                pygame.draw.rect(self.screen, LIGHT if (i % divisor) == (j % divisor) else DARK, (i, j, SQUARESIZE, SQUARESIZE))

    def draw_pieces(self):
        for row in self.board:
            for piece in row:
                if piece:
                    self.screen.blit(PIECES[piece.code], piece.rect)
        for selection in self.selections:
            surface = pygame.Surface((SQUARESIZE, SQUARESIZE))
            surface.set_alpha(128)
            surface.fill((255, 0, 0))
            self.screen.blit(surface, selection.rect)

    def check_status(self):

        if self.turn == WHITE and self.whiteking.is_check(self.board,self.whiteking.pos):
            print("White King in Check")
        if self.turn == BLACK and self.blackking.is_check(self.board, self.blackking.pos):
            print("Black King in Check")

        if self.whiteking.is_checkmate(self):
            print("Black Wins!")
        if self.blackking.is_checkmate(self):
            print("White Wins!")

    def check_events(self):

        for row in self.board:

            for piece in row:

                if piece and piece.check_pressed() and piece.color == self.turn:
                    self.clicked_piece = piece
                    self.selections = piece.get_valid_moves(self)
                    break
        for move in self.selections:
            if move.check_pressed():
                self.clicked_piece.make_move(move, self.board)
                self.turn = BLACK if self.turn == WHITE else WHITE
                self.selections = []
                self.clicked_piece = None
