# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yandex.ui'
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
        self.uploadButton.setGeometry(QtCore.QRect(180, 110, 99, 71))
        self.uploadButton.setToolTip("")
        self.uploadButton.setIconSize(QtCore.QSize(32, 32))
        self.uploadButton.setObjectName("uploadButton")
        self.downloadButton = QtWidgets.QPushButton(Dialog)
        self.downloadButton.setGeometry(QtCore.QRect(30, 110, 99, 71))
        self.downloadButton.setToolTip("")
        self.downloadButton.setIconSize(QtCore.QSize(32, 32))
        self.downloadButton.setObjectName("downloadButton")
        self.splitter_3 = QtWidgets.QSplitter(Dialog)
        self.splitter_3.setGeometry(QtCore.QRect(40, 20, 231, 71))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.getUsername = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.getUsername.setFont(font)
        self.getUsername.setText("")
        self.getUsername.setObjectName("getUsername")
        self.getPassword = QtWidgets.QLineEdit(self.splitter)
        self.getPassword.setObjectName("getPassword")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.uploadButton.setText(_translate("Dialog", "Upload"))
        self.downloadButton.setText(_translate("Dialog", "Download"))
        self.label.setText(_translate("Dialog", "Username"))
        self.label_2.setText(_translate("Dialog", "Password"))

