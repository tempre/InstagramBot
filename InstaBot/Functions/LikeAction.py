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
        https://twitter.com/nslonez
'''

from PyQt5 import QtTest
from random import randint
from PyQt5.QtCore import QThread

def likePost(browser, count, actions, tags, MaxSkip):

#pragma regiom Check if post embed has closed

    if browser.current_url == 'https://www.instagram.com/explore/tags/' + tags + '/':
        postLocation = browser.find_elements_by_xpath('//*[@class="_9AhH0"]')
        postLocation[MaxSkip].click()
        QThread.sleep(3)

#pragma regionend

#pragma Like / check if liked

    try:
        browser.find_element_by_xpath('//*[@aria-label="Unlike"]')
        print('Post already liked.')
        QThread.sleep(2)
        actions.perform()
        QThread.sleep(3)
        return count
    except:
        # Like photo
        browser.find_element_by_xpath('//*[@aria-label="Like"]').click()
        count += 1

#pragma endregion

#pragma region Move to next post

    QThread.sleep(3)
    print('Post liked successfully. ' + str(count) + ' post(s) in total.')
    actions.perform()
    QThread.sleep(2)
    return count

#pragma endregion
