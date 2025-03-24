import pygame,sys,copy,random,time  
pygame.init() 

#Ойын параметрлерін орнату  
scale=15  #Масштаб (ұяшық өлшемі)  
score=0  #Ойыншының ұпайы  
level=0  #Ойын деңгейі  
SPEED=10  #Жылдамдық  
food_x=10  #Тамақтың x координатасы  
food_y=10  #Тамақтың y координатасы  

#Ойын терезесін жасау  
display=pygame.display.set_mode((500,500))  
pygame.display.set_caption("Snake Game")  # Терезенің тақырыбын орнату  
clock=pygame.time.Clock()  # Ойындағы уақытты басқару  

#Түстерді анықтау  
background_top=(0,0,50)  #Фонның жоғарғы бөлігі  
background_bottom=(0,0,0)  #Фонның төменгі бөлігі  
snake_colour=(255,137,0)  #Жыланның денесінің түсі  
food_colour=(random.randint(1,255),random.randint(1,255),random.randint(1,255))  #Тамақтың түсі (кездейсоқ)  
snake_head=(255,247,0)  #Жыланның басының түсі  
font_colour=(255,255,255)  #Шрифт түсі  
defeat_colour=(255,0,0)  #Жеңіліс үсі  

# Жылан класы  
class Snake:  
    def __init__(self,x_start,y_start):  
        self.x=x_start  
        self.y=y_start  
        self.w=15  #Жыланның ені  
        self.h=15  #Жыланның биіктігі  
        self.x_dir=1  #Жыланның x бойымен қозғалыс бағыты (1 = оңға, -1 = солға)  
        self.y_dir=0  #Жыланның y бойымен қозғалыс бағыты (1 = төмен, -1 = жоғары)  
        self.history=[[self.x,self.y]]  #Жыланның координаталарының тарихы  
        self.length=1  #Жыланның ұзындығы  

    #Жыланды қайта бастау  
    def reset(self):  
        self.x=500/2-scale  
        self.y=500/2-scale  
        self.x_dir=1  
        self.y_dir=0  
        self.history=[[self.x,self.y]]  
        self.length=1  

    #Жыланды экранға шығару  
    def show(self):  
        for i in range(self.length):  
            if not i==0:  
                pygame.draw.rect(display,snake_colour,(self.history[i][0],self.history[i][1],self.w,self.h))  
            else:  
                pygame.draw.rect(display,snake_head,(self.history[i][0],self.history[i][1],self.w,self.h))  

    #Жылан тамақты жеді ма  
    def check_eaten(self):  
        if abs(self.history[0][0]-food_x)<scale and abs(self.history[0][1]-food_y)<scale:  
            return True  

    #Жаңа деңгейге жетті ме?  
    def check_level(self):  
        global level  
        if self.length%5==0:  
            return True  

    #Жыланның ұзындығын арттыру  
    def grow(self):  
        self.length+=1  
        self.history.append(self.history[self.length-2])  

    #Жылан өзін-өзі тістеді ме
    def death(self):  
        for i in range(1,self.length):  
            if abs(self.history[0][0]-self.history[i][0])<self.w and abs(self.history[0][1]-self.history[i][1])<self.h:  
                return True  

    #Жыланның орнын жаңарту  
    def update(self):  
        for i in range(self.length-1,0,-1):  
            self.history[i]=copy.deepcopy(self.history[i-1])  
        self.history[0][0]+=self.x_dir*scale  
        self.history[0][1]+=self.y_dir*scale  

#Тамақ класы  
class Food:  
    #Жаңа тамақтың орнын орнату  
    def new_location(self):  
        global food_x,food_y  
        food_x=random.randrange(1,int(500/scale)-1)*scale  
        food_y=random.randrange(1,int(500/scale)-1)*scale  

    #Тамақты экранға шығару  
    def show(self):  
        pygame.draw.rect(display,food_colour,(food_x,food_y,scale,scale))  

#Ұпайды экранға шығару  
def show_score():  
    font=pygame.font.SysFont(None,20)  
    text=font.render("Score:"+str(score),True,font_colour)  
    display.blit(text,(scale,scale))  

#Деңгейді экранға шығару  
def show_level():  
    font=pygame.font.SysFont(None,20)  
    text=font.render("Level:"+str(level),True,font_colour)  
    display.blit(text,(90-scale,scale))  

#Ойын циклі  
def gameLoop():  
    global score,level,SPEED  
    snake=Snake(500/2,500/2)  
    food=Food()  
    food.new_location()  

    while True:  
        for event in pygame.event.get():  
            if event.type==pygame.QUIT:  #ерезені жабу  
                pygame.quit()  
                sys.exit()  
            if event.type==pygame.KEYDOWN:  
                if event.key==pygame.K_q:  
                    pygame.quit()  
                    sys.exit()  
                if snake.y_dir==0:  
                    if event.key==pygame.K_UP:  
                        snake.x_dir=0  
                        snake.y_dir=-1  
                    if event.key==pygame.K_DOWN:  
                        snake.x_dir=0  
                        snake.y_dir=1  
                if snake.x_dir==0:  
                    if event.key==pygame.K_LEFT:  
                        snake.x_dir=-1  
                        snake.y_dir=0  
                    if event.key==pygame.K_RIGHT:  
                        snake.x_dir=1  
                        snake.y_dir=0  

        #Фонды шығару  
        for y in range(500):  
            color=(background_top[0]+(background_bottom[0]-background_top[0])*y/500,background_top[1]+(background_bottom[1]-background_top[1])*y/500,background_top[2]+(background_bottom[2]-background_top[2])*y/500)  
            pygame.draw.line(display,color,(0,y),(500,y))  

        snake.show()  
        snake.update()  
        food.show()  
        show_score()  
        show_level()  

        #Тамақ жеген жағдайда  
        if snake.check_eaten():  
            food.new_location()  
            score+=random.randint(1,5)  
            snake.grow()  

        #Жаңа деңгейге жеткенде  
        if snake.check_level():  
            food.new_location()  
            level+=1  
            SPEED+=1  
            snake.grow()  

        #Жеңіліс болса
        if snake.death():  
            score=0  
            level=0  
            font=pygame.font.SysFont(None,100)  
            text=font.render("Game Over!",True,defeat_colour)  
            display.blit(text,(50,200))  
            pygame.display.update()  
            time.sleep(3)  
            snake.reset()  

        #Шекарадан шықса қарама-қарсы жаққа шығару  
        if snake.history[0][0]>500:  
            snake.history[0][0]=0  
        if snake.history[0][0]<0:  
            snake.history[0][0]=500  
        if snake.history[0][1]>500:  
            snake.history[0][1]=0  
        if snake.history[0][1]<0:  
            snake.history[0][1]=500  

        pygame.display.update()  
        clock.tick(SPEED)  

#Ойынды іске қосу  
gameLoop()
