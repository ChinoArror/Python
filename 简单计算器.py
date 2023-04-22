b=5
while b!=3:
    num1 = float(input("请输入第一个数："))
    op = input("请输入运算符（+ - * /）：")
    num2 = float(input("请输入第二个数："))
    result = 0
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("除数不能为零！")
            continue
        result = num1 / num2
    else:
        print("无效的运算符！")
        continue
    print("计算结果是：" + str(result))
    dic={'0':0,'1':1}
    a=input('想要继续查询？  输入0继续 ，输入1结束')
    d=dic.get(a,100)
    if d==0:
        b=5
    else: 
        b=3
print('bye')

