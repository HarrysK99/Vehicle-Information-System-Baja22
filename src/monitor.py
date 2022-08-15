from msilib.schema import Dialog
import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QPen, QPicture
from PyQt5.Qt import Qt
from PyQt5 import QtGui
import pyqtgraph
import pyqtgraph.opengl as opengl


class GPS():
    def __init__(self, latitude, longitude, altitude):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude

avgGPS = GPS(35.94669525695068, 126.59118543077346, 0)

class PointLabel(QLabel):
    def __init__(self, lat, lon, parent):
        super().__init__(parent)
        self.lat = lat
        self.lon = lon
        self.setMouseTracking(True)
        self.setStyleSheet('background-color: #000000;')
        self.setFixedSize(5, 5)
    
    def mouseMoveEvent(self, ev: QtGui.QMouseEvent) -> None:
        print("위도 : " + str(self.lat) + " 경도 : " + str(self.lon))

    
class CarPointLabel(QLabel):
    def __init__(self, lat, lon, parent):
        super().__init__(parent)
        self.lat = lat
        self.lon = lon
        self.parent = parent
        self.setStyleSheet('background-color:#FF0000;')
        self.setFixedSize(21, 21)

    def move_GPS(self, lat, lon ):
        self.lat = lat
        self.lon = lon
        self.parent.moveWidget(self, self.parent.ratio, self.parent.avgGPS)
        self.move(self.x() - 8, self.y() - 8)

class MonitorManager():
    def __init__(self, parent):
        arr = json.loads(self.readJSON())
        self.parent = parent
        self.avgGPS = self.calcAVG_GPS(arr)
        self.liveCarPoint = CarPointLabel(avgGPS.latitude, avgGPS.longitude, parent)
        self.liveCarPoint.move_GPS(avgGPS.latitude, avgGPS.longitude)
        self.ratio = self.calcRatio(arr)
        for obj in arr:
            self.moveWidget(PointLabel( obj['latitude'], obj['longitude'], parent), self.ratio, self.avgGPS)

        
    def calcRatio(self, dataArr):
        minlat = 9999.0
        maxlat = 0.0
        minlon = 9999.0
        maxlon = 0.0

        for point in dataArr:
            minlat = min(minlat, float(point['latitude']))
            maxlat = max(maxlat, float(point['latitude']))
            minlon = min(minlon, float(point['longitude']))
            maxlon = max(maxlon, float(point['longitude']))
        
        ratio = 700.0 / max(maxlat - minlat, maxlon - minlon)
        return ratio
            

    def readJSON(self):
        fd = open('./asset/mapData.json')
        while True:
            line = fd.readline()
            if not line:
                break
            return line
    
    def calcAVG_GPS(self, dataArr):
        sum_latitude = 0.0
        sum_longitude = 0.0
        for point in dataArr:
            sum_latitude = sum_latitude + float(point['latitude'])
            sum_longitude = sum_longitude + float(point['longitude'])
        sum_latitude = sum_latitude / len(dataArr)
        sum_longitude = sum_longitude / len(dataArr)
        return GPS(sum_latitude, sum_longitude, 0)
        

    def pointClickEvent(self, lat=None, lon=None):
        print("위도 : " + str(lat) + " 경도 : " + str(lon))


    
    
    def moveWidget(self, widget, ratio, avgGPS):
        x = int((float(widget.lon) - avgGPS.longitude)*ratio)
        y = int((float(widget.lat) - avgGPS.latitude)*ratio)
        
        widget.move(x + 400, 400 - y)
        widget.show()


