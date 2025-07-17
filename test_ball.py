# test_ball.py

import pytest
import math
from ball import Ball
from paddle import Paddle
from collision_handler import CollisionHandler
from config import (
    STANDARD_BALL_INCREMENT,
    SPEED_INCREMENT
)

@pytest.fixture
def ball():
    return Ball()

@pytest.fixture
def paddle():
    # start paddle somewhere non-zero so coordinates matter
    return Paddle((10, 20))

@pytest.fixture
def collision_handler():
    return CollisionHandler()

def get_sizes(ball, paddle):
    """
    Returns (ball_w, ball_h, paddle_w, paddle_h) in pixels,
    using each shape's pure-logic get_size().
    """
    bw, bh = ball.get_size()
    pw, ph = paddle.get_size()
    return bw, bh, pw, ph

def test_defaults(ball):
    # increments come from config
    assert ball.x_increment == STANDARD_BALL_INCREMENT
    assert ball.y_increment == STANDARD_BALL_INCREMENT
    assert ball.x == 0
    assert ball.y == 0

def test_move_updates_coordinates(ball):
    # place ball at (10, 15)
    ball.x, ball.y = 10, 15
    # override increments
    ball.x_increment = 5
    ball.y_increment = -3

    ball.move()

    # expect (10 + 5, 15 - 3)
    assert ball.x == 15
    assert ball.y == 12

def test_bounce_flips_y_increment(ball, collision_handler):
    orig = ball.y_increment
    collision_handler.handle_y_bounce(ball)
    assert ball.y_increment == -orig

    # bounce again flips back
    collision_handler.handle_y_bounce(ball)
    assert ball.y_increment == orig

def test_bounce_flips_x_increment(ball, collision_handler):
    orig = ball.x_increment
    collision_handler.handle_x_bounce(ball)
    result = ball.x_increment
    assert math.isclose(result, -orig * (1 + SPEED_INCREMENT)) is True

    # bounce again flips back
    orig = result
    collision_handler.handle_x_bounce(ball)
    result = ball.x_increment
    assert math.isclose(result, -orig * (1 + SPEED_INCREMENT)) is True

@pytest.mark.parametrize("dx, dy, expected", [
    # center overlap
    (0, 0, True),
    # just inside horizontal overlap
    (lambda bw, pw: pw/2 + bw/2 - 0.1, 0, True),
    # just outside horizontal overlap
    (lambda bw, pw: pw/2 + bw/2 + 0.1, 0, False),
    # just inside vertical overlap
    (0, lambda bh, ph: ph/2 + bh/2 - 0.1, True),
    # just outside vertical overlap
    (0, lambda bh, ph: ph/2 + bh/2 + 0.1, False),
])
def test_is_collision_with_paddle_edge_cases(ball, paddle, collision_handler, dx, dy, expected):
    bw, bh, pw, ph = get_sizes(ball, paddle)

    # resolve dx, dy lambdas if needed
    real_dx = dx(bw, pw) if callable(dx) else dx
    real_dy = dy(bh, ph) if callable(dy) else dy

    # position the ball relative to the paddle
    ball.x = paddle.xcor() + real_dx
    ball.y = paddle.ycor() + real_dy

    orig = ball.x_increment

    collision_handler.check_paddle_collision(ball, paddle)

    result = True if math.isclose(ball.x_increment, -orig * (1 + SPEED_INCREMENT)) else False

    assert result is expected
