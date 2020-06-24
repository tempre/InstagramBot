#from selenium import webdriver
from time import sleep
from Drivers import driver
from Logins import Login

um = Login.LoginUM()
pw = Login.LoginPW()

class InstaBot:

    def __init__(self, um, pw):
        #self.driver = webdriver.Opera(executable_path = 'Atom\InstagramBot\InstagramBot\InstaBot\Drivers\operadriver.exe')

        self.browser = driver.driver();

        sleep(4)
        self.browser.find_element_by_xpath('//input[@name=\"username\"]')\
        .send_keys(um)

        self.browser.find_element_by_xpath('//input[@name=\"password\"]')\
        .send_keys(pw)

        self.browser.find_element_by_xpath('//button[@type="submit"]')\
        .click()

        sleep(3)
        self.browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
        .click()

        sleep(3)
        self.browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
        .click()

botIM = InstaBot(um, pw)
