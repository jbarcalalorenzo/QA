# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Menu.ui'
#
# Created: Sun Oct 05 21:46:17 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(827, 523)
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(20, 50, 591, 351))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(20, 410, 601, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(680, 410, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(620, 50, 101, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.palabras = QtGui.QLabel(Dialog)
        self.palabras.setGeometry(QtCore.QRect(730, 50, 46, 13))
        self.palabras.setText(_fromUtf8(""))
        self.palabras.setObjectName(_fromUtf8("palabras"))
        self.toolButton = QtGui.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(580, 20, 21, 21))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 561, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(620, 70, 101, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.errores = QtGui.QLabel(Dialog)
        self.errores.setGeometry(QtCore.QRect(720, 70, 46, 13))
        self.errores.setText(_fromUtf8(""))
        self.errores.setObjectName(_fromUtf8("errores"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(620, 120, 51, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(620, 90, 121, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pkeyword = QtGui.QLabel(Dialog)
        self.pkeyword.setGeometry(QtCore.QRect(750, 90, 46, 13))
        self.pkeyword.setText(_fromUtf8(""))
        self.pkeyword.setObjectName(_fromUtf8("pkeyword"))
        self.skeyword = QtGui.QLineEdit(Dialog)
        self.skeyword.setGeometry(QtCore.QRect(670, 120, 113, 20))
        self.skeyword.setObjectName(_fromUtf8("skeyword"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "QA Article", None))
        self.pushButton.setText(_translate("Dialog", "Validar", None))
        self.label.setText(_translate("Dialog", "Número de Palabras :", None))
        self.toolButton.setText(_translate("Dialog", "...", None))
        self.label_2.setText(_translate("Dialog", "Número de Errores :", None))
        self.label_3.setText(_translate("Dialog", "Keyword : ", None))
        self.label_4.setText(_translate("Dialog", "Porcentaje de Keyword :", None))

