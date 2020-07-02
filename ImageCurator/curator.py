import os
import glob
import urllib.request
from time import sleep
from selenium import webdriver
from PIL import Image

#region Params

author_value = 'data-pin-url'
#endregion

#region URL |Experimental |

url = 'https://www.tumblr.com/search/%2335mm+film'
#url = 'https://www.pinterest.com/search/pins/?q=%2335mm%20film&rs=typed&term_meta[]=%2335mm%7Ctyped&term_meta[]=film%7Ctyped'

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
        #images = browser.find_elements_by_xpath('//*[@class="%s"]' % active_value)
        images = browser.find_elements_by_tag_name("img")
        print(str(images))

        for image in images:
            image_src = images[number].get_attribute('src')

            author_src = images[number].get_attribute('data-pin-url')

            new_src = []

#not allowing gifs for my use

            if "gif" not in image_src:
                new_src = image_src
                if len(new_src) != 0:
                    print(str(id) + " Image")
                    print('IMAGE = ' + new_src)
                    print('SIZE = ' + str(images[number].size))
                    print('AUTHOR = ' + str(author_src) + '\n')

                    dict = images[number].size
                    width = dict.get('width')
                    height = dict.get('height')

                    if width > 150 and height > 150:
                        urllib.request.urlretrieve(''.join(new_src), 'ImageDownloadTEMP/' + str(id) + '.jpg')
                        f = open('ImageDownloadTEMP/image_authors.txt',"a")
                        f.write("Image " + str(id) + ": " + str(author_src) + "\n")
                        f.close()
                    id += 1
            number += 1
    except IndexError:
        print("Waiting for page scroll...")

    if new_height == last_height:
        break
    last_height = new_height
#endregion
