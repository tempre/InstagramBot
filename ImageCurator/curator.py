import requests
import urllib.request
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


url = 'https://www.tumblr.com/search/%2335mm+film'

browser = webdriver.Chrome()

browser.get(url)
sleep(1)

elem = browser.find_element_by_tag_name("body")

response = requests.get(url)

last_height = browser.execute_script("return document.body.scrollHeight")

number = 0
number_alt = 0
range_for_scroll = 10

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    sleep(0.5)

    new_height = browser.execute_script("return document.body.scrollHeight")

    try:
        images = browser.find_elements_by_xpath('//img[@class="photo"]')
        for image in images:
            image_src = images[number].get_attribute('src')
            new_src = []
            if "gif" not in image_src:
                new_src = image_src
            if len(new_src) != 0:
                print(new_src)
                print(images[number].size)
                urllib.request.urlretrieve(''.join(new_src), 'ImageDownloadTEMP/' + str(number) + '.jpg')
            number += 1
    except IndexError:
        print("All Duplicates on screen")
