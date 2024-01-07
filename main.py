import pygame
import sys


pygame.init()


width = 800
height = 600
board = pygame.display.set_mode((width, height))
pygame.display.set_caption("Achtung, die Kurve!")


white = (255, 255, 255)
black = (0, 0, 0)


class Player:
    def __init__(self, color, start_x, start_y):
        self.color = color
        self.x = start_x
        self.y = start_y
        self.length = 1
        self.direction = (1, 0)  

    def move(self):
        self.x += self.direction[0]
        self.y += self.direction[1]

    def change_direction(self, new_direction):
        if self.direction != (-new_direction[0], -new_direction[1]):
            self.direction = new_direction


player1 = Player((255, 0, 0), width // 4, height // 2)
player2 = Player((0, 0, 255), width * 3 // 4, height // 2)

players = [player1, player2]


def initialize_players():
    player1.x = width // 4
    player1.y = height // 2
    player2.x = width * 3 // 4
    player2.y = height // 2


game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player1.change_direction((-1, 0))
        elif keys[pygame.K_RIGHT]:
            player1.change_direction((1, 0))
        elif keys[pygame.K_UP]:
            player1.change_direction((0, -1))
        elif keys[pygame.K_DOWN]:
            player1.change_direction((0, 1))

        if keys[pygame.K_a]:
            player2.change_direction((-1, 0))
        elif keys[pygame.K_d]:
            player2.change_direction((1, 0))
        elif keys[pygame.K_w]:
            player2.change_direction((0, -1))
        elif keys[pygame.K_s]:
            player2.change_direction((0, 1))


        if keys[pygame.K_BACKSPACE]:
            game_running = False  # End the game


    for player in players:
        player.move()


    for player in players:
        if (player.x < 0 or player.x >= width or player.y < 0 or player.y >= height):
            initialize_players()  


    for player1 in players:
        for player2 in players:
            if player1 is not player2 and (player1.x == player2.x and player1.y == player2.y):
                initialize_players()  


    board.fill(black)
    for player in players:
        pygame.draw.rect(board, player.color, (player.x, player.y, 10 * player.length, 10))

    pygame.display.update()


pygame.quit()
sys.exit()
