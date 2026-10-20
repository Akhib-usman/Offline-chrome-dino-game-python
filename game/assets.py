"""Crops original Chromium Dino graphics from assets/images/chrome-dino-sprite.png.

The sprite coordinates correspond to Chromium's 1x (LDPI) offline sprite sheet.
"""
from pathlib import Path
import pygame

ROOT = Path(__file__).resolve().parent.parent
SPRITE_PATH = ROOT / "assets" / "images" / "chrome-dino-sprite.png"


class GameAssets:
    def __init__(self):
        if not SPRITE_PATH.exists():
            raise FileNotFoundError(
                "\nOriginal Chromium sprite sheet is missing.\n"
                f"Copy your existing chrome-dino-sprite.png to:\n{SPRITE_PATH}\n"
                "Then run python main.py again."
            )
        self.sheet = pygame.image.load(str(SPRITE_PATH)).convert_alpha()
        self.bounds = self.sheet.get_rect()

    def crop(self, x, y, width, height):
        rect = pygame.Rect(x, y, width, height)
        if not self.bounds.contains(rect):
            raise ValueError(
                f"Sprite crop {rect} is outside sheet size "
                f"{self.sheet.get_size()}. Check the sprite sheet version."
            )
        out = pygame.Surface((width, height), pygame.SRCALPHA)
        out.blit(self.sheet, (0, 0), rect)
        return out

    def load(self):
        # TREX frames start at x=848. These are the standard 1x frame offsets.
        return {
            "trex_wait_1": self.crop(892, 2, 44, 47),
            "trex_wait_2": self.crop(848, 2, 44, 47),
            "trex_run_1": self.crop(936, 2, 44, 47),
            "trex_run_2": self.crop(980, 2, 44, 47),
            "trex_jump": self.crop(848, 2, 44, 47),
            "trex_crash": self.crop(1068, 2, 44, 47),
            "trex_duck_1": self.crop(1112, 2, 59, 47),
            "trex_duck_2": self.crop(1171, 2, 59, 47),

            # Original obstacle and background sprites.
            "bird_1": self.crop(134, 2, 46, 40),
            "bird_2": self.crop(180, 2, 46, 40),
            "small_cactus": self.crop(228, 2, 17, 35),
            "large_cactus": self.crop(332, 2, 25, 50),
            "cloud": self.crop(86, 2, 46, 14),
            "ground": self.crop(2, 54, 600, 12),
            "moon": self.crop(484, 2, 20, 40),
            "star": self.crop(645, 2, 9, 9),
        }
