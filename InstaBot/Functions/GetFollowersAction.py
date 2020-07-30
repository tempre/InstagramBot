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
from PyQt5.QtCore import QThread

def FollowerAction(browser, targetAccount, count, max):
    if 'https://www.instagram.com/' + targetAccount + '/followers/' in browser.current_url:
        #QtTest.QTest.qWait(randint(2000, 3000))
        QThread.sleep(2)

        browser.execute_script('''
                                var fDialog = document.querySelector('div[role="dialog"] .isgrP');
                                fDialog.scrollTop = fDialog.scrollHeight
                                ''')

        try:
            browser.find_element_by_xpath('//*[@class = "sqdOP  L3NKy   y3zKF     "]').click()
            count += 1
            #QtTest.QTest.qWait(randint(2000, 3000))
            QThread.sleep(2)
        except NoSuchElementException as e:
            print("No more accounts to follow, exiting")
            count = max

        return count

    else:
        print("Something failed. trying again")
        browser.get('https://www.instagram.com/' + targetAccount + '/followers/')
