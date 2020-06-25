from time import sleep
from random import randint
from Functions import LikeAction
from Functions import Scroll
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
    #browser.find_element_by_xpath('//*[@class = "_9AhH0"]').click()

#pragma region Setting Values

    start = randint(5,10)
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
