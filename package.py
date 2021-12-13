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
path_library_platform_plugin = rootPath + 'library_platform_plugin/'
suffix_res_drawable = '/src/main/res/drawable/'
file_icon_name = ''


# 递归删除 gowan_icon gowan_splash 开头的图片文件
def deleteFileByLike(path, starsWithStr, endsWithStr=('jpg', 'png', 'jpeg', 'bmp')):
    if not os.path.exists(path):
        print('不存在路径：' + path)
        return
    for file_name in listdir(path):
        new_path = path + '/' + file_name
        if os.path.isdir(new_path) and file_name.startswith('drawable'):
            deleteFileByLike(new_path, starsWithStr)
        if os.path.isfile(new_path) and file_name.startswith(starsWithStr) and file_name.endswith(endsWithStr):
            os.remove(new_path)


# 将加工后的icon复制到对应的渠道资源目录下
def copyIcon2ChannelModule(channel):
    channelPath = checkPath(channel)
    if channelPath == "":
        return
    # 渠道有角标 则在compile目录中存在加工后的图标，若没有角标则复制直接复制不加工的游戏图标
    if os.path.exists(path_icon_compile + channel + '.png'):
        shutil.copy(path_icon_compile + channel + '.png', channelPath + 'gowan_icon.png')
    else:
        shutil.copy(path_icon_mergeIcon + file_icon_name, channelPath + 'gowan_icon.png')


# 检测channel.txt 中填写的渠道是否正确: 若渠道模块不存在则返回空，若存在渠道模块再判断是否含有资源目录
def checkPath(channel):
    channelPath = path_library_platform_plugin + channel + suffix_res_drawable
    if not os.path.exists(channelPath):
        if os.path.exists(path_library_platform_plugin + channel):
            os.makedirs(channelPath)
        else:
            return ""

    return channelPath


# 将加工后的splash复制到对应的渠道资源目录下
def copySplash2ChannelModule(channel):
    channelPath = checkPath(channel)
    if channelPath == "":
        return

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


def findIconFileName(gameName):
    for file_name in listdir(path_icon_mergeIcon):
        if gameName in file_name and os.path.isfile(path_icon_mergeIcon + file_name):
            return file_name

    return ''


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # print('参数个数为:', len(sys.argv), '个参数。')
    # print('参数列表:', str(sys.argv))
    # if not len(sys.argv) > 1:
    #     print("请输入游戏参数")
    #     exit(1)
    # gameName = sys.argv[1]
    gameName = 'mrz'
    iconFileName = findIconFileName(gameName)
    file_icon_name = iconFileName
    if iconFileName == '':
        print('参数错误，找不到对应图标')
        exit(0)

    # print(sys.argv[1])
    # icon 处理
    os.system("java -jar mergeIcon/packagetool.jar mergeIcon --icon mergeIcon/%s" % iconFileName)
    # splash 处理

    # my_path = 'C:\Python Pool\Test\\'
    # f = open("channel.txt", "r")  # 设置文件对象
    channel = []
    for line in open("channel.txt", "r"):
        channel.append(line.rstrip())
        my_path = path_library_platform_plugin + line.rstrip() + suffix_res_drawable
        # print(my_path)
        deleteFileByLike(my_path, ('gowan_icon', 'gowan_splash'))
        copyIcon2ChannelModule(line.rstrip())
        copySplash2ChannelModule(line.rstrip())

    print(path_icon_compile)
    print('---------------------------')

    # copyIcon2ChannelModule('57k')
    # copyIcon2ChannelModule('qishizhushou')
    # copyIcon2ChannelModule('leidian')
    # copySplash2ChannelModule('57k')
    # copySplash2ChannelModule('qishizhushou')
    # copySplash2ChannelModule('leidian')
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
