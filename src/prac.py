import sys
from PyQt5.QtWidgets import *
import pyqtgraph as pg
import time


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # layout
        self.w = pg.PlotWidget()
        self.setCentralWidget(self.w)

        # data
        self.x1 = [1, 2, 3, 4]
        y1 = [1, 2, 3, 4]
        x2 = [1, 2, 3, 4]
        y2 = [2, 4, 8, 16]
        self.y3=[y1,y2]

        # style
        self.w.setBackground('w')
        self.w.setTitle("Title")
        self.w.setLabel("left", "y-axis")
        self.w.setLabel("bottom", "x-axis")
        self.w.addLegend()
        self.w.showGrid(x=True, y=True)
        self.w.setRange(self.x1[-1]-10,self.x1[-1]+1)

        # plot 
        self.p1=self.w.plot(x=self.x1, y=self.y3[0], pen=pg.mkPen(width=2, color='r'), name="plot1")
        self.p2=self.w.plot(x=self.x1, y=self.y3[1], pen=pg.mkPen(width=2, color='b'), name="plot2")

    def update(self):
        last_x=self.x1[-1]
        self.x1.append(last_x+1)
        self.y3[0].append(last_x+1)
        self.y3[1].append(2**last_x)
        print("===========================")
        print(self.x1)
        print(self.y3[0])
        print(self.y3[1])
        print("===========================")
        self.w.setRange(last_x-10,last_x+1)
        self.p1.setData(x=self.x1,y=self.y3[0])
        self.p2.setData(x=self.x1,y=self.y3[1])

        #     last_x=x1[-1]
        #     x1.append(last_x+1)
        #     y3[0].append(last_x+1)
        #     y3[1].append(2**last_x)
        #     w.setRange(last_x-10,last_x+1)
        #     p1.setData(x=x1,y=y3[0])
        #     p2.setData(x=x1,y=y3[1])
            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    #while(1):
    #    window.update()
    #    time.sleep(1)
    app.exec_()

