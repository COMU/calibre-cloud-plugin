# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 200)
        Dialog.setMaximumSize(QtCore.QSize(300, 200))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_appname = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_appname.setFont(font)
        self.label_appname.setAlignment(QtCore.Qt.AlignCenter)
        self.label_appname.setObjectName("label_appname")
        self.verticalLayout.addWidget(self.label_appname)
        self.label_version = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_version.setFont(font)
        self.label_version.setAlignment(QtCore.Qt.AlignCenter)
        self.label_version.setObjectName("label_version")
        self.verticalLayout.addWidget(self.label_version)
        self.label_expl = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_expl.setFont(font)
        self.label_expl.setAlignment(QtCore.Qt.AlignCenter)
        self.label_expl.setObjectName("label_expl")
        self.verticalLayout.addWidget(self.label_expl)
        self.label_copy = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_copy.setFont(font)
        self.label_copy.setAlignment(QtCore.Qt.AlignCenter)
        self.label_copy.setObjectName("label_copy")
        self.verticalLayout.addWidget(self.label_copy)
        self.label_cs = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_cs.setFont(font)
        self.label_cs.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cs.setObjectName("label_cs")
        self.verticalLayout.addWidget(self.label_cs)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About"))
        self.label_appname.setText(_translate("Dialog", "TextLabel"))
        self.label_version.setText(_translate("Dialog", "TextLabel"))
        self.label_expl.setText(_translate("Dialog", "TextLabel"))
        self.label_copy.setText(_translate("Dialog", "TextLabel"))
        self.label_cs.setText(_translate("Dialog", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

