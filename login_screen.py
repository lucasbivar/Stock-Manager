# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_screen.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1210, 680)
        MainWindow.setMinimumSize(QtCore.QSize(1210, 680))
        MainWindow.setMaximumSize(QtCore.QSize(1210, 680))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"imgs\bac.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, -10, 1212, 691))
        self.background.setMinimumSize(QtCore.QSize(1212, 680))
        self.background.setAutoFillBackground(False)
        self.background.setStyleSheet("background-image: url(.\imgs\login.PNG);")
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(r"imgs\login.PNG"))
        self.background.setScaledContents(True)
        self.background.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.background.setObjectName("background")
        self.inputEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.inputEmail.setGeometry(QtCore.QRect(180, 280, 250, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputEmail.sizePolicy().hasHeightForWidth())
        self.inputEmail.setSizePolicy(sizePolicy)
        self.inputEmail.setMinimumSize(QtCore.QSize(250, 50))
        self.inputEmail.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.inputEmail.setFont(font)
        self.inputEmail.setTabletTracking(False)
        self.inputEmail.setAutoFillBackground(False)
        self.inputEmail.setStyleSheet(" border: 3px solid #032066;  border-radius: 15px;")
        self.inputEmail.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inputEmail.setObjectName("inputEmail")
        self.btnSignIn = QtWidgets.QPushButton(self.centralwidget)
        self.btnSignIn.setGeometry(QtCore.QRect(220, 440, 160, 45))
        self.btnSignIn.setMinimumSize(QtCore.QSize(160, 45))
        self.btnSignIn.setMaximumSize(QtCore.QSize(160, 45))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnSignIn.setFont(font)
        self.btnSignIn.setStyleSheet("#btnSignIn{\n"
"    background-color: #2CD697; border: 0; border-radius:15px; color: #032066;\n"
"}\n"
"#btnSignIn:hover{\n"
"    background-color: #309F76; border: 0; border-radius:15px; color: #032066;\n"
"}")
        self.btnSignIn.setObjectName("btnSignIn")
        self.inputPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPassword.setGeometry(QtCore.QRect(180, 370, 250, 50))
        self.inputPassword.setMinimumSize(QtCore.QSize(250, 50))
        self.inputPassword.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.inputPassword.setFont(font)
        self.inputPassword.setAutoFillBackground(False)
        self.inputPassword.setStyleSheet(" border: 3px solid #032066;  border-radius: 15px;")
        self.inputPassword.setInputMask("")
        self.inputPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassword.setClearButtonEnabled(False)
        self.inputPassword.setObjectName("inputPassword")
        self.labelLoginError = QtWidgets.QLabel(self.centralwidget)
        self.labelLoginError.setGeometry(QtCore.QRect(160, 490, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.labelLoginError.setFont(font)
        self.labelLoginError.setStyleSheet("color: red;")
        self.labelLoginError.setText("")
        self.labelLoginError.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLoginError.setObjectName("labelLoginError")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stock Manager"))
        self.btnSignIn.setText(_translate("MainWindow", "Sign in"))

