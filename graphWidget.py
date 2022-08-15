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
        #hbox.addWidget(self.pw2)
        #hbox.addWidget(self.pw3)
        #self.setLayout(hbox)

        #self.setGeometry(300, 100, 800, 500)  # x, y, width, height
        #self.setWindowTitle("pyqtgraph 예제 - realtime")

        self.x = [1, 2, 3]
        self.y = [4, 5, 6]
        #self.pw1.setXRange(1, 10)
        #self.pw1.setYRange(1, 10)
        #self.pw1.enableAutoScale()
        #self.pw1.enableAutoRange()  # x,y축 모두 autorange..
        # self.pw1.enableAutoRange(axis='x', enable=True)
        # self.pw1.enableAutoRange(axis='x')
        # self.pw1.enableAutoRange(axis='y')
        # self.pw1.enableAutoRange(axis='xy')

        # self.pw2.enableAutoRange()
        self.pl = self.pw1.plot(pen='r')

        self.mytimer = QTimer()
        self.mytimer.start(1000)  # 1초마다 차트 갱신 위함...
        self.mytimer.timeout.connect(self.get_data)

        self.draw_chart(self.x, self.y)
        self.show()

    def draw_chart(self, x, y):
        self.pl.setData(x=x, y=y)  # line chart 그리기

        cnt = len(y)
        new_y = []
        for i in range(cnt):
            new_y.append(random.random()*60)  # 0 이상 ~ 60 미만 random 숫자 만들기

    @pyqtSlot()
    def get_data(self):
        # print(time.localtime())
        print(time.strftime("%H%M%S", time.localtime()))
        data: str = time.strftime("%S", time.localtime())  # 초 단위만 구함.

        last_x = self.x[-1]
        self.x.append(last_x + 1)

        self.y.append(int(data))
        self.draw_chart(self.x, self.y)

class GraphWidget(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.canvas=MplCanvas()
        self.hbox=QHBoxLayout()
        self.hbox.addWidget(self.canvas)
        self.setLayout(self.hbox)