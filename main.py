#!/usr/bin/env python2
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

__license__   = 'GPL v3'
__copyright__ = '2017, Kerim Ölçer <kerimlcr@gmail.com>, Ali Güven Odabaşıoğlu <agaodabasioglu@gmail.com'
__docformat__ = 'restructuredtext en'

if False:
    get_icons = get_resources = None


from PyQt5.Qt import QDialog, QVBoxLayout, QPushButton, QMessageBox, QLabel, QLineEdit
import os, re
import webdav.client as wc
from calibre_plugins.cloud_sync.config import prefs
from calibre.utils.config import config_dir

class DemoDialog(QDialog):

    def __init__(self, gui, icon, do_user_config):
        QDialog.__init__(self, gui)
        self.gui = gui
        self.do_user_config = do_user_config

        self.db = gui.current_db

        self.l = QVBoxLayout()
        self.setLayout(self.l)
#
        self.label = QLabel('URL Adresi')
        self.l.addWidget(self.label)

        self.get_url = QLineEdit(self)
        self.get_url.setText(prefs['url'])
        self.l.addWidget(self.get_url)
        self.label.setBuddy(self.get_url)

        self.label = QLabel('Kullanici adi')
        self.l.addWidget(self.label)

        self.get_name = QLineEdit(self)
        self.get_name.setText(prefs['username'])
        self.l.addWidget(self.get_name)
        self.label.setBuddy(self.get_name)


        self.label = QLabel('Password')
        self.l.addWidget(self.label)

        self.get_password = QLineEdit(self)
        self.get_password.setEchoMode(QLineEdit.Password)
        self.get_password.setText(prefs['password'])
        self.l.addWidget(self.get_password)
        self.label.setBuddy(self.get_password)

        self.save_button = QPushButton('Save', self)
        self.save_button.clicked.connect(self.save)
        self.l.addWidget(self.save_button)

        self.push_button = QPushButton('Push', self)
        self.push_button.clicked.connect(self.push)
        self.l.addWidget(self.push_button)

        self.pull_button = QPushButton('Pull', self)
        self.pull_button.clicked.connect(self.pull)
        self.l.addWidget(self.pull_button)
#
        self.setWindowTitle('Cloud Sync')
        self.setWindowIcon(icon)

        self.resize(self.sizeHint())


    def save(self):
        prefs['password'] = self.get_password.text()
        prefs['username'] = self.get_name.text()
        prefs['url'] = self.get_url.text()

    def yandexDisk(self, choice):
        options = {
         'webdav_hostname': prefs['url'],
         'webdav_login'   : prefs['username'],
         'webdav_password': prefs['password']
        }
        client = wc.Client(options)

#        kwargs = {
 #           'remote_path': "calibre",
  #          'local_path':  prefs['librarypath']
   #     }
                
        
        
        if (client.check() == False):
            QMessageBox.information(self, "Error", "Giriş bilgileri yanlış!")            
            return 1
        if (client.check('Calibre') == False):
            client.mkdir('Calibre')
        if(choice == "pull"):        
            #download missing file
    #        client.download_async(**kwargs)            
            #client.pull(remote_directory="calibre", local_directory=prefs['librarypath'])
            client.download_sync(remote_path="Calibre", local_path=prefs['librarypath'])

        else:
            client.upload_sync(remote_path="Calibre", local_path=prefs['librarypath'])            
            #upload missing file
            #client.push(remote_directory="calibre", local_directory=prefs['librarypath'])
     #       client.upload_async(**kwargs)

    def pull(self):
        self.yandexDisk("pull")
        return 1
        
    def push(self):
        self.yandexDisk("push")
        return 1
    

