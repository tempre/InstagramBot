#from selenium import webdriver
from time import sleep
from Drivers import driver
from Logins import Login

um = Login.LoginUM()
pw = Login.LoginPW()


class InstaBot:

    def __init__(self, um, pw):
        self.browser = driver.driver();

        self.browser.get('https://www.instagram.com/')
        #pragma region Login
        sleep(4)
        self.browser.find_element_by_xpath('//input[@name=\"username\"]')\
        .send_keys(um)

        self.browser.find_element_by_xpath('//input[@name=\"password\"]')\
        .send_keys(pw)
        #pragma regionend

        #pragma region Instagram Auth Junk

        #checking for instagram popup for saving login info
        sleep(2)
        if self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/section/div/div[2]"):
                self.browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
                .click()

        #checking for instagram popup for notifcations
        sleep(2)
        if self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/h2"):
            self.browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()

        #pragma end

    def getFollowers(self, um):
        self.browser.get("https://www.instagram.com/" + um + "/")
        sleep(2)

        self.browser.find_element_by_xpath("//a[contains(@href,'/follower')]")\
        .click()

botIM = InstaBot(um, pw)
botIM.getFollowers(um)
