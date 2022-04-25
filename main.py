import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def multi(a,b):
    return a*b

def selenium():
    driver = webdriver.Chrome(executable_path='/Users/hothaifa/Desktop/chromedriver')
    driver.get("https://www.reebok.co.il")
    time.sleep(3)
    return driver.current_url