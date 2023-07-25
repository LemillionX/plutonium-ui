import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class BaseUI(QWidget):
    def __init__(self, width, height):
        super().__init__()

        self.layout = QHBoxLayout()

        self.image = QLabel(self)
        self.image.resize(width//2, height)
        self.url_image = "../medias/test.png"
        self.setImage()
        self.layout.addWidget(self.image)

        self.settings_widget = QWidget(self)
        self.settings_widget.move(width//2,0)
        self.settings = QFormLayout(self.settings_widget)
        self.test_button = QPushButton("Test")
        self.settings.addWidget(self.test_button)
        self.layout.addWidget(self.settings_widget)

    def setImage(self):
        self.image.setStyleSheet(f"background-image: url({self.url_image})")
