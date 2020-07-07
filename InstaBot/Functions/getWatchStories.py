from PyQt5 import QtTest
from Functions import WatchStoriesAction
from random import randint

def watchStoriesFromAccount(browser, targetAccount, TargetAmount):

    #RR-M- h5uC0 SAvC5

    browser.get('https://www.instagram.com/' + targetAccount + '/')
    browser.find_element_by_xpath("//a[contains(@href,'/follower')]").click()
    QtTest.QTest.qWait(randint(2000, 3000))

    count = 0
    while count < TargetAmount:
        count = WatchStoriesAction.watchStoriesAction(browser, count, targetAccount)
        #QtTest.QTest.qWait(randint(2000, 3000))
