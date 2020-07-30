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
          twitter.com/nslonez
'''

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from time import sleep
from Drivers import driver
from config import likeConfig
from Functions import LikePost, GetFollowers, GrabUserData, getWatchStories
from random import randint
import numpy as np
from PIL import Image, ImageDraw
import pyfiglet
import ctypes
import urllib.request
import threading
import os
import datetime
import git
import subprocess
import win32gui

repo = git.Repo('InstagramBot\InstagramBot\.git')

master = repo.head.reference

commits = list(repo.iter_commits('master', max_count=30))
commitsString = ([c.message for c in commits])

class InstaBot():

#pragma region Init

    def __init__(self):

        print("Initilize Function")


#pragma call Instagram Start
    def startBrowser(self):

        self.browser = driver.driver();

    def startInstagram(self, um, pw):

        self.browser.get('https://www.instagram.com/')
#pragma region Login

        sleep(randint(3,5))
        self.browser.find_element_by_xpath('//input[@name=\"username\"]')\
        .send_keys(um)

        sleep(randint(3,6))

        self.browser.find_element_by_xpath('//input[@name=\"password\"]')\
        .send_keys(pw)

        sleep(randint(2,4))

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
        sleep(randint(3,5))
        if self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/h2"):
            self.browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
                .click()
#pragma endregion


#pragma region Actions

    def startLikingPost(self, max, tag):
        LikePost.LikePost(self.browser, max, tag)

    def getFollowersFromAccount(self, acc, max):
        GetFollowers.getFollowers(self.browser, acc, max)

    def getStory(self, acc, amt):
        getWatchStories.watchStoriesFromAccount(self.browser, acc, amt)

    def getProfilePicture(self):
        src = GrabUserData.grabProfilePicture(self.browser, likeConfig['USERNAME'])
        return src

botIM = InstaBot()

class Ui_MainWindow(object):

    def Submit_follow(self):
        botIM.getFollowersFromAccount(self.lineEdit_3.text(), int(self.lineEdit_4.text()))
        print('done')


    def likeAction(self):
        botIM.startLikingPost(int(self.lineEdit_2.text()), self.lineEdit.text())

    def storyAction(self):
        list = self.lineEdit_6.text().split (",")
        list = [i.strip() for i in list]
        botIM.getStory(list, int(self.lineEdit_5.text()))

    def setupUi(self, MainWindow, hwnd):
        MainWindow.setObjectName("Azul")
        MainWindow.setWindowIcon(QIcon('InstagramBot\InstagramBot\InstaBot\Images\Icon_ICO.ico'))
        MainWindow.resize(1379, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.profilePicture = QtWidgets.QLabel(self.centralwidget)
        self.profilePicture.setGeometry(QtCore.QRect(10, 10, 151, 141))
        self.profilePicture.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.profilePicture.setAutoFillBackground(False)
        self.profilePicture.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.profilePicture.setLineWidth(1)
        self.profilePicture.setTextFormat(QtCore.Qt.AutoText)
        self.profilePicture.setObjectName("profilePicture")
        self.WelcomeMessage = QtWidgets.QLabel(self.centralwidget)
        self.WelcomeMessage.setGeometry(QtCore.QRect(170, 10, 621, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(True)
        self.WelcomeMessage.setFont(font)
        self.WelcomeMessage.setAutoFillBackground(True)
        self.WelcomeMessage.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.WelcomeMessage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.WelcomeMessage.setLineWidth(5)
        self.WelcomeMessage.setMidLineWidth(5)
        self.WelcomeMessage.setScaledContents(False)
        self.WelcomeMessage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignCenter|QtCore.Qt.AlignVCenter)
        self.WelcomeMessage.setObjectName("WelcomeMessage")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(170, 50, 20, 541))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 190, 151, 391))
        self.listWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.listWidget.setAutoFillBackground(True)
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget.setLineWidth(1)
        self.listWidget.setAutoScroll(False)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listWidget.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.listWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget.setMovement(QtWidgets.QListView.Free)
        self.listWidget.setUniformItemSizes(True)
        self.listWidget.setWordWrap(True)
        self.listWidget.setObjectName("listWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(190, 50, 601, 541))
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.LikeFunctions = QtWidgets.QWidget()
        self.LikeFunctions.setObjectName("LikeFunctions")
        self.label = QtWidgets.QLabel(self.LikeFunctions)
        self.label.setGeometry(QtCore.QRect(4, -1, 591, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setLineWidth(0)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.line_2 = QtWidgets.QFrame(self.LikeFunctions)
        self.line_2.setGeometry(QtCore.QRect(130, 30, 341, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lineEdit = QtWidgets.QLineEdit(self.LikeFunctions)
        self.lineEdit.setGeometry(QtCore.QRect(200, 50, 191, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.LikeFunctions)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 80, 191, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.LikeFunctions)
        self.pushButton.setGeometry(QtCore.QRect(260, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.LikeFunctions, "")
        self.FollowFunctions = QtWidgets.QWidget()
        self.FollowFunctions.setObjectName("FollowFunctions")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.FollowFunctions)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 50, 191, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.line_3 = QtWidgets.QFrame(self.FollowFunctions)
        self.line_3.setGeometry(QtCore.QRect(130, 30, 341, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.FollowFunctions)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 80, 191, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.FollowFunctions)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 110, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.FollowFunctions)
        self.label_2.setGeometry(QtCore.QRect(4, -1, 591, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setLineWidth(0)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.FollowFunctions, "")
        self.StoryFunctions = QtWidgets.QWidget()
        self.StoryFunctions.setObjectName("StoryFunctions")
        self.pushButton_3 = QtWidgets.QPushButton(self.StoryFunctions)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 110, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.StoryFunctions)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 80, 191, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_4 = QtWidgets.QLabel(self.StoryFunctions)
        self.label_4.setGeometry(QtCore.QRect(4, -1, 591, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_4.setLineWidth(0)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.line_4 = QtWidgets.QFrame(self.StoryFunctions)
        self.line_4.setGeometry(QtCore.QRect(130, 30, 341, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.StoryFunctions)
        self.lineEdit_6.setGeometry(QtCore.QRect(200, 50, 191, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.tabWidget.addTab(self.StoryFunctions, "")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(800, 10, 571, 581))
        self.widget.setMinimumSize(QtCore.QSize(571, 581))
        self.widget.setBaseSize(QtCore.QSize(581, 581))
        self.widget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.widget.setObjectName("widget")

        #exePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        #p = subprocess.Popen(exePath)
        #sleep(0.25)

        print(hwnd)
        self.window = QWindow.fromWinId(hwnd)
        self.windowcontainer = self.widget.createWindowContainer(self.window, self.widget)
        self.windowcontainer.setMinimumSize(QSize(571,581))
        self.windowcontainer.setFixedSize(QSize(571,581))

        self.pushButton.clicked.connect(self.likeAction)
        self.pushButton_2.clicked.connect(self.Submit_follow)
        self.pushButton_3.clicked.connect(self.storyAction)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Azul", "Azul"))

        data = urllib.request.urlopen(likeConfig['PICTURE']).read()
        image = QImage()
        image.loadFromData(data)

        self.profilePicture.setText(_translate("MainWindow", "PlaceHolder for Image"))
        self.profilePicture.setScaledContents(True)
        self.profilePicture.setPixmap(QPixmap(image))

        for i in range(len(commitsString)):
            item = QListWidgetItem(commitsString[i])
            self.listWidget.addItem(item)

        self.WelcomeMessage.setText(_translate("MainWindow", "Welcome, " + likeConfig['USERNAME']))
        self.label_3.setText(_translate("MainWindow", "Updates"))

        self.label_2.setText(_translate("MainWindow", "Follow Followers From Another Account"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.FollowFunctions), _translate("MainWindow", "Follow Functions"))
        self.lineEdit_3.setPlaceholderText('accToGrabFollowers')
        self.lineEdit_4.setPlaceholderText('Max Followers to Grab')
        self.pushButton_2.setText(_translate("MainWindow", "Submit"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.LikeFunctions), _translate("MainWindow", "Like Functions"))
        self.label.setText(_translate("MainWindow", "Like Post From a Tag"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.lineEdit.setPlaceholderText('tagForLikes')
        self.lineEdit_2.setPlaceholderText('Max Amount to Like')

        self.label_4.setText(_translate("MainWindow", "View Stories From Another Account"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.StoryFunctions), _translate("MainWindow", "Story Functions"))
        self.pushButton_3.setText(_translate("MainWindow", "Submit"))
        self.lineEdit_6.setPlaceholderText('targetAccounts')
        self.lineEdit_5.setPlaceholderText('Max Amount of Stories')

class AppLogin(QWidget):

    keyPressed = QtCore.pyqtSignal(QtCore.QEvent)

    def __init__(self):
        super(AppLogin, self).__init__()
        self.setWindowIcon(QIcon('InstagramBot\InstagramBot\InstaBot\Images\Icon_ICO.ico'))
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

#pragma region Visual Attributes

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
        self.pixmapLogo = QPixmap('InstagramBot\InstagramBot\InstaBot\Images\Logo.png')
        self.labelLogo.setPixmap(self.pixmapLogo)
        self.labelLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLogo.resize(self.pixmapLogo.width(),
                          self.pixmapLogo.height())

        self.labelTempre = QLabel(self)
        self.labelTempre.setFont(QFont('Arial', 15))
        self.labelTempre.setText("@tempre")
        self.labelTempre.setStyleSheet("padding-bottom : 65px")
        self.labelTempre.setAlignment(QtCore.Qt.AlignCenter)


#pragma endregion

#pragma region Adding to Layouts

        row = QHBoxLayout()
        row.setSpacing(10)

        qvBox = QVBoxLayout()
        qvBox.setAlignment(Qt.AlignTop)

        qvBox.addWidget(self.labelLogo)
        qvBox.addWidget(self.labelTempre)

        qvBox.addWidget(self.umLine, alignment=QtCore.Qt.AlignCenter)
        qvBox.addWidget(self.pwLine, alignment=QtCore.Qt.AlignCenter)

        qvBox.addWidget(self.btn_submit, alignment=QtCore.Qt.AlignCenter)

        row.addLayout(qvBox)
        row.addSpacing(5)

        self.setLayout(row)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.center()
        self.show()

#pragma endregion

#pragma region Functions

    def Submit_btn(self):
        um = self.umLine.text()
        pw = self.pwLine.text()

        likeConfig['USERNAME'] = um

        print("Logging in...")

        self.close()

        botIM.startBrowser()

        hwnd = win32gui.FindWindowEx(0, 0, "Chrome_WidgetWin_1", None)

        if 'Google Chrome' in win32gui.GetWindowText(hwnd):
            print("hook working!")

            botIM.startInstagram(um, pw)
            likeConfig['PICTURE'] = botIM.getProfilePicture()

            self.MainWindow = QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.MainWindow, hwnd)
            self.MainWindow.show()
        else:
            print("Something went wrong, hook failed.")

        print(win32gui.GetWindowText(hwnd))
        print(hwnd)




    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    ex = AppLogin()
    sys.exit(app.exec_())
