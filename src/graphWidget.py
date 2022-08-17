import pyqtgraph as pg

from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject, Qt, QThread, QTimer

import time, random

class GraphWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)

        hbox=QHBoxLayout()
        self.pw1=pg.PlotWidget()

        hbox.addWidget(self.pw1)
        self.setLayout(hbox)

        self.x=[0]
        self.y=[0]

        self.pw1.enableAutoRange()

        self.p1=self.pw1.plot(pen='w')
        
        self.draw_chart(self.x,self.y)
        self.show()

    def clear_plot(self):
        self.x=[0]
        self.y=[0]
        self.draw_chart(self.x,self.y)

    def draw_chart(self,x,y):
        self.p1.setData(x=x,y=y)

    def addValue(self,data):
        last_x=self.x[-1]
        self.x.append(last_x+0.125)
        self.y.append(data)
        self.draw_chart(self.x,self.y)

if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    ex=GraphWidget()
    sys.exit(app.exec_())