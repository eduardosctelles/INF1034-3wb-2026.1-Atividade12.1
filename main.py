import pygame, sys
from pygame.locals import QUIT, KEYDOWN

clock = pygame.time.Clock()

#Definição de variáveis e etc
curr_frame = 0
anim_time = 0
pos_x = 100
pos_y = 200
run_animation = False
curr_frame_mm = 0
anim_time_mm = 0
direcao = 0

#mapas
mapa = []


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Jogo teste')

sprite_sheet = pygame.image.load("professor_walk_cycle_no_hat.png")


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        run_animation = True
        direcao = 1
    elif keys[pygame.K_d]:
        run_animation = True
        direcao = 3
    elif keys[pygame.K_w]:
        run_animation = True
        direcao = 0
    elif keys[pygame.K_s]:
        run_animation = True
        direcao = 2
                

    clock.tick(60)
    dt = clock.get_time()

    if run_animation:
        anim_time_mm = anim_time_mm + dt
        anim_time_mm_sec = anim_time_mm / 1000

        if anim_time_mm_sec > 0.1:
            curr_frame_mm = curr_frame_mm + 1
            if direcao == 1:
                pos_x = pos_x - 6.25
            elif direcao == 3:
                pos_x = pos_x + 6.25
            elif direcao == 0:
                pos_y = pos_y - 6.25
            elif direcao == 2:
                pos_y = pos_y + 6.25

            if curr_frame_mm > 9:
                curr_frame_mm = 0
                run_animation = False

            anim_time_mm = 0

    # Desenho dos elementos na tela
    screen.fill((255,255,255))

    if curr_frame_mm < 5:
        screen.blit(sprite_sheet,(pos_x, pos_y),(64 * curr_frame_mm, 0 + 64*direcao, 64, 64))
    else:
        screen.blit(sprite_sheet,(pos_x, pos_y),(64 * (curr_frame_mm - 5), 0 + 64*direcao, 64, 64))

    pygame.display.update()