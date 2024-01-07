import pygame
import sys

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

class Game:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.board = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Achtung, die Kurve!")

        self.player = Player((255, 0, 0), width // 2, height // 2)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.change_direction((-1, 0))
        elif keys[pygame.K_RIGHT]:
            self.player.change_direction((1, 0))
        elif keys[pygame.K_UP]:
            self.player.change_direction((0, -1))
        elif keys[pygame.K_DOWN]:
            self.player.change_direction((0, 1))
        elif keys[pygame.K_BACKSPACE]:
            return False  # End the game

        return True

    def update_player(self):
        self.player.move()

        if (self.player.x < 0 or self.player.x >= self.width or
                self.player.y < 0 or self.player.y >= self.height):
            self.player.x = self.width // 2
            self.player.y = self.height // 2

    def draw_player(self):
        self.board.fill((0, 0, 0))
        pygame.draw.rect(self.board, self.player.color, (self.player.x, self.player.y, 10 * self.player.length, 10))
        pygame.display.update()

    def run(self):
        game_running = True
        while game_running:
            game_running = self.handle_events()
            self.update_player()
            self.draw_player()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game(800, 600)
    game.run()
