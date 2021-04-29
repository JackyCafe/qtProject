# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from oncidium.image import Image


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.image_label = QLabel(Form)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setGeometry(QRect(150, 50, 800, 800))
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.image_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi


    @Slot(int)
    def set_label(self,label):
        self.image_label.setText(str(label))

    @Slot(Image)
    def set_image(self,camera_image):
        image = QImage(camera_image, 1800, 1600, 1800, QImage.Format_ARGB32)
        pix = QPixmap.fromImage(image)
        self.image_label.setPixmap(pix)
