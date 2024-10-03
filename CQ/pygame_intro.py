import pygame 

# Initialize Pygame
pygame.init()

# Create a screen object (width: 640, height: 480)
screen = pygame.display.set_mode((640, 480))

# Set the title of the window
pygame.display.set_caption("My First Pygame Window")

# Define colors
WHITE = (255, 255, 255)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white color
    screen.fill(WHITE)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
