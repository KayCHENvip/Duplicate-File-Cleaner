import os
import PySimpleGUI as sg

def main(filepath):
    dict = {}
    for root, dirs, files in os.walk(filepath):
        for file in files:
            # 组合得到文件夹所有文件的路径
            path = os.path.join(root, file)
            f = open(path, 'rb').read()
            if f in dict:
                # 删除
                os.remove(path)
                print('删除重复文件:', path)
            else:
                dict[f] = path

# 主题设置
sg.theme('LightBrown3')

# 布局设置
layout = [
    [sg.Frame(layout=[
        [sg.InputText(key='file_path', size=(41, 1), font=("微软雅黑", 10), enable_events=True),
         sg.FolderBrowse('选择文件夹',
                       font=("微软雅黑", 12)),
         ],
    ],
        title='文件夹选择', title_color='blue', font=("微软雅黑", 10), relief=sg.RELIEF_SUNKEN, )],
    [sg.Frame(layout=[
        [sg.Output(size=(51, 10), font=("微软雅黑", 10))],
    ],
        title='信息展示', title_color='blue', font=("微软雅黑", 10), relief=sg.RELIEF_SUNKEN, )],

    [sg.Button('开始删除', font=("微软雅黑", 12)),
     sg.Text('', font=("微软雅黑", 12), size=(27, 0)), sg.Button('退出程序', font=("微软雅黑", 12), button_color='red')]
]

# 创建窗口
window = sg.Window('删除重复文件', layout, font=("微软雅黑", 12), default_element_size=(80, 1))

filepath = []

# 事件循环
while True:
    # 退出按钮
    event, values = window.read()
    if event in (None, '退出程序'):
        break
window.close()

if event == 'file_path':
    files = values['file_path']
    if os.path.exists(files):
        filepath.append(files)
    else:
        print('文件夹不存在，请重新选择！')
        sg.popup('文件夹不存在，请重新选择！')

if event == '开始删除':
    if len(filepath) != 0:
        main(filepath)
    else:
        print('文件夹路径为空，请选择文件夹！')
        sg.popup('文件夹路径为空，请选择文件夹！')
