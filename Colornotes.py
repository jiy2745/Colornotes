import pygame
import random

#기본설정
pygame.init()
pygame.display.set_caption("Colors")
screen = pygame.display.set_mode((500, 700))
clock = pygame.time.Clock()

img_squares = pygame.image.load("assets/Color_squares.png")
img_notes = pygame.image.load("assets/Color_notes.png")

#변수설정
x = 234
y = 600
state = 1
note_x = [-33] * 10
note_y = [-33] * 10
note_state = [1] * 10
timer = 0
score = 0
best_score = 0
index = 0

font = pygame.font.SysFont("arial", 20, True)

play = True
while play:
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:            
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                state = (state % 4) + 1

    #이동
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        x = x - 10
    if key[pygame.K_d] == True:
        x = x + 10
    if x > 470:
        x = 470
    elif x < 0:
        x = 0
    if timer % 60 == 0:
        note_x[index] = random.randint(50, 450)
        note_y[index] = -32
        note_state[index] = random.randint(1, 4)
        index = (index + 1) % 10

    #음표 이동과 충돌판정
    for i in range(10):
        if note_y[i] >= -32:
            note_y[i] = note_y[i] + 4
        if note_y[i] >= 700:
            for j in range(10):
                note_x[j] = -33
                note_y[j] = -33
            if score > best_score:
                best_score = score
            score = 0
        if ((note_x[i] >= x - 24) and (note_x[i] <= x + 24)) and ((note_y[i] >= y - 26) and (note_y[i] <= y + 26)) and (note_state[i] == state):
            note_y[i] = -33
            score = score + 100

    #화면 그리기
    screen.fill([42, 45, 62])
    for i in range(10):
        screen.blit(img_notes, [note_x[i], note_y[i]], pygame.Rect(32 * (note_state[i] - 1), 0, 32, 32))
    screen.blit(img_squares, [x, y], pygame.Rect(32 * (state - 1), 0, 32, 32))
    font = pygame.font.SysFont("malgungothicsemilightp", 15, True)
    score_text = font.render("current score: " + str(score), True, (255, 255, 255))
    best_score_text = font.render("best score: " + str(best_score), True, (255, 255, 255))
    screen.blit(score_text, [20, 20])
    screen.blit(best_score_text, [20, 60])

    timer = timer + 1
    pygame.display.update()
    clock.tick(60)


pygame.quit()