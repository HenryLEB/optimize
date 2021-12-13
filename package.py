# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys
from os import listdir
import shutil

rootPath = os.getcwd() + '/'
path_icon_compile = rootPath + 'mergeIcon/icon_compile/'
path_icon_mergeIcon = rootPath + 'mergeIcon/'
path_channel_module = rootPath
path_splash = rootPath + 'mergeIcon/splash/'
file_icon_name = 'gowan_icon_xyxz.png'


# 递归删除 gowan_icon gowan_splash 开头的图片文件
def deleteFileByLike(path, starsWithStr, endsWithStr=('jpg', 'png', 'jpeg', 'bmp')):
    for file_name in listdir(path):
        new_path = path + '/' + file_name
        if os.path.isdir(new_path) and file_name.startswith('drawable'):
            deleteFileByLike(new_path, starsWithStr)
        if os.path.isfile(new_path) and file_name.startswith(starsWithStr) and file_name.endswith(endsWithStr):
            os.remove(new_path)


def copyIcon2ChannelModule(channel):
    channelPath = rootPath + channel + '/' + 'res/' + 'drawable/'  # 需要改
    if not os.path.exists(channelPath):
        os.makedirs(channelPath)

    if os.path.exists(path_icon_compile + 'gowan_icon_xyxz_' + channel + '.png'):
        shutil.copy(path_icon_compile + 'gowan_icon_xyxz_' + channel + '.png', channelPath + 'gowan_icon.png')
    else:
        shutil.copy(path_icon_mergeIcon + file_icon_name, channelPath + 'gowan_icon.png')


def copySplash2ChannelModule(channel):
    channelPath = rootPath + channel + '/' + 'res/' + 'drawable/'  # 需要改
    if not os.path.exists(channelPath):
        os.makedirs(channelPath)

    path_file_jpg = path_splash + channel + '.jpg'
    path_file_png = path_splash + channel + '.png'
    if os.path.exists(path_file_jpg):
        shutil.copy(path_file_jpg, channelPath + 'gowan_splash.jpg')
    elif os.path.exists(path_file_png):
        shutil.copy(path_file_png, channelPath + 'gowan_splash.png')

    # for file_name in listdir(path_icon_compile):
    #     if channel in file_name:
    #         path_from = path_icon_compile + file_name
    #         path_destination = channelPath + 'gowan_icon' + os.path.splitext(file_name)[-1]
    #         if not os.path.exists(channelPath):
    #             os.makedirs(channelPath)
    #         shutil.copy(path_icon_compile + file_name, path_destination)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print('参数个数为:', len(sys.argv), '个参数。')
    print('参数列表:', str(sys.argv))

    # icon 处理
    os.system("java -jar mergeIcon/packagetool.jar mergeIcon --icon mergeIcon/gowan_icon_xyxz.png")
    # splash 处理

    # my_path = 'C:\Python Pool\Test\\'
    # f = open("channel.txt", "r")  # 设置文件对象
    channel = []
    for line in open("channel.txt", "r"):
        channel.append(line.rstrip())
        my_path = rootPath + '/' + line.rstrip() + '/res'
        deleteFileByLike(my_path, ('gowan_icon', 'gowan_splash'))

    print(path_icon_compile)
    print('---------------------------')

    copyIcon2ChannelModule('57k')
    copyIcon2ChannelModule('qishizhushou')
    copySplash2ChannelModule('57k')
    copySplash2ChannelModule('qishizhushou')
    copySplash2ChannelModule('leidian')
    # f.close()  # 关闭文件
    # my_path = os.getcwd() + '/qishizhushou/res'

    # print(my_path)
    # deleteFileByLike(my_path, ('gowan_icon', 'gowan_splash'))
    # for file_name in listdir(my_path):
    #     print(my_path + file_name)

    # if file_name.endswith('.txt'):

    # os.remove(my_path + file_name)

    #     deleteFileByLike()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# java -jar packagetool.jar mergeIcon --icon gowan_icon_mrz.png
