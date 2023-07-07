# **Duplicate-File-Cleaner重复文件清理工具**
 **在pycharm上利用python实现重复文件的清理**  



这段代码是一个使用Python制作的删除重复文件的小工具，包括核心代码和GUI界面设计。
核心代码部分：

```
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
```

上述代码定义了一个 `main` 函数，接收一个文件夹路径作为参数。在 `main` 函数中，使用 `os.walk` 函数遍历文件夹下的所有文件，并使用一个字典 `dict` 存储读取的文件内容和路径。如果某个文件的内容已经在字典中出现过，说明该文件是重复文件，使用 `os.remove` 函数删除该文件。


GUI界面设计部分：

```
sg.theme('LightBrown3')

layout = [
    [sg.Frame(layout=[
        [sg.InputText(key='file_path', size=(41, 1), font=("微软雅黑", 10), enable_events=True),
         sg.FolderBrowse('选择文件夹', font=("微软雅黑", 12)),
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

window = sg.Window('删除重复文件', layout, font=("微软雅黑", 12), default_element_size=(80, 1))

filepath = []

while True:
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
```

上述代码使用 `PySimpleGUI` 库创建了一个简单的GUI界面。界面包括一个文件夹选择框、一个信息展示框、一个开始删除按钮和一个退出程序按钮。用户可以通过文件夹选择框选择要删除重复文件的文件夹路径，然后点击开始删除按钮进行删除操作。删除的结果和相关信息会显示在信息展示框中。
整体流程是，用户通过界面选择文件夹路径，然后点击开始删除按钮，程序调用 `main` 函数进行删除操作，并将结果显示在界面上。
这段代码需要安装 `PySimpleGUI` 库，可以使用```pip install PySimpleGUI```命令进行安装。
```
pip install PySimpleGUI
```

在使用这段代码之前，请务必备份重要的文件，以免误删数据。同时，对于不熟悉Python的人来说，建议在使用前仔细阅读代码并理解其功能，避免造成不可逆的损失。


<div>
  <img src="https://github.com/KayCHENvip/Duplicate-File-Cleaner/assets/128878325/270b4ee2-fbcb-466d-a7cb-626125f62fe7" > 
</div>


**[源代码修改于]( https://github.com/KayCHENvip/Duplicate-File-Cleaner/assets/128878325/6b478b89-ae73-4e18-9394-f8776922a9f2)**   

原始发表：2023-07-08，如觉得有侵权请联系 god.me@foxmail.com 
