import pyqtgraph as pg

from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject, Qt, QThread, QTimer

import time, random


class MplCanvas(QWidget):
    def __init__(self):
        super().__init__()

        #hbox = QHBoxLayout()
        self.pw1 = pg.PlotWidget(title="line chart")

        #hbox.addWidget(self.pw1)
        #self.setLayout(hbox)

        self.x = [0]
        self.y = [0]
        self.pw1.enableAutoRange()  # x,y축 모두 autorange..

        self.pl = self.pw1.plot(pen='r')

        self.draw_chart(self.x, self.y)
        self.show()

    def draw_chart(self, x, y):
        self.pl.setData(x=x, y=y)  # line chart 그리기

    def addValue(self,data):
        last_x = self.x[-1]
        self.x.append(last_x + 0.125)

        self.y.append(data)
        self.draw_char(self.x,self.y)


class GraphWidget(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.canvas=MplCanvas()
        self.hbox=QHBoxLayout()
        self.hbox.addWidget(self.canvas)
        self.setLayout(self.hbox)