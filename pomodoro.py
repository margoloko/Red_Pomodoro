#from tkinter import Tk, Entry, Label

from fbs_runtime.application_context.PyQT5 import ApplicationContext
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt

import sys


if __name__=='__main__':
    appctxt = ApplicationContext()
    window = QMainWindow()
    window.resize(250, 150)
    window.show()
    exit_code = appctxt.app.exec__()
    sys.exit(exit_code)


    #app = QApplication([])
    #lable = QLabel("Take a break!")

    #lable.show()

    #app.exec_()



