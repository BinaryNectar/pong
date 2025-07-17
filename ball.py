from config import (
    STANDARD_BALL_INCREMENT,
)

class Ball:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.x_increment = STANDARD_BALL_INCREMENT
        self.y_increment = STANDARD_BALL_INCREMENT

    def move(self):
        self.x += self.x_increment
        self.y += self.y_increment

    def get_size(self):
        # logic size, matches shapesize()*20 in tests
        return (20, 20)

    def reset(self):
        self.x, self.y = 0, 0

        if self.x_increment < 0:
            self.x_increment = STANDARD_BALL_INCREMENT
        else:
            self.x_increment = -STANDARD_BALL_INCREMENT

        if self.y_increment < 0:
            self.y_increment = STANDARD_BALL_INCREMENT
        else:
            self.y_increment = -STANDARD_BALL_INCREMENT