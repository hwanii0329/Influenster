import requests
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver


def get_url():
    driver = webdriver.Firefox()
    driver.get('https://www.sephora.com/best-selling-makeup')

    SCROLL_PAUSE_TIME = 0.5
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


if __name__ == '__main__':
    get_url()
