from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMainWindow



class Ui_main_menu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window22222")
        self.main_menu = QtWidgets.QDialog()
        self.setupUi(self.main_menu)








    def setupUi(self, main_menu):
        main_menu.setObjectName("main_menu")
        main_menu.resize(464, 476)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        main_menu.setFont(font)
        self.orderhistory_btn = QtWidgets.QPushButton(main_menu)
        self.orderhistory_btn.setGeometry(QtCore.QRect(10, 250, 141, 201))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.orderhistory_btn.setFont(font)
        self.orderhistory_btn.setObjectName("orderhistory_btn")
        self.employeeinfo_btn = QtWidgets.QPushButton(main_menu)
        self.employeeinfo_btn.setGeometry(QtCore.QRect(160, 250, 141, 201))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.employeeinfo_btn.setFont(font)
        self.employeeinfo_btn.setObjectName("employeeinfo_btn")
        self.order_btn = QtWidgets.QPushButton(main_menu)
        self.order_btn.setGeometry(QtCore.QRect(310, 250, 141, 201))
        self.order_btn.setObjectName("order_btn")

        self.retranslateUi(main_menu)
        QtCore.QMetaObject.connectSlotsByName(main_menu)

    def retranslateUi(self, main_menu):
        _translate = QtCore.QCoreApplication.translate
        main_menu.setWindowTitle(_translate("main_menu", "Main Menu"))
        self.orderhistory_btn.setText(_translate("main_menu", "Order History"))
        self.employeeinfo_btn.setText(_translate("main_menu", "Employee Info"))
        self.order_btn.setText(_translate("main_menu", "Order"))

    def main_menu_window(self):
        main_menu = QtWidgets.QDialog()
        ui = Ui_main_menu()
        ui.setupUi(main_menu)
        main_menu.show()
        #sys.exit(app.exec_())





