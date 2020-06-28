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

import time
from random import randint

def likePost(browser, count, actions, tags, MaxSkip):

#pragma regiom Check if post embed has closed

    if browser.current_url == 'https://www.instagram.com/explore/tags/' + tags + '/':
        postLocation = browser.find_elements_by_xpath('//*[@class="_9AhH0"]')
        postLocation[MaxSkip].click()
        time.sleep(3)

#pragma regionend

#pragma Like / check if liked

    try:
        browser.find_element_by_xpath('//*[@aria-label="Unlike"]')
        print('Post already liked.')
        time.sleep(randint(3,4))
        actions.perform()
        time.sleep(randint(2,3))
        return count
    except:
        # Like photo
        browser.find_element_by_xpath('//button[@class="wpO6b "]').click()
        count += 1

#pragma endregion

#pragma region Move to next post

    time.sleep(randint(2,4))
    print('Post liked successfully. ' + str(count) + ' post(s) in total.')
    actions.perform()
    time.sleep(randint(2,6))
    return count

#pragma endregion
