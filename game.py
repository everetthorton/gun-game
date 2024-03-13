
import pygame
import random
pygame.init()
running = True
pygame.mouse.set_visible(False)
window = pygame.display.set_mode([1000, 1000])
num1 = random.randint(1, 96)
num2 = random.randint(1, 96)
num1 *= 10
num2 *= 10
z = 500
v = 500
pos_1 = 10
pos_2 = 960
health = 5
gun = "ar"
ar_ammo = 36
sniper_ammo = 4
pistol_ammo = 24
shotgun_ammo = 12
zoom = False
while running:
    x, y = pygame.mouse.get_pos()
    crosshair1 = pygame.Rect(x, y, 5, 17)
    crosshair2 = pygame.Rect(x + 7, y - 7, 17, 5)
    crosshair3 = pygame.Rect(x - 18, y - 7, 17, 5)
    crosshair4 = pygame.Rect(x, y - 25, 5, 17)
    window.fill((123, 123, 123))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        gun = "ar"
    if keys[pygame.K_2]:
        gun = "shotgun"
    if keys[pygame.K_3]:
        gun = "sniper"
    if keys[pygame.K_4]:
        gun = "pistol"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if gun == "ar" and ar_ammo >= 1:
                ar_ammo -= 1
                print("shots fired")
            if gun == "sniper" and sniper_ammo >= 1:
                sniper_ammo -= 1
                print("sniper fired")
            if gun == "pistol" and pistol_ammo >= 1:
                pistol_ammo -= 1
                print("pistol shot")
            if gun == "shotgun" and shotgun_ammo >= 1:
                shotgun_ammo -= 1
                print("shotgun shot")
            if gun == "ar" and ar_ammo == 0:
                print("your out of ar ammo")
            if gun == "shotgun" and shotgun_ammo == 0:
                print("your out of shotgun ammo")
            if gun == "sniper" and sniper_ammo == 0:
                print("your out of sniper ammo")
            if gun == "pistol" and pistol_ammo == 0:
                print("your out of pistol ammo")
    health_bar1 = pygame.Rect(pos_1, pos_2, 200, 30)
    health_bar2 = pygame.Rect(pos_1, pos_2, 160, 30)
    health_bar3 = pygame.Rect(pos_1, pos_2, 120, 30)
    health_bar4 = pygame.Rect(pos_1, pos_2, 80, 30)
    health_bar5 = pygame.Rect(pos_1, pos_2, 40, 30)
    health_bar_shadow = pygame.Rect(pos_1 - 5, pos_2 - 5, 210, 40)
    player = pygame.Rect(z, v, 40, 40)
    shadow = pygame.Rect(z + 5, v + 5, 40, 40)
    window.fill((123, 123, 123))
    pygame.draw.rect(window, (80, 80, 80), shadow)
    pygame.draw.rect(window, (150, 75, 0), player)
    if gun == "ar":
        pygame.draw.rect(window, (255, 255, 255), crosshair1)
        pygame.draw.rect(window, (255, 255, 255), crosshair2)
        pygame.draw.rect(window, (255, 255, 255), crosshair3)
        pygame.draw.rect(window, (255, 255, 255), crosshair4)
    if gun == "shotgun":
        pygame.draw.polygon(window, (255, 255, 255), [(x - 25, y), (x, y - 25), (x + 25, y), (x, y + 25)], 5)
    if gun == "sniper":
        pygame.draw.line(window, (255, 255, 255), (x - 25, y - 25), (x, y), 5)
        pygame.draw.line(window, (255, 255, 255), (x - 2, y - 1), (x + 25, y - 25), 5)
    if gun == "pistol":
        print("pistol")
    pygame.draw.rect(window, (100, 100, 100), health_bar_shadow)
    if health == 5:
        pygame.draw.rect(window, (230, 20, 0), health_bar1)
    if health == 4:
        pygame.drwa.rect(window, (230, 20, 0), health_bar2)
    if health == 3:
        pygame.drwa.rect(window, (230, 20, 0), health_bar3)
    if health == 2:
        pygame.drwa.rect(window, (230, 20, 0), health_bar4)
    if health == 1:
        pygame.draw.rect(window, (230, 20, 0), health_bar5)
    if keys[pygame.K_a]:
        z -= 5
    if keys[pygame.K_d]:
        z += 5
    if keys[pygame.K_w]:
        v -= 5
    if keys[pygame.K_s]:
        v += 5             
    if keys[pygame.K_LEFT]:
        z -= 5
    if keys[pygame.K_RIGHT]:
        z += 5
    if keys[pygame.K_UP]:
        v -= 5
    if keys[pygame.K_DOWN]:
        v += 5               
    pygame.display.flip()
    #replit
    #visual code studio

