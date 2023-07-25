import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class BaseUI(QWidget):
    def __init__(self, width, height):
        super().__init__()

        # File path that is going to be modified
        self.file = ""

        # Content that will be written to the file
        self.content = []

        # Dictionnary of all the maps
        self.maps_dict = {}

        # Layout to display
        self.layout = QHBoxLayout()

        # Image of the map
        self.image = QLabel(self)
        self.image.resize(width//2, height)
        self.url_image = "../medias/test.png"
        self.setImage()
        self.layout.addWidget(self.image)

        # Settings panel
        self.settings_widget = QWidget(self)
        self.settings_widget.move(width//2,0)
        self.settings = QFormLayout(self.settings_widget)
        self.layout.addWidget(self.settings_widget)

        ## Test Button
        self.test_button = QPushButton("Test")
        self.test_button.clicked.connect(self.load_file)
        self.settings.addWidget(self.test_button)

        ## Save Button
        self.save_button = QPushButton("Save settings")
        self.save_button.clicked.connect(self.save_settings)
        self.settings.addWidget(self.save_button)

        ## Launch Button
        self.launch_button = QPushButton("Launch a game")
        self.settings.addWidget(self.launch_button)

    def load_file(self):
        print("Loading settings...")
        with open(self.file, "r", encoding='utf8') as file:
            self.content = file.readlines()
        print(f"{len(self.content)} lines")

    def save_settings(self):
        print("Saving settings...")
        with open(self.file, "w", encoding='utf8') as file:
            file.writelines(self.content)
        print("Settings saved !")

    def setImage(self):
        self.image.setStyleSheet(f"background-image: url({self.url_image})")

    def readAttributeFromText(self, line, idx):
        return self.content[line].split(" ")[idx].split('"')[1]

