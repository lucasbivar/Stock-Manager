import sys
import os
import sqlite3
import platform
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
import login_screen, sale_screen, stock_screen, add_product_screen, register_employee_screen
from coupons import template
from time import sleep
from datetime import datetime


class StockManagerLogin(QMainWindow, login_screen.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnSignIn.clicked.connect(self.check_login_db)
        self.inputPassword.returnPressed.connect(self.check_login_db)

    def check_login_db(self):
        sleep(1)
        try:
            connection = sqlite3.connect(r'data_base.db')
            cursor = connection.cursor()

            cursor.execute('SELECT EMAIL, PASSWORD, USER_NAME, JOB_ROLE FROM employees WHERE EMAIL = :EMAIL AND PASSWORD = :PASSWORD',
                           {'EMAIL': self.inputEmail.text(), 'PASSWORD': self.inputPassword.text()})

            check = list(cursor.fetchall())

            cursor.close()
            connection.close()

            if len(check) != 0:
                _, _, user, job = check[0]

                connection = sqlite3.connect(r'data_base.db')
                cursor = connection.cursor()

                cursor.execute('''UPDATE current SET JOB_ROLE = ? WHERE ID = ?''', (job, 1))
                connection.commit()
                cursor.execute('''UPDATE current SET USER_NAME = ? WHERE ID = ?''', (user, 1))
                connection.commit()

                cursor.close()
                connection.close()

                stock_manager_login.hide()
                stock_manager_sale.set_perfil()
                stock_manager_stock.set_perfil()
                stock_manager_add_product.set_perfil()
                stock_manager_register_employee.set_perfil()
                stock_manager_sale.show()

            else:
                self.labelLoginError.setText('User or password invalid. Try again!')
                self.inputEmail.setText('')
                self.inputPassword.setText('')

        except Exception as e:
            self.labelLoginError.setText('Data base error!')

        finally:
            self.inputEmail.setText('')
            self.inputPassword.setText('')


class StockManagerSale(QMainWindow, sale_screen.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.labelGrandTotal.setText('0')
        self.labelTotal.setText('0')
        self.labelChange.setText('0')
        self.labelDiscount.setText('0')
        self.inputMoneyReceived.setText('0')
        self.btnAddProduct.clicked.connect(self.go_to_add_product)
        self.btnSignOut.clicked.connect(self.back_login)
        self.btnStock.clicked.connect(self.go_to_stock)
        self.btnRegisterEmployee.clicked.connect(self.go_to_register_employee)
        self.btnAdd.clicked.connect(self.add_to_cart)
        self.btnDelete.clicked.connect(self.delete_all)
        self.btnCheckout.clicked.connect(self.checkout)

    def set_perfil(self):
        connection = sqlite3.connect(r'data_base.db')
        cursor = connection.cursor()
        cursor.execute('SELECT USER_NAME, JOB_ROLE FROM current WHERE ID=:id',
                    {'id': 1})
        perfil = list(cursor.fetchall())
        user, job = perfil[0]
        self.labelName.setText(user)
        self.labelJob.setText(job)
        cursor.close()
        connection.close()

    def add_to_cart(self):
        if self.inputId.text() != '':
            connection = sqlite3.connect(r'data_base.db')
            cursor = connection.cursor()
            query = f"SELECT PRODUCT, QUANTITY, PRICE FROM products WHERE ID = {int(self.inputId.text())}"
            cursor.execute(query)
            check = cursor.fetchall()
            if len(check) == 1:
                for items in check:
                    product, quantity, price = items
                cursor.close()
                connection.close()
                if quantity > 0:
                    numRows = self.tableShoppingCart.rowCount()
                    self.tableShoppingCart.insertRow(numRows)
                    self.tableShoppingCart.setItem(numRows, 0, QTableWidgetItem(self.inputId.text()))
                    self.tableShoppingCart.setItem(numRows, 1, QTableWidgetItem(str(product)))
                    self.tableShoppingCart.setItem(numRows, 2, QTableWidgetItem(self.inputQuantity.text()))
                    self.tableShoppingCart.setItem(numRows, 3, QTableWidgetItem(str(price)))
                    subtotal = int(self.inputQuantity.text()) * float(price)
                    self.tableShoppingCart.setItem(numRows, 4, QTableWidgetItem(f'{subtotal:.2f}'))
                    total = float(self.labelTotal.text()) + subtotal
                    grand_total = float(self.labelGrandTotal.text()) + subtotal
                    self.labelTotal.setText(f'{total:.2f}')
                    self.labelGrandTotal.setText(f'{grand_total:.2f}')
                    self.inputQuantity.setText('')
                    self.inputId.setText('')
                else:
                    self.inputQuantity.setText('')
                    self.inputId.setText('')
                    msg = QMessageBox()
                    msg.setWindowTitle("Stock Manager")
                    msg.setText("Product unavailable!")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
            else:
                cursor.close()
                connection.close()
                self.inputQuantity.setText('')
                self.inputId.setText('')
                msg = QMessageBox()
                msg.setWindowTitle("Stock Manager")
                msg.setText("No product found with this id!")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
        else:
            self.inputQuantity.setText('')
            self.inputId.setText('')
            msg = QMessageBox()
            msg.setWindowTitle("Stock Manager")
            msg.setText("Id empty!")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()

    def checkout(self):
        if self.inputClient.text() == '':
            self.inputClient.setText('Empty')

        if self.inputDiscount.text() == '':
            self.labelDiscount.setText('None')
        else:
            self.labelDiscount.setText(self.inputDiscount.text())
            new_grand_total = float(self.labelTotal.text()) - ((float(self.labelTotal.text()) * float(self.inputDiscount.text().replace(',', '.')))/100)
            self.labelGrandTotal.setText(f'{new_grand_total:.2f}')

        change = float(self.inputMoneyReceived.text()) - float(self.labelGrandTotal.text())
        self.labelChange.setText(f'{change:.2f}')

        msg = QMessageBox.question(self, 'Stock Manager', "Are you sure that you want to complete your purchase?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if msg == QMessageBox.Yes:
            connection = sqlite3.connect(r'data_base.db')
            cursor = connection.cursor()
            numRows = self.tableShoppingCart.rowCount()
            for row in range(numRows):
                quantity = self.tableShoppingCart.item(row, 2).text()
                id_product = self.tableShoppingCart.item(row, 0).text()
                cursor.execute(f'''UPDATE products SET QUANTITY = QUANTITY - {int(quantity)} WHERE ID = {id_product}''')
                connection.commit()
            cursor.close()
            connection.close()


            text_lines = [['Id', 'Product:', 'Quantity:', 'Unit price:', 'Subtotal:']]
            for row in range(numRows):
                new_list = []
                for column in range(0, 5):
                    new_list.append(self.tableShoppingCart.item(row, column).text())
                text_lines.append(new_list)

            final_lines = [['Name:', 'Change:', 'Total:', 'Discount:', 'Grand total:']]
            final_lines.append([self.inputClient.text(), self.labelChange.text(), self.labelTotal.text(),
                                self.labelDiscount.text(), self.labelGrandTotal.text()])
            if self.btnYes.isChecked():
                if platform.system() == 'Windows':
                    os.startfile(template.generate_coupon(text_lines, final_lines, self.inputClient.text(), print=True))
                else:
                    template.generate_coupon(text_lines, final_lines, self.inputClient.text())
                    msg = QMessageBox()
                    msg.setWindowTitle("Stock Manager")
                    msg.setText("It is not possible to print the file on your operational system, you can find the pdf in the program folder!")
                    msg.setIcon(QMessageBox.Information)
                    msg.exec_()
            else:
                template.generate_coupon(text_lines, final_lines, self.inputClient.text())

            dt = datetime.now()
            date = dt.strftime('%d/%m/%Y')
            hour = dt.strftime('%H:%M')

            connection = sqlite3.connect(r'data_base.db')
            cursor = connection.cursor()

            cursor.execute('INSERT INTO sales (DATE, HOUR, GRAND_TOTAL, CLIENT) VALUES (:date, :hour, :grand_total, :client)',
                           {
                            'date': date, 'hour': hour, 'grand_total': float(self.labelGrandTotal.text()),
                            'client': self.inputClient.text()
                            })
            connection.commit()
            
            cursor.close()
            connection.close()

            self.delete_all()

    def delete_all(self):
        self.inputId.setText('')
        self.inputQuantity.setText('')

        numRows = self.tableShoppingCart.rowCount()
        for n in range(numRows):
            self.tableShoppingCart.removeRow(0)

        self.labelGrandTotal.setText('0')
        self.labelTotal.setText('0')
        self.labelChange.setText('0')
        self.labelDiscount.setText('0')
        self.inputClient.setText('')
        self.inputQuantity.setText('')
        self.inputDiscount.setText('')
        self.inputMoneyReceived.setText('')
        if self.btnYes.isChecked():
            self.btnYes.setChecked(False)
        if self.btnNo.isChecked():
            self.btnNo.setChecked(False)

    def back_login(self):
        stock_manager_sale.hide()
        stock_manager_login.show()

    def go_to_add_product(self):
        stock_manager_sale.hide()
        stock_manager_add_product.show()

    def go_to_stock(self):
        stock_manager_sale.hide()
        stock_manager_stock.load_product_data()
        stock_manager_stock.show()

    def go_to_register_employee(self):
        stock_manager_sale.hide()
        stock_manager_register_employee.show()


class StockManagerStock(QMainWindow, stock_screen.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.load_product_data()
        self.btnSignOut.clicked.connect(self.back_login)
        self.btnSale.clicked.connect(self.go_to_sale)
        self.btnAddProduct.clicked.connect(self.go_to_add_product)
        self.btnRegisterEmployee.clicked.connect(self.go_to_register_employ)
        self.btnSearch.clicked.connect(self.find_product_id)
        self.lineSearch.returnPressed.connect(self.find_product_id)

    def set_perfil(self):
        connection = sqlite3.connect(r'data_base.db')
        cursor = connection.cursor()
        cursor.execute('SELECT USER_NAME, JOB_ROLE FROM current WHERE ID=:id',
                    {'id': 1})
        perfil = list(cursor.fetchall())
        user, job = perfil[0]
        self.labelName.setText(user)
        self.labelJob.setText(job)
        cursor.close()
        connection.close()

    def load_product_data(self):
        connection = sqlite3.connect(r'data_base.db')
        query = "SELECT * FROM products"
        result = connection.execute(query)
        self.tableStock.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableStock.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableStock.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        connection.close()

    def find_product_id(self):
        connection = sqlite3.connect(r'data_base.db')
        if self.lineSearch.text() == '':
            query = "SELECT * FROM products"
        else:
            query = f"SELECT * FROM products WHERE ID = {self.lineSearch.text()}"
        result = connection.execute(query)
        self.tableStock.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableStock.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableStock.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        connection.close()

    def back_login(self):
        stock_manager_stock.hide()
        stock_manager_login.show()

    def go_to_sale(self):
        stock_manager_stock.hide()
        stock_manager_sale.show()

    def go_to_add_product(self):
        stock_manager_stock.hide()
        stock_manager_add_product.show()

    def go_to_register_employ(self):
        stock_manager_stock.hide()
        stock_manager_register_employee.show()


class StockManagerAddProduct(QMainWindow, add_product_screen.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnSignOut.clicked.connect(self.back_login)
        self.btnSale.clicked.connect(self.go_to_sale)
        self.btnStock.clicked.connect(self.go_to_stock)
        self.btnRegisterEmployee.clicked.connect(self.go_to_register_employee)
        self.btnAddNew.clicked.connect(self.add_new_product)
        self.btnAdd.clicked.connect(self.add_product)

    def set_perfil(self):
        connection = sqlite3.connect(r'data_base.db')
        cursor = connection.cursor()
        cursor.execute('SELECT USER_NAME, JOB_ROLE FROM current WHERE ID=:id',
                    {'id': 1})
        perfil = list(cursor.fetchall())
        user, job = perfil[0]
        self.labelName.setText(user)
        self.labelJob.setText(job)
        cursor.close()
        connection.close()

    def add_new_product(self):
        connection = sqlite3.connect(r'data_base.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO products (PRODUCT, QUANTITY, PRICE) VALUES (:product, :quantity, :price)',
                           {
                            'product': self.inputProductNew.text().strip().title(), 'quantity': int(self.inputQuantityNew.text()),
                            'price': float(self.inputPriceNew.text().replace(',', '.'))
                            })
        connection.commit()
        cursor.close()
        connection.close()
        msg = QMessageBox()
        msg.setWindowTitle("Stock Manager")
        msg.setText("New product successfully added!")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
        self.inputProductNew.setText('')
        self.inputPriceNew.setText('')
        self.inputQuantityNew.setText('')

    def add_product(self):
        connection = sqlite3.connect(r'data_base.db')
        cursor = connection.cursor()
        cursor.execute(f'''UPDATE products SET QUANTITY = QUANTITY + {int(self.inputQuantity.text())} WHERE ID = {self.inputId.text()}''')
        connection.commit()
        msg = QMessageBox()
        msg.setWindowTitle("Stock Manager")
        msg.setText("Product successfully actualized!")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
        self.inputQuantity.setText('')
        self.inputId.setText('')

    def back_login(self):
        stock_manager_add_product.hide()
        stock_manager_login.show()

    def go_to_stock(self):
        stock_manager_stock.load_product_data()
        stock_manager_add_product.hide()
        stock_manager_stock.show()

    def go_to_sale(self):
        stock_manager_add_product.hide()
        stock_manager_sale.show()

    def go_to_register_employee(self):
        stock_manager_add_product.hide()
        stock_manager_register_employee.show()


class StockManagerRegisterEmployee(QMainWindow, register_employee_screen.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnSignOut.clicked.connect(self.back_login)
        self.btnSale.clicked.connect(self.go_to_sale)
        self.btnStock.clicked.connect(self.go_to_stock)
        self.btnAddProduct.clicked.connect(self.go_to_add_product)
        self.btnDelete.clicked.connect(self.delete_all)
        self.btnRegisterNewEmployee.clicked.connect(self.register_new_employee)

    def set_perfil(self):
        connection = sqlite3.connect(r'data_base.db')
        cursor = connection.cursor()
        cursor.execute('SELECT USER_NAME, JOB_ROLE FROM current WHERE ID=:id',
                    {'id': 1})
        perfil = list(cursor.fetchall())
        user, job = perfil[0]
        self.labelName.setText(user)
        self.labelJob.setText(job)
        cursor.close()
        connection.close()

    def register_new_employee(self):
        if self.labelJob.text().strip() == 'Owner':
            connection = sqlite3.connect(r'data_base.db')
            cursor = connection.cursor()
            cursor.execute('INSERT INTO employees (NAME, USER_NAME, EMAIL, PASSWORD, PHONE_NUMBER, JOB_ROLE) VALUES (:name, :user_name, :email, :password, :phone_number, :job_role)',
                           {
                               'name': self.inputName.text().title().strip(), 'user_name': self.inputUserName.text().title().strip(), 'email': self.inputEmail.text().strip(),
                               'password': self.inputPassword.text().strip(), 'phone_number': self.inputPhone.text().strip(), 'job_role': self.inputJob.text().capitalize().strip()
                            })
            connection.commit()
            cursor.close()
            connection.close()
            msg = QMessageBox()
            msg.setWindowTitle("Stock Manager")
            msg.setText("Employee successfully registered!")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
            self.inputName.setText('')
            self.inputUserName.setText('')
            self.inputEmail.setText('')
            self.inputPassword.setText('')
            self.inputPhone.setText('')
            self.inputJob.setText('')
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Stock Manager")
            msg.setText("You don't have permission to register a new employee!")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()

    def delete_all(self):
        self.inputName.setText('')
        self.inputUserName.setText('')
        self.inputEmail.setText('')
        self.inputPassword.setText('')
        self.inputPhone.setText('')
        self.inputJob.setText('')

    def back_login(self):
        stock_manager_register_employee.hide()
        stock_manager_login.show()

    def go_to_stock(self):
        stock_manager_stock.load_product_data()
        stock_manager_register_employee.hide()
        stock_manager_stock.show()

    def go_to_sale(self):
        stock_manager_register_employee.hide()
        stock_manager_sale.show()

    def go_to_add_product(self):
        stock_manager_register_employee.hide()
        stock_manager_add_product.show()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    stock_manager_login = StockManagerLogin()
    stock_manager_sale = StockManagerSale()
    stock_manager_stock = StockManagerStock()
    stock_manager_add_product = StockManagerAddProduct()
    stock_manager_register_employee = StockManagerRegisterEmployee()
    stock_manager_login.show()
    qt.exec_()
