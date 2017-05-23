# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 200)
        Dialog.setMinimumSize(QtCore.QSize(300, 200))
        Dialog.setMaximumSize(QtCore.QSize(300, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('images/icon.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        self.yandex_button = QtWidgets.QPushButton(Dialog)
        self.yandex_button.setGeometry(QtCore.QRect(80, 90, 68, 64))
        self.yandex_button.setStyleSheet("border-color: black;\n"
"border-width: 5px;\n"
"border-radius: 1px;")
        self.yandex_button.setText("Yandex")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap('images/yandex_icon.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.yandex_button.setIcon(icon1)
        self.yandex_button.setIconSize(QtCore.QSize(64, 64))
        self.yandex_button.setObjectName("yandex_button")
        self.google_button = QtWidgets.QPushButton(Dialog)
        self.google_button.setGeometry(QtCore.QRect(150, 90, 68, 64))
        self.google_button.setStyleSheet("border-color: black;\n"
"border-width: 5px;\n"
"border-radius: 1px;")
        self.google_button.setText("Google")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap('images/google_icon.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.google_button.setIcon(icon2)
        self.google_button.setIconSize(QtCore.QSize(64, 64))
        self.google_button.setObjectName("google_button")
        self.label_appname = QtWidgets.QLabel(Dialog)
        self.label_appname.setGeometry(QtCore.QRect(90, 10, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_appname.setFont(font)
        self.label_appname.setAlignment(QtCore.Qt.AlignCenter)
        self.label_appname.setObjectName("label_appname")
        self.label_version = QtWidgets.QLabel(Dialog)
        self.label_version.setGeometry(QtCore.QRect(90, 40, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_version.setFont(font)
        self.label_version.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_version.setAlignment(QtCore.Qt.AlignCenter)
        self.label_version.setObjectName("label_version")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(240, 170, 48, 18))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.license_button = QtWidgets.QPushButton(self.layoutWidget)
        self.license_button.setStyleSheet("border-color: black;\n"
"border-width: 5px;\n"
"border-radius: 1px;")
        self.license_button.setText("L")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap('images/license_icon.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.license_button.setIcon(icon3)
        self.license_button.setObjectName("license_button")
        self.horizontalLayout.addWidget(self.license_button)
        self.question_button = QtWidgets.QPushButton(self.layoutWidget)
        self.question_button.setStyleSheet("border-color: black;\n"
"border-width: 5px;\n"
"border-radius: 1px;")
        self.question_button.setText("A")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap('images/question_icon.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.question_button.setIcon(icon4)
        self.question_button.setObjectName("question_button")
        self.horizontalLayout.addWidget(self.question_button)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", " "))
        self.label_appname.setText(_translate("Dialog", "Cloud Plugin"))
        self.label_version.setText(_translate("Dialog", "version"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

