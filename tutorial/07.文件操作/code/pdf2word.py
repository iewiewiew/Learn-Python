import PySimpleGUI as sg
from pdf2docx import Converter
import re


def pdf_to_word(fileName):
    pdf_file = fileName
    name = re.findall(r'(.*?)\.', pdf_file)[0]
    docx_file = f'{name}.docx'

    # convert pdf to docx
    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()


layout = [
    [sg.Text('你选择的文件是:', font=("宋体", 10)), sg.Text('', key='text1', size=(50, 1), font=("宋体", 10))],
    [sg.Text('程序运行记录', justification='center')],
    [sg.Output(size=(70, 20), font=("宋体", 10))],
    [sg.FileBrowse('选择文件', key='folder', target='text1'), sg.Button('开始转化'), sg.Button('关闭')]
]

window = sg.Window('pdf 转 word 工具，作者@微信公众号：可以叫我才哥', layout, font=("宋体", 15), default_element_size=(50, 1))

while True:
    event, values = window.read()
    if event in (None, '关闭'):  # 如果用户关闭窗口或点击`关闭`
        break
    if event == '开始转化':
        if values['folder'] and re.findall(r'\.(\S+)', values['folder'])[0] == 'pdf':
            fileName = values['folder']
            pdf_to_word(fileName)
            print('{0}转化完毕{0}'.format('*' * 10))
        else:
            print('文件未选取或文件非 pdf 文件\n 请先选择文件')

window.close()
