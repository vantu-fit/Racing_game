import pygame
import pygame_gui
import json,random,re,sys,time
from random import randint
from os.path import isfile, join
from underthesea import sentiment
import numpy as np
from pygame_gui_v2 import input
from face_recognition import create,train,test
from python_tetris_master import tetris
from pong_game import pong
from Bonk_cheems import bonkcheems
from Snake import main as snake
#COLOR 
WHITE=(255,255,255)
YELLOW= (246, 142, 2)
BLUE=(34, 150, 5)
RED=(255,0,0)
BLUE_V2=(11, 67, 160)
LAM=(19, 43, 161)
#================================
input_type={"v2":input,"v1":pygame_gui.elements}
font_setting={"v1":"SourceCodePro-Black.ttf", "v2":"SVN-Retron 2000.ttf"}
font_setting_italic={"v1":"SourceCodePro-BlackItalic.ttf", "v2":"SVN-Retron 2000.ttf"}
color_setting={"v1":YELLOW, "v2":BLUE_V2}
color_history={"v1":WHITE, "v2":LAM}
#================================
running=True
WIDTH,HEIGHT=975,550
screen = pygame.display.set_mode((WIDTH,HEIGHT))
MANAGER=pygame_gui.UIManager((WIDTH,HEIGHT))
CLOCK=pygame.time.Clock()
font_v=pygame.font.Font
SourceCodePro_Black=r'img\font\SourceCodePro-Black.ttf'
win_sound=pygame.mixer.Sound('img/sounds/collect.mp3')
racing_sound=pygame.mixer.Sound('img/sounds/Racing.mp3')
sound_main=pygame.mixer.music.load('img\sounds\Soundtrack.mp3')
click_sound=pygame.mixer.Sound('img/sounds/click.mp3')
pygame.mixer.music.play(-1)
pygame.event.wait()
pygame.mixer.music.set_volume(0.4)
win_sound.set_volume(0.4)
racing_sound.set_volume(0.4)
click_sound.set_volume(0.4)
#SET
set1=[
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set4_fish\fish_1\fish_1_1.png'),(90,90)),"fish1","fish1"],
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set4_fish\fish_2\fish_2_1.png'),(90,90)),"fish2","fish2"],
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set4_fish\fish_3\fish_3_1.png'),(90,90)),"fish3","fish3"],
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set4_fish\fish_4\fish_4_1.png'),(90,90)),"fish4","fish4"],
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set4_fish\fish_5\fish_5_1.png'),(90,90)),"fish5","fish5"]
    ]
set2=[
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set6_dinosaur\dinosaur_1\dinosaur_1_6.png'),(90,90)),"dino1","dino1"],
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set6_dinosaur\dinosaur_2\dinosaur_2_6.png'),(90,90)),"dino2","dino2"],
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set6_dinosaur\dinosaur_3\dinosaur_3_6.png'),(90,90)),"dino3","dino3"],
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set6_dinosaur\dinosaur_4\dinosaur_4_6.png'),(90,90)),"dino4","dino4"],
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set6_dinosaur\dinosaur_5\dinosaur_5_6.png'),(90,90)),"dino5","dino5"]
    ]
set3=[
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set2_bird\bird_1\bird_1_2.png'),(90,90)),"bird1","bird1"],
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set2_bird\bird_2\bird_2_2.png'),(90,90)),"bird2","bird2"],
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set2_bird\bird_3\bird_3_2.png'),(90,90)),"bird3","bird3"],
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set2_bird\bird_4\bird_4_2.png'),(90,90)),"bird4","bird4"],
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set2_bird\bird_5\bird_5_2.png'),(90,90)),"bird5","bird5"]
    ]
set4=[
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set1_space\space_1\space_1_4.png'),(90,90)),"space1","space1"],
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set1_space\space_2\space_2-4.png.png'),(90,90)),"space2","space2"],
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set1_space\space_3\space_3-3.png.png'),(90,90)),"space3","space3"],
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set1_space\space_4\space_4-5.png.png'),(90,90)),"space4","space4"],
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set1_space\space_5\space_5-4.png.png'),(90,90)),"space5","space5"]
    ]
set5=[
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set5_member\member_chau\member_chau_1.png'),(90,90)),"Châu","Châu"],
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set5_member\member_duc\member_duc_1.png'),(90,90)),"Đức","Đức"],
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set5_member\member_dat\member_dat_1.png'),(90,90)),"Đạt","Đạt"],
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set5_member\member_tu\member_tu_1.png'),(90,90)),"Tư","Tư"],
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set5_member\member_tri\member_tri_1.png'),(90,90)),"Trí","Trí"]
    ]
set6=[
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set3_human\human_1\human_1_4.png'),(90,90)),"human1","human1"],
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set3_human\human_2\human_2_4.png'),(90,90)),"human2","human2"],
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set3_human\human_3\human_3_4.png'),(90,90)),"human3","human3"],
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set3_human\human_4\human_4_4.png'),(90,90)),"human4","human4"],
        [pygame.transform.scale(pygame.image.load(r'img\set_nhan_vat\set3_human\human_5\human_5_4.png'),(90,90)),"human5","human5"]
    ]
set=[set1,set2,set3,set4,set5,set6]
chat_random=[
    "Chơi hay quá! Đúng là bạn thân của tớ",
    "Chỉ cần bạn có mặt, thắng thua không quan trọng",
    "ước được thua cơ",
    "để rừng cho thầy",
    "thôi nay chơi nhiêu đủ rồi",
    "coi top top ít thôi",
    "số đá còn lại mày giấu ở đâu",
    "cũng gọi là biết chơi đấy",
    "game này thầy gánh",
    "hổ báo giống các cháu Việt Nam",
    "cậu biết chơi lửa đền không",
    "gk3 zị baaa",
    "Cậu ăn cơm chưa",
    "Cậu làm ngiu tớ nhé",
    "Tớ đồng ý"
]
#__________________________________________________________________________________________________________________________________________________-
#VAR GAME PLAY 
set_character=[
    ["Character_fish",["fish_1","fish_2","fish_3","fish_4","fish_5"],(165,165),4], # set_character[0][0] and set_character[0][1][i] 
    ["Character_dinosaur",["dinosaur_1","dinosaur_2","dinosaur_3","dinosaur_4","dinosaur_5"],(125,100),6],
    ["Character_bird",["bird_1","bird_2","bird_3","bird_4","bird_5",],(200,200),3],
    ["Charecter_Space",["space_1","space_2","space_3","space_4","space_5"],(100,100),4],
    ["Character_member",["member_chau","member_duc","member_dat","member_tu","member_tri"],(175,175),2],
    ["Character_human",["human_1","human_2","human_3","human_4","human_5",],(150,150),4]
]
map=[  # tùy chọn và các thuộc tính  của đường đua  # sai số của bùa lợi là 400 
    ["1_S.png","1_M.png","1_L.png",],               # 925,1300,1800
    ["2_S.png","2_M.png","2_L.png",],
    ["3_S.png","3_M.png","3_L.png",]
]
with_type= [925,1300,1800]
winner=[]
for i in range(10):
    winner.append(pygame.image.load(join("img","finish",f'effect_win_0{i}.png')))
for i in range(10,23):
    winner.append(pygame.image.load(join("img","finish",f'effect_win_{i}.png')))
winner_count=0
#GET DATA FROM JSON
data=[]
with open('data_player/data.json') as file_name:
    data=json.load(file_name)
FPS = 20
PLAYER_VEL = 3
font = pygame.font.SysFont("arialblack",40)

window=pygame.display.set_mode((WIDTH, HEIGHT))
#--------------------------------------------------------------------------------------------------------------------------------------------
class Player(pygame.sprite.Sprite): ########################################################################################################
 #các thành phần   
 def __init__(self,x,y, type,set_input,scale,len, i1):
    super().__init__() 
    self.vel_x = i1
    self.x = x
    self.y = y
    self.set_input=set_input
    self.pos=0
    self.cout = 0
    self.x_vel=0
    self.y_vel=0
    self.mask= None
    self.direction= "up"
    self.animation_count = 0
    self.time_count = 0
    self.print_count = 0
    self.i = 0
    self.flip = False
    self.sprites= []
    for i in range(1,len+1):
        self.sprites.append(pygame.transform.scale((pygame.image.load(join("img",set_input,f"{type}_{i}.png"))),scale))
        if set_input=="Character_member" and i==2:
            self.sprites.append(pygame.transform.scale((pygame.image.load(join("img",set_input,f"{type}_{i-1}.png"))),scale))                                                                                                                  #tạo sprite(thay đổi size ảnh(ảnh))
    for i in range(1,len+1):
        self.sprites.append(pygame.transform.scale((pygame.transform.flip(pygame.image.load(join("img",set_input,f"{type}_{i}.png")),True,False)),scale))
        if set_input=="Character_member" and i==2:
            self.sprites.append(pygame.transform.scale((pygame.image.load(join("img",set_input,f"{type}_{i-1}.png"))),scale))   

    if self.flip == False:
     self.current_sprite = 0
    else:
     self.current_sprite = 4   
    self.image = self.sprites[self.current_sprite]
    self.rect = self.image.get_rect()
    self.rect.center = [x, y]
    self.counter = 0

 def update(self): #chuyển động tại chỗ và di chuyển           
    if self.set_input=="Character_fish":
        self.rect.center = [self.x, self.y] 
        if self.x == 50 :
            self.current_sprite +=0.2
            if self.current_sprite >=3:
                self.current_sprite=0
            self.image = self.sprites[int(self.current_sprite)]
        if 50<self.x<with_type[main.type_choose]:    
            if self.flip == False :       
                self.current_sprite +=0.4
                if self.current_sprite >=4:
                    self.current_sprite=1
                self.image = self.sprites[int(self.current_sprite)]  
            else:
            
                self.current_sprite +=0.4
                if self.current_sprite >= 7:
                    self.current_sprite=4
                self.image = self.sprites[int(self.current_sprite)]     
        else:
            self.current_sprite +=0.2
            if self.current_sprite >=3:
                self.current_sprite=0
            self.image = self.sprites[int(self.current_sprite)]
    elif self.set_input=="Character_dinosaur":
        self.rect.center = [self.x, self.y] 
        if self.x == 50 :
            self.current_sprite +=0.1
            if self.current_sprite >=3:
                self.current_sprite=0
            self.image = self.sprites[int(self.current_sprite)] 

        if 50<self.x<with_type[main.type_choose]:    
            if self.flip == False :       
                self.current_sprite +=1
                if self.current_sprite >=6:
                    self.current_sprite=1
                self.image = self.sprites[int(self.current_sprite)]  
            else:
            
                self.current_sprite +=1
                if self.current_sprite >= 12:
                    self.current_sprite=6
                self.image = self.sprites[int(self.current_sprite)]     
        elif self.x >=with_type[main.type_choose]:
            self.current_sprite +=0.1
            if self.current_sprite >=3:
                self.current_sprite=0
            self.image = self.sprites[int(self.current_sprite)] 
   
    elif self.set_input=="Character_bird":
        self.rect.center = [self.x, self.y] 
        if self.x<=with_type[main.type_choose]:    
            if self.flip == False :       
                self.current_sprite +=0.2
                if self.current_sprite >=3:
                    self.current_sprite=0
                self.image = self.sprites[int(self.current_sprite)]  
            else:
                self.current_sprite +=0.2
                if self.current_sprite >= 6:
                    self.current_sprite=3
                self.image = self.sprites[int(self.current_sprite)]        
    elif self.set_input=="Charecter_Space":
        self.rect.center = [self.x, self.y] 
        if self.x == 50 :
            self.current_sprite=0
        self.image = self.sprites[int(self.current_sprite)] 

        if self.x<with_type[main.type_choose]:    
            if self.flip == False :       
                self.current_sprite +=0.2
                if self.current_sprite >=4:
                    self.current_sprite=1
                self.image = self.sprites[int(self.current_sprite)]  
            else:
            
                self.current_sprite +=0.2
                if self.current_sprite >= 7:
                    self.current_sprite=4
                self.image = self.sprites[int(self.current_sprite)]     
        else:
            self.current_sprite=0
        self.image = self.sprites[int(self.current_sprite)] 

    elif self.set_input=="Character_member":
        self.rect.center = [self.x, self.y] 
        if self.x == 50 :
            self.current_sprite=0
        self.image = self.sprites[int(self.current_sprite)] 

        if 50<self.x<with_type[main.type_choose]:    
            if self.flip == False :       
                self.current_sprite +=0.2
                if self.current_sprite >=3:
                    self.current_sprite=1
                self.image = self.sprites[int(self.current_sprite)]  
            else:
            
                self.current_sprite +=0.2
                if self.current_sprite >= 6:
                    self.current_sprite=4
                self.image = self.sprites[int(self.current_sprite)]     
        else:
            self.current_sprite=3
        self.image = self.sprites[int(self.current_sprite)] 
    elif self.set_input=="Character_human":
        self.rect.center = [self.x, self.y] 
        if self.x == 50 :
            self.current_sprite=0
        self.image = self.sprites[int(self.current_sprite)] 

        if self.x<with_type[main.type_choose]:    
            if self.flip == False :       
                self.current_sprite +=0.2
                if self.current_sprite >=4:
                    self.current_sprite=1
                self.image = self.sprites[int(self.current_sprite)]  
            else:
            
                self.current_sprite +=0.2
                if self.current_sprite >= 7:
                    self.current_sprite=4
                self.image = self.sprites[int(self.current_sprite)]     
        else:
            self.current_sprite=0
        self.image = self.sprites[int(self.current_sprite)] 

 def position(self):
    if self.x<with_type[main.type_choose]:
        
        self.x += self.vel_x*(int(main.speed)/100)
    else:
        self.x +=0    
                                                
 def draw(self, window):
   pygame.draw.rect(window,(255,0,0),(self.x,self.y,50,50))

 def timer(self, timefre):
        if self.x < with_type[main.type_choose]:
            self.time_count += timefre  
#--------------------------------------------------------------------------------------------------------------------------------------------
 #vẽ background,xe
def draw(window, background,p1,p2,p3,p4,p5,bdb1,bdb2,bdb3,bdb4,bdb5):
    window.blit(background,(0,0))

    bdb1.draw(window)
    bdb2.draw(window)
    bdb3.draw(window)
    bdb4.draw(window)
    bdb5.draw(window)

    p1.draw(window)
    p2.draw(window)
    p3.draw(window)
    p4.draw(window)
    p5.draw(window)
    
   # pygame.display.update()
#--------------------------------------------------------------------------------------------------------------------------------------------
  #tạo background  
def get_background(name):
 background = pygame.image.load(join("img",name))
 
 return background
#--------------------------------------------------------------------------------------------------------------------------------------------

def draw_text(text, font, text_col, x, y):
    
    img = font.render(str(text), True, text_col)
    window.blit(img, (x,y))
   
#--------------------------------------------------------------------------------------------------------------------------------------------
class buff_debuff(pygame.sprite.Sprite):
    def __init__(self, x, y, st):
        super().__init__()
        self.x = x
        self.y = y
        self.st = st
        self.show = True
        self.active = False
        
        
        self.sprites= []
        self.sprites.append(pygame.transform.scale((pygame.image.load(join("img","Buffdebuff","charm_def.png"))),(75,75))) 
        self.sprites.append(pygame.transform.scale((pygame.image.load(join("img","Buffdebuff","charm_speedUp.png"))),(75,75)))
        self.sprites.append(pygame.transform.scale((pygame.image.load(join("img","Buffdebuff","backward.png"))),(75,75)))
        self.sprites.append(pygame.transform.scale((pygame.image.load(join("img","Buffdebuff","speedDown.png"))),(75,75)))
        self.sprites.append(pygame.transform.scale((pygame.image.load(join("img","Buffdebuff","Teleport.png"))),(75,75)))
        self.sprites.append(pygame.transform.scale((pygame.image.load(join("img","Buffdebuff","toGoal.png"))),(75,75)))
        self.sprites.append(pygame.transform.scale((pygame.image.load(join("img","Buffdebuff","toStart.png"))),(75,75)))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    def showup(self):
        if self.show == True:
            self.current_sprite += 0.4
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 1
            self.image = self.sprites[int(self.current_sprite)]   

        if self.st ==1 and self.show == False:
             self.current_sprite = 1
             self.image = self.sprites[int(self.current_sprite)]

        if self.st ==2 and self.show == False:
             self.current_sprite = 2
             self.image = self.sprites[int(self.current_sprite)]
        if self.st ==3 and self.show == False:
             self.current_sprite = 3
             self.image = self.sprites[int(self.current_sprite)]
        if self.st ==4 and self.show == False:
             self.current_sprite = 4
             self.image = self.sprites[int(self.current_sprite)]
        if self.st ==5 and self.show == False:
             self.current_sprite = 5
             self.image = self.sprites[int(self.current_sprite)]
        if self.st ==6 and self.show == False:                    
             self.current_sprite = 6
             self.image = self.sprites[int(self.current_sprite)]
    def activebdb(self):
        if self.active == True :
            self.kill()
    

    def draw(self,window):
           pygame.draw.rect(window,(255,0,0),(self.x,self.y,50,50))     
        
#--------------------------------------------------------------------------------------------------------------------------------------------
def remove_Vietnamese_letter(s):
    s = re.sub('[áàảãạăắằẳẵặâấầẩẫậ]', 'a', s)
    s = re.sub('[ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬ]', 'A', s)
    s = re.sub('[éèẻẽẹêếềểễệ]', 'e', s)
    s = re.sub('[ÉÈẺẼẸÊẾỀỂỄỆ]', 'E', s)
    s = re.sub('[óòỏõọôốồổỗộơớờởỡợ]', 'o', s)
    s = re.sub('[ÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢ]', 'O', s)
    s = re.sub('[íìỉĩị]', 'i', s)
    s = re.sub('[ÍÌỈĨỊ]', 'I', s)
    s = re.sub('[úùủũụưứừửữự]', 'u', s)
    s = re.sub('[ÚÙỦŨỤƯỨỪỬỮỰ]', 'U', s)
    s = re.sub('[ýỳỷỹỵ]', 'y', s)
    s = re.sub('[ÝỲỶỸỴ]', 'Y', s)
    s = re.sub('đ', 'd', s)
    s = re.sub('Đ', 'D', s)
    return s
def main_play(window,choose,map_choose,ID):
    print_count = 0
    key = pygame.key.get_pressed()
    clock = pygame.time.Clock()
    #--------------------------------------------
    background= get_background(map[map_choose][main.type_choose])
#     set_character=[
#     ["Character_fish",["fish_1","fish_2","fish_3","fish_4","fish_5"],(165,165),4], # set_character[0][0] and set_character[0][1][i] 
#     ["Character_dinosaur",["dinosaur_1","dinosaur_2","dinosaur_3","dinosaur_4","dinosaur_5"],(125,100),6],
#     ["Character_bird",["bird_1","bird_2","bird_3","bird_4","bird_5",],(200,200),3],
#     ["Charecter_Space",["space_1","space_2","space_3","space_4","space_5"],(100,100),4],
#     ["Character_member",["member_chau","member_duc","member_dat","member_tu","member_tri"],(175,175),2],
#     ["Character_human",["human_1","human_2","human_3","human_4","human_5",],(150,150),4]
# ]
    #-----------------------------------------
    player1= Player(50,87/2,set_character[choose[0][0]][1][choose[0][1]]   ,set_character[choose[0][0]][0],    set_character[choose[0][0]][2],   set_character[choose[0][0]][3] ,   random.randint(3,5))
    player1s=pygame.sprite.Group()

    player1s.add(player1)
    v1p = player1.vel_x +2
    v1m = player1.vel_x -2


    player2= Player(50,87+41,set_character[choose[1][0]][1][choose[1][1]],set_character[choose[1][0]][0],set_character[choose[1][0]][2],set_character[choose[1][0]][3], random.randint(3,5))
    player2s=pygame.sprite.Group()
    player2s.add(player2)
    v2p = player2.vel_x +2
    v2m = player2.vel_x -2

    player3= Player(50,169+(254-169)/2,set_character[choose[2][0]][1][choose[2][1]],set_character[choose[2][0]][0],set_character[choose[2][0]][2],set_character[choose[2][0]][3],random.randint(3,5))
    player3s=pygame.sprite.Group()
    player3s.add(player3)
    v3p = player3.vel_x +2
    v3m = player3.vel_x -2

    player4= Player(50,254+(343-254)/2,set_character[choose[3][0]][1][choose[3][1]],set_character[choose[3][0]][0],set_character[choose[3][0]][2],set_character[choose[3][0]][3],random.randint(3,5))
    player4s=pygame.sprite.Group()
    player4s.add(player4)
    v4p = player4.vel_x +2
    v4m = player4.vel_x -2

    player5= Player(50,343+(428-343)/2,set_character[choose[4][0]][1][choose[4][1]],set_character[choose[4][0]][0],set_character[choose[4][0]][2],set_character[choose[4][0]][3],random.randint(3,5))
    player5s=pygame.sprite.Group()
    player5s.add(player5)
    v5p = player5.vel_x +2
    v5m = player5.vel_x -2
  #---------------------------------------------  
    buffdebuff1 = buff_debuff(random.randint(300,650+400*main.type_choose),40,randint(1,6))
    buffdebuff1s = pygame.sprite.Group()
    buffdebuff1s.add(buffdebuff1)

    buffdebuff2 = buff_debuff(random.randint(300,650+400*main.type_choose),130,randint(1,6))
    buffdebuff2s = pygame.sprite.Group()
    buffdebuff2s.add(buffdebuff2)

    buffdebuff3 = buff_debuff(random.randint(300,650+400*main.type_choose),215,randint(1,6))
    buffdebuff3s = pygame.sprite.Group()
    buffdebuff3s.add(buffdebuff3)

    buffdebuff4 = buff_debuff(random.randint(300,650+400*main.type_choose),303,randint(1,6))
    buffdebuff4s = pygame.sprite.Group()
    buffdebuff4s.add(buffdebuff4)

    buffdebuff5 = buff_debuff(random.randint(300,650+400*main.type_choose),385,randint(1,6))
    buffdebuff5s = pygame.sprite.Group()
    buffdebuff5s.add(buffdebuff5)

 #____________________________________________________________________________________________________________
    with open('data_player/data.json') as file_name:
        data=json.load(file_name)
    user_name=data[0]['user'][ID]['user_name']
    coin=data[0]['user'][ID]['coin']
    AVA=pygame.image.load(r"img\main\ava.png") 
    COIN=pygame.image.load(r"img\main\coin1.png")  
    CHAT=pygame.image.load(r"img\main\btn_chatbox_1.png") 
    INPUT=pygame.image.load(r"img\main\Rectangle_14_e.png") 
    PRINT_CHAT=pygame.image.load(r"img\main\win_chatbox_1.png") 
    X=pygame.image.load(join("img","load_sign_in",f"Xv1.png"))
    font_main=font_v(SourceCodePro_Black,30)
    user=font_main.render(f'@{user_name}',True,(252, 205, 0,))
    user_chat=font_main.render(f'@{user_name}:',True,(255,255,255))
    coin_n=font_main.render(f'{coin}',True,(252, 205, 0,))
    layer=pygame.Surface((300,280))
    running=True
    chat=False
    active=False
    text=''
    dem=0
    hidden=0
    cmt_y=0
    active_cmt=False
    run= False
    user_text=u""
    pos = 0
    active_sound_win=False
    first=True
    user_text_temp=""
    winner_count=0
    while not run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE :
                    run= True
                    break   
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1 :
                    run= True
                    break        
                    
        draw(window, background, player1s, player2s, player3s, player4s, player5s, buffdebuff1s, buffdebuff2s, buffdebuff3s, buffdebuff4s,buffdebuff5s)                                
        pygame.display.update()
#-----------------------------------------------------------------------------------------------------------------------
    if run == True:
        window=pygame.display.set_mode((with_type[main.type_choose]+50,550))           
    while run:  
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False
                break    

            #_____________________________
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                click_sound.play()
                if chat :
                    if pygame.Rect((610,56),(29,60)).collidepoint(event.pos) or not pygame.Rect((285,37),(406,406)).collidepoint(event.pos):
                        chat =False
                if pygame.Rect((260,474),(81,63)).collidepoint(event.pos):
                    chat=True
                if pygame.Rect((341+18*(len(user_name)+2),465),(200,50)).collidepoint(event.pos):
                    active=True
                else :
                    active=False
                    # print(active)
            if event.type==pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_BACKSPACE:
                            # Go dau tieng viet
                            if event.unicode.isalpha():
                                # d + d
                                if remove_Vietnamese_letter(user_text).rfind(
                                    remove_Vietnamese_letter(event.unicode)) == len(user_text) - 1:
                                    user_text = user_text[: -1] + event.unicode
                                # du + d
                                elif remove_Vietnamese_letter(user_text).rfind(
                                    remove_Vietnamese_letter(event.unicode)) == len(user_text) - 2:
                                    user_text = user_text[:-2] + event.unicode + user_text[-1] * 2
                                # day + d
                                elif remove_Vietnamese_letter(user_text).rfind(
                                    remove_Vietnamese_letter(event.unicode)) == len(user_text) - 3:
                                    user_text = user_text[:-3] + event.unicode + user_text[-2:] * 2
                                # dung + d
                                elif remove_Vietnamese_letter(user_text).rfind(
                                    remove_Vietnamese_letter(event.unicode)) == len(user_text) - 4:
                                    user_text = user_text[:-4] + event.unicode + user_text[-3:] * 2
                                # duong + d
                                elif remove_Vietnamese_letter(user_text).rfind(
                                    remove_Vietnamese_letter(event.unicode)) == len(user_text) - 5:
                                    user_text = user_text[:-5] + event.unicode + user_text[-4:] * 2

                                if event.unicode == "ư" and user_text.rfind("ư") + 1 <= len(user_text) - 1:
                                    if user_text[user_text.rfind("ư") + 1] == "o":
                                        vi_tri = user_text.rfind("ư") + 1
                                        user_text = list(user_text)
                                        user_text[vi_tri] = "ơ"
                                        user_text = ''.join(user_text)
                                continue
                            else:
                                user_text = user_text[: -1]
                                continue

                        if len(user_text) <= 40:
                            user_text += event.unicode

                        if event.key == pygame.K_RETURN:
                            user_text_temp = user_text
                            main.text_chat.append(user_text_temp)
                            main.text_chat.append(chat_random[random.randint(0,len(chat_random)-1)])
                            user_text = u""
                            if active_cmt:
                                cmt_y+=2
                            # print(user_text_temp) 

        draw(window, background, player1s, player2s, player3s, player4s, player5s, buffdebuff1s, buffdebuff2s, buffdebuff3s, buffdebuff4s,buffdebuff5s) 
        if player1.x>=with_type[main.type_choose] or player2.x >=with_type[main.type_choose]  or player3.x >=with_type[main.type_choose]  or player4.x >=with_type[main.type_choose]  or player5.x >=with_type[main.type_choose] :
            active_sound_win=True
            if winner_count<=44:
                screen.blit(winner[winner_count//2],winner[winner_count//2].get_rect(center=(with_type[main.type_choose]/2,550/2-70)))
                if player1.x>=with_type[main.type_choose]:
                    winner_rect=set[choose[0][0]][choose[0][1]][0]
                    winner_rect=pygame.transform.scale(winner_rect,(250,250))
                elif player2.x>=with_type[main.type_choose]:
                    winner_rect=set[choose[1][0]][choose[1][1]][0]
                    winner_rect=pygame.transform.scale(winner_rect,(250,250))
                elif player3.x>=with_type[main.type_choose]:
                    winner_rect=set[choose[2][0]][choose[2][1]][0]
                    winner_rect=pygame.transform.scale(winner_rect,(250,250))
                elif player4.x>=with_type[main.type_choose]:
                    winner_rect=set[choose[3][0]][choose[3][1]][0]
                    winner_rect=pygame.transform.scale(winner_rect,(250,250))
                elif player5.x>=with_type[main.type_choose]:
                    winner_rect=set[choose[4][0]][choose[4][1]][0]
                    winner_rect=pygame.transform.scale(winner_rect,(250,250))
                
                screen.blit(winner_rect,winner_rect.get_rect(midtop=(with_type[main.type_choose]/2,550/2-40)))
                winner_count+=1
        if active_sound_win and first:
            racing_sound.stop()
            win_sound.play()
            racing_sound.play(-1)
            active_sound_win=False
            first=False
        if player1.x<=with_type[main.type_choose] or player2.x <=with_type[main.type_choose]  or player3.x <=with_type[main.type_choose]  or player4.x <=with_type[main.type_choose]  or player5.x <=with_type[main.type_choose] :
        #----------------------------------------------------------------------    
            if buffdebuff1.x >= player1.x >= buffdebuff1.x - 200:

                if player1.x >= buffdebuff1.x -100:
                    buffdebuff1.show = False       
                buffdebuff1.showup() 

            if player1.x >= buffdebuff1.x:
                buffdebuff1.active = True
                buffdebuff1.activebdb()
                   
            if player1.x >= buffdebuff1.x  :   #tăng tốc
                if buffdebuff1.st == 1 :
                    player1.vel_x = v1p
                    if (player1.x-buffdebuff1.x)/(v1p) >= 45:
                                player1.vel_x = v1p-2
                else:
                    if buffdebuff1.st == 2 and player1.cout == 0 : #đi lùi
                        player1.vel_x = -(v1m+2)
                        player1.cout = 1
                        player1.flip = True
                        
                        
                    else:
                        if buffdebuff1.st == 3 :  #giảm tốc
                            player1.vel_x = v1m
                            if (player1.x-buffdebuff1.x)/(v1m) >= 69:
                                player1.vel_x = v1m+2

                        else:
                            if buffdebuff1.st == 4 : #teleport
                                player1.vel_x =200
                                if player1.x >= buffdebuff1.x + 200:
                                    player1.vel_x = v1m + 2
                                
                            else:
                                if buffdebuff1.st == 5 : #về đích
                                    player1.x = with_type[main.type_choose]
                                           
                                else:
                                    if player1.cout ==0 : #cút về nhà 
                                     player1.cout =1
                                     player1.x = 100    
            if player1.x <= buffdebuff1.x and player1.cout ==1 :
                if abs(player1.x - buffdebuff1.x )/(v1m+2)>=49:
                    player1.vel_x = v1m +2
                    player1.flip = False                                                                  
         #------------------------------------------------------------------
            if buffdebuff2.x >= player2.x >= buffdebuff2.x - 200:

                if player2.x >= buffdebuff2.x -100:
                    buffdebuff2.show = False       
                buffdebuff2.showup() 

            if player2.x >= buffdebuff2.x:
                    buffdebuff2.active = True
                    buffdebuff2.activebdb()
                   
            if player2.x >= buffdebuff2.x  :   #tăng tốc
                if buffdebuff2.st == 1 :
                    player2.vel_x = v2p
                    if (player2.x-buffdebuff2.x)/(v2p) >= 45:
                                player2.vel_x = v2p-2
                else:
                    if buffdebuff2.st == 2 and player2.cout == 0 : #đi lùi
                        player2.vel_x = -(v2m+2)
                        player2.cout = 1
                        player2.flip = True
                        
                    else:
                        if buffdebuff2.st == 3 :  # giảm tốc 
                            player2.vel_x = v2m
                            if (player2.x-buffdebuff2.x)/(v2m) >= 69:
                                player2.vel_x = v2m+2

                        else:
                            if buffdebuff2.st == 4 : 
                                player2.vel_x =200
                                if player2.x >= buffdebuff2.x + 200:
                                    player2.vel_x = v2m + 2
                                
                            else:
                                if buffdebuff2.st == 5 :
                                    player2.x = with_type[main.type_choose]
                                           
                                else:
                                    if player2.cout ==0 :
                                     player2.cout =1
                                     player2.x = 100       
            if player2.x <= buffdebuff2.x and player2.cout ==1 :
                if abs(player2.x - buffdebuff2.x )/(v2m+2)>=49:
                    player2.vel_x = v2m +2
                    player2.flip = False
                
        #------------------------------------------------------------------
            if buffdebuff3.x >= player3.x >= buffdebuff3.x - 200: 
           
                if player3.x >= buffdebuff3.x - 100:
                    buffdebuff3.show = False       
                buffdebuff3.showup() 
            if player3.x >= buffdebuff3.x:

                buffdebuff3.active = True
                buffdebuff3.activebdb()
                   
            if player3.x >= buffdebuff3.x  :   
                if buffdebuff3.st == 1 :
                    player3.vel_x = v3p
                    if (player3.x-buffdebuff3.x)/(v3p) >= 50:
                                player3.vel_x = v3p-2
                else:
                    if buffdebuff3.st == 2 and player3.cout == 0 : #đi lùi
                        player3.vel_x = -(v3m+2)
                        player3.cout = 1
                        player3.flip = True
                        
                        
                    else:
                        if buffdebuff3.st == 3 : 
                            player3.vel_x = v3m
                            if (player3.x-buffdebuff3.x)/(v3m) >= 69:
                                player3.vel_x = v3m+2

                        else:
                            if buffdebuff3.st == 4 :
                                player3.vel_x =200
                                if player3.x >= buffdebuff3.x + 200:
                                    player3.vel_x = v3m + 2
                                
                            else:
                                if buffdebuff3.st == 5 :
                                    player3.x = with_type[main.type_choose]
                                     
                                else:
                                    if player3.cout ==0 :
                                     player3.cout =1
                                     player3.x = 100  
            if player3.x <= buffdebuff3.x and player3.cout ==1 :
                if abs(player3.x - buffdebuff3.x )/(v3m+2)>=49:
                    player3.vel_x = v3m +2
                    player3.flip = False                                  
        #------------------------------------------------------------------
            if buffdebuff4.x >= player4.x >= buffdebuff4.x - 200:          
                if player4.x >= buffdebuff4.x -100:
                    buffdebuff4.show = False       
                buffdebuff4.showup() 

            if player4.x >= buffdebuff4.x:
                buffdebuff4.active = True
                buffdebuff4.activebdb()
                   
            if player4.x >= buffdebuff4.x  :   
                if buffdebuff4.st == 1 :
                    player4.vel_x = v4p
                    if (player4.x-buffdebuff4.x)/(v4p) >= 50:
                                player4.vel_x = v4p-2
                else:
                    if buffdebuff4.st == 2 and player4.cout == 0 : #đi lùi
                        player4.vel_x = -(v4m+2)
                        player4.cout = 1
                        player4.flip = True
                        
                    else:
                        if buffdebuff4.st == 3 :       
                            player4.vel_x = v4m
                            if (player4.x-buffdebuff4.x)/(v4m) >= 69:
                                player4.vel_x = v4m+2

                        else:
                            if buffdebuff4.st == 4 :
                                player4.vel_x =200
                                if player4.x >= buffdebuff4.x + 200:
                                    player4.vel_x = v4m + 2        

                            else:
                                if buffdebuff4.st == 5 :
                                    player4.x = with_type[main.type_choose]
                                          
                                else:
                                    if player4.cout ==0 :
                                     player4.cout =1
                                     player4.x = 100  
            if player4.x <= buffdebuff4.x and player4.cout ==1 :
                if abs(player4.x - buffdebuff4.x )/(v4m+2)>=49:
                    player4.vel_x = v4m +2
                    player4.flip = False                            
        #------------------------------------------------------------------
            if buffdebuff5.x >= player5.x >= buffdebuff5.x - 200:          
                if player5.x >= buffdebuff5.x -100:
                    buffdebuff5.show = False       
                buffdebuff5.showup() 

            if player5.x >= buffdebuff5.x:
                buffdebuff5.active = True
                buffdebuff5.activebdb()
                   
            if player5.x >= buffdebuff5.x  :   
                if buffdebuff5.st == 1 :
                    player5.vel_x = v5p
                    if (player5.x-buffdebuff5.x)/(v5p) >= 50:
                                player5.vel_x = v5p-2
                else:
                    if buffdebuff5.st == 2 and player5.cout == 0 : #đi lùi
                        player5.vel_x = -(v5m+2)
                        player5.cout = 1
                        player5.flip = True
                        
                        
                    else:
                        if buffdebuff5.st == 3 :       
                            player5.vel_x = v5m
                            if (player5.x-buffdebuff5.x)/(v5m) >= 69:
                                player5.vel_x = v5m+2

                        else:
                            if buffdebuff5.st == 4 :
                                player5.vel_x =200
                                if player5.x >= buffdebuff5.x + 200:
                                    player5.vel_x = v5m + 2        

                            else:
                                if buffdebuff5.st == 5 :
                                    player5.x = with_type[main.type_choose]
                                          
                                else:
                                    if player5.cout ==0 :
                                     player5.cout =1
                                     player5.x = 100   
            if player5.x <= buffdebuff5.x and player5.cout ==1 :
                if abs(player5.x - buffdebuff5.x )/(v5m+2)>=49:
                    player5.vel_x = v5m +2
                    player5.flip = False                                               
        #--------------------------------------------------------------------

            player1.position()   
            player1.update()
            player1.timer(1/FPS)
            
            player2.position()
            player2.update()
            player2.timer(1/FPS)

            player3.position()   
            player3.update()
            player3.timer(1/FPS)

            player4.position()   
            player4.update()
            player4.timer(1/FPS)

            player5.position()   
            player5.update()
            player5.timer(1/FPS)

            screen.blit(AVA,(14,460))
            screen.blit(COIN,(119,500))
            INPUT=pygame.transform.scale(INPUT,(max((341+18*(len(user_name)+2+len(user_text)*0.67)-307+20),408),50))
            screen.blit(INPUT,(307,475))
            screen.blit(CHAT,(260,474))
            screen.blit(user,(119,460))
            screen.blit(coin_n,(157,500))
            screen.blit(user_chat,(341,478))
            screen.blit(font_v(SourceCodePro_Black,20).render(f'{user_text}',True,WHITE),(341+18*(len(user_name)+2),485))
            if active:
                dem+=1
            if  active and dem>=40:
                if hidden<=40:
                    screen.blit(font_v(SourceCodePro_Black,30).render(f'|',True,WHITE),(341+18*(len(user_name)+2+len(user_text)*0.67),478))
                else :
                    hidden=0
                    dem=0
                hidden+=1
            if chat:
                screen.blit(PRINT_CHAT,(285,37))
                screen.blit(X,(610,56))
                screen.blit(layer,(336,100))
            layer.blit(PRINT_CHAT,(-51,-64))
            if len(main.text_chat)!=0:
                for i in range(0,len(main.text_chat)):
                    if i>=6:
                        active_cmt=True

                    if i%2==0:
                        layer.blit(font_v(SourceCodePro_Black,15).render(f'@{user_name}:{main.text_chat[i]}',True,WHITE),(0,18*i))
                        layer.blit(font_v(SourceCodePro_Black,15).render(f'@{user_name}:',True,YELLOW),(0,18*i))
                        screen.blit(font_v(SourceCodePro_Black,15).render(f'@{user_name}:{main.text_chat[i]}',True,WHITE),(10,18*(i-cmt_y)))
                        screen.blit(font_v(SourceCodePro_Black,15).render(f'@{user_name}:',True,YELLOW),(10,18*(i-cmt_y)))

                    else :
                        layer.blit(font_v(SourceCodePro_Black,15).render(f'@bot:{main.text_chat[i]}',True,WHITE),(0,18*i))
                        layer.blit(font_v(SourceCodePro_Black,15).render(f'@bot:',True,BLUE_V2),(0,18*i))
                        screen.blit(font_v(SourceCodePro_Black,15).render(f'@bot:{main.text_chat[i]}',True,WHITE),(10,18*(i-cmt_y)))
                        screen.blit(font_v(SourceCodePro_Black,15).render(f'@bot:',True,BLUE_V2),(10,18*(i-cmt_y)))
        
        #---------------------------------------------------------------------------------------------------------------  
        #---------------------------------------------------------------------------------------------------------------
        if player1.x >= with_type[main.type_choose] and player2.x >= with_type[main.type_choose] and player3.x >= with_type[main.type_choose] and player4.x >= with_type[main.type_choose] and player5.x >= with_type[main.type_choose] and print_count ==0:  
            print_count=1    
            time_run=[0,0,0,0,0]
            i = [0,0,0,0,0]
            x = 0
            time_run[0]=player1.time_count
            time_run[1]=player2.time_count
            time_run[2]=player3.time_count
            time_run[3]=player4.time_count
            time_run[4]=player5.time_count
            time_run_1=sorted(time_run)
            for j in range(5):
                for k in range(5):
                    if(time_run[k] == time_run_1[j]):
                        i[j] = k+1
            for m in range(5) :
                for j in range(5):
                            if (j != m) and i[j]==i[m]:
                                if j<m:
                                    if i[j]==1:
                                        i[m]=i[m]+1
                                    else:
                                        i[m]=i[m]-1
                                if j>m:
                                    if i[j]==1:
                                        i[j]=i[m]+1
                                    else:
                                        i[j]=i[m]-1    
            # print(time_run)
            # print(time_run_1)
            # print(i)                
            run=False
         
        pygame.display.update()     
   #-------------------------------------------------------------------------     
    if run==False :
       window=pygame.display.set_mode((WIDTH,HEIGHT))    
    while run == False:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE :
                    run= True
                    break
        player1.update()
        player2.update()
        player3.update()
        player4.update()
        player5.update()        
                
        draw(window, background, player1s, player2s, player3s, player4s, player5s, buffdebuff1s, buffdebuff2s, buffdebuff3s, buffdebuff4s,buffdebuff5s)                                             
                            
            

        pygame.display.update()     
        return time_run,i
    pygame.quit()
    quit()        
class Main():
    def __init__(self):
        super().__init__()
        self.end_loadBG=False
        self.version="v1"
        self.id=-1
        self.type_choose=0  # mặc định là map ngắn 
        self.text_chat=[]
        self.emotion="normal"
        self.speed="100"
        self.sound=40 #%
        self.emotion_history_id=0
        self.emotion_result_rank=1
        self.method_emotion=0
        self.logout=False
    def load_BG(self):
        RECT_GUI=pygame.transform.scale(pygame.image.load(join("img","history",f"rect_gui{self.version}.png")) ,(667,446))
        TEXT=pygame.image.load(join("img","history",f"text.png"))        
        HEADER=pygame.image.load(join("img","history",f"header.png"))  
        layer=pygame.Surface((667-120,341))  
        COL_SCROLL=pygame.image.load(join("img","history",f"rect_scroll{self.version}.png"))     
        COL_SCROLL_SMALL=pygame.image.load(join("img","history",f"rect_scroll_small{self.version}.png"))
        scroll=0     
        BG=pygame.image.load(join("img","load_sign_in",f"bg_setting{self.version}.png"))
        LOGO=pygame.transform.scale(pygame.image.load(join("img","load_sign_in",f"logo_nobg{self.version}.png")),(WIDTH,HEIGHT))
        SIGN_UP_BTN=pygame.image.load(join("img","load_sign_in",f"btn_signup{self.version}.png"))
        SIGN_UP_BTN_HOVER=pygame.image.load(join("img","load_sign_in",f"btn_signup1_hover{self.version}.png"))
        LOG_IN_BTN=pygame.image.load(join("img","load_sign_in",f"btn_login_1{self.version}.png"))
        LOG_IN_BTN_HOVER=pygame.image.load(join("img","load_sign_in",f"btn_login1_hover{self.version}.png")) 
        SUN=pygame.image.load(join("img","load_sign_in",f"sun.png")) 
        CLOUD=pygame.image.load(join("img","load_sign_in",f"cloud.png")) 
        LOG_IN_B=LOG_IN_BTN
        SIGN_UP_B= SIGN_UP_BTN
        HELP=pygame.image.load(r"img\load_sign_in\info.png")
        running=True
        BG_x=0
        LOGO_y=0
        chieu=1
        active_ver=False
        active_gui=False
        while running:
            CLOCK.tick(60)
            if active_ver:
                active_ver=False
                COL_SCROLL=pygame.image.load(join("img","history",f"rect_scroll{self.version}.png"))     
                COL_SCROLL_SMALL=pygame.image.load(join("img","history",f"rect_scroll_small{self.version}.png"))
                RECT_GUI=pygame.transform.scale(pygame.image.load(join("img","history",f"rect_gui{self.version}.png")) ,(667,446))
                BG=pygame.image.load(join("img","load_sign_in",f"bg_setting{self.version}.png"))
                LOGO=pygame.transform.scale(pygame.image.load(join("img","load_sign_in",f"logo_nobg{self.version}.png")),(WIDTH,HEIGHT))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                    self.id=-2
                #______________guide_________________
                if event.type==pygame.KEYDOWN and event.key==pygame.K_TAB:
                    active_ver=True
                    if self.version=="v1":
                        self.version="v2"
                    else :
                        self.version="v1"   
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if active_gui and event.button==1:
                        click_sound.play()
                        active_gui=False
                    if event.button==4:
                        if scroll<0:
                            scroll+=30
                    elif event.button==5:
                        if scroll>(-TEXT.get_height()+layer.get_height()):
                            scroll-=30
                # HOVER BTN
                if pygame.Rect((158,360),(281,98)).collidepoint(pygame.mouse.get_pos()):
                    LOG_IN_B=LOG_IN_BTN_HOVER
                if pygame.Rect((511,360),(305,98)).collidepoint(pygame.mouse.get_pos()):
                    SIGN_UP_B= SIGN_UP_BTN_HOVER
                if not (pygame.Rect((158,360),(281,98)).collidepoint(pygame.mouse.get_pos()) or pygame.Rect((511,360),(305,98)).collidepoint(pygame.mouse.get_pos())):
                    LOG_IN_B=LOG_IN_BTN
                    SIGN_UP_B= SIGN_UP_BTN
                if event.type==pygame.MOUSEBUTTONDOWN and running and event.button==1: 
                    click_sound.play()
                    if HELP.get_rect(center=(WIDTH-50,50)).collidepoint(event.pos) :
                        active_gui=True
                    #login btn
                    if pygame.Rect((158,360),(281,98)).collidepoint(event.pos)  :
                        main.LOGIN()
                        if self.id!=-1:
                            self.load_BG=True
                            running=False
                            return 1
                        active_ver=True
                    #signup btn   
                    if pygame.Rect((511,360),(305,98)).collidepoint(event.pos)  :                      
                        main.SIGN_UP()
                        if self.id!=-1:
                            self.end_loadBG=True
                            running=False
                            return 1
                        active_ver=True
            #logo move
            LOGO_y+=0.2*chieu
            if LOGO_y<-5:
                chieu=1
            if LOGO_y>5:
                chieu=-1
            BG_x-=0.5
            if BG_x==-975:
                BG_x=0
            screen.blit(BG,(BG_x,0))
            screen.blit(BG,(BG_x+975,0))
            if self.version=="v2":
                screen.blit(SUN,(0,0))
                screen.blit(CLOUD,(BG_x,0))
                screen.blit(CLOUD,(BG_x+975,0))
            screen.blit(LOGO,(0,LOGO_y))
            screen.blit(LOG_IN_B,(158,360))
            screen.blit(SIGN_UP_B,(511,360))
            screen.blit(HELP,HELP.get_rect(center=(WIDTH-50,50)))
            if active_gui:
                screen.blit(RECT_GUI,RECT_GUI.get_rect(center=(WIDTH/2,HEIGHT/2)))
                screen.blit(layer,layer.get_rect(midtop=(WIDTH/2,105+27)))
                screen.blit(HEADER,HEADER.get_rect(midtop=(WIDTH/2,60)))
                layer.blit(RECT_GUI,(-60,-105))
                layer.blit(TEXT,TEXT.get_rect(topleft=(0,scroll)))
                screen.blit(COL_SCROLL,COL_SCROLL.get_rect(center=(975-154-20,105/2+446/2)))
            pygame.display.update()   
    def LOGIN(self):  
        MANAGER.clear_and_reset()  
        data=[] # get data json
        with open('data_player/data.json') as file_name:
            data=json.load(file_name)
        BG1=pygame.image.load(join("img","load_sign_in",f"bg_setting{self.version}.png"))
        BG=pygame.image.load(join("img","load_sign_in",f"Rectangle_4{self.version}.png"))
        EXIT=pygame.image.load(join("img","load_sign_in",f"X{self.version}.png"))
        TEXT_USERNAME=pygame.image.load(join("img","load_sign_in",f"username{self.version}.png"))
        TEXT_PASSWORK=pygame.image.load(join("img","load_sign_in",f"password{self.version}.png"))
        LINE=pygame.image.load(join("img","load_sign_in",f"line1{self.version}.png"))
        INPUT=pygame.image.load(join("img","load_sign_in",f"input-pass{self.version}.png"))
        LOGIN_BTN=pygame.image.load(join("img","load_sign_in",f"btn_login_1{self.version}.png"))
        FACE_ID=pygame.image.load("img/load_sign_in/face_id.png")
        USER_NAME=input_type[self.version].UITextEntryLine(relative_rect=pygame.Rect((440,186),(386,56)),object_id="#text_entry1")
        PASSWORK=input_type[self.version].UITextEntryLine(relative_rect=pygame.Rect((440,276),(386,56)),manager=MANAGER,object_id="#text_entry2")
        PASSWORK.set_text_hidden(True)
        running=True
        user_name=""
        passwork=" "
        active=False
        Warning_mk=False
        Warning_pass=False
        hidden=True # hidden text
        active_ver=False
        while running:
            CLOCK.tick(60)
            UI_REFRESH_RATE=CLOCK.tick(60)/1000
            if active_ver:
                active_ver=False
                BG1=pygame.image.load(join("img","load_sign_in",f"bg_setting{self.version}.png"))
                BG=pygame.image.load(join("img","load_sign_in",f"Rectangle_4{self.version}.png"))
                EXIT=pygame.image.load(join("img","load_sign_in",f"X{self.version}.png"))
                TEXT_USERNAME=pygame.image.load(join("img","load_sign_in",f"username{self.version}.png"))
                TEXT_PASSWORK=pygame.image.load(join("img","load_sign_in",f"password{self.version}.png"))
                LINE=pygame.image.load(join("img","load_sign_in",f"line1{self.version}.png"))
                INPUT=pygame.image.load(join("img","load_sign_in",f"input-pass{self.version}.png"))
                LOGIN_BTN=pygame.image.load(join("img","load_sign_in",f"btn_login_1{self.version}.png"))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                    self.id=-2
                #đăng nhập nhận diện khuôn mặt 
                if  (event.type==pygame.MOUSEBUTTONDOWN and pygame.Rect((230,360),(123,123)).collidepoint(event.pos)): 
                    for id in range(len(data[0]['user'])):
                        if user_name==data[0]['user'][id]['user_name'] :
                            Warning_mk=False
                            if data[0]['user'][id]['face_id']=="yes":
                                if test.check_for_login(id):
                                    self.id=id
                                    running=False
                                    active=True
                                else:
                                    Warning_pass=True
                            else :
                                Warning_pass=True
                            break
                        else: 
                            Warning_mk=True
                         
                if event.type==pygame.KEYDOWN and event.key==pygame.K_TAB:
                    if self.version=="v1":
                        self.version="v2"
                        active_ver=True
                        MANAGER.clear_and_reset()
                        USER_NAME=input_type[self.version].UITextEntryLine(relative_rect=pygame.Rect((440,186),(386,56)),object_id="#text_entry1")
                        PASSWORK=input_type[self.version].UITextEntryLine(relative_rect=pygame.Rect((440,276),(386,56)),manager=MANAGER,object_id="#text_entry2")
                    else :
                        self.version="v1"
                        active_ver=True
                        MANAGER.clear_and_reset()
                        USER_NAME=input_type[self.version].UITextEntryLine(relative_rect=pygame.Rect((440,186),(386,56)),object_id="#text_entry1")
                        PASSWORK=input_type[self.version].UITextEntryLine(relative_rect=pygame.Rect((440,276),(386,56)),manager=MANAGER,object_id="#text_entry2")
                # input text
                if event.type==pygame_gui.UI_TEXT_ENTRY_CHANGED and event.ui_element==USER_NAME:
                        user_name=event.text
                        dem=0
                        for i in range(0,len(user_name)):
                            if user_name[i]==" ":
                                dem+=1
                            if dem!=0:
                                Warning_mk=True
                            else:
                                Warning_mk=False
                #input password
                if event.type==pygame_gui.UI_TEXT_ENTRY_CHANGED and event.ui_element==PASSWORK:
                        passwork=event.text 
                        dem=0
                        for i in range(0,len(passwork)):
                            if passwork[i]==" ":
                                dem+=1
                            if dem!=0:
                                Warning_pass=True
                            else:
                                Warning_pass=False
                if event.type==pygame.MOUSEBUTTONDOWN:
                    # hidden textr
                    if pygame.Rect((440+330,276),(56,56)).collidepoint(event.pos)  and event.button==1:
                        click_sound.play()
                        hidden=not hidden
                        PASSWORK.set_text_hidden(hidden)
                    #EXIT   
                    if pygame.Rect((869,52),(29,60)).collidepoint(event.pos)  and event.button==1:
                            click_sound.play()
                            running=False
                            active=True
                    #LOGIN_click
                    if pygame.Rect((347,374),(281,98)).collidepoint(event.pos)  and event.button==1:
                        click_sound.play()
                        i=len(data[0]['user'])
                        for k in range(0,i):
                                if data[0]['user'][k]['user_name']==user_name and data[0]['user'][k]['passwork']==passwork:
                                    self.id=data[0]['user'][k]['id']
                                    active=True
                                    running=False  
                                    return 1
                                else:
                                    if data[0]['user'][k]['user_name']!=user_name:
                                        Warning_mk=True
                                    if data[0]['user'][k]['passwork']!=passwork:
                                        Warning_pass=True
                #LOGIN_ENTER
                if event.type==pygame.KEYDOWN and event.key==pygame.K_RETURN :
                    i=len(data[0]['user'])
                    for k in range(0,i):
                        if data[0]['user'][k]['user_name']==user_name and data[0]['user'][k]['passwork']==passwork:
                                    self.id=data[0]['user'][k]['id']
                                    active=True
                                    running=False  
                                    return 1
                    for k in range(0,i):    
                                    if data[0]['user'][k]['user_name']!=user_name:
                                        Warning_mk=True
                                    else:
                                        Warning_mk=False
                                        break
                    for k in range(0,i):
                                    if data[0]['user'][k]['passwork']!=passwork:
                                        Warning_pass=True
                                    else :
                                        Warning_pass=False
                                        break
                MANAGER.process_events(event)
            MANAGER.update(UI_REFRESH_RATE) 
            screen.blit(BG1,(0,0))
            screen.blit(BG,(35,40))
            screen.blit(EXIT,(869,52))
            screen.blit(TEXT_USERNAME,(120,198))
            screen.blit(TEXT_PASSWORK,(120,285))
            screen.blit(LINE,(35,112.5))
            screen.blit(INPUT,(412,180))
            screen.blit(INPUT,(412,270))
            screen.blit(LOGIN_BTN,(347,374))
            screen.blit(FACE_ID,(230,360))
            MANAGER.draw_ui(screen)
            if Warning_mk:
                screen.blit(pygame.font.Font(r'img\font\SourceCodePro-MediumItalic.ttf',15).render(f'tên đăng nhập không hợp lệ!',True,(255,0,0)),(120,230))
            if Warning_pass:
                screen.blit(pygame.font.Font(r'img\font\SourceCodePro-MediumItalic.ttf',15).render(f'mật khẩu không hợp lệ!',True,(255,0,0)),(120,330))  
            if not running:
                MANAGER.clear_and_reset()
            pygame.display.update()
            if active:
                running=False
    def SIGN_UP(self):
        
        data=[] #get data
        with open('data_player/data.json') as file_name:
            data=json.load(file_name)
        user_name=""
        passwork=" "
        r_passwork="  "
        MANAGER.clear_and_reset()
        BG1=pygame.image.load(join("img","load_sign_in",f"bg_setting{self.version}.png"))
        BG=pygame.image.load(join("img","load_sign_in",f"Rectangle_4{self.version}.png"))
        EXIT=pygame.image.load(join("img","load_sign_in",f"X{self.version}.png"))
        TEXT_USERNAME=pygame.image.load(join("img","load_sign_in",f"username{self.version}.png"))
        TEXT_PASSWORK=pygame.image.load(join("img","load_sign_in",f"password{self.version}.png"))
        TEXT_CONFIRM=pygame.image.load(join("img","load_sign_in",f"confirm_password{self.version}.png"))
        LINE=pygame.image.load(join("img","load_sign_in",f"line1{self.version}.png"))
        SIGN_UP=pygame.image.load(join("img","load_sign_in",f"btn_signup{self.version}.png"))
        INPUT=pygame.image.load(join("img","load_sign_in",f"input-pass{self.version}.png"))
        USER_NAME=input_type[self.version].UITextEntryLine(relative_rect=pygame.Rect((446,117),(386,54)),manager=MANAGER,object_id="#text_entry3")
        PASSWORK=input_type[self.version].UITextEntryLine(relative_rect=pygame.Rect((446,206),(386,54)),manager=MANAGER,object_id="#text_entry4")
        CONFIRM=input_type[self.version].UITextEntryLine(relative_rect=pygame.Rect((446,311),(386,54)),manager=MANAGER,object_id="#text_entry5")
        running=True
        active=False
        #-----------------WARNING--------------------
        Warning_r_pass=False
        Warning_pass=False
        Warning_mk=False
        Warning_exist=False
        active_ver=False
        while running:
            CLOCK.tick(60)
            UI_REFRESH_RATE=CLOCK.tick(60)/1000
            if active_ver:
                active_ver=False
                BG1=pygame.image.load(join("img","load_sign_in",f"bg_setting{self.version}.png"))
                BG=pygame.image.load(join("img","load_sign_in",f"Rectangle_4{self.version}.png"))
                EXIT=pygame.image.load(join("img","load_sign_in",f"X{self.version}.png"))
                TEXT_USERNAME=pygame.image.load(join("img","load_sign_in",f"username{self.version}.png"))
                TEXT_PASSWORK=pygame.image.load(join("img","load_sign_in",f"password{self.version}.png"))
                TEXT_CONFIRM=pygame.image.load(join("img","load_sign_in",f"confirm_password{self.version}.png"))
                LINE=pygame.image.load(join("img","load_sign_in",f"line1{self.version}.png"))
                SIGN_UP=pygame.image.load(join("img","load_sign_in",f"btn_signup{self.version}.png"))
                INPUT=pygame.image.load(join("img","load_sign_in",f"input-pass{self.version}.png"))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                    self.id==-2
                if event.type==pygame.KEYDOWN and event.key==pygame.K_TAB:
                    if self.version=="v1":
                        self.version="v2"
                        active_ver=True
                        MANAGER.clear_and_reset()
                        USER_NAME=input_type[self.version].UITextEntryLine(relative_rect=pygame.Rect((446,117),(386,54)),manager=MANAGER,object_id="#text_entry3")
                        PASSWORK=input_type[self.version].UITextEntryLine(relative_rect=pygame.Rect((446,206),(386,54)),manager=MANAGER,object_id="#text_entry4")
                        CONFIRM=input_type[self.version].UITextEntryLine(relative_rect=pygame.Rect((446,311),(386,54)),manager=MANAGER,object_id="#text_entry5")
                    else :
                        self.version="v1"
                        active_ver=True
                        MANAGER.clear_and_reset()
                        USER_NAME=input_type[self.version].UITextEntryLine(relative_rect=pygame.Rect((446,117),(386,54)),manager=MANAGER,object_id="#text_entry3")
                        PASSWORK=input_type[self.version].UITextEntryLine(relative_rect=pygame.Rect((446,206),(386,54)),manager=MANAGER,object_id="#text_entry4")
                        CONFIRM=input_type[self.version].UITextEntryLine(relative_rect=pygame.Rect((446,311),(386,54)),manager=MANAGER,object_id="#text_entry5")
                #GET DATA iNPUT 
                if event.type==pygame_gui.UI_TEXT_ENTRY_CHANGED and event.ui_element==USER_NAME:
                    user_name=event.text
                    dem=0
                    for i in range(0,len(user_name)):
                        if user_name[i]==" ":
                            dem+=1
                        if dem!=0:
                            Warning_mk=True
                        else:
                            Warning_mk=False
                        
                            for i in range(0,len(data[0]['user'])):
                                if data[0]['user'][i]['user_name']==user_name:
                                        Warning_exist=True
                                        break
                                else:
                                        Warning_exist=False   
                #password input 
                if event.type==pygame_gui.UI_TEXT_ENTRY_CHANGED and event.ui_element==PASSWORK:
                    passwork=event.text
                    dem=0
                    for i in range(0,len(passwork)):
                        if passwork[i]==" ":
                            dem+=1
                        if dem==0:
                            Warning_pass=False
                        else:
                            Warning_pass=True
                #password confirm
                if event.type==pygame_gui.UI_TEXT_ENTRY_CHANGED and event.ui_element==CONFIRM:
                    r_passwork=event.text 
                #SIGN_UP   CLICK 
                if event.type==pygame.MOUSEBUTTONDOWN:
                        #EXIT   
                        if pygame.Rect((869,52),(29,60)).collidepoint(event.pos)  and event.button==1:
                            click_sound.play()
                            running=False
                            end=False
                            active=True
                #SIGN_UP ENTER_click
                if (event.type==pygame.KEYDOWN and event.key==pygame.K_RETURN) or (event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and pygame.Rect((347,400),(305,98)).collidepoint(event.pos)):
                    click_sound.play()
                    if not Warning_mk and not Warning_pass and not Warning_exist:
                        if passwork==r_passwork:
                            data[0]['user'].append({"user_name":"","passwork":""})
                            i=len(data[0]['user'])
                            data[0]['user'][i-1]['id']=i-1
                            data[0]['user'][i-1]['user_name']=user_name
                            data[0]['user'][i-1]['passwork']=passwork
                            data[0]['user'][i-1]['coin']=100
                            data[0]['user'][i-1]['face_id']="no"
                            data.append({"history":[],"account":[]})
                            self.id=i-1
                            running=False
                            end=True
                            active=True  
                            with open('data_player/data.json','w') as file_name:
                                json.dump(data,file_name,indent=4) 
                            return 1
                        else : 
                            Warning_r_pass=True
                    
                MANAGER.process_events(event)
            MANAGER.update(UI_REFRESH_RATE)
            screen.blit(BG1,(0,0))
            screen.blit(BG,(35,40))
            screen.blit(EXIT,(869,52))
            screen.blit(TEXT_USERNAME,(113,130))
            screen.blit(TEXT_PASSWORK,(113,207))
            screen.blit(TEXT_CONFIRM,(113,275))
            screen.blit(LINE,(35,90))
            screen.blit(INPUT,(418,112))
            screen.blit(INPUT,(418,200))
            screen.blit(INPUT,(418,306))
            screen.blit(SIGN_UP,(347,400))
            MANAGER.draw_ui(screen)
            if Warning_mk:
                screen.blit(pygame.font.Font(r'img\font\SourceCodePro-MediumItalic.ttf',15).render(f'tên đăng nhập không hợp lệ!',True,(255,0,0)),(113,160))
            else:
                if Warning_exist:
                    screen.blit(pygame.font.Font(r'img\font\SourceCodePro-MediumItalic.ttf',15).render(f'tài khoản đã tồn tại!',True,(255,0,0)),(113,160))
            if Warning_pass:
                screen.blit(pygame.font.Font(r'img\font\SourceCodePro-MediumItalic.ttf',15).render(f'mật khẩu không hợp lệ!',True,(255,0,0)),(112,250))  
            if Warning_r_pass:
                screen.blit(pygame.font.Font(r'img\font\SourceCodePro-MediumItalic.ttf',15).render(f'mật khẩu nhập lại không hợp lệ!',True,(255,0,0)),(113,380))   
            if not running:
                MANAGER.clear_and_reset()
            pygame.display.update()
            if active:   
                running=False
    def chest(self,BG_x):
        running=True
        BG=pygame.transform.scale(pygame.image.load(r"img\main\bgr.png"),(975,550))
        RECT=pygame.image.load(r"img\main\bgr_blue.png")
        while running:
            CLOCK.tick(60)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                    click_sound.play()
                    if pygame.Rect((900,15),(50,50)).collidepoint(event.pos):
                        running=False
                if event.type==pygame.KEYDOWN and event.key==pygame.K_BACKSPACE:
                        running=False
            BG_x-=0.5
            if BG_x==-975:
                BG_x=0
            screen.blit(BG,(BG_x,0))
            screen.blit(BG,(BG_x+975,0))
            screen.blit(RECT,(41,69))
            screen.blit(RECT,(272,69))
            screen.blit(RECT,(503,69))
            screen.blit(RECT,(734,69))
            screen.blit(font_v(SourceCodePro_Black,50).render(f'X',True,YELLOW),(900,15))
            pygame.display.update()
            if not running:
                return BG_x # to background can run continue 
    def arcade(self,BG_x):
        running = True
        data=[] #get data
        with open('data_player/data.json') as file_name:
            data=json.load(file_name)
        BG=pygame.transform.scale(pygame.image.load(r"img\main\bgr.png"),(975,550))
        RECT=pygame.image.load(r"img\main\Rectangle 25.png")
        user_name=data[0]['user'][self.id]['user_name']
        coin=data[0]['user'][self.id]['coin']
        COIN=pygame.image.load(r"img\main\coin1.png")  
        AVA=pygame.image.load(r"img\main\ava.png") 
        font=pygame.font.Font(r'img\font\SourceCodePro-BlackItalic.ttf',30)
        font_coin=pygame.font.Font(r'img\font\SourceCodePro-BlackItalic.ttf',25)
        font_main=font_v(SourceCodePro_Black,30)
        name=font.render(f'@{(user_name)}',True,(31,5,73)) #{str(score)}
        coin_bg=font_coin.render(f'{int(coin)}',True,(31,5,73))
        icon_game=[
            pygame.transform.scale(pygame.image.load(r'img\tetris.png'),(200,200)),
            pygame.transform.scale(pygame.image.load(r'img\pong.png'),(200,200)),
            pygame.transform.scale(pygame.image.load(r'img\bonk_cheems.png'),(200,200)),
            pygame.transform.scale(pygame.image.load(r'img\snake.png'),(200,200))
        ]
        icon_game_re=[
            pygame.transform.scale(pygame.image.load(r'img\tetris.png'),(200,200)),
            pygame.transform.scale(pygame.image.load(r'img\pong.png'),(200,200)),
            pygame.transform.scale(pygame.image.load(r'img\bonk_cheems.png'),(200,200)),
            pygame.transform.scale(pygame.image.load(r'img\snake.png'),(200,200))
        ]
        name_game=[
            "Tettris",
            "Pong",
            "bonk Cheems",
            "Snake"
        ]        
        while running:
            CLOCK.tick(60)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                    click_sound.play()
                    if pygame.Rect((900,15),(50,50)).collidepoint(event.pos):
                        running=False
                    for i in range(4):
                        if pygame.Rect((232*i+29,127),(220,220)).collidepoint(event.pos):   
                            icon_game[i]=pygame.transform.scale(icon_game[i],(220,220))   
                            data[self.id+1]['account'].append({})   
                            if i==0:
                                tentris=tetris.Tetris(16,30)
                                coin_earn=int(tentris.run()/10) 
                                data[0]['user'][self.id]['coin']+=coin_earn
                                data[self.id+1]['account'][len(data[self.id+1]['account'])-1]['activity']="play Tetris"
                            if i==1:
                                coin_earn=pong.pong_game()
                                data[0]['user'][self.id]['coin']+=coin_earn
                                data[self.id+1]['account'][len(data[self.id+1]['account'])-1]['activity']="play Pong"
                            if i==2 :
                                coin_earn=bonkcheems.run()*10   
                                data[0]['user'][self.id]['coin']+=coin_earn
                                data[self.id+1]['account'][len(data[self.id+1]['account'])-1]['activity']="play Bonk cheems"  
                            if i==3:
                                coin_earn=snake.run()*10
                                data[0]['user'][self.id]['coin']+=coin_earn
                                data[self.id+1]['account'][len(data[self.id+1]['account'])-1]['activity']="play Snake"
                            sound_main=pygame.mixer.music.load('img\sounds\Soundtrack.mp3')
                            pygame.mixer.music.play(-1)
                            coin=data[0]['user'][self.id]['coin']
                            coin_bg=font_coin.render(f'{int(coin)}',True,(31,5,73))
                            date=time.localtime(time.time()).tm_mday
                            month=time.localtime(time.time()).tm_mon
                            year=time.localtime(time.time()).tm_year
                            data[self.id+1]['account'][len(data[self.id+1]['account'])-1]['date']=str(date)+"/"+str(month)+"/"+str(year)
                            data[self.id+1]['account'][len(data[self.id+1]['account'])-1]['status']=coin_earn
                            data[self.id+1]['account'][len(data[self.id+1]['account'])-1]['total']=data[0]['user'][self.id]['coin']
                            with open('data_player/data.json','w') as file_name:
                                json.dump(data,file_name,indent=4)  
                            icon_game[i]=pygame.transform.scale(icon_game[i],(200,200))    
                if event.type==pygame.KEYDOWN and event.key==pygame.K_BACKSPACE:
                        running=False
            for i in range(4):
                if pygame.Rect((232*i+29,127),(220,220)).collidepoint(pygame.mouse.get_pos()):   
                    icon_game[i]=pygame.transform.scale(icon_game[i],(210,210)) 
                else:
                    icon_game[i]=icon_game_re[i]
                
            BG_x-=0.5
            if BG_x==-975:
                BG_x=0
            screen.blit(BG,(BG_x,0))
            screen.blit(BG,(BG_x+975,0))
            screen.blit(COIN,(135,54))
            screen.blit(AVA,(31,21))
            screen.blit(name,(136,21))
            screen.blit(coin_bg,(174,61))
            for i in range(4):
                screen.blit(RECT,(232*i+29,127))
                name_game_blit=font_v(SourceCodePro_Black,30).render(f'{name_game[i]}',True,BLUE_V2)
                screen.blit(name_game_blit,name_game_blit.get_rect(center=(232*i+29+110,370)))
                screen.blit(icon_game[i],icon_game[i].get_rect(center=(232*i+29+110,127+110)))            
            screen.blit(font_v(SourceCodePro_Black,50).render(f'X',True,YELLOW),(900,15))
            pygame.display.update()
            if not running:
                return BG_x # to background can continue run
    def setting_match(self):
        with open('data_player/data.json') as file_name:
            data=json.load(file_name)
        LEFT=pygame.image.load(join("img","main",f"left{self.version}.png"))
        RIGHT=pygame.image.load(join("img","main",f"right{self.version}.png"))
        TYPE=[
            [pygame.image.load(r"img\main\moutain.png") ,"mountain view"],
            [pygame.transform.scale(pygame.image.load(r"img\main\2_M.png"),(358,146)),"desert view"],
            [pygame.transform.scale(pygame.image.load(r"img\main\1_S.png"),(358,146)),"space view"]
        ]
        select=0
        font=pygame.font.Font(join("img","font",f"{font_setting[self.version]}"),30)
        COIN=pygame.image.load(r"img\main\coin1.png")  
        CHOOSE=pygame.image.load(join("img","main",f"choose{self.version}.png"))  
        BG=pygame.image.load(join("img","main",f"bg_setting{self.version}.png"))
        INPUT=pygame.image.load(join("img","main",f"input-pass{self.version}.png"))  
        NEXT=pygame.image.load(join("img","main",f"next{self.version}.png"))
        SUN=pygame.image.load(join("img","load_sign_in",f"sun.png")) 
        CLOUD=pygame.image.load(join("img","load_sign_in",f"cloud.png")) 
        OK=pygame.image.load(r"img\main\ok.png")
        running=True
        BG_x=0
        #defaul value of choose length of race
        choose_y=210
        color_short=WHITE
        color_mid=color_setting[self.version]
        color_long=WHITE
        type_race="mid"
        color_ok=WHITE
        color_ok=WHITE
        active_left=False
        active_right=False
        font_exit=50
        active_ver=False
        active_speed=False
        color=WHITE
        self.speed="100"
        # print(self.id)
        coin=data[0]['user'][self.id]['coin']
        while running:
            CLOCK.tick(60)
            if active_ver:
                active_ver=False
                font=pygame.font.Font(join("img","font",f"{font_setting[self.version]}"),30)
                LEFT=pygame.image.load(join("img","main",f"left{self.version}.png"))
                RIGHT=pygame.image.load(join("img","main",f"right{self.version}.png"))
                CHOOSE=pygame.image.load(join("img","main",f"choose{self.version}.png"))  
                BG=pygame.image.load(join("img","main",f"bg_setting{self.version}.png"))
                INPUT=pygame.image.load(join("img","main",f"input-pass{self.version}.png"))  
                NEXT=pygame.image.load(join("img","main",f"next{self.version}.png"))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running =False
                    return 1
                if event.type==pygame.KEYDOWN and event.key==pygame.K_TAB:
                    if self.version=="v1":
                            self.version="v2"
                            active_ver=True
                    else : 
                        self.version="v1"
                        active_ver=True
                #exit hover 
                if pygame.Rect((900,15),(50,50)).collidepoint(pygame.mouse.get_pos()):
                    font_exit=40
                else:
                    font_exit=50
                # hover OK 
                if pygame.Rect((0,0),(WIDTH,HEIGHT)).collidepoint(pygame.mouse.get_pos()):
                    active_left=False
                    active_right=False
                if pygame.Rect((836,331),(80,80)).collidepoint(pygame.mouse.get_pos()):
                        color_ok=YELLOW
                if not pygame.Rect((836,331),(80,80)).collidepoint(pygame.mouse.get_pos()):
                        color_ok=WHITE
                if (event.type==pygame.MOUSEBUTTONDOWN and event.button==1) :
                    click_sound.play()
                    if pygame.Rect((423,337),(420,67)).collidepoint(event.pos):
                        active_speed=True
                        color=BLUE
                    else :
                        active_speed=False
                        if self.speed!='' and  int(self.speed)!=0:
                            if int(self.speed)<0 or int(self.speed)>1000 :
                                color=RED
                            else:
                                color=WHITE
                        else :
                            color=RED

                    #NEXT
                    if pygame.Rect((338,411),(300,111)).collidepoint(event.pos):
                        if color==WHITE:
                            setting=main.setting_set(BG_x)
                            active_ver=True
                            if setting==1:
                                return 1 # exit game 
                            BG_x=setting[1]
                            if setting[0]!=3: 
                                BG_x=main.star(BG_x)
                                if BG_x==1000:
                                    return 1
                                return TYPE[select],setting[0],setting[2],setting[3],setting[4],type_race,setting[5]
                                                                # coin dat cuoc #stt_set #che do dua #choose_t
                    #choose size of race lenght
                    if pygame.Rect((220,150),(100,40)).collidepoint(event.pos):
                        choose_y=160
                        color_short=color_setting[self.version]
                        color_mid=WHITE
                        color_long=WHITE
                        type_race="short"
                    if pygame.Rect((220,200),(100,40)).collidepoint(event.pos):
                        choose_y=210
                        color_short=WHITE
                        color_mid=color_setting[self.version]
                        color_long=WHITE
                        type_race="mid"
                    if pygame.Rect((220,250),(100,40)).collidepoint(event.pos):
                        choose_y=260
                        color_short=WHITE
                        color_mid=WHITE
                        color_long=color_setting[self.version]
                        type_race="long"
                    #CHOOSE ROUND   
                    if  pygame.Rect((434,164),(60,115)).collidepoint(event.pos):
                        active_left=True
                        if select==0:
                            select=2
                        else:
                            select-=1
                    if  pygame.Rect((886,164),(60,115)).collidepoint(event.pos):
                        active_right=True
                        if select==2:
                            select=0
                        else:
                            select+=1
                    #exit 
                    if pygame.Rect((900,15),(50,50)).collidepoint(event.pos):
                        running=False
                        font_exit=40
                        return 0
                if event.type==pygame.KEYDOWN:
                    if active_speed:
                        if event.key == pygame.K_RETURN:
                                print(self.speed)
                                # text = ''
                        elif event.key == pygame.K_BACKSPACE:
                                self.speed = self.speed[:-1]
                        else:
                            for i in range(48,58):
                                if int(event.key)==i:
                                    self.speed += event.unicode
                        if self.speed!='' and  int(self.speed)!=0:
                            if int(self.speed)<0 or int(self.speed)>1000 :
                                color=RED
                            else:
                                color=BLUE
                        else :
                            color=RED
            BG_x-=0.5
            if BG_x==-975:
                BG_x=0
            
            screen.blit(BG,(BG_x,0))
            screen.blit(BG,(BG_x+975,0))
            if self.version=="v2":
                screen.blit(SUN,(0,0))
                screen.blit(CLOUD,(BG_x,0))
                screen.blit(CLOUD,(BG_x+975,0))
            screen.blit(COIN,(238,369))
            screen.blit(font.render(f'RACE TRACK SETUP',True,color_setting[self.version]),(350,8))
            screen.blit(font.render(f'Theme: ',True,WHITE),(474,71))
            screen.blit(font.render(f'Race track length:',True,color_setting[self.version]),(10,90))
            screen.blit(font.render(f'Short',True,color_short),(220,150))
            screen.blit(font.render(f'Medium',True,color_mid),(220,200))
            screen.blit(font.render(f'Long',True,color_long),(220,250))
            screen.blit(font.render(f'initial speed:',True,color_setting[self.version]),(113,328))
            screen.blit(font.render(f'{coin}',True,WHITE),(248+20,369+5))
            screen.blit(font.render(f'{TYPE[select][1]}',True,color_setting[self.version]),(650,71))
            screen.blit(font_v(SourceCodePro_Black,font_exit).render(f'X',True,color_setting[self.version]),(900,15))
            screen.blit(INPUT  ,(393,337))
            text_speed=font_v(SourceCodePro_Black,30).render(f'{self.speed}%',True,color)
            screen.blit(text_speed,text_speed.get_rect(center=(393+210,337+30)))
            screen.blit(OK,(836,331))
            screen.blit(font_v(SourceCodePro_Black,30).render(f'OK',True,color_ok),(858,352))
            if active_left:
                screen.blit(pygame.transform.scale(LEFT,(20,37)),(434+60*0.2,164+115*0.2-10))
            else :
                screen.blit(LEFT,(434,164))
            if active_right:
                screen.blit(pygame.transform.scale(RIGHT,(20,37)),(886+60*0.4/2,164+115*0.4/2-10))
            else:   
                screen.blit(RIGHT,(886,164))
            screen.blit(TYPE[select][0],(501,129))
            screen.blit(CHOOSE ,(170,choose_y))
            screen.blit(NEXT,(338,411))
            pygame.display.update()
    #setting_match(3)
    #========================================================================================
    #choose set and custom character 
    def option_set(self):
        BG=pygame.image.load(join("img","load_sign_in",f"bg_setting{self.version}.png"))     
        RECT_OPTION=pygame.image.load(join("img","set_nhan_vat",f"rect_option_set{self.version}.png"))     
        RECT_OPTION_CHOOSE=pygame.image.load(r"img\set_nhan_vat\rect_option_set_choose.png") 
        EXIT=pygame.image.load(join("img","load_sign_in",f"X{self.version}.png"))    
        SUN=pygame.image.load(join("img","load_sign_in",f"sun.png")) 
        CLOUD=pygame.image.load(join("img","load_sign_in",f"cloud.png"))    
        NEXT=pygame.image.load(join("img","main",f"next{self.version}.png"))
        running=True
        y_scroll=0
        choose_t=[]
        active_ver=True
        BG_x=0
        while running:
            CLOCK.tick(60)
            choose=False
            x_choose=122
            y_choose=81
            if active_ver:
                active_ver=False
                NEXT=pygame.image.load(join("img","main",f"next{self.version}.png"))
                EXIT=pygame.font.Font(join("img","font",f"{font_setting[self.version]}"),50).render(f'X',True,color_setting[self.version])
                BG=pygame.image.load(join("img","load_sign_in",f"bg_setting{self.version}.png"))  
                RECT_OPTION=pygame.image.load(join("img","set_nhan_vat",f"rect_option_set{self.version}.png"))
                text=pygame.font.Font(join("img","font",f"{font_setting[self.version]}"),50).render(f'CUSTOME RACER',True,color_setting[self.version])
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_TAB:
                        if self.version=="v1":
                            self.version="v2"
                        else :
                            self.version="v1"
                        active_ver=True
                    if event.key==pygame.K_RETURN:
                        if len(choose_t)==5:
                            return choose_t
                if event.type==pygame.MOUSEBUTTONDOWN :
                    if NEXT.get_rect(center=(WIDTH/2,81+144*6+y_scroll+45)).collidepoint(event.pos) and event.button==1:
                        click_sound.play()
                        if len(choose_t)==5:
                            return choose_t
                    if pygame.Rect((975-100,50),(29,60)).collidepoint(event.pos)  and event.button==1:
                            click_sound.play()
                            running=False
                            return 0
                    if event.button==4:
                        if y_scroll<0:
                            y_scroll+=30
                    if event.button==5:
                        if y_scroll>-490:
                            y_scroll-=30
                    if event.button==1:
                        click_sound.play()
                        for j in range(0,6):
                            for i in range(0,5):
                                if pygame.Rect((x_choose,y_choose+y_scroll),(120,120)).collidepoint(event.pos):
                                    # print([j,i])
                                    # print([j,i] in np.array(choose_t))
                                    cout=0
                                    for check in choose_t:
                                        if check==[j,i]:
                                            cout+=1
                                    if cout!=0:
                                        choose_t.remove([j,i])
                                    elif len(choose_t)<5:
                                        choose_t.append([j,i])
                                    # print(choose_t)
                                    
                                x_choose+=153
                            x_choose=122
                            y_choose+=144
            BG_x-=0.5
            if BG_x==-975:
                BG_x=0
            screen.blit(BG,(BG_x,0))
            screen.blit(BG,(BG_x+975,0))
            if self.version=="v2":
                screen.blit(SUN,(0,0))
                screen.blit(CLOUD,(BG_x,0))
                screen.blit(CLOUD,(BG_x+975,0))
            for j in range(6):
                for i in range(5):
                    screen.blit(RECT_OPTION,(122+153*i,81+144*j+y_scroll))      
            for x,y in choose_t :
                screen.blit(RECT_OPTION_CHOOSE,(122+153*y,81+144*x+y_scroll))
            for j in range(6):
                for i in range(5):
                    screen.blit(set[j][i][0],(122+153*i+15,81+144*j+y_scroll+15))
            screen.blit(NEXT,NEXT.get_rect(center=(WIDTH/2,81+144*6+y_scroll+45)))
            screen.blit(text,text.get_rect(center=(WIDTH/2,30+y_scroll)))
            screen.blit(EXIT,(975-100,50))
            pygame.display.update()
    # choose_t=option_set()
    # short.main(pygame.display.set_mode((975,550)),choose_t)
    def setting_set(self,BG_x):
        data=[]
        with open('data_player/data.json') as file_name:
            data=json.load(file_name)
        user_name=data[0]['user'][self.id]['user_name']
        coin=data[0]['user'][self.id]['coin']
        stt_set=1
        YELLOW= (246, 142, 2)
        BG=pygame.image.load(join("img","main",f"bg_setting{self.version}.png"))
        RECT_CHOOSE=pygame.image.load(r"img\set_nhan_vat\set_choose.png")  
        SUN=pygame.image.load(join("img","load_sign_in",f"sun.png")) 
        CLOUD=pygame.image.load(join("img","load_sign_in",f"cloud.png")) 
        # RECT_CHOOSE_CLICK= pygame.image.load(r"img\set_nhan_vat\rect_option_set_choose.png")  
        RECT=pygame.image.load(join("img","set_nhan_vat",f"set{self.version}.png"))
        INPUT=pygame.image.load(join("img","main",f"input-pass{self.version}.png"))
        COIN=pygame.image.load(r"img\main\coin1.png")  
        CHOOSE=pygame.image.load(join("img","main",f"choose{self.version}.png"))
        NEXT=pygame.image.load(join("img","main",f"next{self.version}.png"))
        running=True
        choose_y=145
        rect_set=[RECT,RECT,RECT,RECT,RECT]
        #color of rename
        choose=2
        text=str(int(coin//2))
        TEXT=font_v(SourceCodePro_Black,30).render(f'{text}',True,WHITE)
        color=WHITE
        active=False
        color_rename=[color_setting[self.version],BLUE,color_setting[self.version],color_setting[self.version],color_setting[self.version],color_setting[self.version]]
        name=[]
        for i in range (0,5):
            name.append(set[stt_set][i][1])
        active_enter=[False,False,False,False,False]
        font_exit=50
        active_ver=False
        font_30=pygame.font.Font(join("img","font",f"{font_setting[self.version]}"),30)
        font_20=pygame.font.Font(join("img","font",f"{font_setting[self.version]}"),20)
        font_40=pygame.font.Font(join("img","font",f"{font_setting[self.version]}"),40)
        choose_t=0
        text_set=[
            font_30.render(f'Fishs',True,color_rename[0]),
            font_30.render(f'Dinosaurs',True,color_rename[1]),
            font_30.render(f'Birds',True,color_rename[2]),
            font_30.render(f'Spacecrafts',True,color_rename[3]),
            font_30.render(f'Group 5',True,color_rename[4]),
            font_30.render(f'people',True,color_rename[5])
        ]
        while running:
            CLOCK.tick(60)
            if active_ver:
                NEXT=pygame.image.load(join("img","main",f"next{self.version}.png"))
                CHOOSE=pygame.image.load(join("img","main",f"choose{self.version}.png"))
                INPUT=pygame.image.load(join("img","main",f"input-pass{self.version}.png"))
                BG=pygame.image.load(join("img","main",f"bg_setting{self.version}.png"))
                font_30=pygame.font.Font(join("img","font",f"{font_setting[self.version]}"),30)
                font_20=pygame.font.Font(join("img","font",f"{font_setting[self.version]}"),20)
                font_40=pygame.font.Font(join("img","font",f"{font_setting[self.version]}"),40)
                color_rename=[color_setting[self.version],BLUE,color_setting[self.version],color_setting[self.version],color_setting[self.version],color_setting[self.version]]
                RECT=pygame.image.load(join("img","set_nhan_vat",f"set{self.version}.png"))
                rect_set=[RECT,RECT,RECT,RECT,RECT]
                active_ver=False
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                    return 1 # exit game 
                if event.type==pygame.KEYDOWN and event.key==pygame.K_TAB:
                    if self.version=="v1":
                            self.version="v2"
                            active_ver=True
                    else : 
                        self.version="v1"
                        active_ver=True
                if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                    click_sound.play()
                    #tùy chọn nhân vật đua 
                    if pygame.Rect((490,100),(280,30)).collidepoint(event.pos):
                        choose_t=main.option_set()
                        if choose_t!=0:
                            color_rename=[color_setting[self.version],color_setting[self.version],color_setting[self.version],color_setting[self.version],color_setting[self.version],color_setting[self.version]]
                            SET_NV=[]
                            for i in range(0,5):
                                SET_NV.append(set[choose_t[i][0]][choose_t[i][1]])
                    dem=0 
                    for i in range(0,5):
                        if pygame.Rect((371+108*i,179),(100,100)).collidepoint(pygame.mouse.get_pos()):
                            choose=i+1
                            for i in range(0,5):
                                active_enter[i]=False
                            active_enter[choose-1]=True
                            # print(choose)
                        else:
                            dem+=1
                    if dem==5:
                        for i in range(0,5):
                                active_enter[i]=False
                #choose and rename character 
                # hover effect  
                for k in range(0,5):            
                    if pygame.Rect((371+108*k,179),(100,100)).collidepoint(pygame.mouse.get_pos()):
                        for i in range(0,5):
                            rect_set[i]=RECT
                        rect_set[k]=RECT_CHOOSE
                if not(pygame.Rect((371,179),(100,100)).collidepoint(pygame.mouse.get_pos()) or pygame.Rect((479,179),(100,100)).collidepoint(pygame.mouse.get_pos()) or pygame.Rect((587,179),(100,100)).collidepoint(pygame.mouse.get_pos()) or pygame.Rect((695,179),(100,100)).collidepoint(pygame.mouse.get_pos()) or pygame.Rect((803,179),(100,100)).collidepoint(pygame.mouse.get_pos())):
                    for i in range(0,5):
                        rect_set[i]=RECT
                # exit _hover 
                if pygame.Rect((900,15),(50,50)).collidepoint(pygame.mouse.get_pos()):
                    font_exit=40
                else :
                    font_exit=50
                if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                    click_sound.play()
                    #choose set character
                    for k in range(0,6):
                        if text_set[k].get_rect(topleft=(80,100+40*k)).collidepoint(event.pos):
                            for i in range(0,6):
                                color_rename[i]=color_setting[self.version]
                            color_rename[k]=BLUE
                            choose_y=105+40*k
                            stt_set=k
                            choose_t=0
                    text_set=[
                        font_30.render(f'Fishs',True,color_rename[0]),
                        font_30.render(f'Dinosaurs',True,color_rename[1]),
                        font_30.render(f'Birds',True,color_rename[2]),
                        font_30.render(f'Spacecrafts',True,color_rename[3]),
                        font_30.render(f'Group 5',True,color_rename[4]),
                        font_30.render(f'people',True,color_rename[5])
                    ]    
                    #NEXT
                    if pygame.Rect((338,411),(300,111)).collidepoint(event.pos): 
                        if color==WHITE and int(text)!=0:
                            if choose_t==0:
                                return set[stt_set],BG_x,choose,int(text),stt_set,choose_t
                            else:
                                return SET_NV,BG_x,choose,int(text),stt_set,choose_t
                    # exit
                    if pygame.Rect((900,15),(50,50)).collidepoint(event.pos):
                        running=False
                    if pygame.Rect((260,349),(420,67)).collidepoint(event.pos):
                        active=True
                        color=BLUE   
                    else :
                        active=False
                        if text!='' and  int(text)!=0:
                            if int(text)>coin :
                                color=RED
                            else:
                                color=WHITE
                        else :
                            color=RED
                # input coin bet 
                if event.type==pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                                print(text)
                                
                                # text = ''
                        elif event.key == pygame.K_BACKSPACE:
                                text = text[:-1]
                                
                        else:
                            for i in range(48,58):
                                if int(event.key)==i and len(text)<=20:
                                    text += event.unicode
                        if text!='' and  int(text)!=0:
                            if int(text)>coin :
                                color=RED
                            else:
                                color=BLUE
                        else :
                            color=RED
                    #rename character
                    if choose_t==0:
                            if active_enter[choose-1]:
                                        if event.key == pygame.K_RETURN:
                                                        # print(set[stt_set][choose-1][1])
                                                        active_enter[choose-1]=False
                                        elif event.key == pygame.K_BACKSPACE:
                                                        set[stt_set][choose-1][1] = set[stt_set][choose-1][1][:-1]
                                        elif len(set[stt_set][choose-1][1])<9:
                                                        set[stt_set][choose-1][1] += event.unicode
                    else:
                            if active_enter[choose-1]:
                                        # print(choose_t[choose-1][1])
                                        if event.key == pygame.K_RETURN:
                                                        # print(set[choose_t[choose-1][0]][choose_t[choose-1][1]][1])
                                                        active_enter[choose-1]=False
                                        elif event.key == pygame.K_BACKSPACE:
                                                        set[choose_t[choose-1][0]][choose_t[choose-1][1]][1] = set[choose_t[choose-1][0]][choose_t[choose-1][1]][1][:-1]
                                        elif len(set[choose_t[choose-1][0]][choose_t[choose-1][1]][1])<9:
                                                        set[choose_t[choose-1][0]][choose_t[choose-1][1]][1] += event.unicode
        
            BG_x-=0.5
            if BG_x==-975:
                BG_x=0
            screen.blit(BG,(BG_x,0))
            screen.blit(BG,(BG_x+975,0))
            if self.version=="v2":
                screen.blit(SUN,(0,0))
                screen.blit(CLOUD,(BG_x,0))
                screen.blit(CLOUD,(BG_x+975,0))
            screen.blit(COIN,(366,312))
            screen.blit(COIN,(578,312))
            screen.blit(INPUT,(260,349))
            screen.blit(font_30.render(f'bet',True,color_setting[self.version]),(465,310-15))
            screen.blit(font_40.render(f'SELECT RACERS',True,color_setting[self.version]),(347,13))
            if choose_t==0:
                for i in range(5):
                    text_name=font_20.render(f'{set[stt_set][i][1]}',True,color_setting[self.version])
                    screen.blit(text_name,text_name.get_rect(midtop=(376+50+108*i,145-10)))
                text_name=font_20.render(f'{set[stt_set][choose-1][1]}',True,BLUE)
                screen.blit(text_name,text_name.get_rect(midtop=(376+50+108*(choose-1),145-10)))
                screen.blit(CHOOSE,(30,choose_y))
            else:
                for i in range(5):
                    text_name=font_20.render(f'{set[choose_t[i][0]][choose_t[i][1]][1]}',True,color_setting[self.version])
                    screen.blit(text_name,text_name.get_rect(midtop=(376+50+108*i,145-10)))
                text_name=font_20.render(f'{set[choose_t[choose-1][0]][choose_t[choose-1][1]][1]}',True,BLUE)
                screen.blit(text_name,text_name.get_rect(midtop=(376+50+108*(choose-1),145-10)))
            for i in range(6):
                screen.blit(text_set[i],(80,100+40*i)) # text_set 
            screen.blit(font_30.render(f'Character Sets:',True,color_setting[self.version]),(10,60))
            screen.blit(font_40.render(f'Custom racer',True,color_setting[self.version]),(490,100-20))
            screen.blit(font_v(SourceCodePro_Black,font_exit).render(f'X',True,YELLOW),(900,15))
            for i in range(0,5):
                if not active_enter[i]:
                    screen.blit(rect_set[i],(371+108*i,179))
                    if choose_t==0:
                        screen.blit(set[stt_set][i][0],(376+108*i,184))
                    else:
                        screen.blit(SET_NV[i][0],(376+108*i,184))
                else :
                    screen.blit(rect_set[i],(371+108*i,170))
                    if choose_t==0:
                        screen.blit(set[stt_set][i][0],(376+108*i,184-9))
                    else :
                        screen.blit(SET_NV[i][0],(376+108*i,184-9))
            screen.blit(NEXT,(338,411))
            TEXT=font_v(SourceCodePro_Black,30).render(f'{text}',True,color)
            screen.blit(TEXT,TEXT.get_rect(center=(260+210,394-15)))
            pygame.display.update() # 260,394 + (420,67)
            if not running:
                return 3,BG_x
    # setting_set(4,2)
    def star(self,BG_x):
        BG=pygame.image.load(join("img","load_sign_in",f"bg_setting{self.version}.png"))
        NEXT=pygame.image.load(join("img","main",f"start{self.version}.png"))
        LOGO=pygame.transform.scale(pygame.image.load(join("img","load_sign_in",f"logo_nobg{self.version}.png")),(WIDTH,HEIGHT))
        SUN=pygame.image.load(join("img","load_sign_in",f"sun.png")) 
        CLOUD=pygame.image.load(join("img","load_sign_in",f"cloud.png")) 
        running=True
        active_ver=False
        
        while running:
            CLOCK.tick(60)
            if active_ver:
                active_ver=False
                BG=pygame.image.load(join("img","load_sign_in",f"bg_setting{self.version}.png"))
                NEXT=pygame.image.load(join("img","main",f"start{self.version}.png"))
                LOGO=pygame.transform.scale(pygame.image.load(join("img","load_sign_in",f"logo_nobg{self.version}.png")),(WIDTH,HEIGHT))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running==False
                    return 1000
                if event.type==pygame.KEYDOWN and event.key==pygame.K_TAB:
                    if self.version=="v1":
                        self.version="v2"
                        active_ver=True
                    else :
                        self.version="v1"
                        active_ver=True
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect((338,411),(300,111)).collidepoint(event.pos): 
                        return BG_x
            BG_x-=0.5
            if BG_x==-975:
                BG_x=0
            screen.blit(BG,(BG_x,0))    
            screen.blit(BG,(BG_x+975,0))
            if self.version=="v2":
                screen.blit(SUN,(0,0))
                screen.blit(CLOUD,(BG_x,0))
                screen.blit(CLOUD,(BG_x+975,0))
            screen.blit(LOGO,(0,0))  
            screen.blit(NEXT,(338,411))
            pygame.display.update()

    def rank(self,set,time,rank,choose,coin_earn):
        data=[]
        with open('data_player/data.json') as file_name:
            data=json.load(file_name)
        user_name=data[0]['user'][self.id]['user_name']
        coin=data[0]['user'][self.id]['coin']
        running=True
        BG=pygame.image.load(r"img\rank\bg_winv1.png") 
        STAR1=pygame.image.load(r"img\rank\star1.png") 
        STAR2=pygame.image.load(r"img\rank\star2.png")
        LEADERBOARD=pygame.image.load(r"img\rank\LEADERBOARDv1.png")
        YOUWON=pygame.image.load(r"img\rank\YOUWONN!v1.png")
        YOULOST=pygame.image.load(r"img\rank\YOULOST!v1.png")
        RANK=[
            pygame.image.load(r"img\rank\#1.png") ,
            pygame.image.load(r"img\rank\#2.png") ,
            pygame.image.load(r"img\rank\#3.png") ,
            pygame.image.load(r"img\rank\#4.png") ,
            pygame.image.load(r"img\rank\#5.png") 
        ]
        RECT_RANK=[
            pygame.image.load(r"img\rank\rect_#1.png") ,
            pygame.image.load(r"img\rank\rect_#2.png") ,
            pygame.image.load(r"img\rank\rect_#3.png") ,
            pygame.image.load(r"img\rank\rect_#4.png") ,
            pygame.image.load(r"img\rank\rect_#5.png") 
        ]
        AVA=pygame.image.load(r"img\main\ava.png") 
        COIN=pygame.image.load(r"img\main\coin1.png") 
        COIN_2=pygame.image.load(r"img\rank\coin_2.png") 
        won_y=445  
        chieu=1
        
        while running:
            CLOCK.tick(60)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        running=False
                if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                    click_sound.play()
                    running=False
            won_y+=0.3*chieu
            if won_y<435:
                chieu=1
            if won_y>455:
                chieu=-1 
            screen.blit(BG,(0,0))
            screen.blit(STAR1,(466,9))
            screen.blit(STAR2,(424,30))
            screen.blit(STAR2,(512,30))
            screen.blit(LEADERBOARD,(357,76))
            screen.blit(AVA,(14,460))
            screen.blit(COIN,(119,500))
            screen.blit(COIN_2,(775,414))
            if coin_earn>=0:
                screen.blit(font_v(SourceCodePro_Black,60).render(f'+{coin_earn}',True,(252, 205, 0,)),(825,392))
            else:
                screen.blit(font_v(SourceCodePro_Black,60).render(f'{coin_earn}',True,(252, 205, 0,)),(825,392))
            screen.blit(font_v(SourceCodePro_Black,30).render(f'@{user_name}',True,(252, 205, 0,)),(119,460))
            screen.blit(font_v(SourceCodePro_Black,30).render(f'{coin}',True,(252, 205, 0,)),(157,500))
            screen.blit(RANK[0],(474,121))
            screen.blit(RANK[1],(292,138))
            screen.blit(RANK[2],(654,150))
            screen.blit(RANK[3],(130,161))
            screen.blit(RANK[4],(816,173))
            screen.blit(RECT_RANK[0],(423,171))
            screen.blit(RECT_RANK[1],(246,181))
            screen.blit(RECT_RANK[2],(610,191))
            screen.blit(RECT_RANK[3],(89,201))
            screen.blit(RECT_RANK[4],(777,211))
            screen.blit(font_v(SourceCodePro_Black,20).render(f'{set[rank[0]-1][1]}',True,YELLOW),(470,344))
            screen.blit(font_v(SourceCodePro_Black,20).render(f'{set[rank[1]-1][1]}',True,YELLOW),(285,344))
            screen.blit(font_v(SourceCodePro_Black,20).render(f'{set[rank[2]-1][1]}',True,YELLOW),(647,344))
            screen.blit(font_v(SourceCodePro_Black,20).render(f'{set[rank[3]-1][1]}',True,YELLOW),(120,344))
            screen.blit(font_v(SourceCodePro_Black,20).render(f'{set[rank[4]-1][1]}',True,YELLOW),(800,344))
            screen.blit(set[rank[0]-1][0],(423+30,171+30))
            screen.blit(set[rank[1]-1][0],(246+25,181+25))
            screen.blit(set[rank[2]-1][0],(610+20,191+20))
            screen.blit(set[rank[3]-1][0],(89+17,201+17))
            screen.blit(set[rank[4]-1][0],(777+10,211+10))
            if rank[0]==choose :
                screen.blit(YOUWON,(420,won_y))
            else :
                screen.blit(YOULOST,(420,won_y))
            #time=========================================
            screen.blit(pygame.font.Font(r'img\font\SourceCodePro-BlackItalic.ttf',20).render(f'00:{round(time[rank[0]-1],2)}',True,YELLOW),(449,375))
            screen.blit(pygame.font.Font(r'img\font\SourceCodePro-BlackItalic.ttf',20).render(f'00:{round(time[rank[1]-1],2)}',True,YELLOW),(265,375))
            screen.blit(pygame.font.Font(r'img\font\SourceCodePro-BlackItalic.ttf',20).render(f'00:{round(time[rank[2]-1],2)}',True,YELLOW),(627,375))
            screen.blit(pygame.font.Font(r'img\font\SourceCodePro-BlackItalic.ttf',20).render(f'00:{round(time[rank[3]-1],2)}',True,YELLOW),(112,375))
            screen.blit(pygame.font.Font(r'img\font\SourceCodePro-BlackItalic.ttf',20).render(f'00:{round(time[rank[4]-1],2)}',True,YELLOW),(784,375))
            #=============================================
            screen.blit(font_v(SourceCodePro_Black,25).render(f'emotion:',True,WHITE),(785,460))
            screen.blit(font_v(SourceCodePro_Black,35).render(f'{self.emotion}',True,BLUE),(760,490))
            pygame.display.update()
    #rank(set[4],"tu",100)
    # rank(set[1],2,[1,2,3,4,5],[1,2,3,4,5],3,100)


    def result_rank(self,set_nv,time,rank,choose,coin_earn):
        data=[]

        with open('data_player/data.json') as file_name:
            data=json.load(file_name)
            user_name=data[0]['user'][self.id]['user_name']
            coin=data[0]['user'][self.id]['coin']
        running=True
        BG=pygame.image.load(join("img","rank",f"bg_win{self.version}.png")) 
        RECT_M=pygame.image.load(join("img","rank",f"Rectangle_19{self.version}.png")) 
        STAR1=pygame.image.load(r"img\rank\star1.png") 
        STAR2=pygame.image.load(r"img\rank\star2.png")
        LEADERBOARD=pygame.image.load(join("img","rank",f"LEADERBOARD{self.version}.png")) 
        YOUWON=pygame.image.load(join("img","rank",f"YOUWONN!{self.version}.png")) 
        YOULOST=pygame.image.load(join("img","rank",f"YOULOST!{self.version}.png")) 
        RECT_60x60=pygame.image.load(r"img\rank\rect_60x60.png")
        AVA=pygame.image.load(r"img\main\ava.png") 
        COIN=pygame.image.load(r"img\main\coin1.png") 
        COIN_2=pygame.image.load(r"img\rank\coin_2.png")  
        RANK=[
            pygame.image.load(r"img\rank\#1.png") ,
            pygame.image.load(r"img\rank\#2.png") ,
            pygame.image.load(r"img\rank\#3.png") ,
            pygame.image.load(r"img\rank\#4.png") ,
            pygame.image.load(r"img\rank\#5.png") 
        ]
        font_25=pygame.font.Font(join("img","font",f"{font_setting[self.version]}"),25)
        font_20=pygame.font.Font(join("img","font",f"{font_setting[self.version]}"),20)
        font_55=pygame.font.Font(join("img","font",f"{font_setting[self.version]}"),55)
        font_35=pygame.font.Font(join("img","font",f"{font_setting[self.version]}"),35)
        active_ver=False
        while running:
            CLOCK.tick(60)
            if active_ver:
                active_ver=False
                font_20=pygame.font.Font(join("img","font",f"{font_setting[self.version]}"),20)
                font_55=pygame.font.Font(join("img","font",f"{font_setting[self.version]}"),55)
                font_25=pygame.font.Font(join("img","font",f"{font_setting[self.version]}"),25)
                font_35=pygame.font.Font(join("img","font",f"{font_setting[self.version]}"),35)
                BG=pygame.image.load(join("img","rank",f"bg_win{self.version}.png")) 
                RECT_M=pygame.image.load(join("img","rank",f"Rectangle_19{self.version}.png")) 
                LEADERBOARD=pygame.image.load(join("img","rank",f"LEADERBOARD{self.version}.png")) 
                YOUWON=pygame.image.load(join("img","rank",f"YOUWONN!{self.version}.png")) 
                YOULOST=pygame.image.load(join("img","rank",f"YOULOST!{self.version}.png")) 
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                if event.type==pygame.KEYDOWN and event.key==pygame.K_TAB:
                    if self.version=="v1":
                        self.version="v2"
                        active_ver=True
                    else :
                        self.version="v1"
                        active_ver=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE :
                        running=False
                if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                    click_sound.play()
                    running=False
                if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                    click_sound.play()
                    if pygame.Rect((900,15),(50,50)).collidepoint(event.pos):
                        running=False
            screen.blit(BG ,(0,0))
            screen.blit(RECT_M ,(360,88))
            screen.blit(STAR1,(622,0))
            screen.blit(STAR2,(580,21))
            screen.blit(STAR2,(668,21))
            screen.blit(LEADERBOARD,(512,68))
            if rank[0]==choose :
                screen.blit(YOUWON ,(90,214))
            else :
                screen.blit(YOULOST ,(90,214))
            screen.blit(font_25.render(f'position:',True,WHITE),(393,148-20))
            screen.blit(font_25.render(f'racer',True,WHITE),(584,148-20))
            screen.blit(font_25.render(f'time',True,WHITE),(823,148-20))
            for i in range(0,5):
                screen.blit(RECT_60x60,(538,187+67*i))
                color=WHITE
                screen.blit(pygame.transform.scale(set_nv[rank[i]-1][0],(50,50)),(538+5,187+67*i+5))
                if rank[i]==choose:
                    color=color_setting[self.version]
                screen.blit(font_20.render(f'{set_nv[rank[i]-1][1]}',True,color),(630,204+67*i))
                screen.blit(font_20.render(f'00:{round(time[rank[i]-1],2)}',True,color),(799,204+67*i))
            screen.blit(RANK[0],(417,210))
            screen.blit(RANK[1],(420,280))
            screen.blit(RANK[2],(420,345))
            screen.blit(RANK[3],(423,415))
            screen.blit(RANK[4],(423,485))
            screen.blit(AVA,(14,460))
            screen.blit(COIN,(119,500))
            screen.blit(COIN_2,(88,268))
            screen.blit(font_v(SourceCodePro_Black,50).render(f'X',True,YELLOW),(900,15))
            if coin_earn>=0:
                screen.blit(font_55.render(f'+{coin_earn}',True,YELLOW),(138,252))
            else:
                screen.blit(font_55.render(f'{coin_earn}',True,YELLOW),(138,252))
            screen.blit(font_25.render(f'emotion:',True,WHITE),(95,332-20))
            if self.method_emotion==0:
                emotion_re=self.emotion
            elif self.method_emotion==1:
                emotion_re=data[self.id+1]['history'][self.emotion_history_id]['emotion']
            screen.blit(font_35.render(f'{emotion_re}',True,BLUE),(75,370))
            screen.blit(font_v(SourceCodePro_Black,30).render(f'@{user_name}',True,color_setting[self.version]),(119,460))
            screen.blit(font_v(SourceCodePro_Black,30).render(f'{coin}',True,color_setting[self.version]),(157,500))
            screen.blit(pygame.transform.scale(set_nv[choose-1][0],(123,123)),(101,78))
            pygame.display.update()
    # time=[12.3,11.4,13.6,11.1,19.6]
    # rank=[2,5,4,1,3]
    # result_rank(set[1],2,time,rank,3,50)
    # #infor_race(2)
    #setting_set(4,2)


    def history(self):
        data=[]
        with open('data_player/data.json') as file_name:
            data=json.load(file_name)
        username=data[0]['user'][self.id]['user_name']
        coin=data[0]['user'][self.id]['coin']
        AVA=pygame.image.load(r"img\main\ava.png") 
        COIN=pygame.image.load(r"img\main\coin1.png") 
        RECT_60x60=pygame.image.load(r"img\rank\rect_60x60.png")
        BG=pygame.image.load(join("img","rank",f"bg_win{self.version}.png"))     
        TABLE=pygame.image.load(join("img","rank",f"table_rect{self.version}.png"))     
        COIN_HIS=pygame.image.load(r"img\rank\coin_history.png")
        WIN=pygame.image.load(r"img\rank\WIN.png")
        LOSE=pygame.image.load(r"img\rank\LOSE.png")
        #____________layer3________________________
        delta_x=self.sound*448/100
        scroll=False
        SCROLL_LONG=pygame.image.load(join("img","history",f"scroll_long{self.version}.png"))  
        SCROLL_SCALE=pygame.image.load(join("img","history",f"scroll_scale{self.version}.png"))  
        EXIT_HIS=pygame.image.load(r"img\history\exit_his.png") 
        VER1=pygame.image.load(r"img\history\ver1_racingGame_racer 1.png") 
        VER2=pygame.image.load(r"img\history\ver2_racingGame_racer 1.png") 
        SOUND_ON=pygame.image.load(r"img\history\sound_on.png") 
        SOUND_OFF=pygame.image.load(r"img\history\sound_off.png") 
        COL_SCROLL=pygame.image.load(join("img","history",f"rect_scroll{self.version}.png"))     
        COL_SCROLL_SMALL=pygame.image.load(join("img","history",f"rect_scroll_small{self.version}.png"))     
        layer1=pygame.Surface((667,446-50-10))
        layer2=pygame.Surface((667,446-50-10))
        layer3=pygame.Surface((667,446-50-10))
        y_scroll=0
        running=True
        dem=0
        layer_choose=0
        color_choose=[BLUE,YELLOW,YELLOW]
        layer=[layer1,layer2,layer3]
        active_ver=False
        active_scroll=True
        while running:
            if active_ver:
                active_ver=False
                BG=pygame.image.load(join("img","rank",f"bg_win{self.version}.png"))     
                TABLE=pygame.image.load(join("img","rank",f"table_rect{self.version}.png"))     
                COL_SCROLL=pygame.image.load(join("img","history",f"rect_scroll{self.version}.png")) 
                SCROLL_LONG=pygame.image.load(join("img","history",f"scroll_long{self.version}.png"))  
                SCROLL_SCALE=pygame.image.load(join("img","history",f"scroll_scale{self.version}.png"))      
            CLOCK.tick(60)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                    return 1
                if event.type==pygame.KEYDOWN and event.key==pygame.K_TAB:
                    if self.version=="v1":
                        self.version="v2"
                        active_ver=True
                    else :
                        self.version="v1"
                        active_ver=True
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect((900,15),(50,50)).collidepoint(event.pos):
                            running=False
                            return 0
                    #set_choose_history : layer_choose 
                    
                    for i in range(3):
                            if pygame.Rect((25,200+50*i),(150,40)).collidepoint(event.pos) and event.button==1:
                                click_sound.play()
                                for j in range(3):
                                    color_choose[j]=YELLOW
                                    color_choose[i]=BLUE
                                    layer_choose=i
                                    y_scroll=0
                    if layer_choose<=1 :  
                            if event.button==5:
                                if (58+76*dem-50+y_scroll+52+50)>(52+50+446-60):
                                    y_scroll-=30
                            if event.button==4:
                                if y_scroll<0:
                                    y_scroll+=30
                    #__________________________________________layer_choose=2_____________________________________
                    else :
                        if pygame.Rect((440,70),(200,40)).collidepoint(event.pos):
                            main.create_rename(0)
                            with open('data_player/data.json') as file_name:
                                data=json.load(file_name)
                        elif pygame.Rect((440,102),(200,40)).collidepoint(event.pos):   
                            main.create_rename(1)
                            with open('data_player/data.json') as file_name:
                                data=json.load(file_name)
                        elif pygame.Rect((440,130),(200,40)).collidepoint(event.pos):
                            main.create_face_id()
                            with open('data_player/data.json') as file_name:
                                data=json.load(file_name)
                        if VER1.get_rect(bottomleft=(120+281,380+102)).collidepoint(event.pos):
                            self.version="v1"
                            active_ver=True
                        if VER2.get_rect(bottomright=(667-120+281,380+102)).collidepoint(event.pos):
                            self.version="v2"
                            active_ver=True
                        if SCROLL_LONG.get_rect(center=(667/2+281,285)).collidepoint(event.pos):
                            scroll=True
                        rect_logout=font_v(join("img","font",f"{font_setting[self.version]}"),25).render(f'Change profile logout',True,color_history[self.version])
                        if rect_logout.get_rect(topleft=((440,160))).collidepoint(event.pos) and event.button==1:
                            self.logout=True
                            return 2
                if event.type==pygame.MOUSEBUTTONUP:
                    if layer_choose==2:
                            scroll=False
                            # print("oke")
                    #history_game_______________________________layer_choose=0_________________________________________________________
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if layer_choose==0:
                        if event.button==1:
                            click_sound.play()
                            if dem<len(data[self.id+1]['history']):
                                count=len(data[self.id+1]['history'])
                            else: 
                                count=dem 
                            if pygame.Rect((281,52+50),(667,446-50-10)).collidepoint(event.pos):
                                for i in range(0,dem):
                                    if pygame.Rect((281,58+76*i-50+y_scroll+52+50),(667,60)).collidepoint(event.pos):
                                        print("man",i)
                                        choose_t=data[self.id+1]['history'][count-i-1]['set']
                                        name=data[self.id+1]['history'][count-i-1]['name'] # là một mảng 
                                        set_nv=[]
                                        self.emotion_history_id=count-i-1
                                        # print(count-i-1)
                                        for h in range(5):
                                            set_nv.append([set[choose_t[h][0]][choose_t[h][1]][0],name[h]])
                                        self.method_emotion=1
                                        main.result_rank(set_nv     ,data[self.id+1]['history'][count-i-1]['race'][1]      ,data[self.id+1]['history'][count-i-1]['race'][2]       ,data[self.id+1]['history'][count-i-1]['choose']+1,    data[self.id+1]['history'][count-i-1]['coin_earn'])
                                        self.method_emotion=0
                    
                if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_UP:
                            if (58+76*dem-50+y_scroll+52+50)>(52+50+446-60):
                                y_scroll-=30
                        if event.key==pygame.K_DOWN:
                            if y_scroll<0:
                                y_scroll+=30

            screen.blit(BG,(0,0))
            screen.blit(TABLE,(281,52))
                    
            layer[layer_choose].blit(BG,(-281,-102))
            layer[layer_choose].blit(TABLE,(0,-50))
            
            #_______________________________________________layer_choose=0_________________________________________
            if layer_choose==0:
                dem=min(len(data[self.id+1]['history']),19)
                for i in range(0,dem):
                    k=len(data[self.id+1]['history'])-1-i
                    rank=data[self.id+1]['history'][k]['rank']
                    time=data[self.id+1]['history'][k]['time']
                    resutl=data[self.id+1]['history'][k]['result']
                    emotion=data[self.id+1]['history'][k]['emotion']
                    coin_earn=data[self.id+1]['history'][k]['coin_earn']
                    layer1.blit(RECT_60x60,(17,58+76*i-50+y_scroll))
                    choose_t=data[self.id+1]['history'][k]['set']
                    layer1.blit(pygame.transform.scale(set[choose_t[data[self.id+1]['history'][k]['choose']][0]][choose_t[data[self.id+1]['history'][k]['choose']][1]][0],(50,50)),(17+5,58+76*i-50+y_scroll+5))
                    layer1.blit(font_v(SourceCodePro_Black,20).render((data[self.id+1]['history'][k]['name'][data[self.id+1]['history'][k]['choose']]),True,color_history[self.version]),(94,76+76*i-50+y_scroll))
                    layer1.blit(font_v(SourceCodePro_Black,25).render(f'#{rank}',True,color_history[self.version]),(185,72+76*i-50+y_scroll))
                    layer1.blit(font_v(join("img","font",f"{font_setting_italic[self.version]}"),20).render(f'00:{round(time,2)}',True,color_history[self.version]),(310,76+76*i-50+y_scroll-3))
                    layer1.blit(font_v(join("img","font",f"{font_setting_italic[self.version]}"),20).render(f'{emotion}',True,BLUE),(440,76+76*i-50+y_scroll-3))
                    layer1.blit(COIN_HIS,(544,83+76*i-50+y_scroll))
                    if coin_earn>=0:
                        layer1.blit(font_v(join("img","font",f"{font_setting_italic[self.version]}"),20).render(f'+{coin_earn}',True,YELLOW),(563,76+76*i-50+y_scroll))
                    else:
                        layer1.blit(font_v(join("img","font",f"{font_setting_italic[self.version]}"),20).render(f'{coin_earn}',True,color_history[self.version]),(563,76+76*i-50+y_scroll))
                    if resutl=="win":
                        layer1.blit(WIN,(240,76+76*i-50+y_scroll+8))
                    else : 
                        layer1.blit(LOSE,(240,76+76*i-50+y_scroll+8))
                screen.blit(font_v(SourceCodePro_Black,25).render(f'result',True,color_history[self.version]),(465,65))
                screen.blit(font_v(SourceCodePro_Black,25).render(f'racer',True,color_history[self.version]),(300,65))
                screen.blit(COL_SCROLL,COL_SCROLL.get_rect(midright=(975-47,446/2+52)))
                if dem!=0:
                    screen.blit(pygame.transform.scale(COL_SCROLL_SMALL,(15,380*min( (5/dem), 1 ))),COL_SCROLL_SMALL.get_rect(topright=(975-47,min(446/2+52-380/2-(y_scroll*((5/dem)*380/386)),380+52+33-380*min( (5/dem), 1 )))))
            #__________________________________________layer_choose==1_____________________________________________
            elif layer_choose==1:
                dem=min(len(data[self.id+1]['account']),19)
                for i in range(0,dem):
                    k=len(data[self.id+1]['account'])-1-i
                    date=data[self.id+1]['account'][k]['date']
                    activity=data[self.id+1]['account'][k]['activity']
                    status=data[self.id+1]['account'][k]['status']
                    total=data[self.id+1]['account'][k]['total']
                    layer2.blit(font_v(join("img","font",f"{font_setting[self.version]}"),20).render(date,True,BLUE),(21,76+76*i-50+y_scroll))
                    ACTIVITY=font_v(join("img","font",f"{font_setting[self.version]}"),25).render(f'{activity}',True,color_history[self.version])
                    layer2.blit(ACTIVITY,ACTIVITY.get_rect(center=(240+60,15+72+76*i-50+y_scroll)))
                    layer2.blit(font_v(join("img","font",f"{font_setting[self.version]}"),20).render(f'{status}',True,color_history[self.version]),(490,76+76*i-50+y_scroll))
                    layer2.blit(font_v(join("img","font",f"{font_setting[self.version]}"),20).render(f'{total}',True,BLUE),(590,76+76*i-50+y_scroll))
                    layer2.blit(COIN_HIS,(460,83+76*i-50+y_scroll))
                    layer2.blit(COIN_HIS,(570,83+76*i-50+y_scroll))
                screen.blit(font_v(SourceCodePro_Black,25).render(f'Date',True,color_history[self.version]),(338,65))
                screen.blit(font_v(SourceCodePro_Black,25).render(f'Activity',True,color_history[self.version]),(502,65))
                screen.blit(font_v(SourceCodePro_Black,25).render(f'Status',True,color_history[self.version]),(720,65))
                screen.blit(font_v(SourceCodePro_Black,25).render(f'Total',True,color_history[self.version]),(840,65))
            #__________________________________________layer_choose==2_____________________________________________
            else :
                if scroll  and SCROLL_LONG.get_rect(center=(667/2+281,285)).collidepoint(pygame.mouse.get_pos()):
                    x,y=pygame.mouse.get_pos()
                    delta_x=x-281-109.5
                    self.sound=(100*delta_x)/448
                    pygame.mixer.music.set_volume(self.sound/100)
                    win_sound.set_volume(self.sound/100)
                    racing_sound.set_volume(self.sound/100)
                    click_sound.set_volume(self.sound/100)
                screen.blit(font_v(SourceCodePro_Black,25).render(f'Account:',True,WHITE),(301,70))
                screen.blit(font_v(join("img","font",f"{font_setting[self.version]}"),25).render(f'Change username',True,color_history[self.version]),(440,60))
                layer3.blit(font_v(join("img","font",f"{font_setting[self.version]}"),25).render(f'Change passwork',True,color_history[self.version]),(440-281,0))
                layer3.blit(font_v(join("img","font",f"{font_setting[self.version]}"),25).render(f'Change face id',True,color_history[self.version]),(440-281,130-102))
                layer3.blit(font_v(join("img","font",f"{font_setting[self.version]}"),25).render(f'Change profile logout',True,color_history[self.version]),(440-281,160-102))
                layer3.blit(font_v(SourceCodePro_Black,25).render(f'Sound:',True,WHITE),(301-281,230-102))
                layer3.blit(font_v(SourceCodePro_Black,25).render(f'Graphics:',True,WHITE),(301-281,330-102))
                layer3.blit(SCROLL_LONG,SCROLL_LONG.get_rect(center=(667/2,285-102)))
                layer3.blit(pygame.transform.scale(SCROLL_SCALE,(delta_x+1,15)),SCROLL_SCALE.get_rect(midleft=(109.5,285-102)))
                layer3.blit(VER1,VER1.get_rect(bottomleft=(120,380)))
                layer3.blit(VER2,VER2.get_rect(bottomright=(667-120,380)))
                layer3.blit(SOUND_ON,SOUND_ON.get_rect(midright=(667-20,285-102+5)))
                layer3.blit(SOUND_OFF,SOUND_OFF.get_rect(midleft=(40,285-102+2)))
                if self.version=="v1":
                    pygame.draw.rect(layer3,(32, 227, 116),VER1.get_rect(bottomleft=(120,380)),5)
                else :
                    pygame.draw.rect(layer3,(32, 227, 116),VER2.get_rect(bottomright=(667-120,380)),5)
            screen.blit(layer[layer_choose],(281,52+50))      
            screen.blit(font_v(SourceCodePro_Black,50).render(f'X',True,YELLOW),(900,15))
            screen.blit(COIN,(135,54))
            screen.blit(AVA,(31,21))
            screen.blit(pygame.font.Font(r'img\font\SourceCodePro-BlackItalic.ttf',30).render(f'@{username}',True,YELLOW),(136,21))
            screen.blit(pygame.font.Font(r'img\font\SourceCodePro-BlackItalic.ttf',30).render(f'{coin}',True,YELLOW),(174,55))
            screen.blit(font_v(join("img","font",f"{font_setting[self.version]}"),27).render(f'Racing History',True,color_choose[0]),(25,200))
            screen.blit(font_v(join("img","font",f"{font_setting[self.version]}"),27).render(f'Account History',True,color_choose[1]),(25,250))
            screen.blit(font_v(join("img","font",f"{font_setting[self.version]}"),27).render(f'Settings',True,color_choose[2]),(25,300))
            if layer_choose<=1:
                screen.blit(COL_SCROLL,COL_SCROLL.get_rect(midright=(975-47,446/2+52)))
                if dem!=0:
                    screen.blit(pygame.transform.scale(COL_SCROLL_SMALL,(15,380*min( (5/dem), 1 ))),COL_SCROLL_SMALL.get_rect(topright=(975-47,min(446/2+52-380/2-(y_scroll*((5/dem)*380/386)),380+52+33-380*min( (5/dem), 1 )))))
            pygame.display.update()
    def create_rename(self,method): #0:rename , 1 passwork 2, dace
        with open('data_player/data.json') as file_name:
            data=json.load(file_name)
        BG=pygame.image.load(join("img","load_sign_in",f"bg_setting{self.version}.png"))
        SUN=pygame.image.load(join("img","load_sign_in",f"sun.png")) 
        CLOUD=pygame.image.load(join("img","load_sign_in",f"cloud.png")) 
        INPUT=pygame.image.load(join("img","load_sign_in",f"input-pass{self.version}.png"))
        NEXT=pygame.image.load(join("img","main",f"next{self.version}.png"))
        EXIT_HIS=pygame.image.load(r"img\history\exit_his.png") 
        text_rename=[]
        if method==0:   
            text_rename.append(font_v(join("img","font",f'{font_setting[self.version]}'),50).render(f'change username',True,color_setting[self.version]))
            text_rename.append(font_v(join("img","font",f'{font_setting[self.version]}'),30).render(f'old username : ',True,color_setting[self.version]))
            text_rename.append(font_v(join("img","font",f'{font_setting[self.version]}'),30).render(f'new username : ',True,color_setting[self.version]))
        else:
            text_rename.append(font_v(join("img","font",f'{font_setting[self.version]}'),50).render(f'change passwork',True,color_setting[self.version]))
            text_rename.append(font_v(join("img","font",f'{font_setting[self.version]}'),50).render(f'old passwork',True,color_setting[self.version]))
            text_rename.append(font_v(join("img","font",f'{font_setting[self.version]}'),50).render(f'mew passwork',True,color_setting[self.version]))
        active_ver=True
        active=[False,False]
        running=True
        BG_x=0
        color_active=[color_setting[self.version],color_setting[self.version]]
        text=["",""]
        while running:
            CLOCK.tick(60)
            if active_ver:
                active_ver=False
                NEXT=pygame.image.load(join("img","main",f"next{self.version}.png"))
                BG=pygame.image.load(join("img","load_sign_in",f"bg_setting{self.version}.png"))
                INPUT=pygame.image.load(join("img","main",f"input-pass{self.version}.png"))
                text_rename=[]
                if method==0:   
                    text_rename.append(font_v(join("img","font",f'{font_setting[self.version]}'),50).render(f'change username',True,color_setting[self.version]))
                    text_rename.append(font_v(join("img","font",f'{font_setting[self.version]}'),30).render(f'old username : ',True,color_active[0]))
                    text_rename.append(font_v(join("img","font",f'{font_setting[self.version]}'),30).render(f'new username : ',True,color_active[1]))
                else:
                    text_rename.append(font_v(join("img","font",f'{font_setting[self.version]}'),50).render(f'change passwork',True,color_setting[self.version]))
                    text_rename.append(font_v(join("img","font",f'{font_setting[self.version]}'),30).render(f'old passwork',True,color_active[0]))
                    text_rename.append(font_v(join("img","font",f'{font_setting[self.version]}'),30).render(f'mew passwork',True,color_active[1]))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running==False
                    return 0
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if event.button==1:
                        click_sound.play()
                        if EXIT_HIS.get_rect(topleft=(10,510)).collidepoint(event.pos):
                            running=False
                        for i in range(2):
                            if INPUT.get_rect(midleft=(WIDTH/2+10,200+100*i)).collidepoint(event.pos):
                                # print(INPUT.get_rect(midleft=(WIDTH/2+10,200+100*i)))
                                # print(active)
                                active[i]=True
                                color_active[i]=BLUE
                                active_ver=True
                            else : 
                                active[i]=False
                                color_active[i]=color_setting[self.version]
                                active_ver=True
                        if NEXT.get_rect(center=(WIDTH/2,HEIGHT-100)).collidepoint(event.pos):
                            if method==0:
                                if text[0]==data[0]['user'][self.id]['user_name']:
                                    data[0]['user'][self.id]['user_name']=text[1]
                                    with open('data_player/data.json','w') as file_name:
                                        json.dump(data,file_name,indent=4) 
                                    running=False
                            else :
                                if text[0]==data[0]['user'][self.id]['passwork']:
                                    data[0]['user'][self.id]['passwork']=text[1]
                                    with open('data_player/data.json','w') as file_name:
                                        json.dump(data,file_name,indent=4) 
                                    running=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_TAB:
                        if self.version=="v1":
                            self.version="v2"
                            active_ver=True
                        else :
                            self.version="v1"
                            active_ver=True
                    for i in range(2):
                        if active[i]:
                            if event.key == pygame.K_RETURN:
                                    print(text[i])
                                    # text = ''
                            elif event.key == pygame.K_BACKSPACE:
                                    text[i] = text[i][:-1]
                            else:
                                    text[i] += event.unicode
            BG_x-=0.5
            if BG_x==-975:
                BG_x=0
            screen.blit(BG,(BG_x,0))
            screen.blit(BG,(BG_x+975,0))
            if self.version=="v2":
                screen.blit(SUN,(0,0))
                screen.blit(CLOUD,(BG_x,0))
                screen.blit(CLOUD,(BG_x+975,0))
            screen.blit(text_rename[0],text_rename[0].get_rect(center=(WIDTH/2,30)))
            screen.blit(text_rename[1],text_rename[1].get_rect(midright=(WIDTH/2-10,200)))
            screen.blit(text_rename[2],text_rename[2].get_rect(midright=(WIDTH/2-10,290)))
            screen.blit(INPUT,INPUT.get_rect(midleft=(WIDTH/2+10,200)))
            screen.blit(INPUT,INPUT.get_rect(midleft=(WIDTH/2+10,300)))
            screen.blit(NEXT,NEXT.get_rect(center=(WIDTH/2,HEIGHT-100)))
            screen.blit(EXIT_HIS,(10,510))
            for i in range(2):
                text_blit=font_v(join("img","font",f'{font_setting[self.version]}'),20).render(f'{text[i]}',True,color_setting[self.version])
                screen.blit(text_blit,text_blit.get_rect(center=(WIDTH/2+10+420/2,200+100*i)))
            pygame.display.update()
    def create_face_id(self): #method 0: create , 1 change face id
        with open('data_player/data.json') as file_name:
            data=json.load(file_name)
        BG=pygame.image.load(join("img","load_sign_in",f"bg_setting{self.version}.png"))
        SUN=pygame.image.load(join("img","load_sign_in",f"sun.png")) 
        CLOUD=pygame.image.load(join("img","load_sign_in",f"cloud.png")) 
        NEXT=pygame.image.load(join("img","main",f"next{self.version}.png"))
        RECT_FACEID=pygame.image.load(join("img","history",f"rect_faceid{self.version}.png"))
        EXIT_HIS=pygame.image.load(r"img\history\exit_his.png") 
        text_change=font_v(join("img","font",f'{font_setting[self.version]}'),20).render(f' Change Face ID ',True,color_setting[self.version])
        text_new=font_v(join("img","font",f'{font_setting[self.version]}'),20).render(f' Create Face ID ',True,color_setting[self.version])
        running =True
        active_ver=True
        BG_x=0
        while running:
            CLOCK.tick(60)
            if active_ver:
                active_ver=False
                NEXT=pygame.image.load(join("img","main",f"next{self.version}.png"))
                BG=pygame.image.load(join("img","load_sign_in",f"bg_setting{self.version}.png"))
                RECT_FACEID=pygame.image.load(join("img","history",f"rect_faceid{self.version}.png"))
                text_change=font_v(join("img","font",f'{font_setting[self.version]}'),40).render(f' Change Face ID ',True,color_setting[self.version])
                text_new=font_v(join("img","font",f'{font_setting[self.version]}'),40).render(f' Create Face ID ',True,color_setting[self.version])
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running==False
                    return 0
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if event.button==1:
                        click_sound.play()
                        if EXIT_HIS.get_rect(topleft=(10,510)).collidepoint(event.pos):
                            running=False
                        with open('data_player/data.json') as file_name:
                            data=json.load(file_name)
                        if text_change.get_rect(center=(WIDTH/2,60)).collidepoint(event.pos) and data[0]['user'][self.id]['face_id']=="yes":
                            create.create_recognition(self.id,1)
                            train.train_data_face(self.id)
                        if text_change.get_rect(center=(WIDTH/2,HEIGHT-70)).collidepoint(event.pos) and data[0]['user'][self.id]['face_id']=="no":
                            create.create_recognition(self.id,0)
                            data[0]['user'][self.id]['face_id']="yes"
                            with open('data_player/data.json','w') as file_name:
                                json.dump(data,file_name,indent=4) 
                            train.train_data_face(self.id)
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_TAB:
                        if self.version=="v1":
                            self.version="v2"
                            active_ver=True
                        else :
                            self.version="v1"
                            active_ver=True
            BG_x-=0.5
            if BG_x==-975:
                BG_x=0
            screen.blit(BG,(BG_x,0))
            screen.blit(BG,(BG_x+975,0))
            if self.version=="v2":
                screen.blit(SUN,(0,0))
                screen.blit(CLOUD,(BG_x,0))
                screen.blit(CLOUD,(BG_x+975,0))
            screen.blit(RECT_FACEID,RECT_FACEID.get_rect(center=(WIDTH/2,HEIGHT/2)))
            screen.blit(text_change,text_change.get_rect(center=(WIDTH/2,60)))
            screen.blit(text_new,text_new.get_rect(center=(WIDTH/2,HEIGHT-70)))
            screen.blit(EXIT_HIS,(10,510))
            pygame.display.update()
    # def guide(self):
        
    #     running=True
        
    #     while running :
    #         CLOCK.tick(60)
    #         for event in pygame.event.get():
    #             if event.type==pygame.QUIT:
    #                 running==False
    #                 return 0
                
                    
            
    #         pygame.display.update()
                
            
    def main_game(self):
        running=True
        font=pygame.font.Font(r'img\font\SourceCodePro-BlackItalic.ttf',30)
        font_coin=pygame.font.Font(r'img\font\SourceCodePro-BlackItalic.ttf',25)
        font_main=font_v(SourceCodePro_Black,30)
        BG=pygame.transform.scale(pygame.image.load(r"img\main\bgr.png"),(975,550))
        BG_x=0
        SCALE_X1=0
        SCALE_Y1=0
        SCALE_X2=0
        SCALE_Y2=0
        SCALE_X3=0
        SCALE_Y3=0
        WHITE=(255,255,255)
        BLUE=(31,5,73)
        COLOR1=BLUE
        COLOR2=BLUE
        COLOR3=BLUE
        MEDAL=pygame.image.load(r"img\main\medal.png")
        MEDAL=pygame.transform.scale(MEDAL,(185,221))
        COIN=pygame.image.load(r"img\main\coin1.png")  
        AVA=pygame.image.load(r"img\main\ava.png") 
        CHEST=pygame.image.load(r"img\main\chest.png") 
        ARCADE=pygame.image.load(r"img\main\arcade_pic.png")
        HELP=pygame.image.load(r"img\load_sign_in\info.png")
        TEXT_GUI=pygame.image.load(r"img\history\text_gui_main.png")
        RECT_GUI=pygame.transform.scale(pygame.image.load(join("img","history",f"rect_gui{self.version}.png")) ,(875,432))
        active_gui=False
        while running:
            with open('data_player/data.json') as file_name:
                data=json.load(file_name)
            user_name=data[0]['user'][self.id]['user_name']
            coin=data[0]['user'][self.id]['coin']
            CHEST_RECT=pygame.image.load(r"img\main\chest_rect.png") 
            RACE=pygame.image.load(r"img\main\RACE.png")
            BG_GREEN=pygame.image.load(r"img\main\bg_green.png")
            CLOCK.tick(60)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                if event.type==pygame.KEYDOWN and event.key==pygame.K_TAB:
                    if self.version=="v1":
                        self.version="v2"
                    else :
                        self.version="v1"
                if event.type== pygame.MOUSEBUTTONDOWN and event.button==1:
                    click_sound.play()
                    #help
                    active_gui=False
                    if HELP.get_rect(center=(WIDTH-50,50)).collidepoint(event.pos):
                        active_gui=True
                    # view profile avatar
                    if pygame.Rect(((31,21),(80,80))).collidepoint(event.pos):
                        his=main.history()
                        if his==1 or his==2:
                            return 1  
                    #chest_shop
                    if pygame.Rect((60,153),(257,378)).collidepoint(pygame.mouse.get_pos()):
                        BG_x=main.chest(BG_x)
                    # star racing game 
                    if pygame.Rect((352,117),(257,378)).collidepoint(pygame.mouse.get_pos()):
                        setting=main.setting_match()
                        self.text_chat=[]
                        if setting==1:
                            return 1
                        if setting!=0:
                            MAP=setting[0] # map 
                            SET_NV=setting[1] # your set
                            choose=setting[2] # your character
                            coin_set=setting[3] # coin bet
                            stt_set=setting[4] # stt_set
                            map_type=setting[5]
                            if setting[6]==0: # check choose_t xem thử có tùy chọn nhân vậy hay không   
                                choose_t=[]
                                for i in range(0,5):
                                    choose_t.append([stt_set,i])
                            else:
                                choose_t=setting[6]
                            # print()
                            # print(MAP)
                            # print(SET_NV)
                            result=0 
                            if MAP[1]=="space view":
                                map_choose=0
                            elif MAP[1]=="desert view":
                                map_choose=1
                            elif MAP[1]=="mountain view":
                                map_choose=2
                            if map_type=="short":
                                self.type_choose=0
                            if map_type=="mid":
                                self.type_choose=1
                            if map_type=="long":
                                self.type_choose=2
                            pygame.mixer.music.stop()
                            racing_sound.play(-1)
                            result=main_play(pygame.display.set_mode((975,550)),choose_t,map_choose,self.id)
                            racing_sound.stop()
                            pygame.mixer.music.play(-1)
        #======================================================================================  
                            rank_t=result[1]
                            if choose==rank_t[0]:
                                coin_earn=coin_set*5
                            elif choose==rank_t[1]:
                                    coin_earn=-coin_set
                            elif choose==rank_t[2] :
                                coin_earn=-coin_set
                            elif choose==rank_t[3]:
                                coin_earn=-coin_set
                            elif choose==rank_t[4]:
                                coin_earn=-coin_set
                            # create a new history
                            data[0]['user'][self.id]['coin']+=coin_earn
                            data[self.id+1]['history'].append({})
                            data[self.id+1]['history'][len(data[self.id+1]['history'])-1]['set']=choose_t
                            data[self.id+1]['history'][len(data[self.id+1]['history'])-1]['choose']=choose-1
                            data[self.id+1]['history'][len(data[self.id+1]['history'])-1]['name']=[]
                            for i in range(5):
                                data[self.id+1]['history'][len(data[self.id+1]['history'])-1]['name'].append(set[choose_t[i][0]][choose_t[i][1]][1])
                            for i in range(0,5):
                                if result[1][i]==choose:
                                    rank_choose=i+1
                                    break
                            data[self.id+1]['history'][len(data[self.id+1]['history'])-1]['rank']=rank_choose
                            data[self.id+1]['history'][len(data[self.id+1]['history'])-1]['time']=result[0][choose-1]
                            if rank_choose==1:
                                data[self.id+1]['history'][len(data[self.id+1]['history'])-1]['result']="win"
                            else:
                                data[self.id+1]['history'][len(data[self.id+1]['history'])-1]['result']="lose"
                            count_negative=0
                            count_positive=0
                            for i in range(len(self.text_chat)):
                                if i%2==0:
                                    if sentiment(self.text_chat[i])=="positive":
                                        count_positive+=1
                                    elif sentiment(self.text_chat[i])=="negative":
                                        count_negative+=1
                            if (count_negative!=0 and count_positive!=0) or (count_negative==0 and  count_positive==0 ):
                                data[self.id+1]['history'][len(data[self.id+1]['history'])-1]['emotion']="normal"
                            elif count_positive!=0 and count_negative==0:
                                data[self.id+1]['history'][len(data[self.id+1]['history'])-1]['emotion']="cheerful"
                            elif count_negative!=0 and count_positive==0 :
                                data[self.id+1]['history'][len(data[self.id+1]['history'])-1]['emotion']="upset"
                            self.emotion=data[self.id+1]['history'][len(data[self.id+1]['history'])-1]['emotion']
                            data[self.id+1]['history'][len(data[self.id+1]['history'])-1]['coin_earn']=coin_earn
                            data[self.id+1]['history'][len(data[self.id+1]['history'])-1]['race']=self.id,result[0],result[1]
                            #_______________account____________________
                            date=time.localtime(time.time()).tm_mday
                            month=time.localtime(time.time()).tm_mon
                            year=time.localtime(time.time()).tm_year
                            data[self.id+1]['account'].append({})
                            data[self.id+1]['account'][len(data[self.id+1]['account'])-1]['activity']=data[self.id+1]['history'][len(data[self.id+1]['history'])-1]['result']+" a bet"
                            data[self.id+1]['account'][len(data[self.id+1]['account'])-1]['date']=str(date)+"/"+str(month)+"/"+str(year)
                            data[self.id+1]['account'][len(data[self.id+1]['account'])-1]['status']=coin_earn
                            data[self.id+1]['account'][len(data[self.id+1]['account'])-1]['total']=data[0]['user'][self.id]['coin']
                            # dump data to json
                            with open('data_player/data.json','w') as file_name:
                                json.dump(data,file_name,indent=4)
                            # print rank 
                            if self.version=="v1":
                                main.rank(SET_NV,result[0],result[1],choose,coin_earn)
                            #print result
                            self.method_emotion=0
                            main.result_rank(SET_NV,result[0],result[1],choose,coin_earn) 
                    # arcade another game
                    if pygame.Rect((658,153),(257,378)).collidepoint(pygame.mouse.get_pos()):
                        BG_x=main.arcade(BG_x)
                #hover effect 3 button of main game 
                if pygame.Rect((60,153),(257,378)).collidepoint(pygame.mouse.get_pos()) or pygame.Rect((352,117),(257,378)).collidepoint(pygame.mouse.get_pos()) or pygame.Rect((658,153),(257,378)).collidepoint(pygame.mouse.get_pos()):
                    if pygame.Rect((60,153),(257,378)).collidepoint(pygame.mouse.get_pos()):
                        COLOR3=BLUE
                        COLOR2=BLUE
                        COLOR1=WHITE
                        SCALE_X1=0
                        SCALE_Y1=0
                        SCALE_X2=0
                        SCALE_Y2=0
                        SCALE_X3=0
                        SCALE_Y3=0
                        SCALE_X1=14
                        SCALE_Y1=36
                    if pygame.Rect((352,117),(257,378)).collidepoint(pygame.mouse.get_pos()):
                
                        COLOR3=BLUE
                        COLOR1=BLUE
                        COLOR2=WHITE
                        SCALE_X1=0
                        SCALE_Y1=0
                        SCALE_X2=0
                        SCALE_Y2=0
                        SCALE_X3=0
                        SCALE_Y3=0
                        SCALE_X2=14
                        SCALE_Y2=36
                    if pygame.Rect((658,153),(257,378)).collidepoint(pygame.mouse.get_pos()):
                        COLOR1=BLUE
                        COLOR2=BLUE
                        COLOR3=WHITE
                        SCALE_X1=0
                        SCALE_Y1=0
                        SCALE_X2=0
                        SCALE_Y2=0
                        SCALE_X3=0
                        SCALE_Y3=0
                        SCALE_X3=14
                        SCALE_Y3=36
                else: 
                    SCALE_X1=0
                    SCALE_Y1=0
                    SCALE_X2=0
                    SCALE_Y2=0
                    SCALE_X3=0
                    SCALE_Y3=0
                    COLOR1=BLUE
                    COLOR2=BLUE
                    COLOR3=BLUE
            BG_x-=0.5
            if BG_x==-975:
                BG_x=0
            name=font.render(f'@{(user_name)}',True,(31,5,73)) #{str(score)}
            coin_bg=font_coin.render(f'{int(coin)}',True,(31,5,73))
            CHEST_RECT=pygame.transform.scale(CHEST_RECT,(257+SCALE_X1,378+SCALE_Y1))
            RACE=pygame.transform.scale(RACE,(257+SCALE_X2,378+SCALE_Y2))
            BG_GREEN=pygame.transform.scale(BG_GREEN,(257+SCALE_X3,378+SCALE_Y3))
            screen.blit(BG,(BG_x,0))
            screen.blit(BG,(BG_x+975,0))
            if BG_x==-975:
                BG_x=0
            screen.blit(CHEST_RECT,(60-SCALE_X1/2,153-SCALE_Y1))
            screen.blit(CHEST,(96,204))
            screen.blit(RACE,(357-SCALE_X2/2,153-SCALE_Y2))
            screen.blit(MEDAL,(393,172))
            screen.blit(BG_GREEN,(658-SCALE_X3/2,153-SCALE_Y3))
            screen.blit(COIN,(135,54))
            screen.blit(AVA,(31,21))
            screen.blit(ARCADE,(687,167))
            screen.blit(HELP,HELP.get_rect(center=(WIDTH-50,50)))
            screen.blit(name,(136,21))
            screen.blit(coin_bg,(174,61))
            screen.blit(font_main.render(f'CHEST',True,COLOR1),(136,448))
            screen.blit(font_main.render(f'RACING',True,COLOR2),(435,414))
            screen.blit(font_main.render(f'GAME',True,COLOR2),(450,448))
            screen.blit(font_main.render(f'ARCADE',True,COLOR3),(735,448))
            if active_gui:
                RECT_GUI=pygame.transform.scale(pygame.image.load(join("img","history",f"rect_gui{self.version}.png")) ,(875,432))
                TEXT_GUIDE=font_v(join("img","font",f"{font_setting[self.version]}"),50).render(f'Racing Game',True,color_setting[self.version])
                screen.blit(RECT_GUI,RECT_GUI.get_rect(center=(WIDTH/2,HEIGHT/2+10)))
                screen.blit(TEXT_GUI,TEXT_GUI.get_rect(center=(WIDTH/2,HEIGHT/2+10)))
                screen.blit(TEXT_GUIDE,TEXT_GUIDE.get_rect(center=(WIDTH/2,40)))
            pygame.display.update()
#===================================================================================
    def play(self):
            main.load_BG()
            if not self.load_BG:
                return 1
            if self.id==-2: 
                return 1
            else :
                check_logout=main.main_game()
#====================================================================================
pygame.init()
run_main=True
while run_main:
    main=Main()
    main.play()
    if not main.logout:
        run_main=False