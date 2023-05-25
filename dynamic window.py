import pygame

color = (50,50,50)
title = "window"

def get_info():
    title = input("Title: ")
    color = input("Color:")
    match color:
        case "red":
            color = (255,50,50)
        case "green":
            color = (50,255,50)
        case "blue":
            color = (50,50,255)
        case "black":
            color = (50,50,50)
        case "white":
            color = (240,240,240)

    return title, color

window = pygame.display.set_mode((600,500),pygame.RESIZABLE)

clock = pygame.time.Clock()

running = True

#pygame_icon = pygame.image.load(f"").convert_alpha()

#pygame.display.set_icon(None)

fps = 60

while running:
    pygame.display.set_caption(title)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                letter = chr(event.key)
                title += letter
            if event.key >= pygame.K_a and event.key <= pygame.K_z:
                letter = chr(event.key)
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:  # Check if SHIFT key is pressed
                    letter = letter.upper()
                else:
                    letter = letter.lower()
                title += letter
            if event.key == pygame.K_BACKSPACE:
                letter = chr(event.key)
                modified_title = title[:-1]
                title = modified_title

    if pygame.key.get_pressed()[pygame.K_1]:
        color = (255,50,50)
    if pygame.key.get_pressed()[pygame.K_2]:
        color = (50,255,50)
    if pygame.key.get_pressed()[pygame.K_3]:
        color = (50,50,255)
    if pygame.key.get_pressed()[pygame.K_4]:
        color = (50,50,50)
    if pygame.key.get_pressed()[pygame.K_5]:
        color = (240,240,240)

    clock.tick(fps)
    window.fill(color)
    pygame.display.update()

pygame.quit