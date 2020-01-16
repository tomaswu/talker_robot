# -*- coding:utf-8 -*-
'''
    @Author: Tomas
    @Date: 2020-01-15 14:30:21
    @Last Modified by:   Tomas
    @Last Modified time: 2020-01-15 14:30:21
    Desc:
'''

from PySide2 import QtWidgets, QtCore, QtGui
import dialog
import numpy as np
import time
from threading import Thread
from queue import Queue
import Brain,Model

class MySingal(QtCore.QObject):
    answer = QtCore.Signal(str)

class Dialog(dialog.Ui_Form, QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.history = []
        self.listen_queue=Queue()
        self.setupUi(self)
        self.show()
        self.lineEdit.returnPressed.connect(self.listen)
        self.mysignal = MySingal()
        self.answer = self.mysignal.answer
        self.answer.connect(self.talk)

    def listen(self):
        sentence = self.lineEdit.text()
        if sentence != '':
            self.history.append([0, sentence])
            self.listen_queue.put(sentence)
            self.textBrowser.append('何又满：'+sentence+';\n')
            self.lineEdit.setText('')

    def talk(self, a):
        self.history.append([1, a])
        self.textBrowser.append('罗伯特：' + a + ';\n')

    def closeEvent(self,event):
        Model.model_save()
        event.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    ui = Dialog()
    brain=Brain.brain([ui.answer,ui.listen_queue])
    app.exec_()
