from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MainFrame(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle('Labeling program')
        self.resize(1280, 720)

        upLayout = QHBoxLayout()
        self.pixmap = QPixmap()
        self.image = QLabel()
        self.image.setPixmap(self.pixmap)

        upLayout.addWidget(self.image)
        groupBox = QGroupBox()
        vbox = QVBoxLayout()
        self.dogRBtn = QRadioButton("Dog")
        self.catRBtn = QRadioButton("Cat")
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

    def dirChoiceBtn_clicked(self):
        Path = QFileDialog.getOpenFileName()
        self.pixmap = QtGui.QPixmap(Path[0])
        self.image.setPixmap(self.pixmap)
        self.dirShowLabel.setText(Path[0])

app = QtWidgets.QApplication([])
MainFrame = MainFrame()
MainFrame.show()
app.exec()