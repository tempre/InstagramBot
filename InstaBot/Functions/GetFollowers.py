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
from random import randint
from Functions import GetFollowersAction

def getFollowers(browser, targetAccount, FollowTargetAmount):

    browser.get('https://www.instagram.com/' + targetAccount + '/')
    browser.find_element_by_xpath("//a[contains(@href,'/follower')]").click()
    sleep(randint(1,5))

    print('Currently following ' + str(FollowTargetAmount) + ' accounts from this ' + str(targetAccount) + ' account.')

    count = 0
    while count < FollowTargetAmount:
        GetFollowersAction.FollowerAction(browser, targetAccount, count, max)
