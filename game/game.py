import random
import pygame

from .settings import (
    WIDTH, HEIGHT, FPS, GROUND_Y, DINO_X,
    START_SPEED, MAX_SPEED, SPEED_INCREASE_PER_SECOND,
    GAP_MIN, GAP_MAX, BIRD_CHANCE, BIRDS_START_SCORE,
)
from .assets import GameAssets


class DinoGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Chrome Dino — Python Edition")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 16, bold=True)
        self.big_font = pygame.font.SysFont("Arial", 21, bold=True)
        self.assets = GameAssets()
        self.s = self.assets.load()
        self.reset()

    def reset(self):
        self.night = False
        self.moon_x = float(WIDTH - 150)
        self.star_offset = 0.0
        self.score = 0.0
        self.speed = START_SPEED
        self.game_over = False
        self.jumping = False
        self.ducking = False
        self.dino_y = float(GROUND_Y - 47)
        self.dino_vy = 0.0
        self.anim_time = 0.0
        self.anim_frame = 0
        self.ground_offset = 0.0
        self.clouds = [
            {"x": 90.0, "y": 55}, {"x": 420.0, "y": 90},
            {"x": 740.0, "y": 42},
        ]
        self.cloud_timer = 0.0
        self.obstacles = []
        self.next_spawn_x = float(WIDTH + random.randint(180, 260))
        self.next_gap = random.randint(GAP_MIN, GAP_MAX)
        self.night = False
        self.day_night_timer = 0.0
        self.night_duration = 0.0

    def choose_obstacle(self):
        # Single queue: one spawn decision produces a cactus OR a bird.
        if self.score >= BIRDS_START_SCORE and random.random() < BIRD_CHANCE:
            y = random.choice([GROUND_Y - 82, GROUND_Y - 58, GROUND_Y - 39])
            return {
                "kind": "bird", "x": float(WIDTH + 10), "y": float(y),
                "frame": 0, "anim": 0.0,
            }
        large = random.random() < 0.35
        image = self.s["large_cactus"] if large else self.s["small_cactus"]
        return {
            "kind": "cactus", "x": float(WIDTH + 10),
            "y": float(GROUND_Y - image.get_height()), "large": large,
        }

    def obstacle_image(self, obstacle):
        if obstacle["kind"] == "bird":
            return self.s["bird_1"] if obstacle["frame"] == 0 else self.s["bird_2"]
        return self.s["large_cactus"] if obstacle["large"] else self.s["small_cactus"]

    def update(self, dt):
        if self.game_over:
            return

        self.score += dt * 10
        # Starts at 190 px/s, rises slowly, and caps at 390 px/s.
        self.speed = min(
            START_SPEED + self.score * SPEED_INCREASE_PER_SECOND / 10,
            MAX_SPEED,
        )

        # Gentle day/night alternation.
        self.day_night_timer += dt
        if self.day_night_timer >= 18:
            self.day_night_timer = 0
            self.night = not self.night

        # Slowly move the moon and stars during nighttime
        if self.night:
            self.moon_x -= 8 * dt
            self.star_offset -= 5 * dt

            # Return them to their starting area after a short drift
            if self.moon_x < WIDTH - 220:
                self.moon_x = float(WIDTH - 150)

            if self.star_offset < -40:
                self.star_offset = 0.0

        keys = pygame.key.get_pressed()
        self.ducking = bool(keys[pygame.K_DOWN] and not self.jumping)

        if self.jumping:
            self.dino_vy += 1500 * dt
            self.dino_y += self.dino_vy * dt
            if self.dino_y >= GROUND_Y - 47:
                self.dino_y = float(GROUND_Y - 47)
                self.dino_vy = 0.0
                self.jumping = False

        self.anim_time += dt
        frame_delay = 0.085 if not self.ducking else 0.12
        if self.anim_time >= frame_delay:
            self.anim_time = 0
            self.anim_frame = 1 - self.anim_frame

        self.ground_offset = (self.ground_offset + self.speed * dt) % self.s["ground"].get_width()

        # Clouds move independently from ground.
        self.cloud_timer += dt
        for cloud in self.clouds:
            cloud["x"] -= 30 * dt
        self.clouds = [c for c in self.clouds if c["x"] > -60]
        if self.cloud_timer >= 3.0:
            self.clouds.append({"x": WIDTH + 20.0, "y": random.randint(30, 95)})
            self.cloud_timer = 0.0

        # Single obstacle scheduler with a consistent distance gap.
        if not self.obstacles:
            self.obstacles.append(self.choose_obstacle())
            self.next_gap = random.randint(GAP_MIN, GAP_MAX)
        else:
            last = self.obstacles[-1]
            # Trigger next spawn only once prior obstacle has moved left
            # by the configured gap. This avoids independent bird/cactus overlaps.
            if last["x"] <= WIDTH - self.next_gap:
                self.obstacles.append(self.choose_obstacle())
                self.next_gap = random.randint(GAP_MIN, GAP_MAX)

        for obstacle in self.obstacles:
            obstacle["x"] -= self.speed * dt
            if obstacle["kind"] == "bird":
                obstacle["anim"] += dt
                if obstacle["anim"] >= 0.14:
                    obstacle["frame"] = 1 - obstacle["frame"]
                    obstacle["anim"] = 0.0
        self.obstacles = [o for o in self.obstacles if o["x"] > -80]

        # Collision rectangles use slight inset for fair play.
        if self.ducking:
            dino_rect = pygame.Rect(DINO_X + 6, GROUND_Y - 24, 46, 20)
        else:
            dino_rect = pygame.Rect(DINO_X + 5, int(self.dino_y) + 4, 34, 39)
        for obstacle in self.obstacles:
            img = self.obstacle_image(obstacle)
            rect = pygame.Rect(
                int(obstacle["x"]) + 3, int(obstacle["y"]) + 3,
                max(1, img.get_width() - 6), max(1, img.get_height() - 6),
            )
            if dino_rect.colliderect(rect):
                self.game_over = True
                break

    def draw(self):
        bg = (25, 25, 28) if self.night else (247, 247, 247)
        ink = (235, 235, 235) if self.night else (83, 83, 83)
        self.screen.fill(bg)

        # Original cloud sprites.
        for cloud in self.clouds:
            self.screen.blit(self.s["cloud"], (int(cloud["x"]), cloud["y"]))


        if self.night:
            # Draw the slowly moving moon
            self.screen.blit(
                self.s["moon"],
                (int(self.moon_x), 30),
            )

            # Draw the slowly moving stars
            for x, y in [(650, 45), (710, 78), (810, 55), (570, 35)]:
                star_x = int(x + self.star_offset)

                if 0 <= star_x < WIDTH:
                    self.screen.blit(
                        self.s["star"],
                        (star_x, y),
                    )


        # Repeat the original horizon/ground crop to cover the full viewport.
        ground = self.s["ground"]
        gw = ground.get_width()
        offset = int(self.ground_offset % gw)
        for x in range(-gw, WIDTH + gw, gw):
            self.screen.blit(ground, (x - offset, GROUND_Y))

        # Obstacles.
        for obstacle in self.obstacles:
            self.screen.blit(
                self.obstacle_image(obstacle),
                (int(obstacle["x"]), int(obstacle["y"])),
            )

        # Original T-Rex frames.
        if self.game_over:
            dino = self.s["trex_crash"]
        elif self.ducking:
            dino = self.s["trex_duck_1"] if self.anim_frame == 0 else self.s["trex_duck_2"]
        elif self.jumping:
            dino = self.s["trex_jump"]
        else:
            dino = self.s["trex_run_1"] if self.anim_frame == 0 else self.s["trex_run_2"]
        dy = GROUND_Y - dino.get_height() if self.ducking else int(self.dino_y)
        self.screen.blit(dino, (DINO_X, dy))

        # Score.
        score = self.font.render(f"{int(self.score):05d}", True, ink)
        self.screen.blit(score, (WIDTH - score.get_width() - 22, 18))

        if self.game_over:
            # Text is rendered in a matching monochrome style; original sprite
            # sheet's score/text atlas varies between Chromium versions.
            label = self.big_font.render("GAME OVER", True, ink)
            restart = self.font.render("Press SPACE to restart", True, ink)
            self.screen.blit(label, label.get_rect(center=(WIDTH // 2, 112)))
            self.screen.blit(restart, restart.get_rect(center=(WIDTH // 2, 142)))
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            dt = min(self.clock.tick(FPS) / 1000.0, 0.04)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_SPACE, pygame.K_UP):
                        if self.game_over:
                            self.reset()
                        elif not self.jumping and not self.ducking:
                            self.jumping = True
                            self.dino_vy = -560.0
            self.update(dt)
            self.draw()
        pygame.quit()
