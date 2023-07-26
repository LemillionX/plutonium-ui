from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os
from subprocess import Popen


class BaseUI(QWidget):
    def __init__(self, width, height):
        super().__init__()

        # File path for settings that are going to be modified
        self.file = ""

        # File path to launch the server
        self.start = ""

        # Content that will be written to the file
        self.content = []

        # Dictionnary of all the maps
        self.maps_dict = {}

        # Layout to display
        self.layout = QHBoxLayout()

        # Image of the map
        self.images_dict = {}
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

        ## .cfg file
        self.file_widget = QWidget(self)
        self.file_display = QLineEdit(self.file_widget)
        self.file_display.setReadOnly(True)
        self.file_widget_h = QHBoxLayout(self.file_widget)
        self.file_widget_h.addWidget(self.file_display)
        self.file_button = QPushButton("Load .cfg file")
        self.file_button.clicked.connect(self.set_file)
        self.file_widget_h.addWidget(self.file_button)
        self.settings.addRow("Configuration file", self.file_widget)

        ## .bat file
        self.start_widget = QWidget(self)
        self.start_display = QLineEdit(self.start_widget)
        self.start_display.setReadOnly(True)
        self.start_widget_h = QHBoxLayout(self.start_widget)
        self.start_widget_h.addWidget(self.start_display)
        self.start_button = QPushButton("Load .bat file")
        self.start_button.clicked.connect(self.set_launch)
        self.start_widget_h.addWidget(self.start_button)
        self.settings.addRow("Batch file (to launch the server)", self.start_widget)


        ## Test Button
        self.test_button = QPushButton("Test")
        # self.test_button.clicked.connect(self.load_file)
        self.settings.addWidget(self.test_button)

        ## Save Button
        self.save_button = QPushButton("Save settings")
        self.save_button.clicked.connect(self.save_settings)
        self.settings.addWidget(self.save_button)

        ## Launch Button
        self.launch_button = QPushButton("Launch a game")
        self.launch_button.clicked.connect(self.launch_server)
        self.settings.addWidget(self.launch_button)

    def load_file(self):
        print("Loading settings...")
        with open(self.file, "r", encoding='utf8') as file:
            self.content = file.readlines()
        print(f"{len(self.content)} lines loaded")

    def save_settings(self):
        print("Saving settings...")
        with open(self.file, "w", encoding='utf8') as file:
            file.writelines(self.content)
        print("Settings saved !")

    def setImage(self):
        self.image.setStyleSheet(f"background-image: url({self.url_image})")

    def readAttributeFromText(self, line, idx, subidx=1):
        return self.content[line].split(" ")[idx].split('"')[subidx]
    
    def launch_server(self):
        print("Starting server...")
        os.chdir(os.path.dirname(self.start))
        Popen(['start', 'cmd', '/k', 'call', os.path.basename(self.start)], shell=True)

    def set_file(self):
        fileName = QFileDialog.getOpenFileName(self, 'OpenFile')[0]
        self.file_display.setText(fileName)
        self.file = fileName

    def set_launch(self):
        fileName = QFileDialog.getOpenFileName(self, 'OpenFile')[0]
        self.start_display.setText(fileName)
        self.start = fileName
