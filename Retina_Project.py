import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
#QApplication, QMainWindow, QWidget, QLabel
#QPalette, QColor, QPixmap
class AnotherWindow(QMainWindow):
    def __init__(self):
        super(AnotherWindow, self).__init__()
        self.showMaximized()
        label = QLabel(self)
        pixmap = QPixmap('cat.jpg')
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
        
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.toggle_window)
        self.setCentralWidget(self.button)

    def toggle_window(self, checked):
        if self.window1.isVisible():
            self.window1.hide()

        else: 
            self.window1.show()

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

app.exec()