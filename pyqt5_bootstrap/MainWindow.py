#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QStyle

from Ui_MainWindow import Ui_MainWindow


# noinspection PyPep8Naming
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        # noinspection PyArgumentList
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

        # noinspection PyArgumentList
        x = QApplication.style().standardIcon(QStyle.SP_TitleBarCloseButton)
        self.actionExit.setIcon(x)
        self.actionExit.triggered.connect(self.__actionExit)

        # noinspection PyArgumentList
        x = QApplication.style().standardIcon(QStyle.SP_MessageBoxInformation)
        self.actionAbout.setIcon(x)
        self.actionAbout.triggered.connect(self.__actionAbout)

        # noinspection PyArgumentList
        x = QApplication.style().standardIcon(QStyle.SP_TitleBarMenuButton)
        self.actionAbout_Qt.setIcon(x)
        self.actionAbout_Qt.triggered.connect(self.__actionAbout_Qt)

    def __actionExit(self):
        self.close()

    def __actionAbout(self):
        title = 'About'
        text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' \
               'Mauris eu dui luctus, rhoncus magna vitae, mattis metus. ' \
               'Nunc in enim eu justo tincidunt tempus elementum ut lectus. ' \
               'Etiam nulla nibh, tempus nec sollicitudin a, venenatis sed ' \
               'leo. Nam at pretium purus, sit amet auctor magna. Curabitur ' \
               'porttitor urna auctor, tempus mi non, convallis dolor. ' \
               'Donec molestie felis eget enim dictum, sit amet hendrerit ' \
               'arcu gravida. Pellentesque in blandit tortor, at efficitur ' \
               'ipsum. Pellentesque eget purus at magna lobortis porta.' \
               ' Nulla facilisi. Nulla sodales posuere neque, id semper ' \
               'risus dictum in. Nullam eleifend lorem non ultrices ' \
               'dignissim. Aenean vel felis vel quam vulputate tincidunt' \
               'in porta mauris.'
        QMessageBox().about(self, title, text)

    # noinspection PyMethodMayBeStatic
    def __actionAbout_Qt(self):
        # noinspection PyArgumentList
        QApplication.aboutQt()
