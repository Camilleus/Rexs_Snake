import pygame
import sys
import random

class Player:
    def __init__(self, color, start_x, start_y, speed):
        self.color = color
        self.x = start_x
        self.y = start_y
        self.length = 1
        self.speed = speed
        self.direction = (1, 0)

    def move(self):
        self.x += self.direction[0] * self.speed
        self.y += self.direction[1] * self.speed

    def change_direction(self, new_direction):
        if self.direction != (-new_direction[0], -new_direction[1]):
            self.direction = new_direction

class Food:
    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height
        self.spawn_food()

    def spawn_food(self):
        self.x = random.randrange(0, self.width, 10)
        self.y = random.randrange(0, self.height, 10)

class Game:
    def __init__(self, width, height, player_speed):
        pygame.init()
        self.width = width
        self.height = height
        self.board = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake Game")

        self.player = Player((0, 255, 0), width // 2, height // 2, player_speed)
        self.food = Food((255, 0, 0), width, height)

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
            return False

        return True

    def update_player(self):
        self.player.move()

        if (self.player.x < 0 or self.player.x >= self.width or
                self.player.y < 0 or self.player.y >= self.height):
            self.player.x = self.width // 2
            self.player.y = self.height // 2

    def check_food_collision(self):
        if (self.player.x == self.food.x and self.player.y == self.food.y):
            self.player.length += 1
            self.food.spawn_food()

    def draw_player(self):
        self.board.fill((0, 0, 0))
        pygame.draw.rect(self.board, self.player.color, (self.player.x, self.player.y, 10 * self.player.length, 10))
        pygame.draw.rect(self.board, self.food.color, (self.food.x, self.food.y, 10, 10))
        pygame.display.update()

    def run(self):
        game_running = True
        while game_running:
            game_running = self.handle_events()
            self.update_player()
            self.check_food_collision()
            self.draw_player()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    player_speed = float(input("Enter the player speed (e.g., 0.1): "))
    game = Game(800, 600, player_speed)
    game.run()
