import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from base import *

class ZombieT5(BaseUI):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.file = "../files/t5/dedicated_sp.cfg"
        self.load_file()

        self.g_inactivity = int(self.readAttributeFromText(line=4, idx=1))
        self.g_inactivity_input = QLineEdit(str(self.g_inactivity))
        self.g_inactivity_input.setValidator(QIntValidator())
        self.g_inactivity_input.textChanged.connect(self.set_g_inactivity)
        self.settings.addRow("AFK time expiration ", self.g_inactivity_input)

        self.party_minplayers = int(self.readAttributeFromText(line=5, idx=1))
        self.party_minplayers_input = QLineEdit(str(self.party_minplayers))
        self.party_minplayers_input.setValidator(QIntValidator(1, 4))
        self.party_minplayers_input.textChanged.connect(self.set_party_minplayers)
        self.settings.addRow("Minimum number of players (1 to 4) ", self.party_minplayers_input)

        self.disableClientConsole = self.readAttributeFromText(line=6, idx=1)
        self.disableClientConsole_input = QCheckBox()
        self.disableClientConsole_input.stateChanged.connect(self.setClientConsole)
        self.settings.addRow("Players ability to access server commands", self.disableClientConsole_input)

        self.floodProtect = int(self.readAttributeFromText(line=7, idx=1))
        self.floodProtect_input =QLineEdit(str(self.floodProtect))
        self.floodProtect_input.setValidator(QIntValidator())
        self.settings.addRow("Chat Spam protection", self.floodProtect_input)

        self.kickBanTime = int(self.readAttributeFromText(line=8, idx=1))
        self.kickBanTime_input = QLineEdit(str(self.kickBanTime))
        self.kickBanTime_input.setValidator(QIntValidator())
        self.settings.addRow("Kick Ban Duration", self.kickBanTime_input)

        self.voice = int(self.readAttributeFromText(line=9, idx=1))
        self.voice_input = QCheckBox()
        self.voice_input.setChecked(True)
        self.settings.addRow("Voice Chat ", self.voice_input)

        self.voice_quality = int(self.readAttributeFromText(line=10,idx=1))
        self.voice_quality_input = QSlider(Qt.Horizontal)
        self.voice_quality_input.setValue(self.voice_quality)
        self.voice_quality_input.setMinimum(1)
        self.voice_quality_input.setMaximum(9)
        self.voice_quality_input.setTickPosition(QSlider.TicksBelow)
        self.voice_quality_input.setTickInterval(1)
        self.settings.addRow("Voice Quality ", self.voice_quality_input)

        self.map = "zombie_theater"
        self.map_input = QComboBox()
        self.maps_dict["Kino Der Toten"] = "zombie_theater"
        self.maps_dict["Five"] = "zombie_pentagon"
        self.maps_dict["Dead Ops Arcade"] = "zombietron"
        self.maps_dict["Ascension"] = "zombie_cosmodrome"
        self.maps_dict["Call Of The Dead"] = "zombie_coast"
        self.maps_dict["Shangri-La"] = "zombie_temple"
        self.maps_dict["Moon"] = "zombie_moon"
        self.maps_dict["Nacht Der Untoten"] = "zombie_cod5_prototype"
        self.maps_dict["Verrückt"] = "zombie_cod5_asylum"
        self.maps_dict["Shi No Numa"] = "zombie_cod5_sumpf"
        self.maps_dict["Der Riese"] = "zombie_cod5_factory"
        self.map_input.addItems(self.maps_dict.keys())
        self.settings.addRow("Map selected", self.map_input)

    def set_g_inactivity(self, g_inactivity):
        if len(g_inactivity.strip()) > 0:
            self.g_inactivity = int(g_inactivity)
        else:
            self.g_inactivity = 200

    def set_party_minplayers(self, party_minplayers):
        if len(party_minplayers.strip()) > 0:
            self.party_minplayers = max(min(int(party_minplayers),4) , 1)
            self.party_minplayers_input.setText(str(self.party_minplayers))

    def setClientConsole(self, state):
        if state == Qt.Checked:
            self.disableClientConsole = 1
        else:
            self.disableClientConsole = 0

    def set_floodProtect(self, floodProtect):
        print("Setting floodProtect...")
        if len(floodProtect.strip()) > 0:
            self.floodProtect = int(floodProtect)
        else:
            self.floodProtect = 200

    def set_kickBanTime(self, kickBanTime):
        print("Setting kickBanTime...")

    def set_voice(self, voice):
        print("Setting voice...")

    def set_voice_quality(self, voice_quality):
        print("Setting voice_quality...")

    def set_map(self, map):
        print("Choosing the map...")
