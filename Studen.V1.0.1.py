#!/usr/bin/env python3
"""
**      * 学生成绩管理系统
**      * 录入功能
**      * 查询功能
**      * 删除功能
**      * 修改功能
**      * 显示所有
**      * 数据字段：学生姓名，学生班级，学生所学课程
**      * id自增长
**      * stu1 = {'id':1,'sname':'tom','class':1,'linux':100}
"""

"""
**      * 修复了一些已知bug
**      * 添加新功能
**      * 增加学生学号，学号唯一且不可重复
"""

Id = 0
stu_info = []

def menu():
    print("""
    |----------学生管理系统---------|
    
    |===========主功能菜单==========|
    |                               |
    |    1，录入学生成绩            |
    |    2，查询学生成绩            |
    |    3，删除学生成绩            |
    |    4，修改学生成绩            |
    |    5，显示所有成绩            |
    |    6，退出系统                |
    |                               |
    |===============================|
    """)

"""
**
**      * 函数名：addIonfo
**      * 功能：添加学生信息
**
"""
def addInfo():
    while True:
        sname = input('输入学生姓名：')
        global Id
        if not sname: # 判断名字是否为空，如果空，调用当前函数
            print('名字不能为空，请重新输入')
            addInfo()
        else:
            stuNum = input('输入学生学号：')
            stuNumList = [stu_info[i].get('stuNum') for i in range(len(stu_info))]
            if stuNum in stuNumList: # 判断学号是否重复
                print('学号存在，请重新输入')
                num = input('Y/y，继续  N/n，退出：')
                thisFunction = addInfo
                ifTrue(num,thisFunction)
            else:
                bj = input('输入学生班级：')
                linux = input('输入学生linux成绩：')
                php = input('输入学生php成绩：')
                python = input('输入学生python成绩：')
                Id += 1
            stu = {'Id':Id,'sname':sname,'bj':bj,'stuNum':stuNum,'linux':linux,'php':php,'python':python} # 将所有字段存入一个字典
            stu_info.append(stu) # 将字典添加到列表
        num = input('Y/y，继续  N/n，退出：')
        thisFunction = addInfo
        ifTrue(num,thisFunction)

"""
**
**      * 函数名：search
**      * 功能：查询单个指定名字的学生成绩信息
**
"""
def search():
    format_title = '{:^6}{:^12}\t{:^10}{:^10}{:^10}{:^10}{:^10}'
    format_data  = '{:^6}{:^14}\t{:^10}{:^16}{:^4}{:^18}{:^6}'
    sname = input('输入查询的学生姓名：')
    print(format_title.format('ID','姓名','班级','linux成绩','php成绩','python成绩'))
    # 循环获得stu_info列表内所有字典的姓名字段，并将其全部复制到name_list列表里
    name_list = [stu_info[i].get('sname') for i in range(len(stu_info))] 
    if sname in name_list: # 查看输入的姓名是否存在于name_list列表里
        for i in stu_info: # 存在的情况下，循环获取该名字所在字典所有信息
            if sname == i.get('sname'):
                Id = i.get('Id')
                sname = i.get('sname')
                bj = i.get('bj')
                stuNum = i.get('stuNum')
                linux = i.get('linux')
                php = i.get('php')
                python = i.get('python')
                print(format_data.format(Id,sname,bj,stuNum,linux,php,python)) # 将所有信息全部打印输出
    else: # 不存在的情况下，打印信息不存在
        print("学生信息不存在")
    num = input('Y/y，继续  N/n，退出：')
    thisFunction = search
    ifTrue(num,thisFunction)

"""
**
**      * 函数名：delete
**      * 功能：删除指定单个学生
**
"""
def delete():
    global Id
    sname = input('请输入学生姓名：')
    sStuNum = input('请输入学生学号')
    for i in stu_info: # 遍历stu_info里的所有信息赋值给i
        if i['sname'] == sname: # 判断用户输入的姓名是否存在于i里 如果存在，判断学号是否存在
            if i['stuNum'] == sStuNum: # 学号存在，将该id赋值
                Id = i.get('Id')
                stu_info.remove(i) # 删除该字段
                print('删除成功')
                for a in stu_info: # 遍历stu_info里的所有信息赋值给a
                    if a['Id'] > Id: # 判断a里所有的id，有没有大于被删除id，如果有，该大于被删除id的id自减1
                        Ids = a.get('Id') - 1
                        a['Id'] = Ids
    Id_list = [stu_info[i].get('Id') for i in range(len(stu_info))] # 遍历整个列表所有字典的Id字段赋值给Id_list
    if not Id_list: # 判断Id_list是否为空，如果为空，Id字段赋值为0，并返回菜单页
        Id = 0
        print('学生信息已全部清空，返回菜单页面')
        main()
    num = input('Y/y，继续  N/n，退出：')
    thisFunction = delete
    ifTrue(num, thisFunction)

"""
**
**      * 函数名：modify
**      * 功能：修改指定学生的成绩，不允许修改id，姓名，班级
**
"""
def modify():
    sname = input('请输入学生名字：')
    global stu_info
    for i in stu_info:
        if i['sname'] == sname:
            Id = i.get('Id')
            stuId = Id - 1 # 列表的下标从零开始，获取该字段Id，与该字段所在字典的下标差1
            sname = i.get('sname')
            bj = i.get('bj')
            stuNum = i.get('stuNum')
            newLinux = input('请输入学生linux成绩：')
            newPHP = input('请输入学生php成绩：')
            newPython = input('请输入学生python成绩：')
            # 将获取到的用户输入的新成绩全部赋值到新的字典
            newStudent = {"id":Id,"sname":sname,"bj":bj,'stuNum':stuNum,'linux':newLinux,'php':newPHP,'python':newPython}
            stu_info[stuId].update(newStudent) # 将新字典更新到列表同位置下标下
    num = input('Y/y，继续  N/n，退出：')
    thisFunction = modify
    ifTrue(num, thisFunction)

"""
**
**      * 函数名：show
**      * 功能：查询全部学生成绩信息
**
"""
def show():
    format_title = '{:^6}{:^12}\t{:^10}{:^10}{:^10}{:^10}{:^10}'
    format_data  = '{:^6}{:^14}\t{:^10}{:^16}{:^4}{:^18}{:^6}'
    print(format_title.format('ID','姓名','班级','学号','linux成绩','php成绩','python成绩'))
    for i in stu_info: # 遍历所有学生信息
        Id = i.get('Id')
        sname = i.get('sname')
        bj = i.get('bj')
        stuNum = i.get('stuNum')
        linux = i.get('linux')
        php = i.get('php')
        python = i.get('python')
        # 遍历所有信息并格式化打印输出
        print(format_data.format(Id,sname,bj,stuNum,linux,php,python))

"""
**
**      * 函数名：ifTrue
**      * 功能：判断用户是否继续在当前被调用函数里操作
**      * 该函数可以被任何功能函数调用，调用时，传入参数
**      * num参数，获取用户输入的选项
**      * thisFunction参数，获取调用ifTrue函数的函数
**
"""
def ifTrue(num,thisFunction):
    if num == "Y" or num == "y":
        thisFunction() # thisFunction作为参数传参，传参前已赋值了当前调用ifTrue函数的函数名
    elif num == "N" or num == "n":
        main()
    else:
        num = input('请输入正确选项  Y/y,继续  N/n,退出:')
        ifTrue(num,thisFunction) # 如果用户输入非继续或退出指令，则提示重新输入，并调用ifTrue

"""
**
**      * 函数名：main
**      * 功能：主函数，判断用户输入的数字，并调用相关功能
**
"""
def main():
    while True:
        menu()
        numExit = input('请选择菜单选项：')
        if numExit == "1":
            addInfo()
        elif numExit == "2":
            search()
        elif numExit == "3":
            delete()
        elif numExit == "4":
            modify()
        elif numExit == "5":
            show()
        elif numExit == "6":
            exit()
        else:
            print('请输入正确选项')

main()