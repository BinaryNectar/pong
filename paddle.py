# paddle.py
from config import PADDLE_INCREMENT

class Paddle:
    def __init__(self, pos=(0,0)):
        self.x, self.y = pos

        # Reset movement flags for continuous input
        self.is_moving_up = False
        self.is_moving_down = False

    def goto(self, x, y):
        self.x, self.y = x, y

    def xcor(self):
        return self.x

    def ycor(self):
        return self.y

    def move_up(self):
        self.y += PADDLE_INCREMENT

    def move_down(self):
        self.y -= PADDLE_INCREMENT

    def get_size(self):
        return (20, 20 * 5)  # stretch_len=1, stretch_wid=5 → width=20, height=100
