import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from base import *

class ZombieT5(BaseUI):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.file = "../files/t5/dedicated_sp.cfg"

