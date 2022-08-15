# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CTui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1600, 900)
        #self.live_monitor = Monitor(Dialog)
        #self.live_monitor.setGeometry(QtCore.QRect(0, 0, 800, 900))
        #self.live_monitor.setObjectName("live_monitor")
        self.plotter = GraphWidget(Dialog)
        self.plotter.setGeometry(QtCore.QRect(810, 0, 771, 441))
        self.plotter.setObjectName("plotter")
        self.laps_left = QtWidgets.QTableWidget(Dialog)
        self.laps_left.setGeometry(QtCore.QRect(1230, 550, 351, 61))
        self.laps_left.setMaximumSize(QtCore.QSize(530, 61))
        self.laps_left.setStyleSheet("")
        self.laps_left.setObjectName("laps_left")
        self.laps_left.setColumnCount(2)
        self.laps_left.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.laps_left.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.laps_left.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.laps_left.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.laps_left.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.laps_left.setItem(0, 1, item)
        self.laps_left.horizontalHeader().setVisible(False)
        self.laps_left.horizontalHeader().setDefaultSectionSize(170)
        self.laps_left.verticalHeader().setVisible(False)
        self.laps_left.verticalHeader().setDefaultSectionSize(58)
        self.laps_left.verticalHeader().setHighlightSections(True)
        self.total_time = QtWidgets.QTableWidget(Dialog)
        self.total_time.setGeometry(QtCore.QRect(1230, 480, 351, 61))
        self.total_time.setMaximumSize(QtCore.QSize(530, 61))
        self.total_time.setStyleSheet("")
        self.total_time.setObjectName("total_time")
        self.total_time.setColumnCount(2)
        self.total_time.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.total_time.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.total_time.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.total_time.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.total_time.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.total_time.setItem(0, 1, item)
        self.total_time.horizontalHeader().setVisible(False)
        self.total_time.horizontalHeader().setDefaultSectionSize(170)
        self.total_time.verticalHeader().setVisible(False)
        self.total_time.verticalHeader().setDefaultSectionSize(58)
        self.total_time.verticalHeader().setHighlightSections(True)
        self.choose_item = QtWidgets.QComboBox(Dialog)
        self.choose_item.setGeometry(QtCore.QRect(1480, 450, 101, 25))
        self.choose_item.setEditable(False)
        self.choose_item.setObjectName("choose_item")
        self.choose_item.addItem("")
        self.choose_item.addItem("")
        self.choose_item.addItem("")
        self.choose_item.addItem("")
        self.choose_item.addItem("")
        self.choose_item.addItem("")
        self.choose_item.addItem("")
        self.choose_item.addItem("")
        self.choose_item.activated[str].connect(self.onchanged)
        self.velocity_table = QtWidgets.QTableWidget(Dialog)
        self.velocity_table.setGeometry(QtCore.QRect(810, 450, 411, 191))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.velocity_table.setFont(font)
        self.velocity_table.setShowGrid(True)
        self.velocity_table.setObjectName("velocity_table")
        self.velocity_table.setColumnCount(2)
        self.velocity_table.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.velocity_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.velocity_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.velocity_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.velocity_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.velocity_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.velocity_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.velocity_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.velocity_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.velocity_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.velocity_table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.velocity_table.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.velocity_table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.velocity_table.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.velocity_table.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.velocity_table.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.velocity_table.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.velocity_table.setItem(4, 1, item)
        self.velocity_table.horizontalHeader().setVisible(False)
        self.velocity_table.horizontalHeader().setCascadingSectionResizes(True)
        self.velocity_table.horizontalHeader().setDefaultSectionSize(200)
        self.velocity_table.verticalHeader().setVisible(False)
        self.velocity_table.verticalHeader().setCascadingSectionResizes(True)
        self.velocity_table.verticalHeader().setDefaultSectionSize(36)
        self.lap_count = QtWidgets.QTableWidget(Dialog)
        self.lap_count.setGeometry(QtCore.QRect(1230, 620, 351, 61))
        self.lap_count.setMaximumSize(QtCore.QSize(530, 61))
        self.lap_count.setStyleSheet("")
        self.lap_count.setObjectName("lap_count")
        self.lap_count.setColumnCount(2)
        self.lap_count.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.lap_count.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lap_count.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lap_count.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.lap_count.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.lap_count.setItem(0, 1, item)
        self.lap_count.horizontalHeader().setVisible(False)
        self.lap_count.horizontalHeader().setDefaultSectionSize(170)
        self.lap_count.verticalHeader().setVisible(False)
        self.lap_count.verticalHeader().setDefaultSectionSize(58)
        self.lap_count.verticalHeader().setHighlightSections(True)
        self.torque_table = QtWidgets.QTableWidget(Dialog)
        self.torque_table.setGeometry(QtCore.QRect(1230, 700, 351, 151))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.torque_table.setFont(font)
        self.torque_table.setObjectName("torque_table")
        self.torque_table.setColumnCount(2)
        self.torque_table.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.torque_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.torque_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.torque_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.torque_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.torque_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.torque_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.torque_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.torque_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.torque_table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.torque_table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.torque_table.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.torque_table.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.torque_table.setItem(3, 1, item)
        self.torque_table.horizontalHeader().setVisible(False)
        self.torque_table.horizontalHeader().setDefaultSectionSize(170)
        self.torque_table.verticalHeader().setVisible(False)
        self.torque_table.verticalHeader().setDefaultSectionSize(37)
        self.laptimeperlap = QtWidgets.QTableWidget(Dialog)
        self.laptimeperlap.setGeometry(QtCore.QRect(810, 650, 401, 231))
        self.laptimeperlap.setObjectName("laptimeperlap")
        self.laptimeperlap.setColumnCount(2)
        self.laptimeperlap.setRowCount(11)
        item = QtWidgets.QTableWidgetItem()
        self.laptimeperlap.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.laptimeperlap.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.laptimeperlap.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.laptimeperlap.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.laptimeperlap.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.laptimeperlap.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.laptimeperlap.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.laptimeperlap.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.laptimeperlap.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.laptimeperlap.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.laptimeperlap.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.laptimeperlap.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.laptimeperlap.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.laptimeperlap.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.laptimeperlap.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.laptimeperlap.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.laptimeperlap.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.laptimeperlap.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.laptimeperlap.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.laptimeperlap.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.laptimeperlap.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.laptimeperlap.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.laptimeperlap.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.laptimeperlap.setItem(10, 0, item)
        self.laptimeperlap.horizontalHeader().setDefaultSectionSize(180)
        self.laptimeperlap.verticalHeader().setVisible(False)
        self.laptimeperlap.verticalHeader().setDefaultSectionSize(30)
        self.laptimeperlap.verticalHeader().setHighlightSections(False)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def onchanged(self,text):
        if(text=="Throttle"):
            self.plot_data1()

        if(text=="C"):
            self.clear_data1()
        

    def plot_data1(self):
        x=range(0,10)
        y=[1,5,3,2,4,7,6,5,3,2]
        self.plotter.canvas.ax.plot(x,y,label="1")
        self.plotter.canvas.draw()

    def clear_data1(self):
        self.graph1.canvas.ax.clear()
        self.graph1.canvas.draw()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        __sortingEnabled = self.laps_left.isSortingEnabled()
        self.laps_left.setSortingEnabled(False)
        item = self.laps_left.item(0, 0)
        item.setText(_translate("Dialog", "남은 랩수"))
        self.laps_left.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.total_time.isSortingEnabled()
        self.total_time.setSortingEnabled(False)
        item = self.total_time.item(0, 0)
        item.setText(_translate("Dialog", "총 주행 시간"))
        self.total_time.setSortingEnabled(__sortingEnabled)
        self.choose_item.setItemText(0, _translate("Dialog", "Throttle"))
        self.choose_item.setItemText(1, _translate("Dialog", "B"))
        self.choose_item.setItemText(2, _translate("Dialog", "C"))
        self.choose_item.setItemText(3, _translate("Dialog", "D"))
        self.choose_item.setItemText(4, _translate("Dialog", "New Item"))
        self.choose_item.setItemText(5, _translate("Dialog", "New Item"))
        self.choose_item.setItemText(6, _translate("Dialog", "New Item"))
        self.choose_item.setItemText(7, _translate("Dialog", "New Item"))
        __sortingEnabled = self.velocity_table.isSortingEnabled()
        self.velocity_table.setSortingEnabled(False)
        item = self.velocity_table.item(0, 0)
        item.setText(_translate("Dialog", "현재속도"))
        item = self.velocity_table.item(1, 0)
        item.setText(_translate("Dialog", "FL 속도"))
        item = self.velocity_table.item(2, 0)
        item.setText(_translate("Dialog", "FR 속도"))
        item = self.velocity_table.item(3, 0)
        item.setText(_translate("Dialog", "RL 속도"))
        item = self.velocity_table.item(4, 0)
        item.setText(_translate("Dialog", "RR 속도"))
        self.velocity_table.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.lap_count.isSortingEnabled()
        self.lap_count.setSortingEnabled(False)
        item = self.lap_count.item(0, 0)
        item.setText(_translate("Dialog", "현재 랩수"))
        self.lap_count.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.torque_table.isSortingEnabled()
        self.torque_table.setSortingEnabled(False)
        item = self.torque_table.item(0, 0)
        item.setText(_translate("Dialog", "FL 토크"))
        item = self.torque_table.item(1, 0)
        item.setText(_translate("Dialog", "FR 토크"))
        item = self.torque_table.item(2, 0)
        item.setText(_translate("Dialog", "RL 토크"))
        item = self.torque_table.item(3, 0)
        item.setText(_translate("Dialog", "RR 토크"))
        self.torque_table.setSortingEnabled(__sortingEnabled)
        item = self.laptimeperlap.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "New Row"))
        item = self.laptimeperlap.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "New Row"))
        item = self.laptimeperlap.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "New Row"))
        item = self.laptimeperlap.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "New Row"))
        item = self.laptimeperlap.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "New Row"))
        item = self.laptimeperlap.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "New Row"))
        item = self.laptimeperlap.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "New Row"))
        item = self.laptimeperlap.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "New Row"))
        item = self.laptimeperlap.verticalHeaderItem(8)
        item.setText(_translate("Dialog", "New Row"))
        item = self.laptimeperlap.verticalHeaderItem(9)
        item.setText(_translate("Dialog", "New Row"))
        item = self.laptimeperlap.verticalHeaderItem(10)
        item.setText(_translate("Dialog", "New Row"))
        item = self.laptimeperlap.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "랩 수"))
        item = self.laptimeperlap.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "랩 타임"))
        __sortingEnabled = self.laptimeperlap.isSortingEnabled()
        self.laptimeperlap.setSortingEnabled(False)
        self.laptimeperlap.setSortingEnabled(__sortingEnabled)
from graphWidget import GraphWidget
#from monitor import Monitor


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
