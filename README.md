# Chrome Dino — Python / Pygame

A Chrome Dino-style runner using the original Chromium 1x sprite sheet.

## Important: add the sprite sheet
This ZIP includes the game code, but not the original sprite image because that image is already on your Mac and could not be retrieved from your local project remotely.

Copy your existing `chrome-dino-sprite.png` into:
`assets/images/chrome-dino-sprite.png`

The expected image is the Chromium 1x sheet, approximately 1233 × 100 pixels. The code crops the dinosaur, cactus, bird, cloud, moon, star, and ground from it.

## Run on macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

If the venv already exists, activate it and run `python main.py`.

## Controls
- SPACE or UP: jump
- DOWN: duck
- SPACE after Game Over: restart

## Gameplay changes
- Slower initial speed: 190 pixels/second.
- Maximum speed: 390 pixels/second.
- Gradual speed increase.
- One shared obstacle scheduler chooses either a cactus or bird.
- Obstacle spawn positions are separated by a randomized 360–500 pixel gap, so the bird is not spawned by a separate timer.
- Day/night alternation, clouds, score, restart and collision detection.

## Structure
```text
chrome-dino-original-sprites/
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
├── THIRD_PARTY_NOTICES.md
├── .gitignore
├── game/
│   ├── __init__.py
│   ├── settings.py
│   ├── assets.py
│   └── game.py
└── assets/
    ├── images/
    │   └── chrome-dino-sprite.png 
    └── sounds/
```

## Attribution
Chromium is an open-source project. The sprite sheet is not bundled in this ZIP. If redistributing that image, retrieve it from the official Chromium source and preserve the relevant copyright and BSD license notices.
