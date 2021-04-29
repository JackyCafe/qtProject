import argparse
from pathlib import Path
import cv2
from fancy import config as cfg
from oncidium.configs import PylonCameraConfig
from oncidium.machine import PylonCamera


def main():
    args = get_arg_parser().parse_args()
    camera_config = PylonCameraConfig(cfg.YamlConfigLoader(args.camera_config))
    camera = PylonCamera(camera_config)
    camera.open()
    image = camera.get_image()
    cv2.namedWindow("camera", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("camera", 450, 800)
    cv2.imshow("camera",image)
    cv2.waitKey(0)


def get_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--camera_config", type=Path, default=Path("../configs/camera.yaml"))
    return parser


if __name__ == '__main__':
    main()