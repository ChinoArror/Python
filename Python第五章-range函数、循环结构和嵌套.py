#range()函数，用于生成一个整数序列(可迭代对象)，生成的序列中，包含起始值，不包含结束值。
#range()函数的三种创建方式
print('第一种创建方式，只有一个参数')
r=range(10) #[0,1,2,3,4,5,6,7,8,9]，默认从0开始，默认相差1，称为步长，range(stop)
print(r) #range(10)
print( list(r) ) #用于查看range对象中的整数序列    --->list是列表的意思

print('第二种创建方式，给了两个参数')
r=range(1,10) #指定了起始值，从1开始，到10结束(不包括10)，默认步长为1，range(start,stop)
print( list(r) ) #[1,2,3,4,5,6,7,8,9]

print('第三种创建方式，给了三个参数')
r=range(1,10,2) #指定了start，stop和step(步长)，从1开始，到10结束，步长为2，range(start,stop,step)
print( list(r) ) #[1,3,5,7,9]

print('判断指定的整数在序列中是否存在，使用in或not in')
print(10 in r) #False，10不在当前的r这个整数序列中。
print(9 not in r) #False，9不是不在当前r这个整数序列中。

#while循环
"""四步循环法：
1.初始化变量（a=0,sum=0）
2.条件判断（while a<5）
3.条件执行体(循环体)（sum+=a )
4.改变变量（a+=1）
总结：初始化的变量 与 条件判断的变量 与 改变的变量 为同一个"""
#计算0到4之间的累加和
a=0
sum=0
while a<5:
    sum+=a
    a+=1
print(sum)
#计算0-100间的偶数和
#方法一
b=0
summ=0
while b<101:
    summ+=b
    b+=2
print('1到100间的偶数和为',summ)
#方法二
sum=0
c=0
while c<101:
    if c%2==0: #c为偶数时为True
        sum+=c
    c+=1 #改变变量，退出循环
print('1到100间的偶数和为',sum)
#方法三，拓展
sum=0
for d in range(2,101,2):
    sum+=d
print('1到100间的偶数和为',sum)

#for in循环，公式：for+ 变量 + in + 可迭代对象(字符串、序列等)
for item in 'python': #第一次取出来的是P，会重复将 可迭代对象 赋值给 变量，直到全部赋值，结束循环。
    print(item)
#range()产生一个整数序列
for i in range(10):
    print(i)
#如果在循环体中不需要使用自定义变量，可将自定义变量写为 下划线（_）。
for _ in range(5): #range的参数填几，就重复执行几遍。_用来占位，不用会出错。
    print('hello world')

print('使用for循环，计算1到100间的偶数和')
sum=0 #用于存储偶数和
for a in range(2,101,2):
    sum+=a
print('1到100间的偶数和为',sum)
#练习：计算100-999间的水仙花数(一个三位数的每一位的三次方之和等于这个数)
#方法一
suma=0
print('100到999之间的水仙花数有：')
for a in range(100,1000): #重复将100-999间的数赋值给a。
    for b in str(a): #按顺序将a的百位、十位、个位赋值给b，in后的必须为可迭代对象，即此处必须转为字符串
        suma+=int(b)**3 #将三个b值的三次方相加
    if suma==a: #判断，True即为水仙花数。
        print(suma)
    suma=0 #将suma归0，进行100-999间数的下一次循环。
#方法二
print('100到999之间的水仙花数有：')
for a in range(100,1000):
    ge=a%10      #个位，a除以10取余得出
    shi=a//10%10 #十位，a先整除10，再除以10取余得出
    bai=a//100    #百位，a整除100得出
    if ge**3+shi**3+bai**3==a: #判断
        print(a)

#break语句：用于退出一层循环
#注意：使用break退出循环是 非正常退出
"""练习1：从键盘录入密码，最多录入3次，如果正确就结束循环"""
for item in range(3):  #3次机会，计算 2-item 为剩余次数
    pwd=input('请输入密码')
    if pwd=='123456':  #注意123456应为字符串，因为input为字符串格式
        print('密码正确！')
        break #退出一层循环，退出for循环
    else: #密码错误的情况
        if item==2: #此时已经密码错误，item==2表示机会已用完，所以锁定。
            print('密码错误，程序已锁定')
        else:  #此时密码错误，但还有机会，继续for循环
            print('密码错误，剩余',2-item,'次机会')

#continue语句：用于立即结束此次循环，不执行后面的代码，直接开始下一次循环。
"""练习：要求输出1到50之间所有5的倍数,\，并使用continue语句"""
print('1到50之间5的倍数有：')
for item in range(1,51):
    if item%5!=0:
        continue
    print(item)

"""else语句：与while和for循环搭配，正常结束循环体时执行它；非正常结束循环体(包括但不限于使用break)
时，不执行else。"""
#举例：
for item in range(3):  #3次机会，计算 2-item 为剩余次数
    pwd=input('请输入密码')
    if pwd=='123456':  #注意123456应为字符串，因为input为字符串格式
        print('密码正确！')
        break #退出一层循环，退出for循环，因是非正常退出循环，不执行与for搭配的else语句。
    else: 
        print('密码错误，剩余',2-item,'次机会')#此时密码错误，但还有机会，继续for循环
else:
    print('程序已锁定') #else与for搭配，只有循环正常退出，即3次密码都输错时才执行此语句。

#嵌套循环：内层循环做为外层循环的循环体执行
"""练习：输出一个三行四列的矩形"""
for i in range(1,4): #行数，执行三次，一次是一行
    for j in range(1,5): #列数，执行四次，一次是一列
        print('*',end='\t') #打印*，end=是print()的内置参数，指在末尾应用等号后面的内容，\t是制表符，控制每个*间的间隔，也可直接引号加空格
    print() #换行

"""练习：九九乘法表"""
for i in range(1,10): #行数
    for j in range(1,i+1): #列数，循环次数和当时行数一样
        print(i,'*',j,'=',i*j,end='\t') #打印乘法表，end后的字符串中的空格是相邻算式间的间距。
    print() #换行

"""流程控制语句break与continue在二重循环中的使用"""
for i in range(5): #代表外层循环要执行5次
    for j in range(1,11): #代表内层循环执行10次
        if j%2==0:
            break #跳出内层循环
        print(j)

for i in range(5): #代表外层循环要执行5次
    for j in range(1,11):
        if j%2==0:
            continue #直接重复内层循环
        print(j,end='\t')
    print() #空括号默认转义字符为 \n 即换行