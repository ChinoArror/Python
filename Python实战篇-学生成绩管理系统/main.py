import os
import time

filename='student.txt' #文件名

def main(): #定义主程序函数
    while True:
        menu() #显示菜单
        try:
            choise=int(input('请选择：'))
            if choise in [0,1,2,3,4,5,6,7]: #检测输入是否在范围内
                if choise==0: 
                    answer=input('您确定要退出系统吗?y/n：')
                    if answer=='y' or answer=='Y':
                        print('谢谢您的使用！')
                        break #退出循环，结束程序
                    else:
                        continue #重新执行循环
                elif choise==1:
                    insert() #录入学生系统
                elif choise==2:
                    search() #查找
                elif choise==3:
                    delete() #删除
                elif choise==4:
                    modify() #编辑学生信息
                elif choise==5:
                    student_sort() #排序
                elif choise==6:
                    total() #计算学生数量
                elif choise==7:
                    show() #显示
        except:
            print('请重新输入')
            continue


                

def menu():
    print('\t=====================学生信息管理系统=====================')
    print('\t--------------------------功能菜单------------------------')
    print('\t\t\t1.录入学生信息')
    print('\t\t\t2.查找学生信息')
    print('\t\t\t3.删除学生信息')
    print('\t\t\t4.修改学生信息')
    print('\t\t\t5.排序')
    print('\t\t\t6.统计学生总人数')
    print('\t\t\t7.显示所有学生信息')
    print('\t\t\t0.退出系统')
    print('--------------------------------------------------------------------------')

def insert():
    student_lst=[] #定义列表
    while True:
        id=input('请输入学生的ID(如1001)：') 
        if not id: #空值的布尔值为False，如果id值为空，not id为True，将会退出循环
            break
        name=input('请输入姓名：')
        if not name: #检测姓名是否为空
            print('输入无效，请重新输入')
            continue
        gender1=input('请输入学生的性别，1-男，2-女：')
        if gender1=='1': #gender1使用字符串格式，不使用整数类型，防止输入字母导致报错
            gender='Male'
        elif gender1=='2':
            gender='Female'
        else:
            print('输入无效，请重新输入')
            continue

        try: #运行try下的代码，如正常，即输入的均为数字，则继续，如输入其他字符，会报错，执行except下的内容
            age=int(input('请输入学生的年龄：'))
            english=float(input('请输入英语成绩：'))
            python=float(input('请输入Python成绩：'))
            java=float(input('请输入Java成绩：'))
        except:
            print('输入无效，请重新输入')
            continue
        #将录入学生的信息保存到字典
        student={'id':id,'name':name,'age':age,'gender':gender,'english':english,'python':python,'java':java}
        #将学生信息添加到列表
        student_lst.append(student)
        answer=input('是否继续添加?y/n：')
        if answer=='y' or answer== 'Y':
            continue
        elif answer=='n' or answer=='N':
            break
    #调用save()，存储学生信息
    save(student_lst)
    print('学生信息录入完毕')

def save(lst):
    try: #打开文件，如还没有创建文件，则执行except，创建新文件
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt=open(filename,'w',encoding='utf-8')
    for item in lst: #遍历列表中的学生信息，分行存储到文件中，\n表示换行
        stu_txt.write(str(item)+'\n')
    stu_txt.close() #关闭文件

def search():
    student_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename): #检测文件是否存在
            mode=input('按ID查找请输1，按姓名查找请输2：')
            if mode=='1':
                id=input('请输入学生ID：')
            elif mode=='2':
                name=input('请输入学生姓名：')
            else:
                print('输入有误，请重新输入')
                search() #此处相当于continue，重新执行此函数
            with open(filename,'r',encoding='utf-8') as rfile:
                student=rfile.readlines() #将文件信息存到列表中
                for item in student: #遍历列表的内容
                    dic=dict(eval(item)) #存入字典中
                    if id!='': #条件为id不为空，即选择了使用id查询
                        if dic['id']==id: #匹配对应的id，并输出学生信息到新列表
                            student_query.append(dic)
                    elif name!='': #条件为name不为空，即选择了使用name查询
                        if dic['name']==name: #匹配对应name
                            student_query.append(dic)
                    else: #如果id、name均为空，即没有输入查询信息
                        print('请重新输入')
                        continue #重新执行函数
                if not student_query: #遍历完后，判断新列表是否为空
                    print('查无此人，请重新输入') #如为空，即遍历时没有找到对应学生信息
                    continue
            #显示查询结果
            show_student(student_query) #调用后面定义的show_student()函数
            student_query.clear() #清空新列表
            answer=input('是否要继续查询?y/n：')
            if answer=='y' or answer=='Y':
                continue
            else:
                time.sleep(0.09) #等待0.09秒，防止报错
                return    
        else:
            print('暂未保存数据信息')
            break

def delete():
    while True:
        student_id=input('请输入要删除学生的ID：')
        if student_id!='': #检测是否输入学生id
            if os.path.exists(filename): #检测文件是否存在
                with open(filename,'r',encoding='utf-8') as file: #打开文件
                    student_old=file.readlines() #将学生信息存入列表
            else:
                student_old=[] #若文件不存在，则设置为空列表
            flag=False #标记是否删除
            if student_old: 
                with open(filename,'w',encoding='utf-8') as wfile:
                    dic={}
                    for item in student_old:
                        dic=dict(eval(item)) #将字符串转成字典
                        if dic['id']!=student_id: #若学生id不等于要删除的学生id，则将他写回原文件中
                            wfile.write(str(dic)+'\n') #将不需要删除的学生写回原文件，相当于删除了目标学生
                        else:
                            flag=True #表示已找到目标学生并删除
                    if flag:
                        print(f'ID为{student_id}的学生信息已被删除')
                    else:
                        print(f'没有找到ID为{student_id}的学生信息')
            else:
                print('无学生信息')
                break
            show() #删除之后要重新展示学生信息
        answer=input('是否继续删除?y/n：')
        if answer=='y' or answer=='Y':
            continue
        else:
            break

def modify():
    show() #先展示所有学生信息
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_old=rfile.readlines()
    else:
        student_old=[]
    student_id=input('请输入要修改的学生ID：')
    if student_old: #检测是否有学生信息
        with open(filename,'w',encoding='utf-8') as wfile:
            for item in student_old: #遍历学生信息，将其存入字典中
                dic=dict(eval(item))
                if dic['id']==student_id:
                    print('找到学生信息，可以修改了') #当目标id和学生id相等时，找到目标学生
                    while True:
                        name=input('请输入姓名：')
                        if not name:
                            print('输入无效，请重新输入')
                            continue
                        gender1=int(input('请输入性别，1-男，2-女：'))
                        if gender1==1:
                            dic['gender']='Male' #将字典性别一项修改为新
                        elif gender1==2:
                            dic['gender']='Female'
                        else:
                            print('输入无效，请重新输入')
                            continue

                        try:
                            dic['age']=int(input('请输入年龄：')) #修改字典年龄一项
                            dic['english']=float(input('请输入英语成绩：'))
                            dic['python']=float(input('请输入Python成绩：'))
                            dic['java']=float(input('请输入Java成绩：'))
                        except:
                            print('输入有误，请重新输入')
                        else: #执行完try或except后，执行else项
                            break
                    wfile.write(str(dic)+'\n') #将修改后的字典写入文件
                    print('修改成功')
                else:
                    wfile.write(str(dic)+'\n') #若不是目标学生，则执行此项，直接写回文件
    else:
        print('无学生信息')
    answer=input('是否继续修改学生信息?y/n：')
    if answer=='y' or answer=='Y':
        modify() #重新执行此函数
    else:
        return #退出此函数

def student_sort():
    show() #展示学生信息
    if os.path.exists(filename): #判断文件是否存在
        with open(filename,'r',encoding='utf-8') as rfile: #打开文件
            student_lst=rfile.readlines() #读取全部数据
        student_new=[]
        for item in student_lst: #遍历学生信息并加入新函数
            dic=dict((eval(item)))
            student_new.append(dic)
    else:
        print('暂未保存数据信息')
        return #直接结束此函数
    while True: #循环，可以反复排序
        asc_or_desc=input('请选择(0-升序；1-降序)：') #询问排序模式
        if asc_or_desc=='0':
            asc_or_desc_bool=False #.sort()给参数reverse=False代表升序，=True代表降序
        elif asc_or_desc=='1':
            asc_or_desc_bool=True
        else:
            print('输入有误，请重新输入')
            student_sort() #重新执行此函数
        mode=input('请选择排序方式(1-按年龄排序；2-按英语成绩排序；3-按Python成绩排序；4-按Java成绩排序；0-按总成绩排序)：')
        if mode=='1':  #.sort()给参数reverse=False代表升序，=True代表降序
            student_new.sort(key=lambda x: float(x['age']),reverse=asc_or_desc_bool)
        elif mode=='2':
            student_new.sort(key=lambda x: float(x['english']),reverse=asc_or_desc_bool)
        elif mode=='3':
            student_new.sort(key=lambda x: float(x['python']),reverse=asc_or_desc_bool)
        elif mode=='4':
            student_new.sort(key=lambda x: float(x['java']),reverse=asc_or_desc_bool)
        elif mode=='0':
            student_new.sort(key=lambda x: float(x['english'])+float(x['python'])+float(x['java']),reverse=asc_or_desc_bool)
        else:
            print('输入有误，请重新输入')
            student_sort()
        show_student(student_new) #调用后面定义的show_student()函数
        answer=input('是否继续排序?y/n：')
        if answer=='y' or answer=='Y':
            continue
        else:
            break

def total():
    if os.path.exists(filename): #判断文件是否存在
        with open(filename,'r',encoding='utf-8') as rfile: #只读打开文件
            students=rfile.readlines()  #读取全部内容
            if students:
                print('一共有{}名学生'.format(len(students)))
            else:
                print('无学生信息')
    else:
        print('暂未保存数据信息')

def show():
    student_lst=[]
    if os.path.exists(filename): #判断文件是否存在
        with open(filename,'r',encoding='utf-8') as rfile: #打开文件
            students=rfile.readlines() #读取全部数据
        for item in students: #遍历学生信息并写入新列表
            student_lst.append(eval(item))
        if student_lst: #判断新列表是否为空
            show_student(student_lst)#调用后面定义的show_student()函数
        else:
            print('无学生信息')
    else:
        print('暂未保存数据信息')

def show_student(lst):
    if len(lst)==0: #判断列表长度，len()
        print('无学生信息')
        return
    #定义标题显示格式
    format_title='{:^6}\t{:^10}\t{:^7}\t{:^6}\t{:^7}\t{:^10}\t{:^11}\t{:^8}'
    print(format_title.format('ID','姓名','年龄','性别','英语成绩','Python成绩','Java成绩','总成绩'))
    #定义内容显示格式
    format_data='{:^6}\t{:^11}\t{:^9}\t{:^8}\t{:^10}\t{:^10}\t{:^11}\t{:^11}'
    for item in lst: #遍历列表内容并分行显示学生信息，.get()用来获取字典中对应键的值
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('age'),
                                 item.get('gender'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 float(item.get('english'))+float(item.get('python'))+float(item.get('java'))))


if __name__=='__main__':
    main() #执行主程序函数
