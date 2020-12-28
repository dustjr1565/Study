from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
from Shape import *

class Ui_MainWindow(object):
    def __init__(self):
        self.shapeList=[]
        self.shape=None
        self.startX, self.startY = None, None
        self.endX, self.endY = None, None
        self.img = np.full((570, 1260, 3), 255, dtype=np.uint8)
        self.h,self.w,self.c = self.img.shape
        self.qImg=QtGui.QImage(self.img.data, self.w,self.h,self.w*self.c, QtGui.QImage.Format_RGB888)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.canvas = QtWidgets.QLabel(self.centralwidget)
        self.canvas.setGeometry(QtCore.QRect(10, 140, 1260, 570))
        self.canvas.setObjectName("canvas")
        self.canvas.setStyleSheet('background-color: white;')
        self.pixmap = QtGui.QPixmap.fromImage(self.qImg)
        self.canvas.setPixmap(self.pixmap)
        self.canvas.show()
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(10, 10, 71, 51))
        self.save.setObjectName("save")
        self.load = QtWidgets.QPushButton(self.centralwidget)
        self.load.setGeometry(QtCore.QRect(10, 70, 71, 51))
        self.load.setObjectName("load")
        self.shape_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.shape_groupBox.setGeometry(QtCore.QRect(90, 10, 161, 111))
        self.shape_groupBox.setObjectName("groupBox")
        self.pen = QtWidgets.QRadioButton(self.shape_groupBox)
        self.pen.setGeometry(QtCore.QRect(10, 20, 108, 19))
        self.pen.setObjectName("pen")
        self.pen.setChecked(True)
        self.line = QtWidgets.QRadioButton(self.shape_groupBox)
        self.line.setGeometry(QtCore.QRect(10, 50, 108, 19))
        self.line.setObjectName("line")
        self.rect = QtWidgets.QRadioButton(self.shape_groupBox)
        self.rect.setGeometry(QtCore.QRect(80, 20, 108, 19))
        self.rect.setObjectName("rect")
        self.circle = QtWidgets.QRadioButton(self.shape_groupBox)
        self.circle.setGeometry(QtCore.QRect(80, 50, 108, 19))
        self.circle.setObjectName("circle")
        self.triangle = QtWidgets.QRadioButton(self.shape_groupBox)
        self.triangle.setGeometry(QtCore.QRect(10, 80, 108, 19))
        self.triangle.setObjectName("triangle")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 10, 31, 16))
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(360, 30, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setValue(1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(260, 10, 91, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.empty = QtWidgets.QRadioButton(self.groupBox_2)
        self.empty.setGeometry(QtCore.QRect(10, 30, 108, 19))
        self.empty.setObjectName("radioButton_6")
        self.empty.setChecked(True)
        self.fill = QtWidgets.QRadioButton(self.groupBox_2)
        self.fill.setGeometry(QtCore.QRect(10, 60, 108, 19))
        self.fill.setObjectName("radioButton_7")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 70, 64, 15))
        self.label_2.setObjectName("label_2")
        self.eraser = QtWidgets.QCheckBox(self.centralwidget)
        self.eraser.setGeometry(QtCore.QRect(360, 90, 96, 19))
        self.eraser.setObjectName("checkBox")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(420, 10, 845, 111))
        self.groupBox_3.setObjectName("groupBox_3")
        self.background_color = QtWidgets.QPushButton(self.groupBox_3)
        self.background_color.setGeometry(QtCore.QRect(10, 30, 108, 19))
        self.background_color.setObjectName("radioButton_8")
        self.shape_color = QtWidgets.QPushButton(self.groupBox_3)
        self.shape_color.setGeometry(QtCore.QRect(10, 60, 108, 19))
        self.shape_color.setObjectName("radioButton_9")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.canvas.mouseMoveEvent = self.canvas_mouseMoveEvent
        self.canvas.mousePressEvent = self.canvas_mousePressEvent
        self.canvas.mouseReleaseEvent = self.canvas_mouseRelaseEvent
        self.canvas.repaint = self.canvas_repaint

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.save.setText(_translate("MainWindow", "save"))
        self.load.setText(_translate("MainWindow", "load"))
        self.shape_groupBox.setTitle(_translate("MainWindow", "도형"))
        self.pen.setText(_translate("MainWindow", "펜"))
        self.line.setText(_translate("MainWindow", "선"))
        self.rect.setText(_translate("MainWindow", "사각형"))
        self.circle.setText(_translate("MainWindow", "원"))
        self.triangle.setText(_translate("MainWindow", "세모"))
        self.label.setText(_translate("MainWindow", "두께"))
        self.groupBox_2.setTitle(_translate("MainWindow", "내부색상"))
        self.empty.setText(_translate("MainWindow", "비우기"))
        self.fill.setText(_translate("MainWindow", "채우기"))
        self.label_2.setText(_translate("MainWindow", "지우개"))
        self.eraser.setText(_translate("MainWindow", "사용"))
        self.groupBox_3.setTitle(_translate("MainWindow", "색상"))
        self.background_color.setText(_translate("MainWindow", "배경 색상"))
        self.shape_color.setText(_translate("MainWindow", "도형 색상"))

    def canvas_mousePressEvent(self, e):
        self.startX = e.x()
        self.startY = e.y()
        self.endX = self.startX
        self.endY = self.startY

    def canvas_mouseRelaseEvent(self, e):

        if self.fill.isChecked():
            thickness=-1
        else:
            thickness=self.spinBox.value()

        if self.line.isChecked():
            self.shapeList.append(Line(self.startX, self.startY, self.endX, self.endY, (0,0,0), self.spinBox.value()))

        if self.triangle.isChecked():
            self.shapeList.append(Triangle(self.startX, self.startY, self.endX, self.endY, (0,0,0), self.spinBox.value()))

        if self.rect.isChecked():
            self.shapeList.append(Rect(self.startX, self.startY, self.endX, self.endY, (0,0,0), thickness))

        if self.circle.isChecked():
            self.shapeList.append(Circle(self.startX, self.startY, self.endX, self.endY, (0,0,0), thickness))

        self.canvas.repaint()
        self.pixmap = QtGui.QPixmap.fromImage(self.qImg)
        self.canvas.setPixmap(self.pixmap)

    def canvas_mouseMoveEvent(self, e):
        self.endX=e.x()
        self.endY=e.y()

        if self.fill.isChecked():
            thickness=-1
        else:
            thickness=self.spinBox.value()

        if self.pen.isChecked():
            self.shape = Shape(self.endX, self.endY, (0, 0, 0), self.spinBox.value())
            self.shape.Draw(self.img)
            self.shapeList.append(self.shape)
        if self.line.isChecked():
            self.shape=Line(self.startX, self.startY, self.endX, self.endY, (0,0,0), self.spinBox.value())
        if self.rect.isChecked():
            self.shape=Rect(self.startX, self.startY, self.endX, self.endY, (0,0,0), thickness)
        if self.circle.isChecked():
            self.shape=Circle(self.startX, self.startY, self.endX, self.endY, (0,0,0), thickness)
        if self.triangle.isChecked():
            self.shape=Triangle(self.startX, self.startY, self.endX, self.endY, (0,0,0), self.spinBox.value())

        self.canvas.repaint()
        self.shape.Draw(self.img)
        self.qImg = QtGui.QImage(self.img.data, self.w, self.h, self.w * self.c, QtGui.QImage.Format_RGB888)
        self.pixmap = QtGui.QPixmap.fromImage(self.qImg)
        self.canvas.setPixmap(self.pixmap)

    def canvas_repaint(self):
        self.img = np.full((570, 1260, 3), 255, dtype=np.uint8)
        for shape in self.shapeList:
            shape.Draw(self.img)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
