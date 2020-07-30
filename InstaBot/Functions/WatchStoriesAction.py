from PyQt5 import QtTest
from random import randint
from time import sleep
from PyQt5.QtCore import QThread
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def watchStoriesAction(browser, count, targetAccount, pageMovement):
    try:
        data = browser.find_elements_by_xpath("//div[contains(@class, 'RR-M- h5uC0 SAvC5')]")
        data[count].click()
        elements = browser.find_elements_by_xpath('//div[contains(@class, "yS4wN ")]')
        QThread.sleep(2)
        while '/stories/' in browser.current_url:
            #QtTest.QTest.qWait(randint(2000, 5000))
            QThread.sleep(3)
            pageMovement.perform()
        QThread.sleep(4)
        count += 1
        print('currenly have watched ' + str(count) + ' stories from ' + targetAccount + '\'s follower list!')
    except:
        print("No account with story visible. searching...")

    if browser.current_url == 'https://www.instagram.com/' + targetAccount + '/followers/':
        browser.execute_script('''
                                var fDialog = document.querySelector('div[role="dialog"] .isgrP');
                                fDialog.scrollTop = fDialog.scrollHeight
                                ''')
        QThread.sleep(3)

    return count
