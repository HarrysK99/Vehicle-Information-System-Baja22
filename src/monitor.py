
from pickle import decode_long
import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QPen, QPicture
from PyQt5.Qt import Qt
from PyQt5 import QtGui
import pyqtgraph
import pyqtgraph.opengl as opengl


class GPS():
    def __init__(self, latitude, longitude, altitude=0):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude

avgGPS = GPS(37.5417714, 127.07913649999999, 0)

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
    def __init__(self, lat, lon, parent, manager):
        super().__init__(parent)
        self.lat = lat
        self.lon = lon
        self.manager = manager
        self.setMouseTracking(True)
        self.parent = parent
        self.setStyleSheet('background-color:#FF0000;')
        self.setFixedSize(21, 21)

    def move_GPS(self, lat, lon ):
        point = self.manager.getClosestPointLabel(self.manager.pointWidgets, GPS(lat, lon))
        self.lat = point.lat
        self.lon = point.lon
        self.manager.moveWidget(self, self.manager.ratio, self.manager.avgGPS)
        self.raise_()
        self.move(self.x() - 8, self.y() - 8)

        self.lat = lat
        self.lon = lon
        print("[이동] 위도 : " + str(self.lat) + " 경도 : " + str(self.lon))

    def mouseMoveEvent(self, ev:QtGui.QMouseEvent) -> None:
        print("[현위치] 위도 : " + str(self.lat) + " 경도 : " + str(self.lon))

class MonitorManager():
    

    def __init__(self, parent):
        arr = json.loads(self.readJSON())
        
        self.parent = parent
        self.ratio = self.calcRatio(arr)
        self.avgGPS = self.calcAVG_GPS(arr)
        self.pointWidgets = []
        for obj in arr:
            point = PointLabel( obj['latitude'], obj['longitude'], parent)
            self.pointWidgets.append(point)
            self.moveWidget(point, self.ratio, self.avgGPS)
        self.liveCarPoint = CarPointLabel(avgGPS.latitude, avgGPS.longitude, parent, self)
        self.liveCarPoint.move_GPS(avgGPS.latitude, avgGPS.longitude)

        # returns closests point from point
    def getClosestPointLabel(self, dataArr, targetPoint):
        minIndex = 0
        minSquare = 200000.0
        for i in range(len(dataArr)):
            dlat_2 =  abs(targetPoint.latitude - float(dataArr[i].lat))
            dlon_2 =  abs(targetPoint.longitude - float(dataArr[i].lon))
            if minSquare > dlat_2 + dlon_2:
                minIndex = i
                minSquare = dlat_2 + dlon_2
                print("위도 : " + str(dataArr[minIndex].lat) + " 경도 : " + str(dataArr[minIndex].lon))
                print(str(dlat_2) + " " + str(dlon_2))  
                print(minSquare)
        return dataArr[minIndex]

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


