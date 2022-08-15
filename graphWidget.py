import sys
import numpy as np
from PyQt5 import QtGui
from PyQt5 import QtWidgets
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas

class MplCanvas(Canvas):
    def __init__(self):
        self.fig=Figure()
        self.ax=self.fig.add_subplot(111)
        Canvas.__init__(self,self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)


class GraphWidget(QtWidgets.QWidget):

    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.canvas=MplCanvas()
        self.vbl=QtWidgets.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
        

