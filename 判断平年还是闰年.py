#判断闰年还是平年
"""4年一闰，百年不闰，400年再闰"""
t=0
while t!=1:
    y=int( input('请输入要判断的年份') )
    if y%4==0 and y%100==0:
        if y%400==0:
            print(y,'年','是闰年')
        else:
            print(y,'年','是平年')
    elif y%4==0 and y%100!=0:
        print(y,'年','是闰年')
    elif y%4!=0:
        print(y,'年','是平年')
    else:
        print('数据不合法')
    t=int( input('想要继续查询吗？输入0继续，输入1结束。'))
