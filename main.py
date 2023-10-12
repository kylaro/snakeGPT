import pygame
from model import SnakeModel
from view import SnakeView
from controller import SnakeController

def main():
    model = SnakeModel()
    view = SnakeView()
    controller = SnakeController(model)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        controller.update(event)
        view.draw(model.snake_body, model.food_location)
        pygame.time.delay(100)  # Add delay to slow the token usage

    pygame.quit()

if __name__ == "__main__":
    main()




"""
import pygame
import sys


# Initialize Pygame
pygame.init()

# Set up display
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hello, World!")

# Set up colors and shapes
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

circle_pos = (320, 240)
circle_radius = 50

square_size = 100
square_pos = (width - square_size, height - square_size)




# Main game loop
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                check_arrow_keys()
        
        # Draw everything
        window.fill(white)  # Fill the screen with white color
        pygame.draw.circle(window, red, circle_pos, circle_radius)  # Draw a red circle
        pygame.draw.rect(window, blue, (square_pos[0], square_pos[1], square_size, square_size))  # Draw a blue square

        # Update display
        pygame.display.flip()

        # Cap the frame rate to 60 frames per second
        pygame.time.Clock().tick(60)

# Start the game
main()
# Clean up
pygame.quit()
sys.exit()
"""