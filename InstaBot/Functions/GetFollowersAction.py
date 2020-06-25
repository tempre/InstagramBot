from time import sleep
from random import randint
from selenium.webdriver.common.action_chains import ActionChains

def FollowerAction(browser, targetAccount, count, max):
    if browser.current_url == 'https://www.instagram.com/' + targetAccount + '/followers/':
        sleep(randint(1,3))

        browser.execute_script('''
                                var fDialog = document.querySelector('div[role="dialog"] .isgrP');
                                fDialog.scrollTop = fDialog.scrollHeight
                                ''')

        try:
            browser.find_element_by_xpath('//*[@class = "sqdOP  L3NKy   y3zKF     "]').click()
            count += 1
            sleep(randint(1,2))
        except NoSuchElementException as e:
            print("No more accounts to follow, exiting")
            return count = Max
        finally:
            try:
                browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/h4')
                return count = Max
            except NoSuchElementException as e:
                print(Not Following Suggested Accounts, exiting)
            finally:
                return count
