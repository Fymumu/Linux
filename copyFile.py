#!/usr/bin/env python3
import os
from shutil import copy2

def myCopy(src, dst):
    
    names = os.listdir(src) # 遍历src目录

    for name in names:
        srcName = os.path.join(src, name) # 拼接路径 源文件
        dstName = os.path.join(dst, name) # 拼接路径 目标地址
        
        if os.path.isdir(srcName): # 判断源文件拼接路径是不是一个目录
            if not os.path.exists(dstName): # 判断目标地址拼接路径目录是否存在
                os.makedirs(dstName) # 不存在，新建目录

            myCopy(srcName, dstName) # 复制源文件目录到目标地址目录
            print('复制目录成功')
        
        if os.path.isfile(srcName): # 判断是否为文件
            copy2(srcName, dstName) # 复制源文件到目标地址
            print('复制文件成功')

myCopy('tests','test')