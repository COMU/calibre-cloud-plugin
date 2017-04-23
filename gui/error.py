# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 239)
        Dialog.setMinimumSize(QtCore.QSize(400, 239))
        Dialog.setMaximumSize(QtCore.QSize(400, 239))
        self.manuel_button = QtWidgets.QPushButton(Dialog)
        self.manuel_button.setGeometry(QtCore.QRect(230, 190, 85, 30))
        self.manuel_button.setObjectName("manuel_button")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(20, 20, 361, 161))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.manuel_button.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Error"))
        self.manuel_button.setText(_translate("Dialog", "Okey"))
        self.label_2.setText(_translate("Dialog", "Cloud Sync için gerekli olan bağımlılıklar yüklü değildir."))
        self.label.setText(_translate("Dialog", "-Pydrive\n"
"$pip install pydrive --user\n"
"\n"
"-Webdavclient-\n"
"$sudo apt-get install libxml2-dev libxslt-dev python-dev\n"
"$sudo apt-get install libcurl4-openssl-dev python-pycurl\n"
"$pip install webdavclient --user"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

