import time
from turtle import Screen, TurtleScreen
from config import DEFAULT_MOVEMENT_DELAY, SCREEN_HEIGHT, SCREEN_WIDTH
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from view import TurtleBall, TurtlePaddle, TurtleScoreboard
from collision_handler import CollisionHandler

def setup_screen() -> TurtleScreen:
    """
    Configure and return the main game window.
    """
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)
    return screen


def bind_paddle_controls(screen: TurtleScreen, paddle: Paddle, up_key: str, down_key: str):
    """
    Attach key-press and key-release events to toggle a paddle's movement flags.

    Args:
        screen (Screen): The turtle screen to listen on.
        paddle (Paddle): The paddle instance to control.
        up_key (str): Key that moves the paddle up.
        down_key (str): Key that moves the paddle down.
    """
    screen.onkeypress(lambda: setattr(paddle, 'is_moving_up', True), up_key)
    screen.onkeyrelease(lambda: setattr(paddle, 'is_moving_up', False), up_key)
    screen.onkeypress(lambda: setattr(paddle, 'is_moving_down', True), down_key)
    screen.onkeyrelease(lambda: setattr(paddle, 'is_moving_down', False), down_key)


def main():
    """
    Main game loop:
    - Initializes screen, paddles, and ball
    - Binds controls
    - Updates game state each frame
    """
    screen = setup_screen()

    # Initialize paddles on left and right
    left_paddle_logic  = Paddle((int(-SCREEN_WIDTH / 2 + 50), 0))
    left_paddle_view = TurtlePaddle(left_paddle_logic)
    
    right_paddle_logic = Paddle((int(SCREEN_WIDTH / 2 - 50), 0))
    right_paddle_view = TurtlePaddle(right_paddle_logic)

    ball_logic = Ball()
    ball_view = TurtleBall(ball_logic)

    scoreboard_logic = Scoreboard()
    scoreboard_view = TurtleScoreboard(scoreboard_logic)
    
    # Initialize collision handler
    collision_handler = CollisionHandler()

    screen.listen()

    bind_paddle_controls(screen, left_paddle_logic,  "w",    "s")
    bind_paddle_controls(screen, right_paddle_logic, "Up",   "Down")

    # Game loop - runs until window closes
    while True:
        # Control frame rate
        time.sleep(DEFAULT_MOVEMENT_DELAY)
        screen.update()

        # Continuous paddle movement
        for paddle in (left_paddle_logic, right_paddle_logic):
            if paddle.is_moving_up:
                paddle.move_up()
            if paddle.is_moving_down:
                paddle.move_down()

        # Move ball and handle all collisions using collision handler
        ball_logic.move()

        collision_handler.check_wall_collision(ball_logic)
        collision_handler.check_paddle_collision(ball_logic, left_paddle_logic)
        collision_handler.check_paddle_collision(ball_logic, right_paddle_logic)
        collision_handler.check_out_of_bounds(ball_logic, scoreboard_logic)

        # synchronize logic with GUI (view)
        left_paddle_view.sync()
        right_paddle_view.sync()
        ball_view.sync()
        scoreboard_view.sync()

if __name__ == "__main__":
    main()
