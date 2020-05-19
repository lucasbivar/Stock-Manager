# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_product_screen.ui'
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
        self.background.setStyleSheet(r"background-image: url(.\imgs\add.PNG);")
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(r"imgs\add.PNG"))
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
"    background-color: #ffffff; border: 0; border-radius:15px; color:#2CD697;\n"
"}\n"
"#btnRegisterEmployee:hover{\n"
"    background-color: #D9D9D9; border: 0; border-radius:15px; color: #2CD697;\n"
"}")
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
        self.btnAddNew = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddNew.setGeometry(QtCore.QRect(980, 230, 100, 45))
        self.btnAddNew.setMinimumSize(QtCore.QSize(100, 45))
        self.btnAddNew.setMaximumSize(QtCore.QSize(100, 45))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnAddNew.setFont(font)
        self.btnAddNew.setStyleSheet("#btnAddNew{\n"
"    background-color: #2CD697; border: 0; border-radius:15px; color:white;\n"
"}\n"
"#btnAddNew:hover{\n"
"    background-color: #309F76; border: 0; border-radius:15px; color: white;\n"
"}")
        self.btnAddNew.setObjectName("btnAddNew")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(980, 390, 100, 45))
        self.btnAdd.setMinimumSize(QtCore.QSize(100, 45))
        self.btnAdd.setMaximumSize(QtCore.QSize(100, 45))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnAdd.setFont(font)
        self.btnAdd.setStyleSheet("#btnAdd{\n"
"    background-color: #2CD697; border: 0; border-radius:15px; color:white;\n"
"}\n"
"#btnAdd:hover{\n"
"    background-color: #309F76; border: 0; border-radius:15px; color: white;\n"
"}")
        self.btnAdd.setObjectName("btnAdd")
        self.inputProductNew = QtWidgets.QLineEdit(self.centralwidget)
        self.inputProductNew.setGeometry(QtCore.QRect(190, 240, 200, 30))
        self.inputProductNew.setMinimumSize(QtCore.QSize(200, 30))
        self.inputProductNew.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(13)
        self.inputProductNew.setFont(font)
        self.inputProductNew.setStyleSheet("border: 0; border-bottom: 2px solid #2CD697; background: #D9D9D9;\n"
"")
        self.inputProductNew.setPlaceholderText("")
        self.inputProductNew.setObjectName("inputProductNew")
        self.inputQuantityNew = QtWidgets.QLineEdit(self.centralwidget)
        self.inputQuantityNew.setGeometry(QtCore.QRect(510, 240, 90, 30))
        self.inputQuantityNew.setMinimumSize(QtCore.QSize(90, 30))
        self.inputQuantityNew.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(13)
        self.inputQuantityNew.setFont(font)
        self.inputQuantityNew.setStyleSheet("border: 0; border-bottom: 2px solid #2CD697; background: #D9D9D9;\n"
"")
        self.inputQuantityNew.setPlaceholderText("")
        self.inputQuantityNew.setObjectName("inputQuantityNew")
        self.inputPriceNew = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPriceNew.setGeometry(QtCore.QRect(670, 240, 120, 30))
        self.inputPriceNew.setMinimumSize(QtCore.QSize(120, 30))
        self.inputPriceNew.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(13)
        self.inputPriceNew.setFont(font)
        self.inputPriceNew.setStyleSheet("border: 0; border-bottom: 2px solid #2CD697; background: #D9D9D9;\n"
"")
        self.inputPriceNew.setPlaceholderText("")
        self.inputPriceNew.setObjectName("inputPriceNew")
        self.inputId = QtWidgets.QLineEdit(self.centralwidget)
        self.inputId.setGeometry(QtCore.QRect(140, 400, 100, 30))
        self.inputId.setMinimumSize(QtCore.QSize(100, 30))
        self.inputId.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(13)
        self.inputId.setFont(font)
        self.inputId.setStyleSheet("border: 0; border-bottom: 2px solid #2CD697; background: #D9D9D9;\n"
"")
        self.inputId.setPlaceholderText("")
        self.inputId.setObjectName("inputId")
        self.inputQuantity = QtWidgets.QLineEdit(self.centralwidget)
        self.inputQuantity.setGeometry(QtCore.QRect(360, 400, 100, 30))
        self.inputQuantity.setMinimumSize(QtCore.QSize(100, 30))
        self.inputQuantity.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(13)
        self.inputQuantity.setFont(font)
        self.inputQuantity.setStyleSheet("border: 0; border-bottom: 2px solid #2CD697; background: #D9D9D9;\n"
"")
        self.inputQuantity.setPlaceholderText("")
        self.inputQuantity.setObjectName("inputQuantity")
        self.inputAlertNew = QtWidgets.QLineEdit(self.centralwidget)
        self.inputAlertNew.setGeometry(QtCore.QRect(810, 240, 150, 30))
        self.inputAlertNew.setMinimumSize(QtCore.QSize(150, 30))
        self.inputAlertNew.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(13)
        self.inputAlertNew.setFont(font)
        self.inputAlertNew.setStyleSheet("color: red; background: #D9D9D9; border: 0;\n"
"\n"
"")
        self.inputAlertNew.setPlaceholderText("")
        self.inputAlertNew.setObjectName("inputAlertNew")
        self.inputAlert = QtWidgets.QLineEdit(self.centralwidget)
        self.inputAlert.setGeometry(QtCore.QRect(820, 400, 150, 30))
        self.inputAlert.setMinimumSize(QtCore.QSize(150, 30))
        self.inputAlert.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(13)
        self.inputAlert.setFont(font)
        self.inputAlert.setStyleSheet("color: red; background: #D9D9D9; border: 0;\n"
"\n"
"")
        self.inputAlert.setPlaceholderText("")
        self.inputAlert.setObjectName("inputAlert")
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
        self.btnAddNew.setText(_translate("MainWindow", "Add"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
