from PySide6.QtCore import QTimer, Slot

from ui import MainWindow, SignalContainer


class LabelUpdateThread:
    label: int
    signal: SignalContainer
    window: MainWindow

    def __init__(self, window: MainWindow):
        self.label = 0
        self.window = window
        self.signal = SignalContainer()
        self.signal.update_label.connect(window.set_label)
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_label)
        self.timer.start()

    @Slot(int)
    def update_label(self):
        self.signal.update_label.emit(self.label)
        self.label += 1
