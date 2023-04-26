#导入turtle 和 time
import turtle as t
import time 
#1.画正方形
a=0
while a<4:
    #前进100像素
    t.forward(100)
    #左转90度
    t.left(90)
    #即a=a+1
    a+=1
#清屏，对于括号里无参数的函数，也要把括号加上
t.clear()


b=0
while b<5:
    t.forward(120)
    #右转144度，也可以是左转216度
    t.right(144)
    b+=1
t.clear()

t.pensize(10)       #调整线条粗细
t.pencolor('red')   #调整颜色
t.circle(105)        #画圆，半径为105像素
t.penup()            #提笔
t.left(90)
t.forward(50)
t.right(90)
t.pendown()         #落笔
t.fillcolor('blue')   #设置填充颜色
t.begin_fill()       #设置开始填充的时间
t.circle(55)         #画圆
t.end_fill()          #结束填充

t.pensize(1)
t.pencolor('white')
t.fillcolor('white')

t.penup()
t.left(90)
t.forward(71)
t.left(90)
t.forward(50)
t.left(180)
t.pendown()

t.begin_fill()
c=0
while c<5:
    t.forward(100)
    t.right(144)
    c+=1
t.end_fill()
#隐藏海龟
t.hideturtle()

#暂停3秒
time.sleep(3)
t.clear()
