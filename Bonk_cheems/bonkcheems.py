import pygame, random

pygame.init()
def run():

    #Create Display Surface
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    #LOAD COLOR
    BLACK = (0, 0, 0)
    ORANGE = (240,158,78)
    BLUE = (85,192,216)
    WHITE = (255, 255, 255)

    #FPS and Clock
    clock = pygame.time.Clock()
    FPS = 60

    #Game Value
    ACCELLERATION = .5
    USER_START_LIVES = 5
    CHEEMS_START_VELOCITY = 3
    dog_dx = random.choice([1, -1])
    cheems_dy = random.choice([1,-1])
    lives = 0
    point = 0
    #LOAD FONT
    font = pygame.font.Font("Bonk_cheems/asset/font.ttf", 32)
    font2 = pygame.font.Font("Bonk_cheems/asset/font.ttf", 60)

    #LOAD TEXT
    point_text = font.render(f'Point:  {point}', True, ORANGE)
    point_text_rect = point_text.get_rect()
    point_text_rect.topleft = (50,32)

    lives_text =  font.render(f'Lives:  {lives}', True, ORANGE)
    lives_text_rect = lives_text.get_rect()
    lives_text_rect.topright = (WINDOW_WIDTH - 50, 32)
    game_over_text = font2.render("GAME OVER, CLICK TO PLAY AGAIN", True, ORANGE)
    game_over_text_rect = game_over_text.get_rect()
    game_over_text_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

    #LOAD IMAGE
    dog = pygame.image.load("Bonk_cheems/asset/dog.png")
    dog_rect = dog.get_rect()
    dog_rect.center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2)
    #Load Sound
    bonk_sound = pygame.mixer.Sound("Bonk_cheems/asset/bonk.mp3")
    miss_sound = pygame.mixer.Sound("Bonk_cheems/asset/miss.mp3")
    game_over_sound = pygame.mixer.Sound("Bonk_cheems/asset/gameover.wav")
    pygame.mixer.music.load("Bonk_cheems/asset/music.mp3")
    pygame.mixer.music.set_volume(.6)


    #BEGIN GAME VALUE
    lives = USER_START_LIVES
    point = 0
    cheems_dx = random.choice([1,-1])
    cheems_dy = random.choice([1,-1])
    cheems_speed = CHEEMS_START_VELOCITY
    cheems_dx = random.choice([1,-1])
    cheems_dy = random.choice([1,-1])
    pygame.mixer.music.play(-1, 0.2)
    dog_rect.center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2)

    #MAIN GAME LOOP
    running = True
    while running:
        #close tab
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #Click the Dog
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]
                if dog_rect.collidepoint((mouse_x, mouse_y)):
                    bonk_sound.play()
                    pre_x = cheems_dx
                    pre_y = cheems_dy
                    while(pre_x == cheems_dx and pre_y == cheems_dy):
                        cheems_dx = random.choice([1, -1])
                        cheems_dy = random.choice([1, -1])
                    point += 1
                    cheems_speed += ACCELLERATION
            #MISS THE DOG
                else:
                    miss_sound.play()
                    lives -= 1
        #Make dog go
        dog_rect.x += cheems_dx * cheems_speed
        dog_rect.y += cheems_dy * cheems_speed

        if dog_rect.left <= 0 or dog_rect.right >= WINDOW_WIDTH:
            cheems_dx *= -1
        if dog_rect.top <=0 or dog_rect.bottom >= WINDOW_HEIGHT:
            cheems_dy *= -1

        #CHECK LOOSE
        if lives == 0:
            game_over_sound.play(-1)
            pygame.mixer.music.stop()
            pause = True
            while pause:
                display_surface.blit(game_over_text, game_over_text_rect)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pause = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        game_over_sound.stop()
                        pause = False
                        lives = USER_START_LIVES
                        point = 0
                        cheems_dx = random.choice([1, -1])
                        cheems_dy = random.choice([1, -1])
                        cheems_speed = CHEEMS_START_VELOCITY
                        cheems_dx = random.choice([1, -1])
                        cheems_dy = random.choice([1, -1])
                        pygame.mixer.music.play(-1, 0.2)
                        dog_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        #Refresh Surface
        display_surface.fill(BLACK)

        #Blit Dog
        display_surface.blit(dog, dog_rect)

        # Blit text
        #ReRender the text when changing
        lives_text = font.render(f'Lives:  {lives}', True, ORANGE)
        point_text = font.render(f'Point:  {point}', True, ORANGE)
        display_surface.blit(point_text, point_text_rect)

        display_surface.blit(lives_text, lives_text_rect)

        #FPS
        clock.tick(FPS)

        #Update
        pygame.display.update()
    game_over_sound.stop()
    pygame.mixer.music.stop()
    display_surface = pygame.display.set_mode((975, 550))
    return point 