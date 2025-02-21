from PyQt5 import uic
import os

def ui_to_py(name):
    uifilename = name + '.ui'
    path_ui = os.path.join(os.path.dirname(__file__),uifilename)
    fin = open(uifilename, 'r', encoding='utf-8')
    pyfilename = name + '.py'
    path_py = os.path.join(os.path.dirname(__file__),pyfilename)
    fout = open(pyfilename, 'w', encoding='utf-8')
    uic.compileUi(fin, fout)
    fin.close()
    fout.close()

ui_to_py('motor')
