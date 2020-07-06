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


from random import randint
from PyQt5 import QtTest
from selenium.webdriver.common.action_chains import ActionChains

def FollowerAction(browser, targetAccount, count, max):
    if browser.current_url == 'https://www.instagram.com/' + targetAccount + '/followers/':
        QtTest.QTest.qWait(randint(2000, 3000))

        browser.execute_script('''
                                var fDialog = document.querySelector('div[role="dialog"] .isgrP');
                                fDialog.scrollTop = fDialog.scrollHeight
                                ''')

        try:
            browser.find_element_by_xpath('//*[@class = "sqdOP  L3NKy   y3zKF     "]').click()
            count += 1
            QtTest.QTest.qWait(randint(2000, 3000))
        except NoSuchElementException as e:
            print("No more accounts to follow, exiting")
            count = max

        return count
