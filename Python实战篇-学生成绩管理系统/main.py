import os

filename='student.txt'

def main():
    while True:
        menu()
        try:
            choise=int(input('请选择：'))
            if choise in [0,1,2,3,4,5,6,7]:
                if choise==0:
                    answer=input('您确定要退出系统吗?y/n：')
                    if answer=='y' or answer=='Y':
                        print('谢谢您的使用！')
                        break
                    else:
                        continue
                elif choise==1:
                    insert() #录入学生系统
                elif choise==2:
                    search() #查找
                elif choise==3:
                    delete() #删除
                elif choise==4:
                    modify() 
                elif choise==5:
                    sort()
                elif choise==6:
                    total()
                elif choise==7:
                    show()
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
    student_lst=[]
    while True:
        id=input('请输入学生的ID(如1001)：')
        if not id:
            break
        name=input('请输入姓名：')
        if not name:
            break

        try:
            english=float(input('请输入英语成绩：'))
            python=float(input('请输入Python成绩：'))
            java=float(input('请输入Java成绩：'))
        except:
            print('输入无效，请重新输入')
            continue
        #将录入学生的信息保存到字典
        student={'id':id,'name':name,'english':english,'python':python,'java':java}
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
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt=open(filename,'w',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()

def search():
    student_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('按ID查找请输1，按姓名查找请输2：')
            if mode=='1':
                id=input('请输入学生ID：')
            elif mode=='2':
                name=input('请输入学生姓名：')
            else:
                print('输入有误，请重新输入')
                search()
            with open(filename,'r',encoding='utf-8') as rfile:
                student=rfile.readlines()
                for item in student:
                    dic=dict(eval(item))
                    if id!='':
                        if dic['id']==id:
                            student_query.append(dic)
                    elif name!='':
                        if dic['name']==name:
                            student_query.append(dic)
                    else:
                        print('请重新输入')
                        continue
                if not student_query:
                    print('查无此人，请重新输入')
                    continue
            #显示查询结果
            show_student(student_query)
            student_query.clear()
            answer=input('是否要继续查询?y/n：')
            if answer=='y' or answer=='Y':
                continue
            else:
                break    
        else:
            print('暂未保存数据信息')
            break

def delete():
    while True:
        student_id=input('请输入要删除学生的ID：')
        if student_id!='':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file:
                    student_old=file.readlines()
            else:
                student_old=[]
            flag=False #标记是否删除
            if student_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    dic={}
                    for item in student_old:
                        dic=dict(eval(item)) #将字符串转成字典
                        if dic['id']!=student_id:
                            wfile.write(str(dic)+'\n')
                        else:
                            flag=True
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
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_old=rfile.readlines()
    else:
        student_old=[]
    student_id=input('请输入要修改的学生ID：')
    if student_old:
        with open(filename,'w',encoding='utf-8') as wfile:
            for item in student_old:
                dic=dict(eval(item))
                if dic['id']==student_id:
                    print('找到学生信息，可以修改了')
                    while True:
                        try:
                            dic['name']=input('请输入姓名：')
                            dic['english']=float(input('请输入英语成绩：'))
                            dic['python']=float(input('请输入Python成绩：'))
                            dic['java']=float(input('请输入Java成绩：'))
                        except:
                            print('输入有误，请重新输入')
                        else:
                            break
                    wfile.write(str(dic)+'\n')
                    print('修改成功')
                else:
                    wfile.write(str(dic)+'\n')
    else:
        print('无学生信息')
    answer=input('是否继续修改学生信息?y/n：')
    if answer=='y' or answer=='Y':
        modify()
    else:
        return

def sort():
    show()
    if os.path.exists(filename): #判断文件是否存在
        with open(filename,'r',encoding='utf-8') as rfile: #打开文件
            student_lst=rfile.readlines() #读取全部数据
        student_new=[]
        for item in student_lst:
            dic=dict((eval(item)))
            student_new.append(dic)
    else:
        print('暂未保存数据信息')
        return
    asc_or_desc=input('请选择(0-升序；1-降序)：')
    if asc_or_desc=='0':
        asc_or_desc_bool=False
    elif asc_or_desc=='1':
        asc_or_desc_bool=True
    else:
        print('输入有误，请重新输入')
        sort()
    mode=input('请选择排序方式(1-按英语成绩排序；2-按Python成绩排序；3-按Java成绩排序；0-按总成绩排序)：')
    if mode=='1':
        student_new.sort(key=lambda x: float(x['english']),reverse=asc_or_desc_bool)
    elif mode=='2':
        student_new.sort(key=lambda x: float(x['python']),reverse=asc_or_desc_bool)
    elif mode=='3':
        student_new.sort(key=lambda x: float(x['java']),reverse=asc_or_desc_bool)
    elif mode=='0':
        student_new.sort(key=lambda x: float(x['english'])+float(x['python'])+float(x['java']),reverse=asc_or_desc_bool)
    else:
        print('输入有误，请重新输入')
        sort()
    show_student(student_new)

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
        for item in students:
            student_lst.append(eval(item))
        if student_lst:
            show_student(student_lst)
        else:
            print('无学生信息')
    else:
        print('暂未保存数据信息')

def show_student(lst):
    if len(lst)==0:
        print('无学生信息')
        return
    #定义标题显示格式
    format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID','姓名','英语成绩','Python成绩','Java成绩','总成绩'))
    #定义内容显示格式
    format_data='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 float(item.get('english'))+float(item.get('python'))+float(item.get('java'))))


if __name__=='__main__':
    main()
