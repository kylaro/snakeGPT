import pygame

class SnakeView:
    def __init__(self):
        pygame.init()
        self.window_size = (640, 480)
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("Snake Game")
        self.grid_size = (self.window_size[0]//20, self.window_size[1]//20)

    def draw(self, snake_body, food_location):
        self.screen.fill((255, 255, 255))  # White background
        # Draw snake with head as blue, body as green
        for i, pos in enumerate(snake_body):
            if i == 0:
                pygame.draw.rect(self.screen, (0, 0, 255), (pos[0]*self.grid_size[0], pos[1]*self.grid_size[1], *self.grid_size))
            else:
                #pygame.draw.rect(self.screen, (min(20+i*20,230), min(20+i*20,230), 255), (pos[0]*self.grid_size[0], pos[1]*self.grid_size[1], *self.grid_size))
                pygame.draw.rect(self.screen, (100, 100, 255), (pos[0]*self.grid_size[0], pos[1]*self.grid_size[1], *self.grid_size))


        pygame.draw.rect(self.screen, (0, 255, 0), (food_location[0]*self.grid_size[0], food_location[1]*self.grid_size[1], *self.grid_size))
        pygame.display.flip()
