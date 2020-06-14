import pygame
import  math

pygame.init()

# Variable
Background_Colour = (0, 0, 0)
Earth = (0, 100, 148)
colour = (241, 211, 2)
sunX = 500
sunY = 300
moonX = 680
moonY = 25
sunmass = 1000
moonmass = 1
totalmass = sunmass / moonmass
icon = pygame.image.load("spring-swing-rocket.png")
cy = sunY - 40
cx = sunX - 30
# Window
screen = pygame.display.set_mode((1024, 600))
pygame.display.set_icon(icon)
image = pygame.image.load("moon.png")
pygame.display.set_caption("Gravity")

# Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.FULLSCREEN:
            pygame.display.toggle_fullscreen()



    # Images
    screen.fill(Background_Colour)
    sun = pygame.draw.circle(screen, Earth, (sunX, sunY), 70, 0)
    screen.blit(image, (moonX, moonY))
    # distance
    startcoords = (moonX - sunX)
    startcoords2 = (moonY - sunY)
    sqrcoords = pow(startcoords, 2)
    sqrcoords2 = pow(startcoords2, 2)
    distancebeforesquare = sqrcoords + sqrcoords2
    distance = math.sqrt(distancebeforesquare)
    # Force
    force = (10 * totalmass) / pow(distance, 2)
    if moonX > cx:
        moonX -= force
    if moonY > cy:
        moonY -= force
    if moonX < cx:
        moonX += force
    if moonY < cy:
        moonY += force
    pygame.display.update()
