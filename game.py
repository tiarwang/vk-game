import pygame
import sys
import random
from drum import Drum
from note import Note

# Initialize Pygame
pygame.init()

drum_path = 'assets/drum.png'
note1_path = 'assets/note1.png'
note2_path = 'assets/note2.png'
background_path = 'assets/background.png'

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Taiko no Tatsujin')

# Load assets
drum_image = pygame.image.load(drum_path)
note1_image = pygame.image.load(note1_path)
note2_image = pygame.image.load(note2_path)
background_image = pygame.image.load(background_path)

# Create sprite groups
drums = pygame.sprite.Group()
notes = pygame.sprite.Group()

# Calculate drum position
drum_width = drum_image.get_width()
drum_height = drum_image.get_height()
drum_x = (SCREEN_WIDTH // 2) - (drum_width // 2)
drum_y = SCREEN_HEIGHT - drum_height - 50

# Create drum
drum = Drum(drum_x, drum_y, drum_image)
drums.add(drum)

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
            if event.key == pygame.K_f:  # Key for note1
                # Check for collision with notes
                hits = pygame.sprite.spritecollide(drum, notes, False)
                for hit in hits:
                    if hit.note_type == 'note1':
                        hit.kill()  # Remove the note
                        score += 10
                        print("Hit note1!")
            elif event.key == pygame.K_j:  # Key for note2
                # Check for collision with notes
                hits = pygame.sprite.spritecollide(drum, notes, False)
                for hit in hits:
                    if hit.note_type == 'note2':
                        hit.kill()  # Remove the note
                        score += 10
                        print("Hit note2!")

    # Add notes at intervals (simple example)
    if pygame.time.get_ticks() % 2000 < 20:  # Adjust timing for real gameplay
        note_type = random.choice(['note1', 'note2'])
        if note_type == 'note1':
            note = Note(SCREEN_WIDTH, SCREEN_HEIGHT - 150, 5, note1_image, 'note1')
        else:
            note = Note(SCREEN_WIDTH, SCREEN_HEIGHT - 150, 5, note2_image, 'note2')
        notes.add(note)

    # Update notes
    notes.update()

    # Draw everything
    screen.blit(background_image, (0, 0))  # Clear screen with background
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
