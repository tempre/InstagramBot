import time
from config import likeConfig
from random import randint

def likePost(browser, count, actions, tags):

    # Check if post embed has closed
    if browser.current_url == 'https://www.instagram.com/explore/tags/' + tags + '/':
        print('Post embed was closed, returning to previous post.')
        browser.find_element_by_xpath('//*[@class="_9AhH0"]').click()
        i = 0
        while i != count:
            time.sleep(.2)
            actions.perform()
            i += 1
        print('Successfully returned to previous post, resuming with likes.')
        time.sleep(randint(1,6))

    # Check for unlike button
    try:
        browser.find_element_by_xpath('//*[@aria-label="Unlike"]')
        print('Post already liked.')
        time.sleep(randint(1,6))
        actions.perform()
        time.sleep(randint(1,6))
        return count
    except:
        print('Post not liked, continuing.')

    # Like photo
    browser.find_element_by_xpath('//button[@class="wpO6b "]').click()
    count += 1

    # Get next post and return
    time.sleep(randint(1,6))
    print('Post liked successfully. ' + str(count) + ' post(s) in total.')
    actions.perform()
    time.sleep(randint(1,6))
    return count
