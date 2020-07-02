import os
import glob
import urllib.request
from time import sleep
from selenium import webdriver

#region URL |Experimental |

url = 'https://www.tumblr.com/search/%2335mm+film'

#endregion

#region Remove TEMP IMAGE FILES

files = glob.glob('ImageDownloadTEMP/*')

for f in files:
    os.remove(f)

#endregion

#region Browser load / Initilize

browser = webdriver.Chrome()

browser.get(url)
sleep(1)

last_height = browser.execute_script("return document.body.scrollHeight")

number = 0
id = 0
number_alt = 0
range_for_scroll = 10

#region Grab Images and Authors and save them

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
                f = open('ImageDownloadTEMP/image_authors.txt',"a")
                f.write("Image " + str(id) + ": " + str(author_src) + "\n")
                f.close()
                id += 1
            number += 1
    except IndexError:
        print("Waiting for page scroll...")

    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

#endregion
