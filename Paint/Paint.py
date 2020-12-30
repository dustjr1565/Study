from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Shape import *
import cv2


load=False
class Ui_MainWindow(object):
    def __init__(self):
        self.background=(255,255,255)
        self.color=(0,0,0)
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
        self.save.clicked.connect(self.saveButtonClicked)
        self.load = QtWidgets.QPushButton(self.centralwidget)
        self.load.setGeometry(QtCore.QRect(10, 70, 71, 51))
        self.load.setObjectName("load")
        self.load.clicked.connect(self.loadButtonClicked)
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
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_6.setGeometry(QtCore.QRect(330, 20, 301, 80))
        self.groupBox_6.setObjectName("groupBox_6")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 20, 301, 80))
        self.groupBox_5.setObjectName("groupBox_5")
        self.BC1 = QtWidgets.QPushButton(self.groupBox_5)
        self.BC1.setGeometry(QtCore.QRect(80, 20, 21, 21))
        self.BC1.setObjectName("BC1")
        self.BC1.setStyleSheet("background-color: white");
        self.BC2 = QtWidgets.QPushButton(self.groupBox_5)
        self.BC2.setGeometry(QtCore.QRect(110, 20, 21, 21))
        self.BC2.setObjectName("BC2")
        self.BC2.setStyleSheet("background-color: red");
        self.BC3 = QtWidgets.QPushButton(self.groupBox_5)
        self.BC3.setGeometry(QtCore.QRect(140, 20, 21, 21))
        self.BC3.setObjectName("BC3")
        self.BC3.setStyleSheet("background-color: yellow");
        self.BC4 = QtWidgets.QPushButton(self.groupBox_5)
        self.BC4.setGeometry(QtCore.QRect(80, 50, 21, 21))
        self.BC4.setObjectName("BC4")
        self.BC4.setStyleSheet("background-color: balck");
        self.BC5 = QtWidgets.QPushButton(self.groupBox_5)
        self.BC5.setGeometry(QtCore.QRect(110, 50, 21, 21))
        self.BC5.setObjectName("BC5")
        self.BC5.setStyleSheet("background-color: green");
        self.BC6 = QtWidgets.QPushButton(self.groupBox_5)
        self.BC6.setGeometry(QtCore.QRect(140, 50, 21, 21))
        self.BC6.setObjectName("BC6")
        self.BC6.setStyleSheet("background-color: blue");
        self.BC_Btn = QtWidgets.QPushButton(self.groupBox_5)
        self.BC_Btn.setGeometry(QtCore.QRect(10, 20, 61, 51))
        self.BC_Btn.setText("")
        self.BC_Btn.setObjectName("BC_Btn")
        self.BC_Btn.setStyleSheet("background-color: white");
        self.B_R = QtWidgets.QLineEdit(self.groupBox_5)
        self.B_R.setGeometry(QtCore.QRect(200, 20, 41, 16))
        self.B_R.setObjectName("B_R")
        self.B_G = QtWidgets.QLineEdit(self.groupBox_5)
        self.B_G.setGeometry(QtCore.QRect(200, 40, 41, 16))
        self.B_G.setObjectName("B_G")
        self.B_B = QtWidgets.QLineEdit(self.groupBox_5)
        self.B_B.setGeometry(QtCore.QRect(200, 60, 41, 16))
        self.B_B.setObjectName("B_B")
        self.B_ChangeBtn = QtWidgets.QPushButton(self.groupBox_5)
        self.B_ChangeBtn.setGeometry(QtCore.QRect(250, 20, 41, 51))
        self.B_ChangeBtn.setObjectName("B_ChangeBtn")
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setGeometry(QtCore.QRect(180, 20, 21, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setGeometry(QtCore.QRect(180, 40, 21, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setGeometry(QtCore.QRect(180, 60, 21, 16))
        self.label_5.setObjectName("label_5")
        self.SC2 = QtWidgets.QPushButton(self.groupBox_6)
        self.SC2.setGeometry(QtCore.QRect(110, 20, 21, 21))
        self.SC2.setObjectName("SC2")
        self.SC2.setStyleSheet("background-color: red");
        self.S_R = QtWidgets.QLineEdit(self.groupBox_6)
        self.S_R.setGeometry(QtCore.QRect(200, 20, 41, 16))
        self.S_R.setObjectName("S_R")
        self.S_ChangeBtn = QtWidgets.QPushButton(self.groupBox_6)
        self.S_ChangeBtn.setGeometry(QtCore.QRect(250, 20, 41, 51))
        self.S_ChangeBtn.setObjectName("S_ChangeBtn")
        self.SC4 = QtWidgets.QPushButton(self.groupBox_6)
        self.SC4.setGeometry(QtCore.QRect(80, 50, 21, 21))
        self.SC4.setObjectName("SC4")
        self.SC4.setStyleSheet("background-color: balck");
        self.SC5 = QtWidgets.QPushButton(self.groupBox_6)
        self.SC5.setGeometry(QtCore.QRect(110, 50, 21, 21))
        self.SC5.setObjectName("SC5")
        self.SC5.setStyleSheet("background-color: green");
        self.SC1 = QtWidgets.QPushButton(self.groupBox_6)
        self.SC1.setGeometry(QtCore.QRect(80, 20, 21, 21))
        self.SC1.setObjectName("SC1")
        self.SC1.setStyleSheet("background-color: white");
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        self.label_7.setGeometry(QtCore.QRect(180, 60, 21, 16))
        self.label_7.setObjectName("label_7")
        self.SC_Btn = QtWidgets.QPushButton(self.groupBox_6)
        self.SC_Btn.setGeometry(QtCore.QRect(10, 20, 61, 51))
        self.SC_Btn.setText("")
        self.SC_Btn.setObjectName("SC_Btn")
        self.SC_Btn.setStyleSheet("background-color: black");
        self.SC3 = QtWidgets.QPushButton(self.groupBox_6)
        self.SC3.setGeometry(QtCore.QRect(140, 20, 21, 21))
        self.SC3.setObjectName("SC3")
        self.SC3.setStyleSheet("background-color: yellow");
        self.S_G = QtWidgets.QLineEdit(self.groupBox_6)
        self.S_G.setGeometry(QtCore.QRect(200, 40, 41, 16))
        self.S_G.setObjectName("S_G")
        self.label_6 = QtWidgets.QLabel(self.groupBox_6)
        self.label_6.setGeometry(QtCore.QRect(180, 20, 21, 16))
        self.label_6.setObjectName("label_6")
        self.S_B = QtWidgets.QLineEdit(self.groupBox_6)
        self.S_B.setGeometry(QtCore.QRect(200, 60, 41, 16))
        self.S_B.setObjectName("S_B")
        self.SC6 = QtWidgets.QPushButton(self.groupBox_6)
        self.SC6.setGeometry(QtCore.QRect(140, 50, 21, 21))
        self.SC6.setObjectName("SC6")
        self.SC6.setStyleSheet("background-color: blue");
        self.label_8 = QtWidgets.QLabel(self.groupBox_6)
        self.label_8.setGeometry(QtCore.QRect(180, 40, 21, 16))
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.BC1.clicked.connect(self.BC1_clicked)
        self.BC2.clicked.connect(self.BC2_clicked)
        self.BC3.clicked.connect(self.BC3_clicked)
        self.BC4.clicked.connect(self.BC4_clicked)
        self.BC5.clicked.connect(self.BC5_clicked)
        self.BC6.clicked.connect(self.BC6_clicked)

        self.SC1.clicked.connect(self.SC1_clicked)
        self.SC2.clicked.connect(self.SC2_clicked)
        self.SC3.clicked.connect(self.SC3_clicked)
        self.SC4.clicked.connect(self.SC4_clicked)
        self.SC5.clicked.connect(self.SC5_clicked)
        self.SC6.clicked.connect(self.SC6_clicked)

        self.canvas.mouseMoveEvent = self.canvas_mouseMoveEvent
        self.canvas.mousePressEvent = self.canvas_mousePressEvent
        self.canvas.mouseReleaseEvent = self.canvas_mouseRelaseEvent
        self.canvas.repaint = self.canvas_repaint

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "그림판"))
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
        self.groupBox_6.setTitle(_translate("MainWindow", "도형"))
        self.groupBox_5.setTitle(_translate("MainWindow", "배경"))
        self.B_ChangeBtn.setText(_translate("MainWindow", "변경"))
        self.label_3.setText(_translate("MainWindow", "R:"))
        self.label_4.setText(_translate("MainWindow", "G:"))
        self.label_5.setText(_translate("MainWindow", "B:"))
        self.S_ChangeBtn.setText(_translate("MainWindow", "변경"))
        self.label_7.setText(_translate("MainWindow", "B:"))
        self.label_6.setText(_translate("MainWindow", "R:"))
        self.label_8.setText(_translate("MainWindow", "G:"))

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

        if self.eraser.isChecked():
            color=self.background
        else:
            color=self.color

        if self.line.isChecked():
            self.shapeList.append(Line(self.startX, self.startY, self.endX, self.endY, color, self.spinBox.value()))

        if self.triangle.isChecked():
            self.shapeList.append(Triangle(self.startX, self.startY, self.endX, self.endY, color, thickness))

        if self.rect.isChecked():
            self.shapeList.append(Rect(self.startX, self.startY, self.endX, self.endY, color, thickness))

        if self.circle.isChecked():
            self.shapeList.append(Circle(self.startX, self.startY, self.endX, self.endY, color, thickness))

        self.canvas.repaint()
        self.qImg = QtGui.QImage(self.img.data, self.w, self.h, self.w * self.c, QtGui.QImage.Format_RGB888)
        self.pixmap = QtGui.QPixmap.fromImage(self.qImg)
        self.canvas.setPixmap(self.pixmap)

    def canvas_mouseMoveEvent(self, e):
        self.endX=e.x()
        self.endY=e.y()

        if self.fill.isChecked():
            thickness=-1
        else:
            thickness=self.spinBox.value()

        if self.eraser.isChecked():
            color=self.background
        else:
            color=self.color

        if self.pen.isChecked():
            self.shape = Shape(self.endX, self.endY, color, self.spinBox.value())
            self.shape.Draw(self.img)
            self.shapeList.append(self.shape)
        if self.line.isChecked():
            self.shape=Line(self.startX, self.startY, self.endX, self.endY, color, self.spinBox.value())
        if self.rect.isChecked():
            self.shape=Rect(self.startX, self.startY, self.endX, self.endY, color, thickness)
        if self.circle.isChecked():
            self.shape=Circle(self.startX, self.startY, self.endX, self.endY, color, thickness)
        if self.triangle.isChecked():
            self.shape=Triangle(self.startX, self.startY, self.endX, self.endY, color, thickness)

        self.canvas.repaint()
        self.shape.Draw(self.img)
        self.qImg = QtGui.QImage(self.img.data, self.w, self.h, self.w * self.c, QtGui.QImage.Format_RGB888)
        self.pixmap = QtGui.QPixmap.fromImage(self.qImg)
        self.canvas.setPixmap(self.pixmap)

    def canvas_repaint(self):
        self.img = np.full((570, 1260, 3), self.background, dtype=np.uint8)
        for shape in self.shapeList:
            shape.Draw(self.img)

    def loadButtonClicked(self):
        Path=QFileDialog.getOpenFileName()
        self.pixmap = QtGui.QPixmap(Path[0])
        self.canvas.setPixmap(self.pixmap)
        self.shapeList=[]

    def saveButtonClicked(self):
        cv2.imwrite('C:/Users/User/Desktop/test.jpg', self.img)

    def BC1_clicked(self):
        self.BC_Btn.setStyleSheet("background-color: white")
        self.background = (255, 255, 255)
        self.shape.Draw(self.img)
        self.canvas.repaint()
        self.qImg = QtGui.QImage(self.img.data, self.w, self.h, self.w * self.c, QtGui.QImage.Format_RGB888)
        self.pixmap = QtGui.QPixmap.fromImage(self.qImg)
        self.canvas.setPixmap(self.pixmap)

    def BC2_clicked(self):
        self.BC_Btn.setStyleSheet("background-color: red")
        self.background = (255, 0, 0)
        self.canvas.repaint()
        self.shape.Draw(self.img)
        self.qImg = QtGui.QImage(self.img.data, self.w, self.h, self.w * self.c, QtGui.QImage.Format_RGB888)
        self.pixmap = QtGui.QPixmap.fromImage(self.qImg)
        self.canvas.setPixmap(self.pixmap)

    def BC3_clicked(self):
        self.BC_Btn.setStyleSheet("background-color: yellow")
        self.background = (255, 255, 0)
        self.canvas.repaint()
        self.shape.Draw(self.img)
        self.qImg = QtGui.QImage(self.img.data, self.w, self.h, self.w * self.c, QtGui.QImage.Format_RGB888)
        self.pixmap = QtGui.QPixmap.fromImage(self.qImg)
        self.canvas.setPixmap(self.pixmap)

    def BC4_clicked(self):
        self.BC_Btn.setStyleSheet("background-color: black")
        self.background = (0, 0, 0)
        self.canvas.repaint()
        self.shape.Draw(self.img)
        self.qImg = QtGui.QImage(self.img.data, self.w, self.h, self.w * self.c, QtGui.QImage.Format_RGB888)
        self.pixmap = QtGui.QPixmap.fromImage(self.qImg)
        self.canvas.setPixmap(self.pixmap)

    def BC5_clicked(self):
        self.BC_Btn.setStyleSheet("background-color: green")
        self.background = (0, 255, 0)
        self.canvas.repaint()
        self.shape.Draw(self.img)
        self.qImg = QtGui.QImage(self.img.data, self.w, self.h, self.w * self.c, QtGui.QImage.Format_RGB888)
        self.pixmap = QtGui.QPixmap.fromImage(self.qImg)
        self.canvas.setPixmap(self.pixmap)

    def BC6_clicked(self):
        self.BC_Btn.setStyleSheet("background-color: blue")
        self.background = (0, 0, 255)
        self.canvas.repaint()
        self.shape.Draw(self.img)
        self.qImg = QtGui.QImage(self.img.data, self.w, self.h, self.w * self.c, QtGui.QImage.Format_RGB888)
        self.pixmap = QtGui.QPixmap.fromImage(self.qImg)
        self.canvas.setPixmap(self.pixmap)

    def SC1_clicked(self):
        self.SC_Btn.setStyleSheet("background-color: white")
        self.color = (255, 255, 255)
        self.shape.Draw(self.img)
        self.canvas.repaint()
        self.qImg = QtGui.QImage(self.img.data, self.w, self.h, self.w * self.c, QtGui.QImage.Format_RGB888)
        self.pixmap = QtGui.QPixmap.fromImage(self.qImg)
        self.canvas.setPixmap(self.pixmap)

    def SC2_clicked(self):
        self.SC_Btn.setStyleSheet("background-color: red")
        self.color = (255, 0, 0)
        self.canvas.repaint()
        self.shape.Draw(self.img)
        self.qImg = QtGui.QImage(self.img.data, self.w, self.h, self.w * self.c, QtGui.QImage.Format_RGB888)
        self.pixmap = QtGui.QPixmap.fromImage(self.qImg)
        self.canvas.setPixmap(self.pixmap)

    def SC3_clicked(self):
        self.SC_Btn.setStyleSheet("background-color: yellow")
        self.color = (255, 255, 0)
        self.canvas.repaint()
        self.shape.Draw(self.img)
        self.qImg = QtGui.QImage(self.img.data, self.w, self.h, self.w * self.c, QtGui.QImage.Format_RGB888)
        self.pixmap = QtGui.QPixmap.fromImage(self.qImg)
        self.canvas.setPixmap(self.pixmap)

    def SC4_clicked(self):
        self.SC_Btn.setStyleSheet("background-color: black")
        self.color = (0, 0, 0)
        self.canvas.repaint()
        self.shape.Draw(self.img)
        self.qImg = QtGui.QImage(self.img.data, self.w, self.h, self.w * self.c, QtGui.QImage.Format_RGB888)
        self.pixmap = QtGui.QPixmap.fromImage(self.qImg)
        self.canvas.setPixmap(self.pixmap)

    def SC5_clicked(self):
        self.SC_Btn.setStyleSheet("background-color: green")
        self.color = (0, 255, 0)
        self.canvas.repaint()
        self.shape.Draw(self.img)
        self.qImg = QtGui.QImage(self.img.data, self.w, self.h, self.w * self.c, QtGui.QImage.Format_RGB888)
        self.pixmap = QtGui.QPixmap.fromImage(self.qImg)
        self.canvas.setPixmap(self.pixmap)

    def SC6_clicked(self):
        self.SC_Btn.setStyleSheet("background-color: blue")
        self.color = (0, 0, 255)
        self.canvas.repaint()
        self.shape.Draw(self.img)
        self.qImg = QtGui.QImage(self.img.data, self.w, self.h, self.w * self.c, QtGui.QImage.Format_RGB888)
        self.pixmap = QtGui.QPixmap.fromImage(self.qImg)
        self.canvas.setPixmap(self.pixmap)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
