from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    COLLISION_ADJUST,
    SPEED_INCREMENT
)

class CollisionHandler:
    """
    Handles all collision detection and response logic for the Pong game.
    """
        
    def __init__(self):
        """
        Initialize the collision handler.
        """
        self._top = SCREEN_HEIGHT/2
        self._bottom = -SCREEN_HEIGHT/2
        
    def check_wall_collision(self, ball):
        """
        Check if ball has collided with top or bottom wall and bounce if necessary.
        
        Args:
            ball: The ball object to check
        """
        if ball.y >= self._top - COLLISION_ADJUST or ball.y <= self._bottom + COLLISION_ADJUST:
            self.handle_y_bounce(ball)
    
    def handle_y_bounce(self, ball):
        """
        Handle the ball bouncing off a wall by reversing its y velocity.
        
        Args:
            ball: The ball object to bounce
        """
        ball.y_increment *= -1
    
    def handle_x_bounce(self, ball):
        """
        Handle the ball bouncing off a paddle by reversing its x velocity
        and applying speed increment.
        
        Args:
            ball: The ball object to bounce
        """
        ball.x_increment *= -(1 + SPEED_INCREMENT)
    
    def check_paddle_collision(self, ball, paddle):
        """
        Check if the ball has collided with a paddle.
        If collision is detected, perform the bounce response.
        
        Args:
            ball: The ball object to check
            paddle: The paddle object to check against
        """
        x_hit = True if paddle.xcor() - 20 <= ball.x <= paddle.xcor() + 20 else False
        y_hit = True if paddle.ycor() - 60 <= ball.y <= paddle.ycor() + 60 else False

        if x_hit and y_hit:
            self.handle_x_bounce(ball)
    
    def check_out_of_bounds(self, ball, scoreboard):
        """
        Check if the ball has gone out of bounds (past the paddles).
        If out of bounds, update the score and reset the ball.
        
        Args:
            ball: The ball object to check
            scoreboard: The scoreboard object to update scores
        """
        if ball.x <= -SCREEN_WIDTH/2 - 10:
            scoreboard.increment_r_score()
            ball.reset()

        if ball.x >= SCREEN_WIDTH/2 + 10:
            scoreboard.increment_l_score()
            ball.reset()
    
