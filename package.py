# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
from os import listdir


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# 递归删除 gowan_icon gowan_splash 开头的图片文件
def deleteFileByLike(path, starsWithStr, endsWithStr=('jpg', 'png', 'jpeg', 'bmp')):
    for file_name in listdir(path):
        new_path = path + '/' + file_name
        if os.path.isdir(new_path) and file_name.startswith('drawable'):
            deleteFileByLike(new_path, starsWithStr)
        if os.path.isfile(new_path) and file_name.startswith(starsWithStr) and file_name.endswith(endsWithStr):
            os.remove(new_path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    os.system("java -jar mergeIcon/packagetool.jar mergeIcon --icon mergeIcon/gowan_icon_xyxz.png")

    # my_path = 'C:\Python Pool\Test\\'
    my_path = os.getcwd() + '/qishizhushou/res'

    print(my_path)
    deleteFileByLike(my_path, ('gowan_icon', 'gowan_splash'))
    # for file_name in listdir(my_path):
    #     print(my_path + file_name)

    # if file_name.endswith('.txt'):

    # os.remove(my_path + file_name)

    #     deleteFileByLike()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# java -jar packagetool.jar mergeIcon --icon gowan_icon_mrz.png
