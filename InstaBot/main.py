from selenium import webdriver
from time import sleep

um = "nslone0"
pw = "lonez09"

class InstaBot:

    def __init__(self, um, pw):
        self.driver = webdriver.Opera(executable_path = 'Atom\InstagramBot\InstagramBot\InstaBot\Drivers\operadriver.exe')

        self.driver.get('https://instagram.com')
        sleep(4)
        self.driver.find_element_by_xpath('//input[@name=\"username\"]')\
        .send_keys(um)
        self.driver.find_element_by_xpath('//input[@name=\"password\"]')\
        .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
        .click()

        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
        .click()

        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
        .click()

    def getFollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(um))\
            .click()
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format("follower"))\
            .click()

botIM = InstaBot(um, pw)
botIM.getFollowers()
