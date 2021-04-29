from pathlib import Path

from PySide6.QtWidgets import QMainWindow
import argparse
from fancy import config as cfg
from oncidium.configs import PylonCameraConfig
from oncidium.machine import PylonCamera
from ui import Ui_Form


class MainWindow(QMainWindow,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

