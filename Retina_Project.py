import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class AnotherWindow(QMainWindow):
    def __init__(self):
        super(AnotherWindow, self).__init__()
        self.showMaximized()
        label = QLabel(self)
        pixmap = QPixmap('/Users/cherylz/Desktop/cat.jpg')
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.window1 = AnotherWindow()
        self.showMaximized()
        self.setWindowTitle("Retina")

        widget = Color('DBF0FF')
        self.setCentralWidget(widget)
        
        self.button = QPushButton("Upload image")
        self.button.setGeometry(100,100,100,100)
        self.button.clicked.connect(self.open_second_window)
        self.setCentralWidget(self.button)

    def open_second_window(self):
        self.hide()
        self.second_window = AnotherWindow()
        self.second_window.show()

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())