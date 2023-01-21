from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import QSize, Qt
from PyQt6 import QtCore, QtGui
from pathlib import Path
from cohereapi import *
from cloudvision import *

import sys

# top-left, top-right, bottom-right, bottom-left
# objCoord = {'glasses': [[500,500], [500, 1000], [1000, 1000], [1000, 500]],
#             'hat': [[0,0], [0, 500], [500, 500], [500, 0]]}

# objCoord = {'glasses': [[0.3, 0.3], [0.3, 0.6], [0.6, 0.6], [0.6, 0.5]]}

objCoord = grabobjects('images\cat.jpg')


current_obj = None

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Retina")
        self.showMaximized()

        self.setMouseTracking(True)

        self.w = None

        self.size = self.screen().size()

    def objClicked(self, event):
        global current_obj
        pos = event.pos()
        for obj in objCoord:
            if objCoord[obj][0][0] * self.size.width() <= pos.x() <= objCoord[obj][2][0] * self.size.width():
                if objCoord[obj][0][1] * self.size.height() <= pos.y() <= objCoord[obj][2][1] * self.size.height():
                    current_obj = obj
                    return True

        

    def mousePressEvent(self, event):
        pos = event.pos()
        if self.objClicked(event): 
            self.show_new_window(pos.x(), pos.y())

    def show_new_window(self, x, y):
        if self.w is None:
            self.w = Definition(x, y)
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

class Definition(QWidget):
    
    def __init__(self, x, y):
        super().__init__()
        self.setFixedSize(500,400)
        layout = QVBoxLayout()
        self.setWindowTitle('Definition')

        global current_obj

        self.label = QLabel()
        worddef = grabDefinition(current_obj)
        # worddef = "hi"
        self.label.setText(current_obj + '\n__________\n\n' + worddef)
        self.label.setStyleSheet(
            "background-color: #DBF0FF;"
            "font-family: times; "
            "font-size: 40px;"
            "color: #0D2333;"
        )
        
        self.label.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.label)

        self.setLayout(layout)



        self.move(x, y)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyleSheet(Path('style.qss').read_text())
    window = MainWindow()
    sys.exit(app.exec())

# window.show()

# app.exec()