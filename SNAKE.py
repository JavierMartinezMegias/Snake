import pygame
import random

# Screen information
WIDTH = 1200
HEIGTH = 990

# Def the sides of the screen
UP = 0
DOWN = HEIGTH
LEFT = 0
RIGHT = WIDTH

# Def colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED =(255,0,0)
GREEN = (0,255,0)

# Def points and font
POINTS = 0
ARIAL = pygame.font.match_font('arial')

# Def speed of the snake, dificulty and work to go into the loop
SPEED = 15
DIFICULTY = 0
WORK = True

# randomFruit chose a random position to the fruits
def randomFruit(LEFT,RIGHT,UP,DOWN):

    random_x = random.choice(range((LEFT+60), (RIGHT-60), 15))
    
    random_y = random.choice(range((UP+60),(DOWN-60), 15))
   
    return random_x,random_y

# makeSnake make a block of the snake and create the sprite
def createSnake(spritesDelJuego,x,y):
    
    snake = pygame.sprite.Sprite()
    
    snake.image = pygame.Surface([15,15])
    snake.image.fill(WHITE)
    
    
    snake.rect = snake.image.get_rect()
    snake.rect.x = x
    snake.rect.y = y
    
    snake.speed_x = 0
    snake.speed_y = 0
    
    spritesDelJuego.add(snake)
    
    return snake

# makeSnake make a block of the snake and create the sprite
def createSnake2(spritesDelJuego,x,y):
    
    snake2 = pygame.sprite.Sprite()
    
    snake2.image = pygame.Surface([15,15])
    snake2.image.fill(BLUE)
    
    
    snake2.rect = snake2.image.get_rect()
    snake2.rect.x = x
    snake2.rect.y = y
    
    snake2.speed_x = 0
    snake2.speed_y = 0
    
    spritesDelJuego.add(snake2)
    
    return snake2

# Make snake a group of sprrites and add a new block make with makeSnake 
def createSnakeBody(spritesDelJuego):
    snake = pygame.sprite.Group()
    snake.add(createSnake(spritesDelJuego,420,420))
    
    return snake

# transform the group snake to a array and add the snake using makeSnake
def addSnakeBody(spritesDelJuego,snake):
    
    list = snake.sprites()
    snake.add(createSnake(spritesDelJuego,list[len(list)-1].rect.x,list[len(list)-1].rect.y))

# Make snake a group of sprrites and add a new block make with makeSnake 
def createSnakeBody2(spritesDelJuego):
    snake2 = pygame.sprite.Group()
    snake2.add(createSnake2(spritesDelJuego,0,0,))
    
    return snake2

# transform the group snake to a array and add the snake using makeSnake
def addSnakeBody2(spritesDelJuego,snake2):
    
    list2 = snake2.sprites()
    snake2.add(createSnake2(spritesDelJuego,list2[len(list2)-1].rect.x,list2[len(list2)-1].rect.y))

# def the attributes of redFruit and create the sprite
def createRedFruit(spritesDelJuego):
    
    redFruit = pygame.sprite.Sprite()
    
    redFruit.image = pygame.Surface([15,15])
    redFruit.image.fill(RED)
    
    redFruit.rect = redFruit.image.get_rect()

    redFruit.rect.x = random.choice(range(15, 870, 15))
    
    redFruit.rect.y = random.choice(range(15, 885, 15))
    
    spritesDelJuego.add(redFruit)
    
    return redFruit

# def the attributes of greenFruit and create the sprite
def createGreenFruit(spritesDelJuego):
    
    greenFruit = pygame.sprite.Sprite()
    
    greenFruit.image = pygame.Surface([15,15])
    greenFruit.image.fill(GREEN)
    
    greenFruit.rect = greenFruit.image.get_rect()

    greenFruit.rect.x = random.choice(range(15, 885, 15))
    
    greenFruit.rect.y = random.choice(range(15, 885, 15))
    
    spritesDelJuego.add(greenFruit)
    
    return greenFruit

#  def the attributes of th walls and create the sprite
def createWall(x,y,WIDTH,HEIGTH):
    
    wall = pygame.sprite.Sprite()
    
    wall.image = pygame.Surface([WIDTH,HEIGTH])
    wall.image.fill(BLUE)
    
    wall.rect = wall.image.get_rect()

    wall.rect.x = x 
    
    wall.rect.y = y
    
   
    
    return wall

# def the walls and add they in a sprite group
def defWalls(spritesDelJuego):
    wallList = pygame.sprite.Group()
    
    upWall = createWall(LEFT,UP,RIGHT,15)
    wallList.add(upWall)
    spritesDelJuego.add(upWall)

    leftWall = createWall(LEFT,UP,15,DOWN)
    wallList.add(leftWall)
    spritesDelJuego.add(leftWall)

    rightWall = createWall(RIGHT-15,UP,15,DOWN)
    wallList.add(rightWall)
    spritesDelJuego.add(rightWall)

    downWall = createWall(LEFT,DOWN-15,RIGHT,15)
    wallList.add(downWall)
    spritesDelJuego.add(downWall)

    return wallList

# def the collision with the fruits and what happend after that
def collideFruit(snake, greenFruit,redFruit, POINTS,SpritesDelJuego,UP,DOWN,RIGHT,LEFT,SPEED,DIFICULTY):
    list = snake.sprites()
    
    # the snake and the points increment
    if list[0].rect.colliderect(greenFruit.rect):
        greenFruit.rect.x, greenFruit.rect.y = randomFruit(LEFT,RIGHT,UP,DOWN)
        POINTS = POINTS + 25
        addSnakeBody(spritesDelJuego, snake)

    # the snake snd the points increment, the walls get close and the snake speed up.    
    if list[0].rect.colliderect(redFruit.rect):
        redFruit.rect.x, redFruit.rect.y = randomFruit(LEFT,RIGHT,UP,DOWN)
        POINTS = POINTS + 25
        addSnakeBody(spritesDelJuego, snake)
        UP += 15
        LEFT += 15
        DOWN -= 15
        RIGHT -= 15
        SPEED += 1
        DIFICULTY += 1
        updateWalls(wallList)   

    return POINTS,UP,DOWN,RIGHT,LEFT,SPEED,DIFICULTY

# update the walls position
def updateWalls(WallList):
    Walls = WallList.sprites()

    Walls[0].rect.y = Walls[0].rect.y +15
    Walls[0].rect.x =Walls[0].rect.x +15

    Walls[1].rect.y = Walls[1].rect.y +15
    Walls[1].rect.x =Walls[1].rect.x +15

    Walls[2].rect.y = Walls[2].rect.y -15
    Walls[2].rect.x =Walls[2].rect.x -15

    Walls[3].rect.y = Walls[3].rect.y -15
    Walls[3].rect.x =Walls[3].rect.x -15
        


# show the text on the screen
def showText(screen):
    font = pygame.font.Font(ARIAL, 25).render("Puntos : "+str(POINTS), True, (255, 0, 0))
    #texto = fuente.render("Puntos : "+str(PUNTOS), True, (255, 0, 0))
    screen.blit(font, [15, 15])
    pygame.display.update()

# update the position of the body chaging the postition of the array one by one following the snake head    
def updateBody(snake):
    list = snake.sprites()
    cont = len(list) -1
    if cont >=1:
        while cont > 0:
            list[cont].rect.y = list[cont-1].rect.y
            list[cont].rect.x =list[cont-1].rect.x
            cont = cont - 1

def updateBody2(snake2):
    list2 = snake2.sprites()
    cont = len(list2) -1
    
    while cont > 0:
        list2[cont].rect.y = list2[cont-1].rect.y
        list2[cont].rect.x =list2[cont-1].rect.x
        cont = cont - 1
    
    
# def the move of the snake head
def snakeMove(snake, WORK):
    list = snake.sprites()
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            WORK = False
            
        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_LEFT and list[0].speed_x != 15:
                list[0].speed_x = -15
                list[0].speed_y = 0
            
            if evento.key == pygame.K_RIGHT and list[0].speed_x != -15:
                list[0].speed_x = 15
                list[0].speed_y = 0

            if evento.key == pygame.K_UP and list[0].speed_y != 15:
                list[0].speed_y = -15
                list[0].speed_x = 0
                
            if evento.key == pygame.K_DOWN and list[0].speed_y != -15:
                list[0].speed_y = 15
                list[0].speed_x = 0
    
    return WORK

# def the move of the snake head
def snakeMove2(snake2,snake):
    list2 = snake2.sprites()
    list = snake.sprites()
    select = random.randint(0,3)

    if list[0].rect.x < list2[0].rect.x and list[0].rect.y < list2[0].rect.y:
        if select == 1:   
            list2[0].speed_x = -15
            list2[0].speed_y = 0
        if select == 0:
            list2[0].speed_x = 0   
            list2[0].speed_y = -15

    elif list[0].rect.x == list2[0].rect.x and list[0].rect.y < list2[0].rect.y:
        if select == 1  or select == 2 or select == 3:   
            list2[0].speed_x = -15
            list2[0].speed_y = 0
        if select == 0:
            list2[0].speed_x = 0   
            list2[0].speed_y = -15     
    
    elif list[0].rect.x > list2[0].rect.x and list[0].rect.y > list2[0].rect.y:
        if select == 1:   
            list2[0].speed_x = 15
            list2[0].speed_y = 0
        if select == 0:
            list2[0].speed_x = 0   
            list2[0].speed_y = 15

    elif list[0].rect.x == list2[0].rect.x and list[0].rect.y > list2[0].rect.y:
        if select == 1:   
            list2[0].speed_x = 0
            list2[0].speed_y = -15
        if select == 0 or select == 2 or select == 3:
            list2[0].speed_x = 15   
            list2[0].speed_y = 0
    
    elif list[0].rect.x < list2[0].rect.x and list[0].rect.y > list2[0].rect.y :
        if select == 1:   
            list2[0].speed_x = -15
            list2[0].speed_y = 0
        if select == 0:
            list2[0].speed_x = 0   
            list2[0].speed_y = 15

    elif list[0].rect.y == list2[0].rect.y and list[0].rect.x > list2[0].rect.x:
        if select == 1:   
            list2[0].speed_x = -15
            list2[0].speed_y = 0
        if select == 0 or select == 2 or select == 3:
            list2[0].speed_x = 0   
            list2[0].speed_y = 15

    elif list[0].rect.x > list2[0].rect.x and list[0].rect.y < list2[0].rect.y:
        if select == 1:   
            list2[0].speed_x = 15
            list2[0].speed_y = 0
        if select == 0:
            list2[0].speed_x = 0   
            list2[0].speed_y = -15

    elif list[0].rect.y == list2[0].rect.y and list[0].rect.x < list2[0].rect.x:
        if select == 1 or select == 2 or select == 3:   
            list2[0].speed_x = 0
            list2[0].speed_y = 15
        if select == 0:
            list2[0].speed_x = -15   
            list2[0].speed_y = 0

def collideSnakeWithSnake2(snake,snake2,WORK):
    list2 = snake2.sprites()
    list = snake.sprites()

    cont = 0
    
    while cont < len(list2):
        if list[0].rect.colliderect(list2[cont].rect):
            WORK = False
        cont = cont +1

    return WORK
    

# Change the position of the fruit if it get out of the walls
def updateFruit():
    if redFruit.rect.x < LEFT+15 or redFruit.rect.x > RIGHT-15 or redFruit.rect.y < UP+15 or redFruit.rect.y > DOWN-15:
        redFruit.rect.x, redFruit.rect.y = randomFruit(LEFT,RIGHT,UP,DOWN)
    if greenFruit.rect.x < LEFT+15 or greenFruit.rect.x > RIGHT-30 or greenFruit.rect.y < UP+15 or greenFruit.rect.y > DOWN-30:
        greenFruit.rect.x, greenFruit.rect.y = randomFruit(LEFT,RIGHT,UP,DOWN)

# update the snake move
def updateSnake(snake):

    list = snake.sprites()
    updateBody(snake)  
    list[0].rect.x += list[0].speed_x
           
    list[0].rect.y += list[0].speed_y

# update the snake move
def updateSnake2(snake2):

    list2 = snake2.sprites()
    updateBody2(snake2)  
    list2[0].rect.x += list2[0].speed_x
           
    list2[0].rect.y += list2[0].speed_y

# the game finish if the snake head collide a wall
def collideWallsDie(WORK,serpiente):
    list = serpiente.sprites()
    if list[0].rect.bottom < UP+30:
        WORK = False 
        
    if list[0].rect.top > DOWN-30 :
        WORK = False
    
    if list[0].rect.right > RIGHT-15 :
        WORK = False
    
    if list[0].rect.left < LEFT+15:
        WORK = False
    return WORK

# finish the game  if the snake collide itself
def collideSnakeWithSnake (snake, WORK):
    list = snake.sprites()
    cont = 1
    if len(list)>1:
        while cont < len(list):
            if list[0].rect.colliderect(list[cont].rect):
                WORK = False
            cont = cont +1
    return WORK

# teleport the snake to the opsite side of the screen when he collide a wall
def collideWallsTeleport(snake):
    list = snake.sprites()

    if list[0].rect.bottom < UP+30:
        list[0].rect.y = DOWN-30 
        
    if list[0].rect.top > DOWN-30 :
        list[0].rect.y = UP+15 
    
    if list[0].rect.right > RIGHT-15 :
        list[0].rect.x = LEFT+15 
    
    if list[0].rect.left < LEFT+15:
        list[0].rect.x = RIGHT-30 
   
def updateSnake2Len(POINTS):
    if POINTS == 100:
        addSnakeBody2(spritesDelJuego,snake2)
        addSnakeBody2(spritesDelJuego,snake2)
        addSnakeBody2(spritesDelJuego,snake2)
        addSnakeBody2(spritesDelJuego,snake2)
        POINTS += 25
    if POINTS == 300:
        addSnakeBody2(spritesDelJuego,snake2)
        addSnakeBody2(spritesDelJuego,snake2)
        addSnakeBody2(spritesDelJuego,snake2)
        addSnakeBody2(spritesDelJuego,snake2)
        addSnakeBody2(spritesDelJuego,snake2)
        addSnakeBody2(spritesDelJuego,snake2)
        addSnakeBody2(spritesDelJuego,snake2)
        addSnakeBody2(spritesDelJuego,snake2)
        POINTS += 25
    if POINTS == 500:
        addSnakeBody2(spritesDelJuego,snake2)
        addSnakeBody2(spritesDelJuego,snake2)
        addSnakeBody2(spritesDelJuego,snake2)
        addSnakeBody2(spritesDelJuego,snake2)
        addSnakeBody2(spritesDelJuego,snake2)
        addSnakeBody2(spritesDelJuego,snake2)
        addSnakeBody2(spritesDelJuego,snake2)
        addSnakeBody2(spritesDelJuego,snake2)
        addSnakeBody2(spritesDelJuego,snake2)
        addSnakeBody2(spritesDelJuego,snake2)
        addSnakeBody2(spritesDelJuego,snake2)
        addSnakeBody2(spritesDelJuego,snake2)
        addSnakeBody2(spritesDelJuego,snake2)
        addSnakeBody2(spritesDelJuego,snake2)
        POINTS += 25
    return POINTS

# start the screen
pygame.init()

# inicialice sprites, frames and screendimensions
dimensiones = [WIDTH, HEIGTH]
sreen = pygame.display.set_mode(dimensiones)
pygame.display.set_caption('SNAKE')

spritesDelJuego = pygame.sprite.Group()
snake = createSnakeBody(spritesDelJuego)
snake2 = createSnakeBody2(spritesDelJuego)

redFruit = createRedFruit(spritesDelJuego)
greenFruit = createGreenFruit(spritesDelJuego)
wallList = defWalls(spritesDelJuego)
clock = pygame.time.Clock()



while WORK :

    WORK = snakeMove(snake, WORK)
    
    if POINTS >= 100:
        snakeMove2(snake2,snake)

    showText(sreen)

    POINTS = updateSnake2Len(POINTS)
    
    updateFruit()

    updateSnake(snake)

    updateSnake2(snake2)

    WORK = collideSnakeWithSnake (snake, WORK)

    WORK = collideSnakeWithSnake2(snake,snake2,WORK)

    POINTS,UP,DOWN,RIGHT,LEFT,SPEED,DIFICULTY = collideFruit(snake, greenFruit,redFruit,POINTS,spritesDelJuego,UP,DOWN,RIGHT,LEFT,SPEED,DIFICULTY)
    
    # control if the snake must die or teleport when he collide a wall
    if DIFICULTY >= 1 :
        WORK = collideWallsDie(WORK,snake)
        
    else :

        collideWallsTeleport(snake)
    
    
    
    sreen.fill((0,0,0))
    
    spritesDelJuego.draw(sreen)
    
    clock.tick(SPEED)
    
    
    pygame.display.flip()
    
pygame.quit()    