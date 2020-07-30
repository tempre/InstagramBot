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

from PyQt5 import QtTest
from random import randint
from Functions import LikeAction
from PyQt5.QtCore import QThread
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def LikePost(browser, Max, tags):

#pragma region Pagemovement Setup

    pageMovement = ActionChains(browser)
    pageMovement.send_keys(Keys.ARROW_RIGHT)

#pragma endregion

#pragma region Actions
    browser.get('https://www.instagram.com/explore/tags/' + tags + '/')
    QThread.sleep(3)

#pragma region Setting Values

    print('Currently Liking ' + str(Max) + ' photos!')
#pragma endregion

#pragma region Start Liking
    count = 0
    while count < Max:
        count = LikeAction.likePost(browser, count, pageMovement, tags, 10)

    if(count == Max):
        print("done!")

#pragma endregion
#pragma endregion
