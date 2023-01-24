import pygame, random

pygame.init()
def run():
    #Create display surface
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    #Define some colors
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0 , 0)
    DARK_GREEN = (145,219,230)
    LIGHT_BLUE = (171,219,227)
    ORANGE = (226,135,67)

    #LOAD Sound
    pygame.mixer.music.load("Snake/asset_snake/music.mp3")
    pygame.mixer.music.set_volume(.5)

    collect_sound = pygame.mixer.Sound('Snake/asset_snake/collect.mp3')
    game_over_sound = pygame.mixer.Sound('Snake/asset_snake/gameover.wav')
    game_over_sound.set_volume(.3)

    #FPS and Clock
    clock = pygame.time.Clock()
    FPS = 60

    #GAME VALUE
    SNAKE_SIZE = 20
    SNAKE_BEGIN_SPEED = 4
    ACCELERATION = .1
    point = 0
    snake_dx = 0
    snake_dy = 0
    head_x = WINDOW_WIDTH // 2
    head_y = WINDOW_HEIGHT // 2
    head_coor = (head_x, head_y , SNAKE_SIZE, SNAKE_SIZE)
    head_rect = pygame.draw.rect(display_surface,GREEN,head_coor,2)
    apple_x = random.randint(0, WINDOW_WIDTH - SNAKE_SIZE)
    apple_y = random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE)
    apple_coor = (apple_x, apple_y ,SNAKE_SIZE, SNAKE_SIZE)
    apple_rect = pygame.draw.rect(display_surface,RED,apple_coor,0)
    head_body = []
    #Font Text
    font = pygame.font.Font("Snake/asset_snake/font.ttf", 32)
    font2 = pygame.font.Font("Snake/asset_snake/font.ttf", 46)
    point_text = font.render(f'Point:  {point}', True, LIGHT_BLUE,ORANGE)
    point_text_rect = point_text.get_rect()
    point_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

    game_over_text =font2.render('Game OVER, PRESS ENTER TO PLAY AGAIN', True, GREEN,DARK_GREEN)
    game_over_text_rect = game_over_text.get_rect()
    game_over_text_rect.center = (WINDOW_WIDTH //2, WINDOW_HEIGHT//2 + 100)


    #BEGIN GAME
    pygame.mixer.music.play()
    point = 0
    hight_point=0
    snake_dx = 0
    snake_dy = 0
    head_x = WINDOW_WIDTH // 2
    head_y = WINDOW_HEIGHT // 2
    head_coor = (head_x, head_y , SNAKE_SIZE, SNAKE_SIZE)
    head_rect = pygame.draw.rect(display_surface,GREEN,head_coor,2)
    apple_x = random.randint(0, WINDOW_WIDTH - SNAKE_SIZE)
    apple_y = random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE)
    apple_coor = (apple_x, apple_y ,SNAKE_SIZE, SNAKE_SIZE)
    apple_rect = pygame.draw.rect(display_surface,RED,apple_coor,0)
    snake_speed = SNAKE_BEGIN_SPEED
    head_body = []

    #MAIN GAME LOOP
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                display_surface = pygame.display.set_mode((975, 550))
                return hight_point
        #Control the Snake
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if snake_dx == 0:
                        snake_dx = -1
                        snake_dy = 0

                if event.key == pygame.K_RIGHT:
                    if snake_dx == 0:
                        snake_dx = 1
                        snake_dy = 0

                if event.key == pygame.K_UP:
                    if snake_dy == 0:
                        snake_dx = 0
                        snake_dy = -1

                if event.key == pygame.K_DOWN:
                    if snake_dy == 0:
                        snake_dx = 0
                        snake_dy = 1
        #Move the Snake
        head_x += snake_speed*snake_dx
        head_y += snake_speed*snake_dy
        #Before Update THe new head Snake, add Store Old one
        head_body.insert(0, head_coor)
        head_body.pop()

        head_coor = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
        #Check loose
        if head_rect.left < 0 or head_rect.top < 0 or head_rect.right > WINDOW_WIDTH or head_rect.bottom > WINDOW_HEIGHT or head_coor in head_body:
            display_surface.blit(game_over_text, game_over_text_rect)
            pygame.display.update()
            pause = True
            pygame.mixer.music.stop()
            while pause:
                game_over_sound.play()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pause = False
                        display_surface = pygame.display.set_mode((975, 550))
                        return hight_point
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            pause = False
                            game_over_sound.stop()
                            pygame.mixer.music.play()
                            point = 0
                            snake_dx = 0
                            snake_dy = 0
                            head_x = WINDOW_WIDTH // 2
                            head_y = WINDOW_HEIGHT // 2
                            head_coor = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
                            head_rect = pygame.draw.rect(display_surface, GREEN, head_coor, 2)
                            apple_x = random.randint(0, WINDOW_WIDTH - SNAKE_SIZE)
                            apple_y = random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE)
                            apple_coor = (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE)
                            apple_rect = pygame.draw.rect(display_surface, RED, apple_coor, 0)
                            snake_speed = SNAKE_BEGIN_SPEED
                            head_body = []
        #Refresh Surface
        display_surface.fill(BLACK)

        #Blit Text
        point_text = font.render(f'Point:  {point}', True, LIGHT_BLUE, ORANGE)
        point_hight_text = font.render(f'Hight_Point:  {hight_point}', True, LIGHT_BLUE)
        display_surface.blit(point_text, point_text_rect)
        display_surface.blit(point_hight_text, (20,20))

        #Blit the Snake
        for body in head_body:
            pygame.draw.rect(display_surface, GREEN, body, 0)
        head_rect = pygame.draw.rect(display_surface,DARK_GREEN,head_coor,0)
        apple_rect = pygame.draw.rect(display_surface, (255 - random.randint(0,100),random.randint(0,50),random.randint(0,20)), apple_coor, 0)

        #Update Display
        pygame.display.update()

        # Check Meeting
        if head_rect.colliderect(apple_rect):
            apple_x = random.randint(0, WINDOW_WIDTH - SNAKE_SIZE)
            apple_y = random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE)
            apple_coor = (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE)
            point += 1
            hight_point=max(point,hight_point)
            snake_speed += ACCELERATION
            collect_sound.play()
            head_body.append(head_coor)
        #Clock Tick
        clock.tick(FPS)
  