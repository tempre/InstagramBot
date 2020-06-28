'''
   ▄████████  ▄███████▄  ███    █▄   ▄█
  ███    ███ ██▀     ▄██ ███    ███ ███
  ███    ███       ▄███▀ ███    ███ ███
  ███    ███  ▀█▀▄███▀▄▄ ███    ███ ███
▀███████████   ▄███▀   ▀ ███    ███ ███
  ███    ███ ▄███▀       ███    ███ ███
  ███    ███ ███▄     ▄█ ███    ███ ███▌    ▄
  ███    █▀   ▀████████▀ ████████▀  █████▄▄██
                                    ▀

                @tempre
'''

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from time import sleep
from Drivers import driver
from config import likeConfig
from Functions import LikePost, GetFollowers
from random import randint
import pyfiglet
import ctypes


class InstaBot:

#pragma region Init

    def __init__(self):

        print("Initilize Function")


#pragma call Instagram Start

    def startInstagram(self, um, pw):

        self.browser = driver.driver();

        self.browser.get('https://www.instagram.com/')

#pragma region Login

        sleep(randint(3,5))
        self.browser.find_element_by_xpath('//input[@name=\"username\"]')\
        .send_keys(um)

        self.browser.find_element_by_xpath('//input[@name=\"password\"]')\
        .send_keys(pw)

        self.browser.find_element_by_xpath("//button[@type='submit']").click()

#pragma endregion
#pragma endregion
#pragma endregion

#pragma region Instagram Auth Junk

#checking for instagram popup for saving login info
        sleep(randint(3,5))
        if self.browser.find_element_by_xpath("//*[@class='pV7Qt        DPiy6            Igw0E     IwRSH      eGOV_         _4EzTm                                                                                                               qhGB0 ZUqME']"):
            self.browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()

#checking for instagram popup for notifcations
        sleep(randint(3,4))
        if self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/h2"):
            self.browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
                .click()
#pragma endregion


#pragma region Actions

    def startLikingPost(self):
        LikePost.LikePost(self.browser, likeConfig['likeMAX'], likeConfig['tagForLikes'])
        sleep(15)

    def getFollowersFromAccount(self):
        GetFollowers.getFollowers(self.browser, likeConfig['accToGrabFollowers'], likeConfig['maxFollowers'])

botIM = InstaBot()

class AppLogin(QWidget):

    keyPressed = QtCore.pyqtSignal(QtCore.QEvent)

    def __init__(self):
        super(AppLogin, self).__init__()
        self.setWindowIcon(QIcon('Atom\InstagramBot\InstagramBot\InstaBot\Images\Icon_ICO.ico'))
        self.setStyleSheet("background-color: white;")
        self.title = 'Azul Instagram Bot'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.setFixedSize(self.width, self.height)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)

        self.umLine = QLineEdit(self)
        self.umLine.setPlaceholderText('Username')
        self.umLine.setMaximumWidth(200)

        self.pwLine = QLineEdit(self)
        self.pwLine.setPlaceholderText('Password')
        self.pwLine.setMaximumWidth(200)
        self.pwLine.setEchoMode(QLineEdit.Password)

        self.btn_submit = QPushButton(" LOGIN ")

        self.btn_submit.clicked.connect(self.Submit_btn)

        self.labelLogo = QLabel(self)
        self.pixmapLogo = QPixmap('Atom\InstagramBot\InstagramBot\InstaBot\Images\Logo.png')
        self.labelLogo.setPixmap(self.pixmapLogo)
        self.labelLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLogo.resize(self.pixmapLogo.width(),
                          self.pixmapLogo.height())

        self.labelTempre = QLabel(self)
        self.labelTempre.setFont(QFont('Arial', 15))
        self.labelTempre.setText("@tempre")
        self.labelTempre.setStyleSheet("padding-bottom : 65px")
        self.labelTempre.setAlignment(QtCore.Qt.AlignCenter)

        row = QHBoxLayout()
        row.setSpacing(10)

        qvBox = QVBoxLayout()
        qvBox.setAlignment(Qt.AlignTop)

        qvBox.addWidget(self.labelLogo)
        qvBox.addWidget(self.labelTempre)

        qvBox.addWidget(self.umLine, alignment=QtCore.Qt.AlignCenter)
        qvBox.addWidget(self.pwLine, alignment=QtCore.Qt.AlignCenter)

        qvBox.addWidget(self.btn_submit, alignment=QtCore.Qt.AlignCenter)

        #qvBox.addWidget(self.confirmLoginButton, alignment=QtCore.Qt.AlignCenter)

        row.addLayout(qvBox)
        row.addSpacing(5)

        #vbox = QVBoxLayout()
        #vbox.addStretch(1)
        #vbox.addWidget(self.labelLogo, 0, QtCore.Qt.AlignTop)
        #vbox.addWidget(self.labelTempre)
        #vbox.addWidget(self.confirmLoginButton)
        #vbox.addLayout(hbox)

        self.setLayout(row)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.center()
        self.show()

    def Submit_btn(self):
        um = self.umLine.text()
        pw = self.pwLine.text()

        print("Logging in...")

        self.close()

        botIM.startInstagram(um, pw)

        self.next=MainWindow()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    @pyqtSlot()
    def on_confirmlogin(self):
        print("Logging in...")
        self.confirmLoginButton.setEnabled(False)
        botIM.startInstagram(um, pw)

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        #self.setWindowIcon(QtGui.QIcon('Atom\InstagramBot\InstagramBot\InstaBot\Images\AppLogo.png'))
        self.setStyleSheet("background-color: white;")
        self.title = 'Azul Instagram Bot'
        self.left = 10
        self.top = 10
        self.width = 1280
        self.height = 720
        self.setFixedSize(self.width, self.height)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AppLogin()
    #mw = MainWindow()

    sys.exit(app.exec_())
