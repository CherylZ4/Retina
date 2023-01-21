from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import QtCore, QtGui
from pathlib import Path
import cloudvision
import cohereapi
import photoshoot

import sys

global objCoord

def grabAllDef(initialdict: dict):
    print('Run grabAllDef')
    finaldict = {}
    for keys in initialdict:
        finaldict[keys] = cohereapi.grabDefinition(keys)
        print(keys)
    print(finaldict)
    return finaldict

current_obj = None

global defDict

class ImageWindow(QMainWindow):
    def __init__(self, file_name):
        super().__init__()
        self.setMouseTracking(True)
        self.w = None
        self.size = self.screen().size()
        self.setWindowTitle("Retina")
        self.setGeometry(100, 100, 800, 600)
        self.showMaximized()
        label = QLabel(self)
        pixmap = QPixmap(file_name)
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())
    
    def objClicked(self, event):
        global objCoord
        global current_obj
        pos = event.pos()
        for obj in objCoord:
            print(pos.x(), pos.y())
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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Retina")

        button = QPushButton("Upload image", self)
        button.setGeometry(self.height(), self.width(), 100, 50)
        button.clicked.connect(self.open_image)
        button = QPushButton("Take photo", self)
        button.setGeometry(100, 200, 100, 50)
        button.clicked.connect(self.take_photo)

        self.showMaximized()
        self.size = self.screen().size()
    def take_photo(self):
        global objCoord
        global defDict
        path = photoshoot.openCam()
        objCoord = cloudvision.grabobjects(path)
        defDict = grabAllDef(objCoord)
        print(objCoord)
        print(self.size.width(), self.size.height())
        if path:
            self.hide()
            self.image_window = ImageWindow(path)
            self.image_window.show()
    def open_image(self):
        global objCoord
        global defDict
        options = QFileDialog.Option.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Images (*.png *.xpm *.jpg *.bmp);;All Files (*)", options=options)
        print(file_name)
        objCoord = cloudvision.grabobjects(file_name)
        defDict = grabAllDef(objCoord)
        print(objCoord)
        print(self.size.width(), self.size.height())

        if file_name:
            self.hide()
            self.image_window = ImageWindow(file_name)
            self.image_window.show()

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
        global defDict

        self.label = QLabel()
        self.label.setWordWrap(True)

        worddef = defDict[current_obj]
        print(worddef)
        self.label.setText(current_obj + '\n__________\n\n' + worddef)
        self.label.setStyleSheet(
            "background-color: #DBF0FF;"
            "font-family: times; "
            "font-size: 20px;"
            "color: #0D2333;"
        )
        
        self.label.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.label)

        self.setLayout(layout)



        self.move(x, y)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    # app.setStyleSheet(Path('style.qss').read_text())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())