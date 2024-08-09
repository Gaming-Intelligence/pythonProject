import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Coin Collector")

# Define Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)  # Coin color

# Set up the game clock
clock = pygame.time.Clock()

# Define the Coin class
class Coin:
    def __init__(self):
        self.radius = 20
        self.x = random.randint(self.radius, screen_width - self.radius)
        self.y = -self.radius  # Start above the screen
        self.speed = random.randint(3, 8)  # Random falling speed
        self.collected = False

    def update(self):
        self.y += self.speed  # Move the coin downwards

    def draw(self, screen):
        pygame.draw.circle(screen, GOLD, (self.x, self.y), self.radius)

    def is_collected(self, pos):
        """Check if the coin is tapped or swiped."""
        distance = ((self.x - pos[0]) ** 2 + (self.y - pos[1]) ** 2) ** 0.5
        return distance < self.radius

# Create a list to hold all the coins
coins = []

# Score tracking
score = 0

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if any coin is collected
            mouse_pos = pygame.mouse.get_pos()
            for coin in coins:
                if coin.is_collected(mouse_pos):
                    coin.collected = True
                    score += 1  # Increase the score

    # Add a new coin periodically
    if random.randint(1, 20) == 1:  # Adjust the frequency of new coins
        coins.append(Coin())

    # Update all coins
    for coin in coins:
        coin.update()

    # Remove collected coins or those that fall off the screen
    coins = [coin for coin in coins if not coin.collected and coin.y < screen_height + coin.radius]

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw all coins
    for coin in coins:
        coin.draw(screen)

    # Draw the score
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate to 60 frames per second
    clock.tick(60)

# Quit Pygame
pygame.quit()