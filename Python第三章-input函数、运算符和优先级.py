#input()函数
    #用于接收用户输入
    #返回值为str
    #使用 = 赋值变量存储

#Python中的运算符

#算术运算符
print(2*3)
print(10/5) #除法，结果自动转换为浮点类型
print(5//2) # 两个除号，整除运算，只保留结果的整数部分，余数省略。
print(5%2) #结果为1，取余运算，只保留结果的余数部分，整数舍去。
print(2**3) #表示2的3次方，两个乘号，幂运算。

print(9//-4) #结果：-3  被除数和除数一正一负时，整除结果向下取整。
print(-9//4) #结果：-3

print(9%-4) #结果：-3  一正一负时取余，要遵循公式：余数=被除数-除数*商 ； 9-(-4)*(-3)=-3
print(-9%4) #结果：3 ；-9-4*(-3)=3  ; 注意商要用整除得出的商，即一正一负向下取整。

#赋值运算符，运算顺序从右到左
i=7
print(i)
#链式赋值
a=b=c=20
print( a, id(a) ) #链式赋值的三个变量id相同，即都指向同一个对象。
print( b, id(b) )
print( c, id(c) )
#参数赋值
a=20
a+=30 #相当于a=a+30
print(a)
a-=10 #相当于a=a-10
print(a)
a*=2 #相当于a=a*2
print(a)
a/=4 #相当于a=a/4，除法结果自动转换为浮点类型
print( a, type(a) )
a//=2#相当于a=a//2，整除的被除数和除数中只要有一个是浮点类型，结果就为浮点类型，反之则为整数类型。
print( a, type(a) )
a%=4#相当于a=a%5，取余的被除数和除数中只要有一个是浮点类型，结果就为浮点类型，反之则为整数类型。
print( a, type(a) )
#系列解包赋值
a,b,c=20,30,40
print(a,b,c)
#a,b=10,20,30 报错，因为左右变量的个数和值的个数不匹配。
print('交换两个变量的值')
a,b=10,20
print('交换之前', a, b)
a,b=b,a #交换，无需引入中间变量
print('交换之后', a, b)

#比较运算符，结果为布尔类型
"""一个=称为赋值运算符，两个=称为比较运算符
    两个=比较的是变量的值。id 用 is 来比较。"""
a=10
b=10
print(a==b)  #True 说明a、b的值相等
print(a is b) #True 说明a、b的id相等
print(a is not b) #False 说明a、b的id不是不相等的。

#布尔运算符，and\or\not\in\not in
a,b=1,2
print(a==1 and b==2) #True ；and两边都为True，结果True；只要有一个False，结果False。

print(a==1 or b==4) #True ; or两边只要有一个True，结果True；两边都为False，结果False。

print(not a==1) #False ；not后为True，结果False；后为False，结果True。

# in和not in能且仅能用来判断字符串的包含情况，注意区分大小写。
s='hello world'
print('w' in s) #True ；在'hello world'中包含'w'。
print('h' not in s) #False ；在'hello world'中不是不包含'h'。

#位运算符，将输入的十进制数转为二进制，八位上下对齐，对应或移位，得出结果再转十进制。
print(4&8) #按位与 & ，对应数位都是1，结果数位才为1，否则为0。
print(4|8) #按位或 | ，同为0时结果为0，否则为1。
print(4<<1) #左移位 << ，向左移动1位，相当于乘2，结果为8
print(4<<2) #向左移动2位，相当于 *2*2，结果为16。
print(4>>1) #右移位 >> ，向右移动1位，相当于除以2，结果为2
print(4>>2) #向右移动2位，相当于除以4，结果为1。

#运算符的优先级
# ()>算术运算符>位运算符>比较运算符>布尔运算符>赋值运算符