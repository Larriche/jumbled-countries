# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jumble.ui'
#
# Created: Fri Aug 12 18:39:05 2016
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(429, 338)
        MainWindow.setStyleSheet(_fromUtf8("background: white;"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.scoreLabel = QtGui.QLabel(self.centralwidget)
        self.scoreLabel.setGeometry(QtCore.QRect(20, 10, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(12)
        self.scoreLabel.setFont(font)
        self.scoreLabel.setObjectName(_fromUtf8("scoreLabel"))
        self.jumbleLabel = QtGui.QLabel(self.centralwidget)
        self.jumbleLabel.setGeometry(QtCore.QRect(70, 70, 251, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(12)
        self.jumbleLabel.setFont(font)
        self.jumbleLabel.setStyleSheet(_fromUtf8("color: green;\n"
"qproperty-alignment: AlignCenter;"))
        self.jumbleLabel.setObjectName(_fromUtf8("jumbleLabel"))
        self.playerText = QtGui.QLineEdit(self.centralwidget)
        self.playerText.setGeometry(QtCore.QRect(70, 150, 271, 41))
        self.playerText.setStyleSheet(_fromUtf8("border: 1px solid darkgoldenrod;\n"
"border-radius: 10px;"))
        self.playerText.setObjectName(_fromUtf8("playerText"))
        self.continueBttn = QtGui.QPushButton(self.centralwidget)
        self.continueBttn.setGeometry(QtCore.QRect(150, 220, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(12)
        self.continueBttn.setFont(font)
        self.continueBttn.setStyleSheet(_fromUtf8("background: teal; color: white; border-radius: 10px;"))
        self.continueBttn.setObjectName(_fromUtf8("continueBttn"))
        self.feedbackLabel = QtGui.QLabel(self.centralwidget)
        self.feedbackLabel.setGeometry(QtCore.QRect(320, 10, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(12)
        self.feedbackLabel.setFont(font)
        self.feedbackLabel.setText(_fromUtf8(""))
        self.feedbackLabel.setObjectName(_fromUtf8("feedbackLabel"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 429, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Jumbled Countries", None, QtGui.QApplication.UnicodeUTF8))
        self.scoreLabel.setText(QtGui.QApplication.translate("MainWindow", "Score: 0", None, QtGui.QApplication.UnicodeUTF8))
        self.jumbleLabel.setText(QtGui.QApplication.translate("MainWindow", "country", None, QtGui.QApplication.UnicodeUTF8))
        self.continueBttn.setText(QtGui.QApplication.translate("MainWindow", "Continue", None, QtGui.QApplication.UnicodeUTF8))

