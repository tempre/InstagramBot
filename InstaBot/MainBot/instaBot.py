#from selenium import webdriver
from time import sleep
from Drivers import driver
from Logins import Login
from config import likeConfig
from Functions import LikePost, GetFollowers
from random import randint

um = Login.LoginUM()
pw = Login.LoginPW()

class InstaBot:

#pragma region Init

    def __init__(self, um, pw):

        self.browser = driver.driver();

        self.browser.get('https://www.instagram.com/')

#pragma region Login

        sleep(randint(3,5))
        self.browser.find_element_by_xpath('//input[@name=\"username\"]')\
        .send_keys(um)

        self.browser.find_element_by_xpath('//input[@name=\"password\"]')\
        .send_keys(pw)

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

    def getFollowersFromAccount(self):
        GetFollowers.getFollowers(self.browser, likeConfig['accToGrabFollowers'], likeConfig['maxFollowers'])

    #botIM = InstaBot(um, pw)
    #botIM.startLikingPost()
    #botIM.getFollowersFromAccount()
