import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import base
from zombie_t5 import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.width = 960
        self.height = 720
        self.resize(self.width, self.height)

        # Main layout
        w = QWidget()
        l = QHBoxLayout()
        w.setLayout(l)

        # self.base = base.BaseUI(self.width, self.height)
        self.zombie_t5 = ZombieT5(self.width, self.height)

        # Sublayouts corresponding to the different fames
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.zombie_t5)
        l.addLayout(self.stacked_layout)

        # Set the widget
        self.setCentralWidget(w)
        self.setWindowTitle("Plutonium - Custom Server Settings")

# Run the UI
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()