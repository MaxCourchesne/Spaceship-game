#___imports
import pygame
import time
import math
import random
pygame.mixer.init()


#________________________________________________________________fun variables
#75
maxSizeEnemyInt = 75
#2
MaxSizeIncreaseSpeed = 3
#3
MaxSpeedIncreaseSpeed = 3
#10 divisor of 1000
speedAddEnemy = 10
#50
playerSizeInt = 50
#600
speedSpawnBoostMin = 800
#1200
speedSpawnBoostMax = 1200
#1000
OnBoost_timer_int = 1000
#15
bulletSize = 15
speedBulletsInt = 4
#8
speedBulletsPp = 8
#70
bullet_strenght_Int = 90
#100
speed_increase_life_enemy = 100
# 800
speedSpawnPpMin = 800
# 1200
speedSpawnPpMax = 1200
# (bullet_strenght_Int * 3)
bullet_strenght_pp = (bullet_strenght_Int * 5)
#2000
packapunchTimerInt = 2000
#________________________________________________________________fun variables end
#_variables
score = 0
gameRunning = True
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
grey = (80, 80, 80)
screenWidth = 1000
screenHeight = 750
numOfLoops = 1
xtra_loop = 0
timeIncreaseEnemy = 3
show_pp_name = False
show_boost_name = False
#20
boostSize = 20
rangeSpawnBoost = random.randint(int(speedSpawnBoostMin), int(speedSpawnBoostMax))
OnBoost = False
OnBoost_timer = OnBoost_timer_int
count_for_colors = 0
count_time_spawn_boost = 0
#_____________________________________________________________________________________________________________not obligated to take pink cube
is_packapunch = False
color_bullet_int = grey
color_unit_pp = (255, 0, 255)
colorBulletPp = green
color_bullet = color_bullet_int
count_time_spawn_pp = 0
packapunchTimer = packapunchTimerInt
bullet_strenght = bullet_strenght_Int
speedBullets = speedBulletsInt
show_pp_name_timer_int = 200
show_pp_name_timer = show_pp_name_timer_int
show_boost_name_timer_int = 200
show_boost_name_timer = show_boost_name_timer_int
#-----------------------------------------------------------------------------------------------------------------------test
image_spaceship = pygame.image.load("spaceship_for_game_space.png")
image_pp = pygame.image.load("packapuch_name.png")
image_boost = pygame.image.load("boost_name.png")
#map = pygame.image.load("map.png")
#___initialise screen

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_icon(pygame.image.load("spaceship.png"))
pygame.display.set_caption("Space Wars")

#___classes


class enemy:
    maxEnemys = 1
    def __init__(self, posX, posY, size, speed):
        self.speed = speed
        self.posX = posX
        self.posY = posY
        self.size = size
        self.life = size * 4 + int(numOfLoops/(1000/speed_increase_life_enemy))
    def draw(self):
        pygame.draw.rect(screen, red, (self.posX, self.posY, self.size, self.size))


    def TestColision(self):
        if self.posX < spaceship.posX and (self.posX + self.size) > spaceship.posX or self.posX > spaceship.posX and self.posX < (spaceship.posX + spaceship.size):
            if self.posY < spaceship.posY and (self.posY + self.size) > spaceship.posY or self.posY > spaceship.posY and (spaceship.posY + spaceship.size) > self.posY:
                return True
        return False


class bullet:
    bulletSpeed = 1
    bulletStrenght = 1
    def __init__(self, posX, posY, size):
        self.posX = posX
        self.posY = posY
        self.size = size

    def TestColision(self, enemy_x, enemy_y, enemy_size):
        if self.posX < enemy_x and (self.posX + self.size) > enemy_x or self.posX > enemy_x and self.posX < (enemy_x + enemy_size):
            if self.posY < enemy_y and (self.posY + self.size) > enemy_y or self.posY > enemy_y and (enemy_y + enemy_size) > self.posY:
                return True
        return False

    def draw(self):
        pygame.draw.rect(screen, color_bullet, (self.posX, self.posY, self.size, self.size))

    def shoot(self):
        listBullets.append(bullet((spaceship.posX + (spaceship.size/2) - (bulletSize/2)), (spaceship.posY - bulletSize), bulletSize))


class boost(enemy):
    def __init__(self, posX, posY, size, speed, color):
        super().__init__(posX, posY, size, speed)
        self.color = color
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.posX, self.posY, self.size, self.size))
        #print("drew a square")



class packapunch(enemy):
    def __init__(self, posX, posY, size, speed, color):
        super().__init__(posX, posY, size, speed)
        self.color = color
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.posX, self.posY, self.size, self.size))
        #print("drew a square")





class player:
    def __init__(self, color, size, posX, posY):
        self.color = color
        self.posX = posX
        self.posY = posY
        self.size = size

    def draw(self):
        # -----------------------------------------------------------------------------------------------------------------------test

        if not OnBoost:
            screen.blit(image_spaceship, (self.posX, self.posY))
        elif OnBoost:
            pygame.draw.rect(screen, self.color, (self.posX, self.posY, self.size, self.size))

#___player initialize
spaceship = player(white, playerSizeInt, (screenWidth/2 - (playerSizeInt/2)), (screenHeight - (playerSizeInt + 20)))

#___functions

def createEnemy():
    if len(listEnemys) <= enemy.maxEnemys:
        size = random.randint(10, (maxSizeEnemyInt + int(numOfLoops/1000) * MaxSizeIncreaseSpeed))
        posX = random.randint(int(0 - size/2), int(screenWidth - size/2))
        speed = random.randint(4, (15 + int(numOfLoops/600) * MaxSpeedIncreaseSpeed))
        listEnemys.append(enemy(posX, 0, size, speed))

def createBoost():
        size = 20
        posX = random.randint(int(0 - size/2), int(screenWidth - size/2))
        speed = 10
        listBoosts.append(boost(posX, 0, size, speed, blue))


def createPackapunch():
    size = 20
    posX = random.randint(int(0 - size / 2), int(screenWidth - size / 2))
    speed = 10
    listPackapunch.append(packapunch(posX, 0, size, speed, color_unit_pp))

#___lists

listEnemys = []
listBullets = []
listBoosts = []
listPackapunch = []
createEnemy()
#___________________________________________________________________________________________________________________________________________________________game loop

#screen.blit(map, (0, 0))
while gameRunning:
    screen.fill((50, 0, 50))
    #screen.blit(map, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if spaceship.posX >= playerSizeInt:
                    spaceship.posX -= playerSizeInt
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if spaceship.posX <= screenWidth - (playerSizeInt*2):
                    spaceship.posX += playerSizeInt

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if spaceship.posY >= (0 + spaceship.size):
                    spaceship.posY -= playerSizeInt

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if spaceship.posY < (screenHeight - (spaceship.size*1.5)):
                    spaceship.posY += playerSizeInt

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet.shoot("")



    #if listBullets:

        #print(f"posX = {listBullets[0].posX} poxY = {listBullets[0].posY} size = {listBullets[0].size}.")

    spaceship.draw()

    for _boost_ in listBoosts:
        _boost_.draw()
        _boost_.posY += 3
        if _boost_.TestColision():
            listBoosts = []
            show_boost_name = True
            OnBoost = True

            #______________________________________________________________test can erase

    for unit in listPackapunch:
        unit.draw()
        unit.posY += 2
        if unit.TestColision():
            listPackapunch = []
            # ______________________________________________________________test can erase
            is_packapunch = True
            show_pp_name = True

    if show_pp_name:
        if show_pp_name_timer > 0:
            show_pp_name_timer -= 1
            screen.blit(image_pp, (200, 300))
        else:
            show_pp_name = False
            show_pp_name_timer = show_pp_name_timer_int


    if show_boost_name:
        if show_boost_name_timer > 0:
            show_boost_name_timer -= 1
            screen.blit(image_boost, (200, 300))
        else:
            show_boost_name = False
            show_boost_name_timer = show_boost_name_timer_int




    if count_for_colors < 255:
        shipColorOnBoost1 = count_for_colors
    elif count_for_colors >= 255 and count_for_colors < 510:
        shipColorOnBoost2 = count_for_colors - 255
        shipColorOnBoost1 = 100
    elif count_for_colors >= 510 and count_for_colors < 765:
        shipColorOnBoost3 = count_for_colors - 510
        shipColorOnBoost2 = 100
        shipColorOnBoost1 = 0
    else:
        count_for_colors = 0


    if OnBoost:
        if OnBoost_timer > 0:
            spaceship.color = (shipColorOnBoost1, shipColorOnBoost2, shipColorOnBoost3)
            spaceship.size = 15
            OnBoost_timer -= 1
        else:
            spaceship.size = 50
            OnBoost = False
            OnBoost_timer = OnBoost_timer_int
            spaceship.color = white



    if is_packapunch:
        if packapunchTimer > 0:
            packapunchTimer -= 1
            color_bullet = colorBulletPp
            image_spaceship = pygame.image.load("spaceship_for_game_2.png")
            bullet_strenght = bullet_strenght_pp
            speedBullets = speedBulletsPp
        else:
            packapunchTimer = packapunchTimerInt
            is_packapunch = False
            bullet_strenght = bullet_strenght_Int
            speedBullets = speedBulletsInt
            image_spaceship = pygame.image.load("spaceship_for_game_space.png")

    else:
        color_bullet = color_bullet_int




    for _enemy_ in listEnemys:
        #print(f"enemy #{listEnemys.index(_enemy_)} posX = {_enemy_.posX} + posY = {_enemy_.posX} = size = {_enemy_.size}")
        _enemy_.draw()
        if numOfLoops % 2 == 0:
            _enemy_.posY += (0.3*_enemy_.speed)
        if _enemy_.posY >= screenHeight:
            _enemy_.posY = 0
            _enemy_.size = random.randint(10, (maxSizeEnemyInt + int(numOfLoops/1000) * MaxSizeIncreaseSpeed))
            _enemy_.speed = random.randint(4, (15 + int(numOfLoops/600) * MaxSpeedIncreaseSpeed))
            _enemy_.life = _enemy_.size*4
            _enemy_.posX = random.randint(int(0 - _enemy_.size/2), int(screenWidth - _enemy_.size/2))
        if _enemy_.TestColision():
            gameRunning = False


    numOfLoops += 1
    count_for_colors += 1
    count_time_spawn_boost += 1
    count_time_spawn_pp += 1
    createEnemy()

    if numOfLoops % (timeIncreaseEnemy*(1000/speedAddEnemy)) == 0:
        #numOfLoops = 0
        enemy.maxEnemys += 1

    rangeSpawnBoost = random.randint(int(speedSpawnBoostMin), int(speedSpawnBoostMax))
    rangeSpawn_pp = random.randint(int(speedSpawnPpMin), int(speedSpawnPpMax))

    if count_time_spawn_boost % rangeSpawnBoost == 0:
        createBoost()
        rangeSpawnBoost = random.randint(int(speedSpawnBoostMin), int(speedSpawnBoostMax))
        count_time_spawn_boost = 0

    if count_time_spawn_pp % rangeSpawn_pp == 0:
        createPackapunch()
        rangeSpawn_pp = random.randint(int(speedSpawnBoostMin), int(speedSpawnBoostMax))
        count_time_spawn_pp = 0


    for _bullet_ in listBullets:
        #print(f"posX = {_bullet_.posX} poxY = {_bullet_.posY} size = {_bullet_.size}.")
        _bullet_.draw()
        _bullet_.posY -= (1 * speedBullets)
        for _enemy_ in listEnemys:
            if _bullet_.TestColision(_enemy_.posX, _enemy_.posY, _enemy_.size):
                if _bullet_ in listBullets:
                    listBullets.remove(_bullet_)
                _enemy_.life -= bullet_strenght
                if _enemy_.life < 0:
                    if _enemy_ in listEnemys:
                        listEnemys.remove(_enemy_)

    pygame.display.update()
    #0.01
    time.sleep(0.01)
    #print(numOfLoops) ____________________________________________________________________________________________________-timer
time_alive = (pygame.time.get_ticks()/1000)
pygame.quit()
sleep = True
print(f"Your score is {numOfLoops}!")
print("you survived " + "%.2f"%(time_alive) + " seconds")

with open("space_game_scores_for_copy.txt", "a") as f:
    f.write("\n" + str(numOfLoops))

with open("space_game_scores_for_copy.txt", "r") as f:
    content = f.read()
    highest_score = 0
    f.seek(0)
    for x in f.readlines():
        try:
            if int(x) > highest_score:
                highest_score = int(x)
        except:
            pass


    if highest_score != numOfLoops:
        f.seek(0)
        print("The highest score is: " + str(highest_score))
        print("the record holder is: %s"%(f.readline()))
    else:
        print("Highest score!!!!!!!!!!")
        name_input = input("Username: ")
        with open("space_game_scores_for_copy.txt", "w") as n:
            n.seek(0)
            n.write(name_input + "\n" + content)
            sleep = False


if sleep:
    time.sleep(10)