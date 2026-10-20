# Offline Chrome Dino Game using Python and Pygame

An offline Chrome Dino game -an endless runner game built using Python and Pygame. This project recreates the basic gameplay of the offline dinosaur game, where the player jumps over obstacles, avoids birds, and tries to achieve the highest possible score.

I built this project to understand how a simple 2D game works, including game loops, keyboard input, collision detection, sprite animation, obstacle generation, scoring, and day-night transitions.

## About the Project
- The player controls a dinosaur running across the ground.
- Obstacles appear from the right side of the screen and move toward the player.
- The objective is to avoid collisions and continue running for as long as possible.
- Instead of drawing every object from scratch, I used a sprite sheet containing visual assets for the dinosaur, cacti, birds, clouds, the moon, stars, and ground.

The project focuses on implementing the core gameplay mechanics while keeping the code organised into separate modules.

## Features

- **Dinosaur movement:** Control the dinosaur and jump over obstacles.
- **Animated sprites:** Use sprite frames for the dinosaur and flying birds.
- **Multiple obstacles:** Avoid small cacti, large cacti, and birds.
- **Endless gameplay:** Obstacles continue to appear as the game progresses.
- **Score system:** Earn points by surviving longer.
- **Increasing difficulty:** Game speed gradually increases as the score grows.
- **Day-night cycle:** The background changes between daytime and nighttime.
- **Moving night elements:** The moon and stars move slowly during nighttime.
- **Random obstacle generation:** Obstacle types and spawn gaps vary during gameplay.
- **Collision detection:** Detect collisions between the dinosaur and obstacles.
- **Game-over state:** End the current run when the dinosaur hits an obstacle.
- **Restart support:** Start another run after a game over.
- **Organized codebase:** Separate files for settings, assets, and game logic.

## Gameplay

The player controls a dinosaur that runs automatically. Cacti appear on the ground, while birds fly at different heights. The player must time jumps carefully to avoid hitting them.

As the game continues, the running speed increases, making it more challenging to react to upcoming obstacles.

The objective is simple: survive for as long as possible and achieve a high score.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pygame | Game window, graphics, input, timing, and collision handling |
| Random module | Random obstacle selection and spacing |
| Python modules | Organizing the game into reusable files |

## Project Structure

```text
chrome-dino-original-sprites/
│
├── assets/
│   └── images/
│       └── chrome-dino-sprite.png
│   
│
├── game/
│   ├── __init__.py
│   ├── assets.py
│   ├── game.py
│   └── settings.py
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
├── THIRD_PARTY_NOTICES.md
└── .gitignore
```

### Folder and file explanation

**`main.py`**

The entry point of the application. It imports the main game class and starts the game.

**`game/`**

Contains the Python modules responsible for the game's implementation.

**`game/game.py`**

Contains the main game logic, including the game loop, player movement, obstacle updates, collision checks, score updates, day-night transitions, drawing, and game-over handling.

**`game/assets.py`**

Loads the sprite sheet and extracts individual images for the dinosaur, obstacles, birds, clouds, moon, stars, and ground. These extracted images are used throughout the game.

**`game/settings.py`**

Stores configuration values such as screen dimensions, frame rate, ground position, dinosaur position, starting speed, maximum speed, and obstacle-generation settings. Keeping these values separate makes it easier to adjust the game.

**`game/__init__.py`**

Marks the `game` directory as a Python package.

**`assets/images/chrome-dino-sprite.png`**

The sprite sheet used to display the game's visual elements.

**`requirements.txt`**

Lists the Python packages required to run the game.

**`.gitignore`**

Specifies files and directories that should not be tracked by Git, such as the virtual environment, Python cache files, and macOS system files.

**`LICENSE`**

Contains the license terms for this project.

**`THIRD_PARTY_NOTICES.md`**

Documents relevant notices and attribution for third-party assets or resources.


## Installation and Setup

### Prerequisites

Make sure Python 3 is installed on your computer.

Check your Python installation:

```bash
python3 --version
```

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/chrome-dino-python.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Open the project directory

```bash
cd chrome-dino-python
```

### 3. Create a virtual environment

```bash
python3 -m venv .venv
```

A virtual environment keeps the project's Python packages separate from other Python projects on your computer.

### 4. Activate the virtual environment

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

This installs Pygame and any other packages listed in the requirements file.

### 6. Run the game

```bash
python main.py
```

The game window should open, and you can start playing.

## How to Play

| Action | Control |
|---|---|
| Jump | Spacebar or Up Arrow |
| Quit the game | Close the game window |

The exact controls depend on the keyboard events implemented in the current version of the game.

### Objective

Avoid the cacti and birds for as long as possible. The longer you survive, the higher your score becomes.

## Game Mechanics

### Dinosaur jumping

The dinosaur jumps in response to keyboard input. Gravity controls the falling motion and returns the dinosaur to the ground.

### Obstacle spawning

The game randomly selects obstacle types and spawn intervals. This creates variation between runs.

### Speed progression

The initial speed is relatively slow. As the score increases, the obstacles move faster until the maximum configured speed is reached.

### Day and night

The game switches between daytime and nighttime periodically. The nighttime scene includes a moon and stars.

### Game over

When a collision is detected, the current run ends. The player can restart the game using the restart behavior implemented in the game code.

## Assets and Credits

This project uses a Chrome Dino-inspired gameplay design and a sprite sheet containing visual assets associated with the Chromium dinosaur game.

The original game and its assets are associated with the Chromium project. This repository is an independent educational project and is not an official Google or Chromium product.

Please refer to `THIRD_PARTY_NOTICES.md` for relevant attribution and licensing information. Check the applicable asset terms before redistributing the sprite sheet separately.

## License

See the `LICENSE` file for the license terms that apply to this project. Third-party assets may be subject to separate terms, as described in `THIRD_PARTY_NOTICES.md`.

---

**Built with Python and Pygame.**

This project was created as a hands-on learning experience in Python game development, sprite handling, animation, collision detection, and game-loop design.
