# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'google.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 200)
        Dialog.setMinimumSize(QtCore.QSize(300, 200))
        Dialog.setMaximumSize(QtCore.QSize(300, 200))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../calibreGUi/calibre-cloud-plugin/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.uploadButton = QtWidgets.QPushButton(Dialog)
        self.uploadButton.setGeometry(QtCore.QRect(170, 110, 99, 71))
        self.uploadButton.setToolTip("")
        self.uploadButton.setIconSize(QtCore.QSize(32, 32))
        self.uploadButton.setObjectName("uploadButton")
        self.downloadButton = QtWidgets.QPushButton(Dialog)
        self.downloadButton.setGeometry(QtCore.QRect(30, 110, 99, 71))
        self.downloadButton.setToolTip("")
        self.downloadButton.setIconSize(QtCore.QSize(32, 32))
        self.downloadButton.setObjectName("downloadButton")
        self.googleAuthButton = QtWidgets.QPushButton(Dialog)
        self.googleAuthButton.setGeometry(QtCore.QRect(30, 20, 99, 71))
        self.googleAuthButton.setToolTip("")
        self.googleAuthButton.setIconSize(QtCore.QSize(32, 32))
        self.googleAuthButton.setObjectName("googleAuthButton")
        self.googleDeauthButton = QtWidgets.QPushButton(Dialog)
        self.googleDeauthButton.setGeometry(QtCore.QRect(170, 20, 99, 71))
        self.googleDeauthButton.setToolTip("")
        self.googleDeauthButton.setIconSize(QtCore.QSize(32, 32))
        self.googleDeauthButton.setObjectName("googleDeauthButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.uploadButton.setText(_translate("Dialog", "Upload"))
        self.downloadButton.setText(_translate("Dialog", "Download"))
        self.googleAuthButton.setText(_translate("Dialog", "Auth"))
        self.googleDeauthButton.setText(_translate("Dialog", "Deauth"))

