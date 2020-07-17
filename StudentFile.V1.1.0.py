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

def addInfo():
    while True:
        sName = input('输入学生名字：')
        if not sName:  # 判断姓名有没有输入，如果没有，重新调用当前函数
            print('名字不能为空，请重新输入')
            addInfo()
        else:  # 如果输入了，进入函数正常流程
            if not os.path.exists(stuOpenFile):  # 如果要打开的文件不存在
                Id = 0  # Id初始化为0
                Id += 1  # Id自加1
                stuNum = input('请输入学号：')
                ifEmpty(stuNum)  # 判断有没有输入学号，如果没有，调用当前函数
            elif os.path.exists(stuOpenFile) and os.path.getsize(stuOpenFile) == 0:  # 如果要打开的文件存在但是里面没有内容
                Id = 0  # 依旧初始化id为0
                Id += 1  # id自加1
                stuNum = input('请输入学号：')
                ifEmpty(stuNum)  # 判断学号有没有输入
            else:  # 如果要打开的文件存在并且里面有内容
                openFile = open(stuOpenFile, 'r+')  # 打开文件并赋值给openFile
                textLines = openFile.readlines()  # 将文件内所有内容全部赋值给textLines变量，此时textLines变量类型为列表
                for i in textLines:  # 遍历i在textLines变量内
                    textStrLines = i  # 将i循环赋值给textStrLines变量，此刻textStrLines变量为字符串
                textDictLines = eval(textStrLines)  # 跳出循环后，textStrLines变量的值是列表最后一条数据，此时将其转成字典
                textDictId = textDictLines.get('Id')  # 转成字典后将其Id取出，这个Id是文件内最后一个Id，赋值给textDictId
                Id = textDictId + 1  # 新数据的Id为textDictId+1
                stuNum = input('请输入学号：')
                ifEmpty(stuNum)  # 判断学号有没有输入
                for j in textLines:  # 如果学号有输入，开始判断是不是重复，和获取Id是一样的逻辑
                    textStrNum = j
                    textDictNum = eval(textStrNum)
                    textDictNums = textDictNum.get('stuNum')  # 唯一不一样的是，这里是循环体内每循环一次就进行一次赋值
                    if stuNum == textDictNums:  # 每赋值一次就进行一次重复判断
                        print('学生学号重复，请重新输入')
                        openFile.close()
                        addInfo()
                openFile.close()  # 关闭文件
            bj = input('输入学生班级：')
            linux = input('请输入学生Linux成绩：')
            php = input('请输入学生PHP成绩：')
            python = input('请输入学生Python成绩：')
            # 将所有用户输入的信息全部写入一个字典
            stu = {'Id': Id, 'sname': sName, 'bj': bj, 'stuNum': stuNum, 'linux': linux, 'php': php, 'python': python}
            stuInfo = str(stu)  # 将字典转为字符串
            saveInfo(stuInfo)  # 调用函数，传入转为字符串的变量，开始写入文件
        num = input('y/Y 继续       n/N 退出')
        thisFunction = addInfo
        ifTure(num,thisFunction)  # 调用函数判断用户退出或继续

def search():
    pass

def delete():
    pass

def modify():
    pass

def show():
    pass

def ifEmpty(stuNum):
    if not stuNum:
        print('学号不能为空，请重新输入')
        addInfo()

def ifTure(num, thisFunction):
    if num == 'Y' or num == 'y':
        thisFunction()
    elif num == 'n' or num == 'N':
        main()
    else:
        num = input('请输入正确选项，Y/y 继续，N/n 退出')
        ifTure(num, thisFunction)

def saveInfo(stuInfoStr):
    with open(stuOpenFile, 'a+') as f:
        f.write(stuInfoStr + '\n')
    f.close()

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