import pygame
import random
pygame.init()

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Snake Game')

white = (255, 255, 255)
yellow = (254, 218, 132)
black = (0, 0, 0)
red = (213, 50, 80)
body= (255, 190, 221)
green = (0, 255, 0)
blue = (122, 152, 237)
grey =(128, 128, 128)
dark_grey = (36,37,38)
bgc = yellow
foodc = (30, 150, 104)
headc= (247, 36, 99)
bodyc = (23, 16, 73)
scorecolor = (67, 69, 127)

clock = pygame.time.Clock()

snake_block = 10  #Size per block


message_font = pygame.font.SysFont(None,40)
score_font = pygame.font.SysFont("comicsansms", 25)

def Your_score(score):  #To display score
    value = score_font.render("                                           Your Score: " + str(score), True, scorecolor)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):   #Function to display the snake
    for x in snake_list:
        pygame.draw.rect(dis, bodyc, [x[0], x[1], snake_block, snake_block])
    pygame.draw.rect(dis, headc, [x[0], x[1], snake_block, snake_block])  #to display snake's head

def message(msg,color):
    mesg = message_font.render(msg,True, color)
    dis.blit(mesg, [dis_width/10,dis_height/2])

def game_loop():
    game_over = False
    game_close = False

    x1 = dis_width/2    #coordinates of snake
    y1 = dis_height/2

    x1_change = 0   
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    last_key_clicked = ""  

    snake_speed = 15

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0     #randomly generating xth position for food(rounded to multiples of 10)
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0    #randomly generating  yth position for food(rounded to multiples of 10)

    while not game_over:

        while game_close == True:
            dis.fill(green)
            message("You Lost!! Press Q to Quit and Press C to Continue",red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:  
                    if event.key == pygame.K_q:   #checks if 'q' is pressed
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:   #checks if 'c' key is pressed
                        game_loop()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:         #checking close button of window is clicked
                game_over = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if last_key_clicked != "right":  #if snake is moving to a direction it shouldn't change to opposite direction 
                        x1_change = -snake_block
                        y1_change = 0
                        last_key_clicked = "left"
                elif event.key == pygame.K_RIGHT:
                    if last_key_clicked != "left":
                        x1_change = snake_block
                        y1_change = 0
                        last_key_clicked = "right"
                elif event.key == pygame.K_UP:
                    if last_key_clicked != "down":
                        y1_change = -snake_block
                        x1_change = 0
                        last_key_clicked = "up" 
                elif event.key == pygame.K_DOWN:
                    if last_key_clicked != "up":
                        y1_change = snake_block
                        x1_change = 0
                        last_key_clicked = "down"  
        
        if x1 < 0:        
            x1 = dis_width
        elif x1 >= dis_width:
            x1 = -10
        elif y1 < 0:
            y1 = dis_height
        elif y1 >= dis_height:
            y1 = -10
            
                
        x1 += x1_change #updating coordinates
        y1 += y1_change

        dis.fill(bgc)

        pygame.draw.rect(dis, foodc, [foodx, foody, snake_block, snake_block])   #displaying food

        snake_Head = []      
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()

        if x1 == foodx and y1 == foody:   #to check if snake has swalowed the food
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            snake_speed = snake_speed + 1

        clock.tick(snake_speed) #refresh rate

    pygame.quit()
    quit()

game_loop()
