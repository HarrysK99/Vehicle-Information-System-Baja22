#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from __future__ import print_function
from curses import intrflush
import time
import rospy
from std_msgs.msg import String, Float32	
from sensor_msgs.msg import Imu
from custom_msg2_pkg.msg import CarSignal, CarState, CarControlSignal

import math
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

#UI파일 연결
#UI파일과 py코드 파일은 같은 디렉토리에 위치
form_class = uic.loadUiType("CTui_proto.ui")[0]

class Communicate(QObject):
    signal1=pyqtSignal(CarSignal)

    def run(self,data):
        print("A")
        print(data.controlSignal.brake)
        self.signal1.emit(data)

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

        self.signal=Communicate()
        self.signal.signal1.connect(self.points_topic_callback)
        #self.signal.run(10)

        #테이블위젯에 데이터 입력
        self.insert_data()

        #타이머 관련
        self.start_time=time.time()
        self.end_time=self.start_time
        self.delta=self.end_time-self.start_time
        self.timerVar = QTimer()
        self.timerVar.setInterval(1000)
        self.timerVar.timeout.connect(self.insert_data)
        self.timerVar.start()

        #랩수와 랩타임
        self.laptimeperlap.setRowCount(100)
        self.laptimeperlap.setColumnCount(2)

        #랩수와 랩당 배터리 사용량
        self.batteryperlap.setRowCount(100)
        self.batteryperlap.setColumnCount(2)


    def insert_data(self):
        self.time += 1
        self.end_time=time.time()
        self.delta = self.end_time - self.start_time
        self.time_table.append(int(int(self.delta)/60))
        self.time_table.append(int(int(self.delta)%60))
        self.time_table.append(int((self.delta-int(self.delta))*100))

        #velocity_table(속도표)
        # for i in range(0,6):
        #     self.velocity_table.setItem(i, 1, QTableWidgetItem(str(self.time) + str("km/h")))
        #     self.velocity_table.item(i, 1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        #     i += 1

        # #current_table(전류표)
        # for j in range(0,5):
        #     self.current_table.setItem(j, 1, QTableWidgetItem(str(self.time) + str("A")))
        #     self.current_table.item(j, 1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        #     j += 1   

        #transit_time_table(총 주행시간, 남은 주행시간)
        self.transit_time_table.setItem(0, 1, QTableWidgetItem(str(self.time//3600) + str(":") + str((self.time//60) - (self.time//3600) * 60) + str(":") + str(self.time - (self.time//60) * 60)))
        self.transit_time_table.item(0, 1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.transit_time_table.setItem(1, 1, QTableWidgetItem(str((5400 - self.time)//3600) + str(":") + str(((5400 - self.time)//60) - ((5400 - self.time)//3600) * 60) + str(":") + str((5400 - self.time) - ((5400 - self.time)//60) * 60)))
        self.transit_time_table.item(1, 1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        #recom_vel_lap(추천속도, 랩 수)
        self.recom_vel_lap.setItem(0, 1, QTableWidgetItem(str(self.time) + str("km/h")))
        self.recom_vel_lap.item(0, 1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.recom_vel_lap.setItem(1, 1, QTableWidgetItem(str(self.time//10)))
        self.recom_vel_lap.item(1, 1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        #battery_table(배터리 누적 사용량, 잔량)
        self.battery_table.setItem(0, 1, QTableWidgetItem(str(self.time//10) + str("%")))
        self.battery_table.item(0, 1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.battery_table.setItem(1, 1, QTableWidgetItem(str(100 - (self.time//10)) + str("%")))
        self.battery_table.item(1, 1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        # #distance_table(총 주행거리, 예상 주행거리, 도착점까지 남은 거리)
        # self.distance_table.setItem(0, 1, QTableWidgetItem(str(self.time//5) + str("km")))
        # self.distance_table.item(0, 1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # self.distance_table.setItem(1, 1, QTableWidgetItem(str(1080 - (self.time//5)) + str("km")))
        # self.distance_table.item(1, 1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # self.distance_table.setItem(2, 1, QTableWidgetItem(str(((2 * ((self.time + 5)//10)) - (self.time//5))) + str("km")))
        # self.distance_table.item(2, 1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        #laptimeperlap(랩 수와 랩타임), batteryperlap(랩 수와 랩당 배터리 사용량)
        if(self.time%10 == 0):
            self.lap += 1
            self.laptimeperlap.setItem(self.row, 0, QTableWidgetItem(str(self.lap)))
            self.batteryperlap.setItem(self.row, 0, QTableWidgetItem(str(self.lap)))
            self.laptimeperlap.setItem(self.row, 1, QTableWidgetItem(str(self.time_table[0])+":"+str(self.time_table[1])+":"+str(self.time_table[2])))
            self.batteryperlap.setItem(self.row, 1, QTableWidgetItem(str((self.time//10)//self.lap)))
            self.laptimeperlap.item(self.row, 0).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.laptimeperlap.item(self.row, 1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.batteryperlap.item(self.row, 0).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.batteryperlap.item(self.row, 1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.row += 1
        
        self.time_table.clear()
    
    def emitSignal(self,data):
        self.signal.run(data)

    @pyqtSlot(CarSignal)     
    def points_topic_callback(self, data):
        # 속도
        print("Yes!")
        
        self.velocity_table.setItem(0, 1, QTableWidgetItem(str(data.state.f_car_velocity_ms)))
        self.velocity_table.setItem(2, 1, QTableWidgetItem(str(data.state.f_wheel_velocity_FL_ms)))
        self.velocity_table.setItem(3, 1, QTableWidgetItem(str(data.state.f_wheel_velocity_FR_ms)))
        self.velocity_table.setItem(4, 1, QTableWidgetItem(str(data.state.f_wheel_velocity_RL_ms)))
        self.velocity_table.setItem(5, 1, QTableWidgetItem(str(data.state.f_wheel_velocity_RR_ms)))
        
        # #모터 토크지만 전류표에
        self.current_table.setItem(1, 1, QTableWidgetItem(str(data.state.f_motor_torque_FL_ms)))
        self.current_table.setItem(2, 1, QTableWidgetItem(str(data.state.f_motor_torque_FR_ms)))
        self.current_table.setItem(3, 1, QTableWidgetItem(str(data.state.f_motor_torque_RL_ms)))
        self.current_table.setItem(4, 1, QTableWidgetItem(str(data.state.f_motor_torque_RR_ms)))
        
        # # 주행거리 표에 브레이크, 스티어링, 가속
        self.distance_table.setItem(0, 1, QTableWidgetItem(str(data.controlSignal.brake)))
        self.velocity_table.setItem(2, 1, QTableWidgetItem(str(data.state.f_wheel_velocity_FL_ms)))
        self.velocity_table.setItem(3, 1, QTableWidgetItem(str(data.state.f_wheel_velocity_FR_ms)))
        self.velocity_table.setItem(4, 1, QTableWidgetItem(str(data.state.f_wheel_velocity_RL_ms)))
        self.velocity_table.setItem(5, 1, QTableWidgetItem(str(data.state.f_wheel_velocity_RR_ms)))
        
        # #모터 토크지만 전류표에
        #self.current_table.setItem(1, 1, QTableWidgetItem(str(data.state.f_motor_torque_FL_ms)))
        #self.current_table.setItem(2, 1, QTableWidgetItem(str(data.state.f_motor_torque_FR_ms)))
        #self.current_table.setItem(3, 1, QTableWidgetItem(str(data.state.f_motor_torque_RL_ms)))
        #self.current_table.setItem(4, 1, QTableWidgetItem(str(data.state.f_motor_torque_RR_ms)))
        
        # # 주행거리 표에 브레이크, 스티어링, 가속
        #self.distance_table.setItem(0, 1, QTableWidgetItem(str(data.controlSignal.brake)))
        #self.distance_table.setItem(1, 1, QTableWidgetItem(str(data.controlSignal.steering)))
        #self.distance_table.setItem(2, 1, QTableWidgetItem(str(data.controlSignal.acceleration)))
        #self.distance_table.setItem(1, 1, QTableWidgetItem(str(data.controlSignal.steering)))
        #self.distance_table.setItem(2, 1, QTableWidgetItem(str(data.controlSignal.acceleration)))


def callback(data, window):
    print("callback")
    #temp=float(str(data.controlSignal.brake))
    #WindowClass.emitSignal(temp)
    window.emitSignal(data)

def rosmain():
    signalGenerator=Communicate()
    #QApllication: 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    rospy.init_node('ui_node', anonymous=False)
    rospy.Subscriber('signals', CarSignal, callback, myWindow)

    #프로그램 화면을 보여주는 코드
    myWindow.show()
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()

    rospy.spin()


if __name__ == "__main__" :
    rosmain()
