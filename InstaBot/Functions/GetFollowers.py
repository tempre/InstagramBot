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

from time import sleep
from PyQt5 import QtTest
from random import randint
from Functions import GetFollowersAction

def getFollowers(browser, targetAccount, FollowTargetAmount):

    browser.get('https://www.instagram.com/' + targetAccount + '/')
    browser.find_element_by_xpath("//a[contains(@href,'/follower')]").click()
    QtTest.QTest.qWait(randint(2000, 3000))

    print('Currently following ' + str(FollowTargetAmount) + ' accounts from this ' + str(targetAccount) + ' account.')

    count = 0
    while count < FollowTargetAmount:
        count = GetFollowersAction.FollowerAction(browser, targetAccount, count, max)
