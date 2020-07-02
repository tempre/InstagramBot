import os
import glob
import requests
import urllib.request
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

url = 'https://www.tumblr.com/search/%2335mm+film'

#pragma region Remove TEMP IMAGE FILES

files = glob.glob('ImageDownloadTEMP/*')

for f in files:
    os.remove(f)

#pragma endregion

browser = webdriver.Chrome()

browser.get(url)
sleep(1)

elem = browser.find_element_by_tag_name("body")

response = requests.get(url)

last_height = browser.execute_script("return document.body.scrollHeight")

number = 0
id = 0
number_alt = 0
range_for_scroll = 10

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    sleep(1)

    new_height = browser.execute_script("return document.body.scrollHeight")

    try:
        images = browser.find_elements_by_xpath('//img[@class="photo"]')
        for image in images:
            image_src = images[number].get_attribute('src')
            author_src = images[number].get_attribute('data-pin-url')
            new_src = []
            if "gif" not in image_src:
                new_src = image_src
            if len(new_src) != 0:
                print(str(id) + " Image")
                print('IMAGE = ' + new_src)
                print('SIZE = ' + str(images[number].size))
                print('AUTHOR = ' + author_src + '\n')

                urllib.request.urlretrieve(''.join(new_src), 'ImageDownloadTEMP/' + str(id) + '.jpg')
                f = open('ImageDownloadTEMP/' + str(id) + "_author.txt","w+")
                f.write(author_src)
                f.close()
                id += 1
            number += 1
    except IndexError:
        print("Waiting for page scroll...")

    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
