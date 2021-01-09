from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os
import natsort

class MainFrame(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.penColor=Qt.red
        self.RadioChecked = "dog"
        self.startX=0
        self.startY=0
        self.endX=0
        self.endY=0
        self.path=""
        self.shapeList = []
        self.pixmap = QPixmap()
        self.painter = QPainter(self.pixmap)
        self.image = QLabel()
        self.image.setAlignment(Qt.AlignTop)
        self.image.setPixmap(self.pixmap)
        self.stat=False
        self.fileList=[]
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle('Labeling program')
        self.resize(1280, 720)
        self.image.installEventFilter(self)

        upLayout = QHBoxLayout()
        upLayout.addWidget(self.image)
        groupBox = QGroupBox()
        vbox = QVBoxLayout()
        self.dogRBtn = QRadioButton("Dog 🟥")
        self.catRBtn = QRadioButton("Cat  🟦")
        self.dogRBtn.setChecked(True)
        vbox.addWidget(self.dogRBtn)
        vbox.addWidget(self.catRBtn)
        groupBox.setLayout(vbox)
        upLayout.addWidget(groupBox)
        downLayout = QHBoxLayout()
        self.dirChoiceBtn = QPushButton("디렉터리 선택")
        downLayout.addWidget(self.dirChoiceBtn)
        self.dirShowLabel = QLabel("C:/")
        downLayout.addWidget(self.dirShowLabel)
        downLayout.addStretch(1)
        self.leftMoveBtn = QPushButton("<")
        downLayout.addWidget(self.leftMoveBtn)
        self.rightMoveBtn = QPushButton(">")
        downLayout.addWidget(self.rightMoveBtn)
        downLayout.setStretch(0,2)
        downLayout.setStretch(1,4)
        downLayout.setStretch(3, 1)
        downLayout.setStretch(4, 1)

        layout = QVBoxLayout()
        layout.setStretch(0,5)
        upLayout.setStretch(0, 4)
        upLayout.setStretch(1, 1)
        downLayout.setAlignment(Qt.AlignBottom)
        layout.addLayout(upLayout)
        layout.addLayout(downLayout)

        self.setLayout(layout)
        self.dirChoiceBtn.clicked.connect(self.dirChoiceBtn_clicked)
        self.dogRBtn.clicked.connect(self.RadioBtn_clicked)
        self.catRBtn.clicked.connect(self.RadioBtn_clicked)
        self.image.mouseMoveEvent = self.image_mouseMoveEvent
        self.image.mousePressEvent = self.image_mousePressEvent
        self.image.mouseReleaseEvent = self.image_mouseRelaseEvent
        self.image.repaint = self.image_repaint
        self.image.enterEvent = self.image_enterEvent
        self.image.leaveEvent = self.image_leaveEvent
        self.leftMoveBtn.clicked.connect(self.leftMoveBtn_clicked)
        self.rightMoveBtn.clicked.connect(self.rightMoveBtn_clicked)

    def leftMoveBtn_clicked(self):
        if len(self.shapeList)>0:
            fname = self.path
            fname = "".join(fname[:-3]) + "txt"
            f = open(fname, mode='wt', encoding='utf-8')
        for shape in self.shapeList:
            s=shape.copy()
            s.pop(4)
            txt = ",".join(map(str, s)) + "\n"
            f.write(txt)
            f.close()
        num=self.p[1]-1
        if num >= 0 :
            self.p[1]=num
            Path=self.p[0]
            self.path=Path+'/'+self.fileList[num]
            self.painter = None
            self.pixmap.load(self.path)
            self.painter = QPainter(self.pixmap)
            self.painter.setPen(self.penColor)
            self.image.setPixmap(self.pixmap)
            self.dirShowLabel.setText(self.path)
            self.shapeList = []
            fname = self.path
            fname = "".join(fname[:-3]) + "txt"
            if os.path.exists(fname):
                f = open(fname, 'r')
                line = f.readline().rstrip()
                while line:
                    line = list(line.split(","))
                    for i in range(4):
                        line[i] = int(line[i])
                    if line[-1] == "dog":
                        self.painter.setPen(Qt.red)
                        line.insert(4, Qt.red)
                    else:
                        self.painter.setPen(Qt.blue)
                        line.insert(4, Qt.blue)
                    self.painter.drawRect(line[0], line[1], line[2] - line[0], line[3] - line[1])
                    self.painter.drawText(line[0], line[1], line[-1])
                    self.shapeList.append(line)
                    line = f.readline()
                f.close()
            self.image.setPixmap(self.pixmap)

    def rightMoveBtn_clicked(self):
        if len(self.shapeList)>0:
            fname = self.path
            fname = "".join(fname[:-3]) + "txt"
            f = open(fname, mode='wt', encoding='utf-8')
        for shape in self.shapeList:
            s=shape.copy()
            s.pop(4)
            txt=",".join(map(str,s))+"\n"
            f.write(txt)
            f.close()
        num = self.p[1] + 1
        if num < len(self.fileList):
            self.p[1] = num
            Path = self.p[0]
            self.path = Path + '/' + self.fileList[num]
            self.painter = None
            self.pixmap.load(self.path)
            self.painter = QPainter(self.pixmap)
            self.painter.setPen(self.penColor)
            self.image.setPixmap(self.pixmap)
            self.dirShowLabel.setText(self.path)
            self.shapeList = []
            fname = self.path
            fname = "".join(fname[:-3]) + "txt"
            if os.path.exists(fname):
                f = open(fname, 'r')
                line = f.readline().rstrip()
                while line:
                    line = list(line.split(","))
                    for i in range(4):
                        line[i] = int(line[i])
                    if line[-1] == "dog":
                        self.painter.setPen(Qt.red)
                        line.insert(4, Qt.red)
                    else:
                        self.painter.setPen(Qt.blue)
                        line.insert(4, Qt.blue)
                    self.painter.drawRect(line[0], line[1], line[2] - line[0], line[3] - line[1])
                    self.painter.drawText(line[0], line[1], line[-1])
                    self.shapeList.append(line)
                    line = f.readline()
                f.close()
            self.image.setPixmap(self.pixmap)

    def image_enterEvent(self,e):
        self.setCursor(QCursor(Qt.CrossCursor))

    def image_leaveEvent(self,e):
        self.setCursor(QCursor(Qt.ArrowCursor))

    def dirChoiceBtn_clicked(self):
        Path = QFileDialog.getExistingDirectory()
        self.p =[Path,0]
        files = os.listdir(Path)
        self.fileList = [file for file in files if file.endswith(".jpg")]
        self.fileList = natsort.natsorted(self.fileList)
        self.painter=None
        self.path=Path+'/'+self.fileList[0]
        self.pixmap.load(self.path)
        self.painter = QPainter(self.pixmap)
        self.painter.setPen(self.penColor)
        self.image.setPixmap(self.pixmap)
        self.dirShowLabel.setText(self.path)
        self.shapeList = []
        fname = self.path
        fname = "".join(fname[:-3]) + "txt"
        if os.path.exists(fname):
            f = open(fname, 'r')
            line = f.readline().rstrip()
            print(line)
            while line:
                line = list(line.split(","))
                for i in range(4):
                    line[i] = int(line[i])
                if line[-1] == "dog":
                    self.painter.setPen(Qt.red)
                    line.insert(4, Qt.red)
                else:
                    self.painter.setPen(Qt.blue)
                    line.insert(4, Qt.blue)
                self.painter.drawRect(line[0], line[1], line[2] - line[0], line[3] - line[1])
                self.painter.drawText(line[0], line[1], line[-1])
                self.shapeList.append(line)
                line = f.readline()
            f.close()
        self.image.setPixmap(self.pixmap)

    def RadioBtn_clicked(self, e):
        if self.dogRBtn.isChecked():
            self.RadioChecked = "dog"
            self.penColor=Qt.red
        else:
            self.RadioChecked = "cat"
            self.penColor=Qt.blue

    def image_mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.stat=True
            self.startX = e.x()
            self.startY = e.y()
            self.endX = self.startX
            self.endY = self.startY

        if e.button() == Qt.RightButton:
            print(e.x(), e.y(),self.shapeList)
            for shape in self.shapeList:
                if shape[0]<e.x()<shape[2] and shape[1]<e.y()<shape[3]:
                    self.shapeList.remove(shape)
            print(self.shapeList)
            self.image.repaint()
            self.image.setPixmap(self.pixmap)

    def image_mouseRelaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.stat = False
            self.image.repaint()
            self.painter.setPen(self.penColor)
            if self.startX > self.endX:
                self.startX, self.endX = self.endX, self.startX
            if self.startY > self.endY:
                self.startY, self.endY = self.endY, self.startY
            self.shapeList.append([self.startX, self.startY, self.endX, self.endY, self.penColor, self.RadioChecked])
            self.painter.drawRect(self.startX, self.startY, self.endX-self.startX, self.endY-self.startY)
            self.painter.drawText(self.startX,self.startY,self.RadioChecked)
            self.image.setPixmap(self.pixmap)


    def image_mouseMoveEvent(self, e):
        if self.stat:
            self.endX=e.x()
            self.endY=e.y()
            self.image.repaint()
            self.painter = QPainter(self.pixmap)
            self.painter.setPen(self.penColor)
            self.painter.drawRect(self.startX, self.startY, self.endX-self.startX, self.endY-self.startY)
            self.image.setPixmap(self.pixmap)


    def image_repaint(self):
        self.pixmap.load(self.path)
        for shape in self.shapeList:
            self.painter.setPen(shape[4])
            self.painter.drawRect(shape[0], shape[1], shape[2]-shape[0], shape[3]-shape[1])
            self.painter.drawText(shape[0], shape[1], shape[5])

app = QtWidgets.QApplication([])
MainFrame = MainFrame()
MainFrame.show()
app.exec()