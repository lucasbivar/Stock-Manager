# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_employee_screen.ui'
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
        MainWindow.setStyleSheet("")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 1212, 680))
        self.background.setMinimumSize(QtCore.QSize(1212, 680))
        self.background.setMaximumSize(QtCore.QSize(1212, 680))
        self.background.setAutoFillBackground(False)
        self.background.setStyleSheet("background-image: url(.\imgs\employee.PNG);")
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(r"imgs\employee.PNG"))
        self.background.setScaledContents(False)
        self.background.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.background.setObjectName("background")
        self.btnSignOut = QtWidgets.QPushButton(self.centralwidget)
        self.btnSignOut.setGeometry(QtCore.QRect(1060, 20, 100, 45))
        self.btnSignOut.setMinimumSize(QtCore.QSize(100, 45))
        self.btnSignOut.setMaximumSize(QtCore.QSize(100, 45))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnSignOut.setFont(font)
        self.btnSignOut.setStyleSheet("#btnSignOut{\n"
"    background-color: #2CD697; border: 0; border-radius:15px; color:white;\n"
"}\n"
"#btnSignOut:hover{\n"
"    background-color: #309F76; border: 0; border-radius:15px; color: white;\n"
"}")
        self.btnSignOut.setObjectName("btnSignOut")
        self.btnRegisterEmployee = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegisterEmployee.setGeometry(QtCore.QRect(870, 20, 160, 45))
        self.btnRegisterEmployee.setMinimumSize(QtCore.QSize(160, 45))
        self.btnRegisterEmployee.setMaximumSize(QtCore.QSize(160, 45))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnRegisterEmployee.setFont(font)
        self.btnRegisterEmployee.setStyleSheet("#btnRegisterEmployee{\n"
"    background-color: #D9D9D9; border: 0; border-radius:15px; color:#2CD697;\n"
"}\n"
"")
        self.btnRegisterEmployee.setObjectName("btnRegisterEmployee")
        self.btnAddProduct = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddProduct.setGeometry(QtCore.QRect(670, 20, 160, 45))
        self.btnAddProduct.setMinimumSize(QtCore.QSize(160, 45))
        self.btnAddProduct.setMaximumSize(QtCore.QSize(160, 45))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnAddProduct.setFont(font)
        self.btnAddProduct.setStyleSheet("#btnAddProduct{\n"
"    background-color: #ffffff; border: 0; border-radius:15px; color:#2CD697;\n"
"}\n"
"#btnAddProduct:hover{\n"
"    background-color: #D9D9D9; border: 0; border-radius:15px; color:#2CD697;\n"
"}\n"
"")
        self.btnAddProduct.setObjectName("btnAddProduct")
        self.btnStock = QtWidgets.QPushButton(self.centralwidget)
        self.btnStock.setGeometry(QtCore.QRect(480, 20, 160, 45))
        self.btnStock.setMinimumSize(QtCore.QSize(160, 45))
        self.btnStock.setMaximumSize(QtCore.QSize(160, 45))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnStock.setFont(font)
        self.btnStock.setStyleSheet("#btnStock{\n"
"    background-color: #ffffff; border: 0; border-radius:15px; color: #2CD697;\n"
"}\n"
"#btnStock:hover{\n"
"    background-color: #D9D9D9; border: 0; border-radius:15px; color: #2CD697;\n"
"}")
        self.btnStock.setObjectName("btnStock")
        self.btnSale = QtWidgets.QPushButton(self.centralwidget)
        self.btnSale.setGeometry(QtCore.QRect(290, 20, 160, 45))
        self.btnSale.setMinimumSize(QtCore.QSize(160, 45))
        self.btnSale.setMaximumSize(QtCore.QSize(160, 45))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnSale.setFont(font)
        self.btnSale.setStyleSheet("#btnSale{\n"
"    background-color: #ffffff; border: 0; border-radius:15px; color: #2CD697;\n"
"}\n"
"#btnSale:hover{\n"
"    background-color: #D9D9D9; border: 0; border-radius:15px; color: #2CD697;\n"
"}")
        self.btnSale.setObjectName("btnSale")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(50, 10, 80, 65))
        self.logo.setMinimumSize(QtCore.QSize(80, 65))
        self.logo.setMaximumSize(QtCore.QSize(80, 65))
        self.logo.setAutoFillBackground(False)
        self.logo.setStyleSheet(r"background-image: url(.\imgs\background_component.png);")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(r"imgs\background_component.png"))
        self.logo.setScaledContents(True)
        self.logo.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.logo.setObjectName("logo")
        self.labelName = QtWidgets.QLineEdit(self.centralwidget)
        self.labelName.setEnabled(False)
        self.labelName.setGeometry(QtCore.QRect(130, 20, 157, 30))
        self.labelName.setMinimumSize(QtCore.QSize(157, 30))
        self.labelName.setMaximumSize(QtCore.QSize(157, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(13)
        self.labelName.setFont(font)
        self.labelName.setStyleSheet("border: 0; background-color: #032066; color: #ffffff;")
        self.labelName.setObjectName("labelName")
        self.labelJob = QtWidgets.QLineEdit(self.centralwidget)
        self.labelJob.setEnabled(False)
        self.labelJob.setGeometry(QtCore.QRect(130, 50, 157, 16))
        self.labelJob.setMinimumSize(QtCore.QSize(157, 16))
        self.labelJob.setMaximumSize(QtCore.QSize(157, 16))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(13)
        self.labelJob.setFont(font)
        self.labelJob.setStyleSheet("border: 0; background-color: #032066; color: #ffffff;")
        self.labelJob.setObjectName("labelJob")
        self.btnDelete = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelete.setGeometry(QtCore.QRect(710, 470, 100, 45))
        self.btnDelete.setMinimumSize(QtCore.QSize(100, 45))
        self.btnDelete.setMaximumSize(QtCore.QSize(100, 45))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnDelete.setFont(font)
        self.btnDelete.setStyleSheet("#btnDelete{\n"
"    background-color: #2CD697; border: 0; border-radius:15px; color:white;\n"
"}\n"
"#btnDelete:hover{\n"
"    background-color: #309F76; border: 0; border-radius:15px; color: white;\n"
"}")
        self.btnDelete.setObjectName("btnDelete")
        self.btnRegisterNewEmployee = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegisterNewEmployee.setGeometry(QtCore.QRect(490, 470, 210, 45))
        self.btnRegisterNewEmployee.setMinimumSize(QtCore.QSize(210, 45))
        self.btnRegisterNewEmployee.setMaximumSize(QtCore.QSize(210, 45))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnRegisterNewEmployee.setFont(font)
        self.btnRegisterNewEmployee.setStyleSheet("#btnRegisterNewEmployee{\n"
"    background-color: #2CD697; border: 0; border-radius:15px; color:white;\n"
"}\n"
"#btnRegisterNewEmployee:hover{\n"
"    background-color: #309F76; border: 0; border-radius:15px; color: white;\n"
"}")
        self.btnRegisterNewEmployee.setObjectName("btnRegisterNewEmployee")
        self.inputName = QtWidgets.QLineEdit(self.centralwidget)
        self.inputName.setGeometry(QtCore.QRect(260, 160, 550, 20))
        self.inputName.setMinimumSize(QtCore.QSize(550, 20))
        self.inputName.setMaximumSize(QtCore.QSize(550, 20))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(13)
        self.inputName.setFont(font)
        self.inputName.setStyleSheet("border: 0; border-bottom: 2px solid #2CD697; background: #ffffff;\n"
"")
        self.inputName.setPlaceholderText("")
        self.inputName.setObjectName("inputName")
        self.inputUserName = QtWidgets.QLineEdit(self.centralwidget)
        self.inputUserName.setGeometry(QtCore.QRect(260, 200, 550, 20))
        self.inputUserName.setMinimumSize(QtCore.QSize(550, 20))
        self.inputUserName.setMaximumSize(QtCore.QSize(550, 20))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(13)
        self.inputUserName.setFont(font)
        self.inputUserName.setStyleSheet("border: 0; border-bottom: 2px solid #2CD697; background: #ffffff;\n"
"")
        self.inputUserName.setPlaceholderText("")
        self.inputUserName.setObjectName("inputUserName")
        self.inputEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.inputEmail.setGeometry(QtCore.QRect(260, 250, 550, 20))
        self.inputEmail.setMinimumSize(QtCore.QSize(550, 20))
        self.inputEmail.setMaximumSize(QtCore.QSize(550, 20))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(13)
        self.inputEmail.setFont(font)
        self.inputEmail.setStyleSheet("border: 0; border-bottom: 2px solid #2CD697; background: #ffffff;\n"
"")
        self.inputEmail.setPlaceholderText("")
        self.inputEmail.setObjectName("inputEmail")
        self.inputPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPassword.setGeometry(QtCore.QRect(260, 290, 550, 20))
        self.inputPassword.setMinimumSize(QtCore.QSize(550, 20))
        self.inputPassword.setMaximumSize(QtCore.QSize(550, 20))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(13)
        self.inputPassword.setFont(font)
        self.inputPassword.setStyleSheet("border: 0; border-bottom: 2px solid #2CD697; background: #ffffff;\n"
"")
        self.inputPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassword.setPlaceholderText("")
        self.inputPassword.setObjectName("inputPassword")
        self.inputPhone = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPhone.setGeometry(QtCore.QRect(260, 340, 550, 20))
        self.inputPhone.setMinimumSize(QtCore.QSize(550, 20))
        self.inputPhone.setMaximumSize(QtCore.QSize(550, 20))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(13)
        self.inputPhone.setFont(font)
        self.inputPhone.setStyleSheet("border: 0; border-bottom: 2px solid #2CD697; background: #ffffff;\n"
"")
        self.inputPhone.setPlaceholderText("")
        self.inputPhone.setObjectName("inputPhone")
        self.inputJob = QtWidgets.QLineEdit(self.centralwidget)
        self.inputJob.setGeometry(QtCore.QRect(260, 380, 550, 20))
        self.inputJob.setMinimumSize(QtCore.QSize(550, 20))
        self.inputJob.setMaximumSize(QtCore.QSize(550, 20))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(13)
        self.inputJob.setFont(font)
        self.inputJob.setStyleSheet("border: 0; border-bottom: 2px solid #2CD697; background: #ffffff;\n"
"")
        self.inputJob.setPlaceholderText("")
        self.inputJob.setObjectName("inputJob")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stock Manager"))
        self.btnSignOut.setText(_translate("MainWindow", "Sign out"))
        self.btnRegisterEmployee.setText(_translate("MainWindow", "Register employee"))
        self.btnAddProduct.setText(_translate("MainWindow", "Add product"))
        self.btnStock.setText(_translate("MainWindow", "Stock"))
        self.btnSale.setText(_translate("MainWindow", "Sale"))
        self.btnDelete.setText(_translate("MainWindow", "Delete"))
        self.btnRegisterNewEmployee.setText(_translate("MainWindow", "Register new employee"))

