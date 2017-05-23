# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'google.ui'
#
# Created by: PyQt5 UI code generator 5.7
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
        icon.addPixmap(QtGui.QPixmap('images/icon.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(280, 0, 21, 21))
        self.pushButton.setStyleSheet("border-color: black;\n"
"border-width: 5px;\n"
"border-radius: 1px;")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/bs_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(25, 20))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.uploadButton.setText(_translate("Dialog", "Upload"))
        self.downloadButton.setText(_translate("Dialog", "Download"))
        self.googleAuthButton.setText(_translate("Dialog", "Auth"))
        self.googleDeauthButton.setText(_translate("Dialog", "Deauth"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

