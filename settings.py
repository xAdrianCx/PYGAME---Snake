

class GameSettings:
    """A class that keeps game settings."""

    # Screen settings.
    screen_width = 1600
    screen_height = 900
    bg_color = (0, 153, 76)

    # Snake settings.
    snake_length = 1
    snake_head = 20
    snake_body = []
    snake_color = (0, 0, 255)
    snake_speed = 20
    snake_lives = 3

    # Bait settings.
    bait_size = 20
    bait_color = (255, 0, 0)

    # Game settings.
    game_speed = 20
    game_paused = False
    game_running = False
    game_over = False
