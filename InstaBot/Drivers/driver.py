from selenium import webdriver

def driver():
    driver = webdriver.Opera(executable_path = 'Atom\InstagramBot\InstagramBot\InstaBot\Drivers\operadriver.exe')
    driver.get('https://www.instagram.com/')
    return driver
