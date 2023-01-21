from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import QSize, Qt
from PyQt6 import QtCore, QtGui

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Retina")
        self.showMaximized()

        self.setMouseTracking(True)

        self.w = None


    def mousePressEvent(self, event):
        pos = event.pos()
        self.show_new_window(pos.x(), pos.y())

    def show_new_window(self, x, y):
        if self.w is None:
            self.w = AnotherWindow(x, y)
            self.w.show()
        else:
            self.w.close()
            self.w = None
    
    def closeEvent(self, event):
        if self.w:
            self.w.close()

class AnotherWindow(QWidget):
    
    def __init__(self, x, y):
        super().__init__()
        self.setFixedSize(400,300)
        layout = QVBoxLayout()
        self.label = QLabel("Definition")
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.move(x, y)



app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()