import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QApplication
from Front.mainmenu import Ui_main_menu
from Front.forgotmypassword import Ui_forgot_password_page
import sys

class Ui_RMS(object):
    def __init__(self):
        self.login_button =  QtWidgets.QPushButton(RMS)
        self.username_label = QtWidgets.QLabel(RMS)
        self.username_linedit = QtWidgets.QLineEdit(RMS)
        self.password_label = QtWidgets.QLabel(RMS)
        self.loginpage_label = QtWidgets.QLabel(RMS)
        self.forgot_link = QtWidgets.QCommandLinkButton(RMS)
        self.login_button.clicked.connect(self.window2)
        self.forgot_link.clicked.connect(self.window3)

    def window2(self):
        self.w = Ui_main_menu()
        self.setup = self.w.setupUi(self.w)
        self.w.main_menu.show()

    def window3(self):
        self.x = Ui_forgot_password_page()
        self.setupf = self.x.setupUi(self.x)
        self.x.forgot_password_page.show()

    def setupUi(self, RMS):
        RMS.setObjectName("RMS")
        RMS.resize(395, 415)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        RMS.setFont(font)

        self.login_button.setGeometry(QtCore.QRect(240, 360, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")
        self.retranslateUi(RMS)
        QtCore.QMetaObject.connectSlotsByName(RMS)

        self.username_label.setGeometry(QtCore.QRect(40, 210, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.username_label.setFont(font)
        self.username_label.setTextFormat(QtCore.Qt.AutoText)
        self.username_label.setObjectName("username_label")

        self.username_linedit.setGeometry(QtCore.QRect(40, 250, 181, 22))
        self.username_linedit.setObjectName("username_linedit")

        self.password_label.setGeometry(QtCore.QRect(40, 290, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.password_linedit = QtWidgets.QLineEdit(RMS)
        self.password_linedit.setGeometry(QtCore.QRect(40, 320, 181, 22))
        self.password_linedit.setObjectName("password_linedit")

        self.forgot_link.setGeometry(QtCore.QRect(0, 360, 231, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.forgot_link.setFont(font)
        self.forgot_link.setObjectName("forgot_link")

        self.loginpage_label.setGeometry(QtCore.QRect(130, -10, 141, 101))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.loginpage_label.setFont(font)
        self.loginpage_label.setObjectName("loginpage_label")

    def retranslateUi(self, RMS):
        _translate = QtCore.QCoreApplication.translate
        RMS.setWindowTitle(_translate("RMS", "RMS"))
        self.login_button.setText(_translate("RMS", "Login"))
        self.username_label.setText(_translate("RMS", "Username"))
        self.password_label.setText(_translate("RMS", "Password"))
        self.forgot_link.setText(_translate("RMS", "Forgot my password"))
        self.loginpage_label.setText(_translate("RMS", "LOGIN PAGE"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RMS = QtWidgets.QDialog()
    ui = Ui_RMS()
    ui.setupUi(RMS)
    RMS.show()
    sys.exit(app.exec_())
