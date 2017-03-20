# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(300, 200)
        Form.setMinimumSize(QtCore.QSize(300, 200))
        Form.setMaximumSize(QtCore.QSize(300, 200))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(87, 183, 242))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(87, 183, 242))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(87, 183, 242))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        Form.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.yandexButton = QtWidgets.QPushButton(Form)
        self.yandexButton.setGeometry(QtCore.QRect(20, 100, 99, 71))
        self.yandexButton.setToolTip("")
        self.yandexButton.setIconSize(QtCore.QSize(32, 32))
        self.yandexButton.setObjectName("yandexButton")
        self.googleButton = QtWidgets.QPushButton(Form)
        self.googleButton.setGeometry(QtCore.QRect(170, 100, 99, 71))
        self.googleButton.setToolTip("")
        self.googleButton.setIconSize(QtCore.QSize(32, 32))
        self.googleButton.setObjectName("googleButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 20, 191, 41))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cloud Plugin"))
        self.yandexButton.setText(_translate("Form", "Yandex"))
        self.googleButton.setText(_translate("Form", "Google"))
        self.label.setText(_translate("Form", "Welcome Cloud Plugin"))

