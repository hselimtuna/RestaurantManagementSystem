
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

class Ui_forgot_password_page(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window1")
        self.forgot_password_page=QtWidgets.QDialog()
        self.setupUi(self.forgot_password_page)

    def setupUi(self, forgot_password_page):
        forgot_password_page.setObjectName("forgot_password_page")
        forgot_password_page.resize(480, 409)
        self.emailsender_label = QtWidgets.QLabel(forgot_password_page)
        self.emailsender_label.setGeometry(QtCore.QRect(60, 200, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.emailsender_label.setFont(font)
        self.emailsender_label.setObjectName("emailsender_label")
        self.lineEdit = QtWidgets.QLineEdit(forgot_password_page)
        self.lineEdit.setGeometry(QtCore.QRect(60, 250, 271, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.emailsender_btn = QtWidgets.QPushButton(forgot_password_page)
        self.emailsender_btn.setGeometry(QtCore.QRect(330, 290, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.emailsender_btn.setFont(font)
        self.emailsender_btn.setObjectName("emailsender_btn")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(forgot_password_page)
        self.commandLinkButton.setGeometry(QtCore.QRect(60, 290, 251, 48))
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.retranslateUi(forgot_password_page)
        QtCore.QMetaObject.connectSlotsByName(forgot_password_page)

    def retranslateUi(self, forgot_password_page):
        _translate = QtCore.QCoreApplication.translate
        forgot_password_page.setWindowTitle(_translate("forgot_password_page", "Forgot My Password"))
        self.emailsender_label.setText(_translate("forgot_password_page", "Please enter your e-mail address:"))
        self.emailsender_btn.setText(_translate("forgot_password_page", "Send Code"))
        self.commandLinkButton.setText(_translate("forgot_password_page", "Didn\'t receive the code"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    forgot_password_page = QtWidgets.QDialog()
    ui = Ui_forgot_password_page()
    ui.setupUi(forgot_password_page)
    forgot_password_page.show()
    sys.exit(app.exec_())
