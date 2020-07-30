from PyQt5 import QtTest
from Functions import WatchStoriesAction
from random import randint
from PyQt5.QtCore import QThread
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def watchStoriesFromAccount(browser, targetAccount, TargetAmount):

    pageMovement = ActionChains(browser)
    pageMovement.send_keys(Keys.ARROW_RIGHT)
    acc_count = 0

    try:
        while acc_count < len(targetAccount):
            browser.get('https://www.instagram.com/' + targetAccount[acc_count] + '/')
            QThread.sleep(5)
            browser.find_element_by_xpath("//a[contains(@href,'/follower')]").click()
            QThread.sleep(5)

            count = 0
            while count < TargetAmount:
                count = WatchStoriesAction.watchStoriesAction(browser, count, targetAccount[acc_count], pageMovement)

            if count == TargetAmount:
                print('Done returning to instagram...')
                browser.get('https://www.instagram.com')
                acc_count += 1
    except:
        print('Account is private or does not exist. Exiting')
        browser.get('https://www.instagram.com')
