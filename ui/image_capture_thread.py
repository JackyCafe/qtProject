from PySide6.QtCore import QTimer, Slot

from oncidium.image import Image
from oncidium.machine import PylonCamera
from ui import MainWindow, SignalContainer


class ImageCaptureThread:
    window: MainWindow
    camera: PylonCamera
    signal: SignalContainer
    image : Image

    def __init__(self,window: MainWindow,camera: PylonCamera):
        self.window = window
        self.camera = camera
        self.camera.open()
        self.image = self.camera.get_image()
        self.signal = SignalContainer()
        self.signal.update_image.connect(self.window.set_image)
        self.timer = QTimer()
        self.timer.setInterval(1000//30)
        self.timer.timeout.connect(self.update_label())
        self.timer.start()

    @Slot(Image)
    def update_label(self):
        self.signal.update_image.emit(self.image)
      #  self.image = self.camera.get_image()