#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from __future__ import print_function
from curses import intrflush
import time
import rospy
from option_system.msg import DrivingData

import math
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

from monitor import *

#UI파일 연결
#UI파일과 py코드 파일은 같은 디렉토리에 위치
form_class = uic.loadUiType("controlTowerUi.ui")[0]

#Driver to Control Tower Communicate
class Communicate(QObject):
    signal=pyqtSignal(DrivingData)

    def run(self,data):
        self.signal.emit(data)

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):

    time = 0
    row = 0
    lap = 0
    start_time=0
    end_time=0
    delta=0
    time_table=[]

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.choose_item.activated[str].connect(self.onActivated)

        self.driver_trigger=Communicate()
        self.driver_trigger.signal.connect(self.SettingByDriver)

        self.laps_left=29
        self.current_lap=1
        self.row=0
        self.text="None"

        self.liveMonitor = MonitorManager(self)

    
    def emitSignalFromDriver(self,data):
        self.driver_trigger.run(data)

    # choose_item 항목을 선택했을 때 실행되는 콜백 함수
    def onActivated(self,text):
        self.text=text
        if (text=="Clear"):
            self.plotter.clear_plot()
            self.plotter.pw1.setTitle("")
        elif (text!="그래프 출력"):
            self.plotter.pw1.setTitle(self.text)

    @pyqtSlot(DrivingData)     
    def SettingByDriver(self, data):

        # liveMonitor 
        self.liveMonitor.liveCarPoint.move_GPS(data.latitude, data.longitude)

        # 한 lap 주행을 감지하면 주행 기록 표(laptimerlap)에 기록.
        if(data.lap!=self.current_lap):
            self.laptimerlap.setItem(self.row, 0, QTableWidgetItem(str(self.lap)))
            self.laptimerlap.setItem(self.row, 1, QTableWidgetItem(data.lap_time_prev))
            self.current_lap+=1
            self.laps_left-=1
            self.row+=1
        
        #현재 랩과 랩타임
        self.laptimerlap.setItem(self.row,0,QTableWidgetItem(str(data.lap)))
        self.laptimerlap.setItem(self.row,0,QTableWidgetItem(data.lap_time_cur))

        #현재 랩 수
        self.lap_count.setItem(0,1,QTableWidgetItem(str(self.lap)))

        #남은 랩 수
        self.laps_left.setItem(0,1,QTableWidgetItem(str(self.laps_left)))
        
        # 속도
        self.velocity_table.setItem(0, 1, QTableWidgetItem(str(data.f_car_velocity_ms)))
        self.velocity_table.setItem(1, 1, QTableWidgetItem(str(data.f_wheel_velocity_FL_ms)))
        self.velocity_table.setItem(2, 1, QTableWidgetItem(str(data.f_wheel_velocity_FR_ms)))
        self.velocity_table.setItem(3, 1, QTableWidgetItem(str(data.f_wheel_velocity_RL_ms)))
        self.velocity_table.setItem(4, 1, QTableWidgetItem(str(data.f_wheel_velocity_RR_ms)))
        
        # 토크
        self.torque_table.setItem(0, 1, QTableWidgetItem(str(data.f_motor_torque_FL_ms)))
        self.torque_table.setItem(1, 1, QTableWidgetItem(str(data.f_motor_torque_FR_ms)))
        self.torque_table.setItem(2, 1, QTableWidgetItem(str(data.f_motor_torque_RL_ms)))
        self.torque_table.setItem(3, 1, QTableWidgetItem(str(data.f_motor_torque_RR_ms)))        

        #그래프
        if      (self.text=="쓰로틀"):
            self.plotter.addValue(data.i_throttle)
        elif    (self.text=="차량 속도") :
            self.plotter.addValue(data.f_car_velocity_ms)
        elif    (self.text=="FL 속도") :
            self.plotter.addValue(data.f_wheel_velocity_FL_ms)
        elif    (self.text=="FR 속도") :
            self.plotter.addValue(data.f_wheel_velocity_FR_ms)
        elif    (self.text=="RL 속도") :
            self.plotter.addValue(data.f_wheel_velocity_RL_ms)    
        elif    (self.text=="RR 속도") :
            self.plotter.addValue(data.f_wheel_velocity_RR_ms)
        elif    (self.text=="FL 토크") :
            self.plotter.addValue(data.f_motor_torque_FL_Nm)
        elif    (self.text=="FR 토크") :
            self.plotter.addValue(data.f_motor_torque_FR_Nm)
        elif    (self.text=="RL 토크") :
            self.plotter.addValue(data.f_motor_torque_RL_Nm)
        elif    (self.text=="RR 토크") :
            self.plotter.addValue(data.f_motor_torque_RR_Nm)


def callback(data, window):
    print("callback")
    window.emitSignalFromDriver(data)

def rosmain():
    signalGenerator=Communicate()
    #QApllication: 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    rospy.init_node('control_tower', anonymous=False)
    rospy.Subscriber('driving_data', DrivingData, callback, myWindow)

    #프로그램 화면을 보여주는 코드
    myWindow.show()
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()

    rospy.spin()


if __name__ == "__main__" :
    rosmain()
