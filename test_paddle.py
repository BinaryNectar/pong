# test_paddle.py

import pytest
from paddle import Paddle
from config import PADDLE_INCREMENT

@pytest.fixture
def paddle_origin():
    return Paddle((0, 0))

@pytest.fixture
def paddle_at_offset():
    p = Paddle((0, 0))
    p.goto(5, 5)
    return p

def test_initial_position(paddle_origin):
    assert (paddle_origin.xcor(), paddle_origin.ycor()) == (0, 0)

def test_move_up_increments_y(paddle_at_offset):
    initial_x, initial_y = paddle_at_offset.xcor(), paddle_at_offset.ycor()
    paddle_at_offset.move_up()
    assert paddle_at_offset.xcor() == initial_x
    assert paddle_at_offset.ycor() == initial_y + PADDLE_INCREMENT

def test_move_down_decrements_y(paddle_at_offset):
    initial_x, initial_y = paddle_at_offset.xcor(), paddle_at_offset.ycor()
    paddle_at_offset.move_down()
    assert paddle_at_offset.xcor() == initial_x
    assert paddle_at_offset.ycor() == initial_y - PADDLE_INCREMENT
