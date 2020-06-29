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
from Functions import LikeAction
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def LikePost(browser, Max, tags):

#pragma region Pagemovement Setup

    pageMovement = ActionChains(browser)
    pageMovement.send_keys(Keys.ARROW_RIGHT)

#pragma endregion

#pragma region Actions
    browser.get('https://www.instagram.com/explore/tags/' + tags + '/')
    sleep(randint(1, 5))

#pragma region Setting Values

    low = Max - 5
    high = Max + 5
    amount_to_like = randint(low, high)

    print('Currently Liking ' + str(amount_to_like) + ' photos!')
#pragma endregion

#pragma region Start Liking
    count = 0
    while count < amount_to_like:
        count = LikeAction.likePost(browser, count, pageMovement, tags, 10)

    if(count == amount_to_like):
        print("done!")

#pragma endregion
#pragma endregion
