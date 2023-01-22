import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import photoshoot
# from PyQt6.QtGui import QLabel, Qfont 

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Retina")

        button = QPushButton("+ Upload image", self)
        button.setGeometry(self.height(), self.width(), 225, 300)
        button.clicked.connect(self.open_image)
        button.setStyleSheet('background-color: #8BC3EB')
        header = QLabel("Find image object name and definition", self)
        header.move(self.height(), 924)
        header.setFont(QFont("italic", 40))
        header.setStyleSheet('color: black')

        button = QPushButton("Take photo", self)
        button.setGeometry(100, 200, 100, 50)
        button.clicked.connect(self.take_photo)


        self.showMaximized()
        # self.setGeometry(200, 200, 400, 300)
    def take_photo(self):
        photoshoot.openCam()
        

    def open_image(self):
        options = QFileDialog.Option.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Images (*.png *.xpm *.jpg *.bmp);;All Files (*)", options=options)
        print(file_name)

        if file_name:
            self.hide()
            self.image_window = ImageWindow(file_name)
            self.image_window.show()

class ImageWindow(QMainWindow):
    def __init__(self, file_name):
        super().__init__()
        self.setWindowTitle("Retina")
        self.setGeometry(100, 100, 800, 600)
        self.showMaximized()
        label = QLabel(self)
        pixmap = QPixmap(file_name)
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())