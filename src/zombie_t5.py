from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from base import *

class ZombieT5(BaseUI):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.file = r"../files/t5/dedicated_sp.cfg"
        self.load_file()

        self.start = os.path.join(os.path.dirname(__file__), "../files/t5/test.bat")

        self.g_inactivity = int(self.readAttributeFromText(line=4, idx=1))
        self.g_inactivity_input = QLineEdit(str(self.g_inactivity))
        self.g_inactivity_input.setValidator(QIntValidator())
        self.g_inactivity_input.textChanged.connect(self.set_g_inactivity)
        self.settings.addRow("AFK time expiration ", self.g_inactivity_input)

        self.party_minplayers = int(self.readAttributeFromText(line=5, idx=1))
        self.party_minplayers_input = QComboBox()
        self.party_minplayers_input.addItems([str(i) for i in range(1,5)])
        self.party_minplayers_input.setCurrentIndex(self.party_minplayers-1)
        self.party_minplayers_input.currentTextChanged.connect(self.set_party_minplayers)
        self.settings.addRow("Minimum number of players", self.party_minplayers_input)

        self.disableClientConsole = self.readAttributeFromText(line=6, idx=1)
        self.disableClientConsole_input = QCheckBox()
        self.disableClientConsole_input.stateChanged.connect(self.setClientConsole)
        self.settings.addRow("Players ability to access server commands", self.disableClientConsole_input)

        self.floodProtect = int(self.readAttributeFromText(line=7, idx=1))
        self.floodProtect_input =QLineEdit(str(self.floodProtect))
        self.floodProtect_input.setValidator(QIntValidator())
        self.floodProtect_input.textChanged.connect(self.set_floodProtect)
        self.settings.addRow("Chat Spam protection", self.floodProtect_input)

        self.kickBanTime = int(self.readAttributeFromText(line=8, idx=1))
        self.kickBanTime_input = QLineEdit(str(self.kickBanTime))
        self.kickBanTime_input.setValidator(QIntValidator())
        self.kickBanTime_input.textChanged.connect(self.set_kickBanTime)
        self.settings.addRow("Kick Ban Duration", self.kickBanTime_input)

        self.voice = int(self.readAttributeFromText(line=9, idx=1))
        self.voice_input = QCheckBox()
        self.voice_input.setChecked(self.voice)
        self.voice_input.stateChanged.connect(self.set_voice)
        self.settings.addRow("Voice Chat ", self.voice_input)

        self.voice_quality = int(self.readAttributeFromText(line=10,idx=1))
        self.voice_quality_input = QSlider(Qt.Horizontal)
        self.voice_quality_input.setValue(self.voice_quality)
        self.voice_quality_input.setMinimum(1)
        self.voice_quality_input.setMaximum(9)
        self.voice_quality_input.setTickPosition(QSlider.TicksBelow)
        self.voice_quality_input.setTickInterval(1)
        self.voice_quality_input.valueChanged.connect(self.set_voice_quality)
        self.settings.addRow("Voice Quality ", self.voice_quality_input)

        self.map = self.readAttributeFromText(line=43, idx=3, subidx=0)
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
        self.map_input.currentTextChanged.connect(self.set_map)
        self.map_input.setCurrentText([k for k in self.maps_dict.keys() if self.maps_dict[k] == self.map][0])
        self.settings.addRow("Map selected", self.map_input)

    def set_g_inactivity(self, g_inactivity):
        if len(g_inactivity.strip()) > 0:
            self.g_inactivity = int(g_inactivity)
        else:
            self.g_inactivity = 200
        self.content[4] = f'g_inactivity "{self.g_inactivity}"                              // Enable or Disable auto kick feature for idle/AFK players.\n'

    def set_party_minplayers(self, party_minplayers):
        self.party_minplayers = int(party_minplayers)
        self.content[5] = f'party_minplayers "{self.party_minplayers}"\n'

    def setClientConsole(self, disableClientConsole):
        if disableClientConsole == Qt.Checked:
            self.disableClientConsole = 1
        else:
            self.disableClientConsole = 0
        self.content[6] = f'sv_disableClientConsole "{self.disableClientConsole}"                     // Enable or Disable players ability to access server commands\n'

    def set_floodProtect(self, floodProtect):
        if len(floodProtect.strip()) > 0:
            self.floodProtect = int(floodProtect)
        else:
            self.floodProtect = 1
        self.content[7] = f'sv_floodProtect "{self.floodProtect}"                             // Chat Spam Protection.(Set this to 20 if you are using a RCon tool)\n'

    def set_kickBanTime(self, kickBanTime):
        if len(kickBanTime.strip()) > 0:
            self.kickBanTime = int(kickBanTime)
        else:
            self.kickBanTime = 300
        self.content[8] = f'sv_kickBanTime "{self.kickBanTime}"                            // Kick Ban Duration. Time before player can re-join the server after getting kicked.\n'
            
    def set_voice(self, voice):
        if voice == Qt.Checked:
            self.voice = 1
        else:
            self.voice = 0
        self.content[9] = f'sv_voice "{self.voice}"                                    // Allow Voice Chat\n'

    def set_voice_quality(self, voice_quality):
        self.voice_quality = voice_quality
        self.content[10] = f'sv_voicequality "{self.voice_quality}"                             // Voice Quality, 9 for high, 1 for low. More bandwidth better quality.\n'

    def set_map(self, map):
        self.map = self.maps_dict[map]
        self.content[43] = f'set sv_maprotation "map {self.map}"\n'

    def init_images(self):
        self.images_dict["Kino Der Toten"] = "../medias/t5/kino-der-toten.jpg"
        self.images_dict["Five"] = "../medias/t/five.png"
        self.images_dict["Dead Ops Arcade"] = "zombietron"
        self.images_dict["Ascension"] = "zombie_cosmodrome"
        self.images_dict["Call Of The Dead"] = "zombie_coast"
        self.images_dict["Shangri-La"] = "zombie_temple"
        self.images_dict["Moon"] = "zombie_moon"
        self.images_dict["Nacht Der Untoten"] = "zombie_cod5_prototype"
        self.images_dict["Verrückt"] = "zombie_cod5_asylum"
        self.images_dict["Shi No Numa"] = "zombie_cod5_sumpf"
        self.images_dict["Der Riese"] = "zombie_cod5_factory"


