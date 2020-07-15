#!/usr/bin/env python3
import os
import shutil
targetDir = 'D:/test/'
sourceDir = 'F:/test/'
def copyFile(targetDir,sourceDir):
    if not os.path.exists(targetDir): # 判断目录是否存在
        os.makedirs(targetDir) # 目录不存在的时候新建目录
        shutil.copy2(sourceDir+'test.txt', targetDir+'test.txt') # 将源文件复制到目标地址
    else: # 目录存在
        if not os.path.exists(targetDir+'test.txt'): # 判断目标地址是否存在文件
            shutil.copy2(sourceDir+'test.txt', targetDir+'test.txt') # 不存在，将源文件复制到目标地址
        elif os.path.getmtime(sourceDir+'test.txt') - os.path.getmtime(targetDir+'test.txt') > 1: # 文件存在，获取两份文件的最近修改时间对比文件新旧
            shutil.copy2(sourceDir+'test.txt', targetDir+'test.txt') # 如果源文件修改时间新于目标地址文件，复制源文件到地址
        else: # 如果旧于目标地址文件，提示目标文件已是最新
            print('目标文件已是最新')

copyFile(targetDir,sourceDir)