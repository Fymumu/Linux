#!/usr/bin/env python3

"""
**
**      * open()函数创建文件对象
**      * 默认只读方式打开
**
"""
# f = open('./for.py')
# print(f)

"""
**
**      * open('','w')创建文件对象
**      * w，，只写方式打开
**
"""
# s = open('./test2.txt','w')
# s.write('hello')
# s.close()

"""
**
**      * open('','r+')
**      * r+，在读的基础上增加了写的功能，追加的方式写
**
"""
# s = open('./test2.txt','r+')
# print(s.read())
# s.write('world')
# s.close()

"""
**
**      * open('','w+')
**      * w+ 在写的基础上增加了读的功能
**
"""
# s = open('./test2.txt','w+')
# print(s.read())

"""
**
**      * 以下代码作业
**
"""

keyName = input('请输入学生名字：')
keyClass = input('请输入学生班级：')
keyAge = input('请输入学生年龄：')
studentInfo = {'Name':keyName,'Class':keyClass,'Age':keyAge}
studentTxt = open('./Student.txt','a+')
studentTxt.write(str(studentInfo))
studentTxt.close()