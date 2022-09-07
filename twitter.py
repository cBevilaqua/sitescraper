import time
import os
import uuid

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# https://chromedriver.chromium.org/downloads
# https://selenium-python.readthedocs.io/locating-elements.html

DOWNLOAD_DIRECTORY = "twitter_imgs"
NUMBER_OF_PAGE_DOWNS = 10

browser = webdriver.Chrome("/Users/cristiano/Documents/chromedriver")

browser.get("https://twitter.com/search?q=%E8%8A%B1%E7%81%AB%E5%B7%A5%E5%A0%B4&src=typed_query&f=top")
time.sleep(5)


def download(url):
	file_name = f"{uuid.uuid4()}.jpg"
	r = requests.get(url, allow_redirects=True)
	if not os.path.exists(DOWNLOAD_DIRECTORY):
		os.makedirs(DOWNLOAD_DIRECTORY)
	open(DOWNLOAD_DIRECTORY + "/" + file_name, "wb").write(r.content)

def get_imgs_src(imgs_list):
	output = []
	for img in imgs_list:
		src = img.get_attribute("src")
		output.append(src)
	return output

no_of_pagedowns = NUMBER_OF_PAGE_DOWNS

body_element = browser.find_elements(By.TAG_NAME, 'body')[0]

imgs_srcs = []

while no_of_pagedowns:
  body_element.send_keys(Keys.PAGE_DOWN)
  time.sleep(5)
  imgs = browser.find_elements(By.TAG_NAME, 'img')
  imgs_srcs.extend(get_imgs_src(imgs))
  time.sleep(3)
  no_of_pagedowns-=1


for src in imgs_srcs:
	if "media" in src:
		print(src)
		if "small" in src:
			# only images with small in src querystring are intersting
			src = src.replace("small", "large")
			download(src)

browser.close()
