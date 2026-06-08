import pygame, sys
from pygame.locals import QUIT, KEYDOWN

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Jogo teste')

clock = pygame.time.Clock()
tileset = pygame.image.load("[64x64] Rocky Grass.png")
#Definição de variáveis e etc
curr_frame = 0
anim_time = 0
pos_x = 100
pos_y = 390
run_animation = False
curr_frame_mm = 0
anim_time_mm = 0
direcao = 0
tile_size_joguinho = 64
collider_1 = pygame.Rect(0, 0, 0, 0)

f = open("mapa.txt", "r")
mapa = [line.strip() for line in f.readlines()]
f.close()

def renderiza_mapa(mapa):
    global collider_1
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == "G":
                screen.blit(tileset, (j * tile_size_joguinho, i * tile_size_joguinho), (64, 0, tile_size_joguinho, tile_size_joguinho))
            elif mapa[i][j] == "T":
                screen.blit(tileset, (j * tile_size_joguinho, i * tile_size_joguinho), (64, 64, tile_size_joguinho, tile_size_joguinho))
            elif mapa[i][j] == "A":
                screen.blit(tileset, (j * tile_size_joguinho, i * tile_size_joguinho), (128, 0, tile_size_joguinho, tile_size_joguinho))
            elif mapa[i][j] == "B":
                screen.blit(tileset, (j * tile_size_joguinho, i * tile_size_joguinho), (192, 192, tile_size_joguinho, tile_size_joguinho))
                collider_1 = pygame.Rect(j * tile_size_joguinho, i * tile_size_joguinho, 64, 64)
                pygame.draw.rect(screen, (0, 0, 255), collider_1, 2)
            elif mapa[i][j] == "P":
                screen.blit(tileset, (j * tile_size_joguinho, i * tile_size_joguinho), (128, 64, tile_size_joguinho, tile_size_joguinho))

sprite_sheet = pygame.image.load("professor_walk_cycle_no_hat.png")


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    old_pos_x = pos_x

    if keys[pygame.K_a]:
        run_animation = True
        direcao = 1
    elif keys[pygame.K_d]:
        run_animation = True
        direcao = 3

    screen.fill((255,255,255))

    renderiza_mapa(mapa)

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

            if curr_frame_mm > 9:
                curr_frame_mm = 0
                run_animation = False

            anim_time_mm = 0

    if pos_x + 16 <= 0:
        pos_x = 0
        run_animation = False
    if pos_x + 16 + 32 >= 800:
        pos_x = 800 - 64
        run_animation = False

    collider_jogador = pygame.Rect(pos_x + 16, pos_y, 32, 64)
    if collider_jogador.colliderect(collider_1):
        pos_x = old_pos_x
        run_animation = False

    if curr_frame_mm < 5:
        screen.blit(sprite_sheet,(pos_x, pos_y),(64 * curr_frame_mm, 0 + 64*direcao, 64, 64))
    else:
        screen.blit(sprite_sheet,(pos_x, pos_y),(64 * (curr_frame_mm - 5), 0 + 64*direcao, 64, 64))

    pygame.display.update()