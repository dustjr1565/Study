from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

class MainFrame(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle('Paint')
        self.setFixedSize(1280,720)

app = QtWidgets.QApplication([])
MainFrame = MainFrame()
MainFrame.show()
app.exec_()