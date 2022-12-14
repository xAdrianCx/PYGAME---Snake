import pygame


class Snake:
    """A class that models a snake"""

    def __init__(self, gs, screen):
        """Initialize snake attributes"""
        self.gs = gs
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Create a rectangle.
        self.rect = pygame.Rect(0, 0, self.gs.snake_head, self.gs.snake_head)
        # Position the snake in the middle of the screen.
        self.rect.center = (self.screen_rect.centerx - (self.gs.snake_head / 2), self.screen_rect.centery)
        # Get the pressed key.
        self.key_pressed = None

    def update(self):
        """A method that updates the snake position."""
        if self.key_pressed == pygame.K_UP:
            self.rect.top -= self.gs.snake_speed
        if self.key_pressed == pygame.K_DOWN:
            self.rect.bottom += self.gs.snake_speed
        if self.key_pressed == pygame.K_LEFT:
            self.rect.left -= self.gs.snake_speed
        if self.key_pressed == pygame.K_RIGHT:
            self.rect.right += self.gs.snake_speed

    def reset(self):
        """ Position the snake in the middle of the screen after it hits an edge.
        Also decrease lives left."""
        self.rect.center = (self.screen_rect.centerx - (self.gs.snake_head / 2), self.screen_rect.centery)
        self.key_pressed = None
        self.gs.snake_body.clear()
        self.gs.snake_lives -= 1


    def draw_snake(self):
        """ Draws the snake on the screen"""
        # Update snake length and draw it to the screen.
        self.gs.snake_body.append(self.rect.copy())
        self.gs.snake_body = self.gs.snake_body[-self.gs.snake_length:]
        [pygame.draw.rect(self.screen, self.gs.snake_color, block) for block in self.gs.snake_body]
