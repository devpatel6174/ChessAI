import pygame

#DISPLAY SETTINGS

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

#CHESSBOARD SETTINGS

SQUARESIZE = 100
DARK = (184, 139, 74)
LIGHT = (227, 193, 111)

#CHESS PIECE CODES

WHITE_KING = 0
WHITE_QUEEN = 1
WHITE_KNIGHT = 3
WHITE_BISHOP = 2
WHITE_ROOK = 4
WHITE_PAWN = 5

BLACK_KING = 6
BLACK_QUEEN = 7
BLACK_KNIGHT = 9
BLACK_BISHOP = 8
BLACK_ROOK = 10
BLACK_PAWN = 11

WHITE = 12
BLACK = 13
PIECES = {}
def load_pieces(screen):
    spritesheet = pygame.image.load("spritesheet.png")

    pieces = []

    for i in range(0,6):
        rect = pygame.Rect((i * 480, 0, 480, 480))
        image = pygame.Surface((480, 480))
        image.blit(spritesheet, (0, 0), rect)

        newimage = pygame.Surface((SQUARESIZE,SQUARESIZE))
        pygame.transform.smoothscale(image, (SQUARESIZE, SQUARESIZE), newimage)

        pieces.append(newimage.convert_alpha())


    for i in range(0,6):
        rect = pygame.Rect((i * 480, 480, 480, 480))
        image = pygame.Surface((480, 480))
        image.blit(spritesheet, (0, 0), rect)

        newimage = pygame.Surface((SQUARESIZE,SQUARESIZE))
        pygame.transform.smoothscale(image, (SQUARESIZE, SQUARESIZE), newimage)

        pieces.append(newimage.convert_alpha())



    PIECES[WHITE_QUEEN] = pieces[WHITE_QUEEN];
    PIECES[WHITE_BISHOP] = pieces[WHITE_BISHOP];
    PIECES[WHITE_KNIGHT] = pieces[WHITE_KNIGHT];
    PIECES[WHITE_ROOK] = pieces[WHITE_ROOK];
    PIECES[WHITE_PAWN] = pieces[WHITE_PAWN];

    PIECES[BLACK_KING] = pieces[BLACK_KING];
    PIECES[BLACK_QUEEN] = pieces[BLACK_QUEEN];
    PIECES[BLACK_BISHOP] = pieces[BLACK_BISHOP];
    PIECES[BLACK_KNIGHT] = pieces[BLACK_KNIGHT];
    PIECES[BLACK_ROOK] = pieces[BLACK_ROOK];
    PIECES[BLACK_PAWN] = pieces[BLACK_PAWN];
    PIECES[WHITE_KING] = pieces[WHITE_KING];


#GAME LOGIC (POSSIBLE MOVES)
