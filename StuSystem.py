# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:24:18 2022

@author: daoxiang
"""
import os
filename='student.txt'
def main():
    while True:
        menu()
        choice=int(input('请输入功能选项：'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice==0:
                answer=input('您确定要退出系统吗？y/n\n')
                if answer=='y' or answer=='Y':
                    print('谢谢您的使用！！！')
                    break #退出系统
                else:
                    continue
            elif choice==1:
                insert() #录入信息
            elif choice==2:
                search() #查找信息
            elif choice==3:
                delete() #删除信息
            elif choice==4:
                modify() #修改信息
            elif choice==5:
                sort()   #排序
            elif choice==6:
                total()  #总计
            elif choice==7:
                show()   #展示所有信息
        else:
            print('请输入正确选项：')
            continue
        
def menu():
    print('===========================学生信息管理系统=================================')
    print('-------------------------------功能菜单------------------------------------')
    print('\t\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t\t0.退出系统')
    print('--------------------------------------------------------------------------')

def insert():
    student_list=[]
    while True:
        id=input('请输入ID（如1001）:')
        if not id:
            break
        name=input('请输入姓名：')
        if not name:
            break
        
        try:
            english=int(input('请输入英语成绩：'))
            python=int(input('请输入Python成绩：'))
            java=int(input('请输入Java成绩：'))
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue
        #将录入的学生信息保存到字典当中
        student={'id':id,'name':name,'english':english,'python':python,'java':java}
        #再将学生信息添加到列表当中
        student_list.append(student)
        answer=input('是否继续录入学生信息？y/n\n')
        if answer=='y' or answer=='Y':
            continue
        else:
            break
    #调用save()函数,保存列表内容
    save(student_list)
    print('学生信息录入完毕！！！')
def save(lst): 
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt=open(filename,'w',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()
    
def search():
    student_query=[]  #定义询问列表，因为有可能出现重名
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('按ID查找请输入1，按NAME查找请输入2：')
            if mode=='1':
                id=input('请输入ID：')
            elif mode=='2':
                name=input('请输入学生姓名：')
            else:
                print('您的输入有误，请重新输入')
                search() #重新调用自己
            with open(filename,'r',encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d=dict(eval(item))
                    if id!='':
                        if d['id']==id:
                            student_query.append(d)
                    elif name !='':
                        if d['name']==name:
                            student_query.append(d)
            #显示查询结果
            show_student(student_query)
            #防止第二次查询列表中有数据，需要先清空列表
            student_query.clear()
            answer=input('是否要继续查询？y/n\n')
            if answer=='y':
                continue
            else:
                break
        else:
            print('暂未保存学生信息')
            return #结束函数
def show_student(lst):
    if len(lst)==0:
        print('未查询到学生信息，无数据显示')
        return
    #定义标题显示格式
    format_title='{:^6}\t{:^10}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'#字符串的格式化，除了format,还有占位符%
    print(format_title.format('ID','姓名','英语成绩','Python成绩','Java成绩','总成绩'))
    #定义内容的显示格式
    format_data='{:^6}\t{:^12}\t{:^4}\t{:^12}\t{:^4}\t{:^10}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english'))+int(item.get('python'))+int(item.get('java'))))
        
def delete():
    while True:
        student_id=input('请输入要删除的学生的ID：')
        if student_id!='':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file:
                    student_old=file.readlines()
            else:
                student_old=[]
            flag=False #标记是否删除
            if student_old:   #列表是对象，空列表布尔值为False,判断是否为True(即有内容)
                with open(filename,'w',encoding='utf-8') as wfile:
                    d={} #经测试，无此行代码也可正常运行
                    for item in student_old:
                        d=dict(eval(item)) #读出来的是字符串，所以需要转化为字典，eval是转化函数
                        if d['id']!=student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除') #f可将后面{}内的内容替换
                    else:
                        print(f'没有找到ID为{student_id}的学生信息')
            else:
                print('无学生信息')
                break
            show() #删完之后要重新显示所以学生信息
            answer=input('是否继续删除?y/n\n')
            if answer=='y':
                continue
            else:
                break
        else:
            print('请输入ID')
            continue
                             
def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_old=rfile.readlines()
    else:
        return
    student_id=input('请输入要修改的学生的ID：')
    with open(filename,'w',encoding='utf-8') as wfile:
        for item in student_old:
            d=dict(eval(item))
            if d['id']==student_id:
                print('找到学生，可以修改其相关信息了')
                while True:  #需要退出循环条件，在后面添加else以退出
                    try:
                        d['id']=input('请输入ID：')
                        d['name']=input('请输入姓名：')
                        d['english']=input('请输入英语成绩：')
                        d['python']=input('请输入Python成绩：')
                        d['java']=input('请输入Java成绩：')
                    except Exception:
                        print('您的输入有误，请重新输入！')
                    else:
                        break
                wfile.write(str(d)+'\n')
                print('修改成功！')
            else:
                wfile.write(str(d)+'\n')
    answer=input('是否要继续修改学生信息？y/n\n')
    if answer=='y':
        modify()
    else:
        pass          

def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_list=rfile.readlines()
        student_new=[]
        for item in student_list:
            d=dict(eval(item))
            student_new.append(d)
    else:
        return
    asc_or_desc=input('请选择输入（0.升序）或（1，降序）：')
    if asc_or_desc=='0':
        asc_or_desc_bool=False
    elif asc_or_desc=='1':
        asc_or_desc_bool=True
    else:
        print('您的输入有误，请重新输入')
        sort()
    mode=input('请选择排序方式（1.按英语成绩排序 2.按PYTHON成绩排序 3.按Java成绩排序 0.按总成绩排序）')
    if mode=='1':
        student_new.sort(key=lambda x :int(x['english']),reverse=asc_or_desc_bool)
    elif mode=='2':          #lambda是匿名函数，x为自定义的参数，表示列表student_new中的每一项，是一个字典
        student_new.sort(key=lambda x :int(x['python']),reverse=asc_or_desc_bool)
    elif mode=='3':
        student_new.sort(key=lambda x :int(x['java']),reverse=asc_or_desc_bool)
    elif mode=='0':
        student_new.sort(key=lambda x :int(x['english'])+int(x['python'])+int(x['java']),reverse=asc_or_desc_bool)
    else:
        print('您的输入有误，请重新输入')
        sort()
    show_student(student_new)

def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students=rfile.readlines()
            if students:
                print(f'一共有{len(students)}名学生')#输出需替换的{},前面＋f
            else:
                print('还没有录入学生信息')
            
    else:
        print('暂未保存学生数据信息。。。')

def show():
    student_list=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf=8') as rfile:
            students=rfile.readlines()
            for item in students:
                student_list.append(eval(item)) #eval将字符串转成相应的对象，如list,tuple,dict,string
            if student_list:
                show_student(student_list) #之前自定义的函数
    else:
        print('暂未保存过学生数据！！')
            

if __name__=='__main__':
    main()
  