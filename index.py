"""
(Quiz) 하늘에서 떨어지는 동선하기 게임을 만드시오
[게임 조건]
1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
2. 등은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
3. 캐릭터가 좋을 피하면 다음 똥이 다시 떨어짐
4. 캐릭터가 등과 충돌하면 게임 종료
5. FPs 는 30 으로 고정

[게임 이미지]
1. 배경 : 648 * 488 (세로 가로) - background. png
2. 캐릭터 : 70* 70 - character.png
3. 똥 : 70 * 70 - enemy. png
"""


import pygame
import random
##################################
#기본 초기화 (It Must be things.)
pygame.init() # reset(reset is essential to write code)


#monitor size settings

screen_width = 480 #Width Size
screen_height = 640 #height Size
screen = pygame.display.set_mode((screen_width, screen_height))

#monitor title settings

pygame.display.set_caption("똥 피하는 게임") #you should make game name

#FPS
clock = pygame.time.Clock()
##################################




#1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 폰트 등)
# 배경 만들기
background = pygame.image.load("/Users/jang-gwangseog/Library/Mobile Documents/com~apple~CloudDocs/CODE/Python/Game/Py_Game_better/Make_better_of_try_No1/Background/background.jpg")


#캐릭터 만들기
character = pygame.image.load("/Users/jang-gwangseog/Library/Mobile Documents/com~apple~CloudDocs/CODE/Python/Game/Py_Game_better/Make_better_of_try_No1/characters/cat.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

#이동 위치
to_x = 0


#똥 만들기

poop = pygame.image.load("/Users/jang-gwangseog/Library/Mobile Documents/com~apple~CloudDocs/CODE/Python/Game/Py_Game_better/Make_better_of_try_No1/characters/poop.png")
poop_size = poop.get_rect().size
poop_width = poop_size[0]
poop_height = poop_size[1]
poop_x_pos = random.randint(0,screen_width - poop_width)
poop_y_pos = 0
poop_speed = 10



#character speed

character_speed = 10

#Event Roop
running = True #You've stil running game? 
while running:
    dt = clock.tick(30)
    """
    print("fps : " + str(clock.get_fps()))
    """
    #이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():#what event happened?
        if event.type == pygame.QUIT: #If You've happened envent that It should closed window?
            running = False #this game isn't  running.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed 
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0



    #3. 게임 케릭터 위치 정의
    character_x_pos += to_x
    
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width


    #poop 처리
    poop_y_pos += poop_speed


    if poop_y_pos > screen_height:
        poop_y_pos = 0
        poop_x_pos = random.randint(0,screen_width - poop_width)
    
    #4. 충돌 처리(캐릭터)
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    #4. 충돌처리(똥)
    poop_rect = poop.get_rect()
    poop_rect.left = poop_x_pos
    poop_rect.top = poop_y_pos


    #충돌 처리 코드
    if character_rect.colliderect(poop_rect):
        print("충돌했어요.")
        running = False




    #5. 화면에 그리기

    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(poop, (poop_x_pos, poop_y_pos))



    pygame.display.update() #Game monitor draw again.(update)


# pygame is being quit
pygame.quit()


