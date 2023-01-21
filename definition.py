from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import QSize, Qt
from PyQt6 import QtCore, QtGui

import sys

# top-left, top-right, bottom-left, bottom-right
objCoord = {'glasses': [[500,500], [500, 1000], [1000, 500], [1000, 1000]],
            'hat': [[0,0], [0, 500], [500, 0], [500, 500]]}

current_obj = None

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Retina")
        self.showMaximized()

        self.setMouseTracking(True)

        self.w = None

    def objClicked(self, event):
        global current_obj
        pos = event.pos()
        for obj in objCoord:
            if objCoord[obj][0][0] <= pos.x() <= objCoord[obj][3][0]:
                if objCoord[obj][0][1] <= pos.y() <= objCoord[obj][3][1]:
                    current_obj = obj
                    return True

        

    def mousePressEvent(self, event):
        pos = event.pos()
        if self.objClicked(event): 
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

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class AnotherWindow(QWidget):
    
    def __init__(self, x, y):
        super().__init__()
        self.setFixedSize(500,400)
        layout = QVBoxLayout()
        self.setWindowTitle('Definition')

        global current_obj

        # layout.addWidget(Color('#DBF0FF'))
        self.label = QLabel()
        self.label.setText(current_obj)
        self.label.setStyleSheet(
            "background-color: #DBF0FF; "
            "font-family: times; "
            "font-size: 40px;"
            "color: #0D2333;"
        )
        
        self.label.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.label)

        self.setLayout(layout)



        self.move(x, y)



app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()