import pygame
import sys
from playergpt import PlayerGPT

class SnakeController:
    def __init__(self, model):
        self.model = model
        self.direction = (0, -1)  # Initially moving upwards
        self.player = PlayerGPT()

    def update(self, event):
        #pygame.time.delay(2000)  # Add delay to make the game playable
        gamestate = self.model.get_gamestate_text()
        # Get direction from PlayerGPT
        player_key = self.player.get_direction(gamestate)
        # The player_key from PlayerGPT gameplay:
        if player_key == "left":
            self.direction = (-1, 0)
        elif player_key == "right":
            self.direction = (1, 0)
        elif player_key == "up":
            self.direction = (0, 1)
        elif player_key == "down":
            self.direction = (0, -1)
        else:
            return
        self.move_snake()

        # The regular arrow key gameplay:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.direction != (0, 1):
                self.direction = (0, -1)
            elif event.key == pygame.K_DOWN and self.direction != (0, -1):
                self.direction = (0, 1)
            elif event.key == pygame.K_LEFT and self.direction != (1, 0):
                self.direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and self.direction != (-1, 0):
                self.direction = (1, 0)
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            else:
                return
            self.move_snake()

    def move_snake(self):
        new_head = (self.model.snake_body[0][0] + self.direction[0],
                    self.model.snake_body[0][1] + self.direction[1])
        self.model.snake_body.insert(0,new_head)
        if new_head == self.model.food_location:
            self.model.food_location = self.model.generate_food()
        else:
            self.model.snake_body.pop()
