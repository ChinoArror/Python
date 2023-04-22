#关于变量
name='hello world' #name为变量名，=是赋值符号，'hello world'是变量的值(value)
id(name) #获取变量的id
type(name) #获取变量的类型
print(name) #获取变量的值
#小练习，证明变量名和变量值、类型分开储存，变量值改变，id可回溯
#一、三行的id相同
a=1
print( id(a) , a)
a=3
print( id(a) , a)
a=1
print( id(a) , a)

#整数类型（int）
#可表示 正数、负数、和0
int1=41
int2=-73
int3=0
print( int1 , type(int1) )
print( int2 , type(int2) )
print( int3 , type(int3) )
#整数可表示为二进制、八进制、十进制、十六进制，默认十进制
print('十进制', 41)
print('二进制', 0b1001011001) #二进制以0b（零b）开头，输出自动转换为十进制数，不能空格
print('八进制', 0o5261)       #八进制以0o（零o）开头，输出自动转换为十进制数，不能空格
print('十六进制', 0x5E6A9) #十六进制以0x（零x）开头，输出自动转换为十进制数，不能空格

#浮点数类型（float）
print(1.1+2.2)
#使用导入的模块精确计算浮点数
from decimal import Decimal
from pickle import TRUE
print( Decimal('1.1') + Decimal('2.2') ) #填入的值必须为类型为字符串的小数

#布尔类型（bool）
f1=True
f2=False
print( f1 , type(f1) )
print( f2 , type(f2) )
#布尔值可以转为整数计算（True为1，False为0）
print(f1+3)
print(int(False) )

#字符串类型（str）
#使用单引号、双引号、三个单引号、三个双引号都可以表示字符串
str1='hello world' #单引号和双引号中的内容只能显示在一行
str2="hello world"
str3='''hello 
world'''             #三个单引号和三个双引号中的内容可以换行显示
str4="""hello 
world"""
print(str1 , type(str1) )
print(str2 , type(str2) )
print(str3 , type(str3) )
print(str4 , type(str4) )

#类型转换
print('str()函数')
name='张三'
age=20
print( type(name) , type(age) ) #说明name和age数据类型不相同
# 错误： print('我叫'+name+'今年'+age+'岁')   字符串不能和整数连接
print('我叫'+name+'今年'+str(age)+'岁')  #str()函数将int类型转换为str类型；此处 + 用来拼接字符串，
                                                     #使各部分间没有空格，如用逗号连接，会空一格。
print('int()函数')
s1='128'
f1=98.7
s2='76.77'
b1=True
s3='hello'
print( type(s1), type(f1), type(s2), type(b1), type(s3) )
print( int(s1), type(int(s1)) )  # int()函数可以将内容为整数的字符串、浮点类型、布尔类型转换成整数类型
print(int(f1), type(int(f1))) #只保留整数部分
print(int(b1),type(int(b1))) #True为1，False为0
#内容为小数的字符串，可以先将其转为浮点类型，再转为整数类型
b=float(s2)
print( int(b), type(int(b)) )

print('float()函数')
s1='128.98'
f1=98
s2='76'
b1=True
s3='hello'
print( type(s1), type(f1), type(s2), type(b1), type(s3) )
print( float(s1), type( float(s1) ) )
print( float(f1), type( float(f1) ) )
print( float(s2), type( float(s2) ) )
print( float(b1), type( float(b1) ) )
#print( float(s3), type( float(s3) ) ) #字符串中的数据如果是非数字串，则不允许转换
#区分：float()函数可直接将整数字符串转为浮点类型；int()函数不能直接将小数字符串转为整数类型

print('bool()函数') #可以将字符串、整数、小数转为布尔类型
s='hello'
s4=''
i=0
i1=1
f3=0.0
f4=1.25
print( type(s), type(s4), type(i), type(i1), type(f3), type(f4) )
print( bool(s), type( bool(s) ) )    #对于字符串，含有内容的字符串(只有空格的也算)为True，空字符串为False
print( bool(s4), type( bool(s4) ) )
print( bool(i), type( bool(i) ) )     #对于整数，非0整数为True，0为False
print( bool(i1), type( bool(i1) ) )
print( bool(f3), type( bool(f3) ) )   #对于小数，非等于0的小数为True，等于0的小数为False。
print( bool(f4), type( bool(f4) ) )

#关于注释
#多行注释： 使用三引号框起来，可随意换行
#中文编码声明注释：在文件第一行加上中文声明注释，用以指定源码的编码格式。示例：
#coding:gbk→ANSI格式； #coding:UTF-8→UTF-8格式