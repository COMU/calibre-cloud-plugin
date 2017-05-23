#!/usr/bin/env python2
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

__license__   = 'GPL v3'
__copyright__ = '2017, Kerim Ölçer <kerimlcr@gmail.com>, Ali Güven Odabaşıoğlu <agaodabasioglu@gmail.com>'
__docformat__ = 'restructuredtext en'

if False:
    get_icons = get_resources = None

#Another import
import os, re, sys
from PyQt5.Qt import QDialog, QVBoxLayout, QPushButton, QMessageBox, QLabel, QLineEdit
from PyQt5.QtWidgets import QWidget, QDesktopWidget
from PyQt5.QtCore import Qt

#Calibre config files import
from calibre_plugins.cloud_sync.config import prefs
from calibre.utils.config import config_dir

#Gui import
from calibre_plugins.cloud_sync.gui.error import Ui_Dialog as ErrorMainWindow

try:
    load_translations()
except NameError:
    pass # load_translations() added in calibre 1.9

class DemoDialog(QDialog):

    def __init__(self, gui, icon, do_user_config):
        QDialog.__init__(self, gui)
        self.gui = gui
        self.do_user_config = do_user_config
        self.db = gui.current_db


#MainWindow 
class MainWindowForm(QWidget, ErrorMainWindow):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.Window)
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())

    def error_dialog(self):
        self.errorMainWindow = ErrorMainWindow()
        self.hide()
        self.errorMainWindow.exec_()
        self.show()


