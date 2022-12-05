from tkinter import Tk, Entry, Label
from fbs_runtime.application_context.PyQt5 import ApplicationContext
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt


if __name__=='__main__':
    appctxt = ApplicationContext()


    app = QApplication([])
    lable = QLabel("Take a break!")

    lable.show()

    app.exec_()



