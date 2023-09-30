import pygame as pygame
import random
import time
import json
import os
pygame.init()

#初始化一个clock变量，使用开头导入的time包。这个变量将用来处理游戏的帧率
clock = pygame.time.Clock()
snake_speed=6 #蛇的速度
#定义游戏状态变量
game_over = False #游戏失败后变为True
game_close = False #决定退出游戏后变为True

#颜色配置 字体配置
snake_color = pygame.Color("#8B7D1C")
food_color = pygame.Color("#8B0000")
background_color = pygame.Color("#BACB03")
text_color = pygame.Color("#EFEFEF")
score_font= pygame.font.SysFont("comicsansms", 35) #分数字体(含大小 )
font_style= pygame.font.SysFont("bahnschrift", 25) #全局字体(含大小)

#长度单位
pixel=15
line=44 #这里指列数
row=36 #这里指行数
window_width=pixel*line
window_high=pixel*row

point_left_up=[pixel*2,pixel*4]
point_left_down=[pixel*2,pixel*(row-2)]
point_right_up=[pixel*(line-2),pixel*4]
point_right_down=[pixel*(line-2),pixel*(row-2)]

#蛇头位置
snake_head=[pixel*8,pixel*8]
#蛇 默认两个小方块
snake_body=[[snake_head[0]-x*pixel,snake_head[1]]for x in range(2)]

#设置屏幕和标题
dis=pygame.display.set_mode( (window_width , window_high) )
pygame.display.set_caption('Snakes')
dis.fill(background_color)
clock = pygame.time.Clock()
#分数设置
score=0
filename='score.json'

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, text_color)
    dis.blit(value, [0, 0])
    pygame.display.update()

def save_score(content):
    with open(filename,'r',encoding='utf-8') as fr:
        #dic1=f.read()
        s_old=json.load(fr)
        s_old_lst=s_old['total']
    with open(filename,'w+',encoding='utf-8') as fw:
        fw.seek(0)
        fw.truncate()
        s_new_dic={'time':time.asctime(), 'score':content}
        s_old_lst.append(s_new_dic)
        dic={'total':s_old_lst}
        
        json.dump(dic,fw, indent=4, ensure_ascii=False) #fw为要写入的文件，dic是要写入的内容，后面部分用来格式化json
        fw.close()

def read_score():
    global highest_score
    s_lst=[]
    highest_score='0'
    with open(filename,'r',encoding='utf-8') as file:
        try:
            s_old=json.load(file)
            if s_old:
                for dic in s_old['total']:
                    s_lst.append(dic['score'])
                    s_lst.sort(reverse=True) #降序排序
                    highest_score=str( s_lst[0] )
        except:
            pass
            '''display_message(s_high, text_color, (550,30) )'''

#显示文字
def display_message(text,color,position):
    text1=score_font.render(text,True,color)
    dis.blit(text1,position)
    pygame.display.update()

#画边线
def draw_box():
    for point in [ [point_left_up , point_right_up] , [point_right_up , point_right_down] , 
                         [point_right_down , point_left_down] , [point_left_down , point_left_up] ]:
        pygame.draw.line(dis, snake_color, point[0], point[1], 1)

#随机生成食物
def creat_food():
    while True:
        x=random.randint(point_left_up[0] / pixel, point_right_up[0] / pixel-1) * pixel
        y=random.randint(point_left_up[1] / pixel, point_left_down[1] / pixel-1) * pixel
        if [x,y] not in snake_body:
            break
    return [x,y]

#画蛇
def draw_snake(food_position):
    for point in snake_body:
        pygame.draw.rect(dis, snake_color, [point[0], point[1], pixel, pixel])
    pygame.draw.rect(dis, food_color, [food_position[0], food_position[1], pixel, pixel]) #画食物

def snake_move(origin_direction):
        global snake_head
        move={'direction_right':[pixel, 0], 'direction_left':[-pixel, 0], 'direction_up':[0, -pixel], 'direction_down':[0, pixel]}   
        #移动
        x1=move[origin_direction]
        snake_head[0]+=x1[0]
        y1=move[origin_direction]
        snake_head[1]+=y1[1]
        snake_body.insert(0, list(snake_head))
        #调用完此函数后要移除蛇尾

snake_length=len(snake_body)

def run():
    global snake_length, score
    check_file(filename)
    read_score()
    game_close=False
    game_over=False
    dire='direction_right'
    food_position=creat_food()
    while game_close==False:
        while game_over==False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_close = True
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        game_close=True
                        return
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        dire='direction_left'
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        dire='direction_right'
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        dire='direction_up'
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        dire='direction_down'
            snake_move(dire)
            if food_position==snake_head:
                food_position=creat_food()
                score+=1
                
                snake_length+=1
            else:
                snake_body.pop() #只要没吃到，就移除蛇尾
            pygame.display.update()
            dis.fill(background_color)
            draw_box()
            draw_snake(food_position)
            Your_score(score)
            show_highest_score()
            pygame.display.flip()
            
            for x in snake_body[1::1]: #反向遍历
                if x == snake_head: #只要蛇头和蛇身坐标一样，即蛇碰到自己，就结束
                    game_over = True
            
            clock.tick(snake_speed)
        if game_over==True:
            dis.fill(background_color)
            display_message("Lost! q quit or p again", text_color, [window_width / 6, window_high / 3])
            Your_score(snake_length - 2 )
            save_score(score)
            while game_over==True:
                for event in pygame.event.get():
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_q:
                            game_over=False
                            game_close=True
                        elif event.key==pygame.K_p:
                            startup()
                            run()
    pygame.quit()
    quit()

def startup():
    global snake_speed, snake_head, snake_body, snake_length, score
    pygame.init()
    #蛇的速度
    snake_speed=int(input('请输入蛇的速度：(6-15)'))
    snake_head=[pixel*8,pixel*8]
    snake_body=[[snake_head[0]-x*pixel,snake_head[1]]for x in range(2)]
    score=0
    snake_length=len(snake_body)
    read_score()

def check_file(f_name): #读取json文件
    dic1={"total":[{"time":"1","score":0}]}
    if os.path.exists(f_name): #检测文件是否存在
        try:
            with open(f_name,'r',encoding='utf-8') as rfile:
                json.load(rfile) #尝试读取json文件
        except:
            with open(f_name,'w+',encoding='utf-8') as wfile:
                wfile.seek(0)
                wfile.truncate()
                json.dump(dic1, wfile)
                wfile.close()
    else:
        with open(f_name,'x',encoding='utf-8') as xfile: #'x'指创建一个新文件，并进行写入
            json.dump(dic1, xfile)
            xfile.close()

def show_highest_score():
    global highest_score
    display_message('Highest Score: '+highest_score, text_color, (360,0) )

run()
            