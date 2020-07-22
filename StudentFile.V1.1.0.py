#!/usr/bin/env python3
import os

stuOpenFile = 'StudentFile.txt'


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
# 添加功能
# * 添加学生姓名，学号，班级，成绩
#! 姓名和学号不能为空
#! 学号不能重复
#! 以追加写入的方式写入文件
"""


def addInfo():
    while True:
        sName = input('输入学生名字：')
        if not sName:  # *判断姓名有没有输入，如果没有，重新调用当前函数
            print('名字不能为空，请重新输入')
            addInfo()
        else:  # *如果输入了，进入函数正常流程
            if not os.path.exists(stuOpenFile):  # !如果要打开的文件不存在
                Id = 0  # !Id初始化为0
                Id += 1  # !Id自加1
                stuNum = input('请输入学号：')
                ifEmpty(stuNum)  # *判断有没有输入学号，如果没有，调用当前函数
            # !如果要打开的文件存在但是里面没有内容
            elif os.path.exists(stuOpenFile) and os.path.getsize(stuOpenFile) == 0:
                Id = 0  # !依旧初始化id为0
                Id += 1  # !id自加1
                stuNum = input('请输入学号：')
                ifEmpty(stuNum)  # *判断学号有没有输入
            else:  # *如果要打开的文件存在并且里面有内容
                openFile = open(stuOpenFile, 'r+')  # !打开文件并赋值给openFile
                textLines = openFile.readlines()  # !将文件内所有内容全部赋值给textLines变量，此时textLines变量类型为列表
                for i in textLines:  # !遍历i在textLines变量内
                    textStrLines = i  # !将i循环赋值给textStrLines变量，此刻textStrLines变量为字符串
                # !跳出循环后，textStrLines变量的值是列表最后一条数据，此时将其转成字典
                textDictLines = eval(textStrLines)
                # !转成字典后将其Id取出，这个Id是文件内最后一个Id，赋值给textDictId
                textDictId = textDictLines.get('Id')
                Id = textDictId + 1  # !新数据的Id为textDictId+1
                stuNum = input('请输入学号：')
                ifEmpty(stuNum)  # *判断学号有没有输入
                for j in textLines:  # !如果学号有输入，开始判断是不是重复，和获取Id是一样的逻辑
                    textStrNum = j
                    textDictNum = eval(textStrNum)
                    # !唯一不一样的是，这里是循环体内每循环一次就进行一次赋值
                    textDictNums = textDictNum.get('stuNum')
                    if stuNum == textDictNums:  # !每赋值一次就进行一次重复判断
                        print('学生学号重复，请重新输入')
                        openFile.close()
                        addInfo()
                openFile.close()  # !关闭文件
            bj = input('输入学生班级：')
            linux = input('请输入学生Linux成绩：')
            php = input('请输入学生PHP成绩：')
            python = input('请输入学生Python成绩：')
            # !将所有用户输入的信息全部写入一个字典
            stu = {'Id': Id, 'sname': sName, 'bj': bj, 'stuNum': stuNum,
                   'linux': linux, 'php': php, 'python': python}
            stuInfo = str(stu)  # !将字典转为字符串
            saveInfo(stuInfo)  # !调用函数，传入转为字符串的变量，开始写入文件
        num = input('y/Y 继续       n/N 退出：')
        thisFunction = addInfo
        ifTure(num, thisFunction)  # *调用函数判断用户退出或继续


"""
# 查询单个学生信息
# * 为了避免同名，以学号查询
#! 输入学号，学号不能为空
#! 将文件内容以列表形式复制
#! 循环这个列表，每次循环赋值出来成为一个字符串
#! 将字符串转为字典，取字典stuNum键值对，对比学号和值是否相等
#! 如果相等，打印这个字典里所有值
#! 如果相等，继续循环，如果全部不
"""


def search():
    format_title = '{:^6}{:^12}\t{:^10}{:^10}{:^10}{:^10}{:^10}'
    format_data = '{:^6}{:^14}\t{:^10}{:^16}{:^4}{:^18}{:^6}'
    if not os.path.exists(stuOpenFile):  # *如果没有要打开的文件，提示文件没有
        print('没有这个文件')
    elif os.path.exists(stuOpenFile) and os.path.getsize(stuOpenFile) == 0:  # *如果文件为空，提示信息没有
        print('学生信息为空')
    else:
        stuName = input('请输入学生姓名：')
        if not stuName:  # *如果用户没有输入名字
            print('学生姓名不能为空，请重新输入')
            search()
        else:  # *用户输入了
            openFile = open(stuOpenFile, 'r+')  # *打开文件
            stuInfo = openFile.readlines()  # *遍历文件信息到一个变量
            stuNum = input('请输入学生学号：')
            if not stuNum:  # *如果用户没有输入学号
                print('学号不能为空，请重新输入')
                search()
            else:  # *用户输入了学号
                for i in stuInfo:
                    stuStrInfo = i
                    stuDictInfo = eval(stuStrInfo)
                    if stuName != stuDictInfo.get('sname') or stuNum != stuDictInfo.get('stuNum'):
                        continue  # !同时判断学号和名字在不在，如果有一个不在，就继续循环
                    # !如果同时都存在，开始获取学生信息
                    elif stuName == stuDictInfo.get('sname') and stuNum == stuDictInfo.get('stuNum'):
                        print(format_title.format('ID', '姓名', '班级', '学号',
                                                  'linux成绩', 'php成绩', 'python成绩'))  # !格式化打印信息头
                        stuId = stuDictInfo.get('Id')  # *获取学生id
                        stuName = stuDictInfo.get('sname')  # *获取学生姓名
                        stuBj = stuDictInfo.get('bj')  # *获取学生班级
                        stuNum = stuDictInfo.get('stuNum')  # *获取学生学号
                        stuLinux = stuDictInfo.get('linux')  # *获取学生linux成绩
                        stuPHP = stuDictInfo.get('php')  # *获取学生php成绩
                        stuPython = stuDictInfo.get('python')  # *获取学生python成绩
                        print(format_data.format(stuId, stuName, stuBj,
                                                 stuNum, stuLinux, stuPHP, stuPython))  # !格式化打印信息
                        num = input('y/Y 继续       n/N 退出：')
                        thisFunction = search
                        ifTure(num, thisFunction)  # *调用函数判断用户退出或继续
                print('学生信息不存在，请重新输入')  # !如果学生姓名和学号均不在文件里，输出学生信息不存在，请重新输入
                search()


"""
# 删除功能
# * 为了方便删除和删除时对同名判断正确，先输出所有信息，使用姓名和学号检测的方式删除
#! 获取用户输入姓名和学号，每一个都要进行判空
#! 主要逻辑点是对文件的操作，这一点具体写在了代码里
"""


def delete():
    show()  # !展示所有信息，方便删除
    openFile = open(stuOpenFile, 'r+')
    textLines = openFile.readlines()
    openFile.close()
    stuName = input('请输入学生姓名：')  # !姓名是一定要输入的
    if not stuName:
        print('姓名不能为空，请重新输入')
        delete()
    else:
        stuNum = input('请输入学生学号：')  # !为了防止重名，需要验证学号
        if not stuNum:
            print('学号不能为空，请重新输入')
            delete()
        else:
            for i in textLines:
                stuStrLines = i
                stuDictInfo = eval(stuStrLines)
                # !如果名字和学号有一个对不上号，就继续循环
                if stuName != stuDictInfo.get('sname') or stuNum != stuDictInfo.get('stuNum'):
                    continue
                # !如果名字和学号都对得上，就将其赋值到一个变量
                elif stuName == stuDictInfo.get('sname') and stuNum == stuDictInfo.get('stuNum'):
                    stuDel = stuDictInfo
                    # ! 当名字和学号对得上，已经将要修改的字典提取出来时，以覆盖写入方式打开文件
                    openFile = open(stuOpenFile, 'w')
                    openFile.write('')  # ! 清空文件
                    openFile.close()  # ! 关闭文件
                    for i in textLines:
                        openFile = open(stuOpenFile, 'a+')  # * 以追加写入的方式打开文件
                        stuList = i  # ! 循环将旧信息列表字符串写入一个变量，准备写入文件
                        stuDict = eval(stuList)  # ! 将字符串转为字典
                        # !如果被提取出来的字典和准备写入文件的信息一致，一致的那条信息不写入文件，继续循环
                        if stuDict == stuDel:
                            continue
                        else:  # ! 如果信息不一致，进入写入文件环节
                            # !判断准备写入文件的信息里有没有id大于被提取出来的信息的id
                            if stuDict.get('Id') > stuDel.get('Id'):
                                # *如果有，这个Id减一并赋值给新的变量
                                Id = stuDict.get('Id') - 1
                                sname = stuDict.get('sname')
                                bj = stuDict.get('bj')
                                stuNum = stuDict.get('stuNum')
                                linux = stuDict.get('linux')
                                php = stuDict.get('linux')
                                python = stuDict.get('python')
                                # *将新的id和旧内容重新写入一个字典
                                newStuDict = {'Id': Id, 'sname': sname, 'bj': bj,
                                              'stuNum': stuNum, 'linux': linux, 'php': php, 'python': python}
                                print('删除成功')
                                newStuStr = str(newStuDict)  # *字典转为字符串，写入文件
                                openFile.write(newStuStr + '\n')
                                openFile.close()
                            else:  # ! 如果id不大于被提取出来的id，直接转为字符串后写入文件
                                stuStr = str(stuDict)
                                openFile.write(stuStr + '\n')
            if stuName != stuDictInfo.get('sname') and stuNum != stuDictInfo.get('stuNum'):
                print('学生信息不存在，请重新输入')
                delete()
        num = input('y/Y 继续       n/N 退出：')
        thisFunction = modify
        ifTure(num, thisFunction)  # *调用函数判断用户退出或继续


"""
# 修改功能
# * 通过学号方式修改，避免同名，为修改方便，显示所有信息
#! 对学号进行判空
#! 对学号进行判断是否存在于从文件提取出来的信息，存在，开始修改，不存在，继续循环，循环结束依旧没有，提示信息不存在
#! 修改后，要对文件进行清空，接着再把信息列表转字符串后逐条遍历写入
"""


def modify():
    show()
    openFile = open(stuOpenFile, 'r+')
    textLines = openFile.readlines()  # 将文件所有内容以列表写入一个变量
    openFile.close()  # !这里关闭一下打开的文件，方便之后操作
    stuNum = input('请输入学号：')  # *为了避免重名，使用学号进行修改
    if not stuNum:
        print('学号不能为空，请重新输入')
        modify()
    else:
        for i in textLines:
            stuList = i
            stuDict = eval(stuList)
            if stuNum == stuDict['stuNum']:  # !如果存在输入的学号在已有信息里，开始修改
                stuId = stuDict['Id']
                stuName = stuDict['sname']
                stuBj = stuDict['bj']
                stuLinux = input('请输入学生Linux成绩：')
                if not stuLinux:  # *如果用户没有输入新的成绩，将继续使用旧成绩
                    stuLinux = stuDict['linux']
                stuPHP = input('请输入学生PHP成绩：')
                if not stuPHP:
                    stuPHP = stuDict['php']
                stuPython = input('请输入学生python成绩：')
                if not stuPython:
                    stuPython = stuDict['python']
                stuDicts = {'Id': stuId, 'sname': stuName, 'bj': stuBj, 'stuNum': stuNum,
                            'linux': stuLinux, 'php': stuPHP, 'python': stuPython}
                openFile = open(stuOpenFile, 'w')  # !已覆盖写入的方式打开文件
                openFile.write('')  # !将文件内容请客
                openFile.close()  # !关闭文件
                for i in textLines:
                    openFile = open(stuOpenFile, 'a+')  # !将文件已追加写入的方式打开
                    stuList = i
                    stuDict = eval(stuList)
                    if stuNum != stuDict.get('stuNum'):  # !如果stuNum不等于
                        stuStr = str(stuDict)  # !将当前整个追加入文件
                        openFile.write(stuStr + '\n')
                    else:  # !如果等于了
                        stuStr = str(stuDicts)  # !将修改好的追加写入，替换了原有的
                        openFile.write(stuStr + '\n')
            elif stuNum != stuDict['stuNum']:  # !如果不存在，继续循环
                continue
            else:  # !如果都不存在，返回信息不存在，调用当前函数
                print('学号信息不存在，请重新输入')
                modify()
        openFile.close()
        num = input('y/Y 继续       n/N 退出：')
        thisFunction = modify
        ifTure(num, thisFunction)  # *调用函数判断用户退出或继续


"""
# 查看所有信息功能
# * 打开文件后，将信息全部以列表写入一个遍历
# * 遍历这个列表，每次遍历将字符串赋值给变量，变量转为字符串，将字符串键值对的值打印输出
"""


def show():
    format_title = '{:^6}{:^12}\t{:^10}{:^10}{:^10}{:^10}{:^10}'  # 格式化信息
    format_data = '{:^6}{:^14}\t{:^10}{:^16}{:^4}{:^18}{:^6}'
    if not os.path.exists(stuOpenFile):  # *如果文件不存在，提示文件不存在
        print('文件不存在')
        main()
    # *如果文件没有内容，提示没有学生信息
    elif os.path.exists(stuOpenFile) and os.path.getsize(stuOpenFile) == 0:
        print('当前没有学生信息')
        main()
    else:
        print(format_title.format('ID', '姓名', '班级',
                                  '学号', 'linux成绩', 'php成绩', 'python成绩'))
        openFile = open(stuOpenFile, 'r+')  # !文件以读的方式打开
        stuTextLines = openFile.readlines()  # !读取全部以列表赋值给一个变量
        for i in stuTextLines:  # *遍历这个列表
            stuStrLines = i  # *将遍历出来的字符串给到一个遍历
            stuDictLines = eval(stuStrLines)  # ! 将字符串转为字典给到一个变量
            # !将该变量里键的值单独赋值给到每个对应键名的变量
            stuId = stuDictLines.get('Id')
            stuNams = stuDictLines.get('sname')
            stuBj = stuDictLines.get('bj')
            stuNum = stuDictLines.get('stuNum')
            stuLinux = stuDictLines.get('linux')
            stuPHP = stuDictLines.get('php')
            stuPython = stuDictLines.get('python')
            # *输出信息，然后继续循环
            print(format_data.format(stuId, stuNams, stuBj,
                                     stuNum, stuLinux, stuPHP, stuPython))
        openFile.close()  # 循环结束，关闭文件


"""
# * 添加功能的调用函数，用于判断学号是否为空
"""


def ifEmpty(stuNum):
    if not stuNum:
        print('学号不能为空，请重新输入')
        addInfo()


"""
# 判断用户是否退出
# * num参数：获取用户的选择
# * thisFunction参数：用于获取调用ifTure的函数名
"""


def ifTure(num, thisFunction):
    if num == 'Y' or num == 'y':  # ! 如果获取选择是Y或者y，调用thisFunction参数赋值的函数
        thisFunction()
    elif num == 'N' or num == 'n':  # ! 如果获取选择是N或者n，调用main寒素
        main()
    else:  # ! 如果获取的都不是这四个选项，提示请重新选择同时调用ifTure函数
        num = input('请输入正确选项，Y/y 继续，N/n 退出：')
        ifTure(num, thisFunction)


def saveInfo(stuInfoStr):  # !将信息写入文件的操作
    with open(stuOpenFile, 'a+') as f:  # !以a+的访问模式打开文件
        f.write(stuInfoStr + '\n')  # !将传入的字符串已追加的方式写入文件并且换行
    f.close()  # !关闭文件


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
