from PyQt5 import QtTest
from random import randint

def watchStoriesAction(browser, count, targetAccount):

    if browser.current_url == 'https://www.instagram.com/' + targetAccount + '/followers/':
        QtTest.QTest.qWait(randint(2000, 3000))

        browser.execute_script('''
                                var fDialog = document.querySelector('div[role="dialog"] .isgrP');
                                fDialog.scrollTop = fDialog.scrollHeight
                                ''')

    try:
        browser.find_element_by_xpath('//*[@class = "RR-M- h5uC0 SAvC5"]').click()
        count += 1
        QtTest.QTest.qWait(randint(2000, 3000))
    except NoSuchElementException as e:
        print("No account with story visible. searching...")

    return count
