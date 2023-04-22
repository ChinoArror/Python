#程序的组织结构——顺序结构、选择结构、循环结构。

#顺序结构
"""把大象装进冰箱一共分几步"""
print('-------程序开始-------')
print('1.把冰箱门打开')
print('2.把大象放冰箱里')
print('3.把冰箱门关上')
print('-------程序结束-------')

#测试对象的布尔值，可以直接将对象放到条件表达式中来判断，会自动生成对象的布尔值。
print('-------以下对象的布尔值为False-------')
print( bool(False) )   #False
print( bool(0) )        #False
print( bool(0.0) )      #False
print( bool(None) )    #False
print( bool('') )        #空字符串
print( bool([]) )       #空列表
print( bool(list() ) )  #空列表
print( bool( () ) )      #空元组
print( bool(tuple() ) ) #空元组
print( bool({}) )        #空字典
print( bool(dict() ) )  #空字典
print( bool(set() ) )   #空集合

print('-------其他对象的布尔值均为True-------')

#选择结构
#单分支结构
money=1000 #余额
s=int( input('请输入取款金额') )
if money>=s:
    money-=s
    print('取款成功，余额为',money)
#双分支结构
"""从键盘录入一个整数，编写程序判断是奇数还是偶数。"""
num=int( input('请输入一个整数') )
if num%2==0:
    print(num,'是偶数')
else:
    print(num,'是奇数')
#多分支结构
"""根据成绩给出等级"""
g=float( input('请输入成绩') )
if 90<=g<=100:
    print(g,'分,','等级为''A')
elif 80<=g<90:
    print(g,'分,','等级为''B')
elif 70<=g<80:
    print(g,'分,','等级为''C')
elif 60<=g<70:
    print(g,'分,','等级为''D')
elif 0<=g<60:
    print(g,'分,','等级为''E')
else:
    print('分数格式错误')
#嵌套if结构
"""
会员>=200  8折
       >=100  9折
       不打折
非会员  >=200  9.5折
       不打折"""
m=float( input('请输入购物金额') )
a=input('有会员卡吗？如有请输入y，如没有请输入n')
if a=='y':
    if m>=200:
        print('打八折','实际付款',0.8*m,'元')
    elif m>=100 and m<200:
        print('打九折','实际付款',0.9*m,'元')
    elif m>=0 and m<100:
        print('不打折','实际付款',m,'元')
    else:
        print('非法数据')
else:
    if m>=200:
        print('打九五折','实际付款',0.95*m,'元')
    elif m>=0 and m<200:
        print('不打折','实际付款',m,'元')
    else:
        print('非法数据')
#条件表达式，结构： A + if + 条件 + else + B （A为条件为True时执行的内容，B为条件为False时执行的内容。
print('-------使用条件表达式-------')
num_a=int( input('请输入第一个整数') )
num_b=int( input('请输入第二个整数') )
print( str(num_a) + '大于等于' + str(num_b) if num_a>=num_b else str(num_a) + '小于' + str(num_b) )

#pass语句，什么都不做，只是一个占位符，用到需要写语句的地方。
if True:
    pass #没想好这里填什么时，可以用pass占位，因为这里如果什么都不填会报错。
else:
    pass #没想好这里填什么时，可以用pass占位，因为这里如果什么都不填会报错。