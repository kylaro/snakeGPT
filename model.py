import random
from collections import deque

class SnakeModel:
    def __init__(self):
        self.snake_body = [(5, 5), (5, 6), (5, 7)]
        self.board_size = (20, 20)
        self.food_location = self.generate_food()

    def generate_food(self):
        while True:
            x = random.randint(0, self.board_size[0]-1)
            y = random.randint(0, self.board_size[1]-1)
            if (x, y) not in self.snake_body:
                return (x, y)
            
    def get_gamestate_text(self):
        gamestate = f"""
The game is the classic Snake game. 
The board size is {self.board_size}.
The snake head is at {self.snake_body[0]}.
The snake body is at {self.snake_body[1:]}.
The food is at {self.food_location}.
"""
        return gamestate
