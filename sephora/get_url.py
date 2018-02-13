import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver

def get_url():
    driver = webdriver.Firefox()
    driver.get('https://www.sephora.com/best-selling-makeup')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")