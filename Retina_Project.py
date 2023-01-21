import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Retina")

        button = QPushButton("Upload image", self)
        button.setGeometry(self.height(), self.width(), 100, 50)
        button.clicked.connect(self.open_image)

        self.showMaximized()
        # self.setGeometry(200, 200, 400, 300)

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