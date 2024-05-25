import pygame
import sys
from drum import Drum
from note import Note

# Initialize Pygame
pygame.init()

drum_path = 'assets/drum.png'
note_path = 'assets/note.png'
background_path = 'assets/background.png'

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Taiko no Tatsujin')

# Load assets
drum_image = pygame.image.load(drum_path)
note_image = pygame.image.load(note_path)
background_image = pygame.image.load(background_path)

# Define classes
# Create sprite groups
drums = pygame.sprite.Group()
notes = pygame.sprite.Group()

# Calculate drum positions
drum_width = drum_image.get_width()
drum_height = drum_image.get_height()
drum_left_x = (SCREEN_WIDTH // 4) - (drum_width // 2)
drum_right_x = (3 * SCREEN_WIDTH // 4) - (drum_width // 2)
drum_y = SCREEN_HEIGHT - drum_height - 50

# Create drums
drum_left = Drum(drum_left_x, drum_y, drum_image)
drum_right = Drum(drum_right_x, drum_y, drum_image)
drums.add(drum_left, drum_right)

# Initialize score
score = 0
font = pygame.font.Font(None, 74)

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:  # Left drum key
                # Check for collision with notes
                hits = pygame.sprite.spritecollide(drum_left, notes, True)
                if hits:
                    score += 10
                    print("Hit left!")
            elif event.key == pygame.K_j:  # Right drum key
                # Check for collision with notes
                hits = pygame.sprite.spritecollide(drum_right, notes, True)
                if hits:
                    score += 10
                    print("Hit right!")


    # Add notes at intervals (simple example)
    if pygame.time.get_ticks() % 2000 < 20:  # Adjust timing for real gameplay
        note = Note(SCREEN_WIDTH, SCREEN_HEIGHT - 150, 5, note_image)
        notes.add(note)

    # Update notes
    notes.update()

    # Draw everything
    screen.blit(background_image, (0, 0))
    drums.draw(screen)
    notes.draw(screen)

    # Render the score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()

