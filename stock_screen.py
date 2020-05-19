# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stock_screen.ui'
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
        self.background.setStyleSheet("background-color: #032066;background-image: url(.\imgs\stock.PNG);")
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(r"imgs\stock.PNG"))
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
"    background-color: #ffffff; border: 0; border-radius:15px; color:#2CD697;\n"
"}\n"
"#btnAddProduct:hover{\n"
"    background-color: #D9D9D9; border: 0; border-radius:15px; color: #2CD697;\n"
"}")
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
"    background-color: #D9D9D9; border: 0; border-radius:15px; color: #2CD697;\n"
"}\n"
"")
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 160, 71, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(20, 25))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#2CD697;\n"
"")
        self.label.setObjectName("label")
        self.tableStock = QtWidgets.QTableWidget(self.centralwidget)
        self.tableStock.setGeometry(QtCore.QRect(110, 220, 990, 365))
        self.tableStock.setMinimumSize(QtCore.QSize(990, 365))
        self.tableStock.setMaximumSize(QtCore.QSize(990, 365))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(16)
        self.tableStock.setFont(font)
        self.tableStock.setStyleSheet("background-color: #D9D9D9; color: #2CD697; border:0;")
        self.tableStock.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableStock.setRowCount(0)
        self.tableStock.setObjectName("tableStock")
        self.tableStock.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableStock.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableStock.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableStock.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableStock.setHorizontalHeaderItem(3, item)
        self.tableStock.horizontalHeader().setVisible(True)
        self.tableStock.horizontalHeader().setCascadingSectionResizes(False)
        self.tableStock.horizontalHeader().setDefaultSectionSize(240)
        self.tableStock.verticalHeader().setVisible(False)
        self.lineSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.lineSearch.setGeometry(QtCore.QRect(180, 160, 520, 35))
        self.lineSearch.setMinimumSize(QtCore.QSize(520, 35))
        self.lineSearch.setMaximumSize(QtCore.QSize(520, 35))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(13)
        self.lineSearch.setFont(font)
        self.lineSearch.setStyleSheet("border: 0; border-bottom: 2px solid #2CD697;")
        self.lineSearch.setObjectName("lineSearch")
        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearch.setGeometry(QtCore.QRect(730, 150, 100, 45))
        self.btnSearch.setMinimumSize(QtCore.QSize(100, 45))
        self.btnSearch.setMaximumSize(QtCore.QSize(100, 45))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnSearch.setFont(font)
        self.btnSearch.setStyleSheet("#btnSearch{\n"
"    background-color: #2CD697; border: 0; border-radius:15px; color:white;\n"
"}\n"
"#btnSearch:hover{\n"
"    background-color: #309F76; border: 0; border-radius:15px; color: white;\n"
"}")
        self.btnSearch.setObjectName("btnSearch")
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
        self.label.setText(_translate("MainWindow", "Stock:"))
        item = self.tableStock.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableStock.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product"))
        item = self.tableStock.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableStock.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Price"))
        self.lineSearch.setPlaceholderText(_translate("MainWindow", "Id"))
        self.btnSearch.setText(_translate("MainWindow", "Search"))

