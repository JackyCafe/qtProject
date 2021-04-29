from PySide6.QtCore import QObject, Signal
from oncidium.image import Image


class SignalContainer(QObject):
    update_image = Signal(Image)