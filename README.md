# Pong Game

A simple implementation of the classic Pong game using Python's turtle graphics.

## Table of Contents

* [Description](#description)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)
* [Controls](#controls)
* [Project Structure](#project-structure)
* [Testing](#testing)
* [Configuration](#configuration)
* [Contributing](#contributing)
* [License](#license)

## Description

Pong is one of the earliest arcade video games. This project recreates Pong using Python and the turtle module, featuring basic collision handling, score tracking, and paddle controls.

## Prerequisites

* Python 3.6 or later
* [pytest](https://pypi.org/project/pytest/) for running tests

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/binarynectar/pong.git
   cd pong
   ```
2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```
3. Install dependencies:

   ```bash
   pip install pytest
   ```

## Usage

Run the main game script:

```bash
python main.py
```

The game window will open. Use the controls below to play.

## Controls

* Left paddle: `W` (up), `S` (down)
* Right paddle: `Up Arrow`, `Down Arrow`
* Close window to exit the game.

## Project Structure

```
.
├── ball.py               # Ball logic and movement
├── collision_handler.py  # Collision detection and response
├── config.py             # Game configuration constants
├── main.py               # Entry point and game loop
├── paddle.py             # Paddle logic and movement
├── scoreboard.py         # Score tracking logic
├── view.py               # Turtle graphics views for game objects
├── test_ball.py          # Unit tests for Ball and CollisionHandler
├── test_paddle.py        # Unit tests for Paddle
└── README.md             # Project overview
```

## Testing

Run the test suite with pytest:

```bash
pytest
```

## Configuration

Adjust game settings in `config.py`:

* `SCREEN_WIDTH` and `SCREEN_HEIGHT` to change window size
* `STANDARD_BALL_INCREMENT` and `SPEED_INCREMENT` for ball speed
* `PADDLE_INCREMENT` for paddle movement speed
* `COLLISION_ADJUST` for collision sensitivity

## Contributing

Contributions are welcome! Please open issues or pull requests for improvements.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
