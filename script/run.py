from pathlib import Path

from PySide6.QtWidgets import QApplication
import sys
import argparse

from oncidium.configs import PylonCameraConfig
from oncidium.machine import PylonCamera
from ui.gui import MainWindow
from fancy import config as cfg

from ui.image_capture_thread import ImageCaptureThread


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    args = get_arg_parser().parse_args()
    camera_config = PylonCameraConfig(cfg.YamlConfigLoader(args.camera_config))
    camera = PylonCamera(camera_config)
    ImageCaptureThread(window,camera)
    window.show()
    exit(app.exec_())


def get_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--camera_config", type=Path, default=Path("../configs/camera.yaml"))
    return parser


if __name__ == '__main__':
    main()