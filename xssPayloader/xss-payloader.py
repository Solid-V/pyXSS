from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import time
import os
import requests
import random

url = requests.get("https://xss-game.appspot.com/level1/frame")

#options required for using existing chrome profiles
options = webdriver.ChromeOptions()
#options.add_argument(f"--user-data-dir={os.environ['PROFILE_PATH']}")
options.add_argument("--profile-directory=Default")

timers = [
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

def get_all_forms(url):
    soup = bs(url.content, "html.parser")
    return soup.find_all("form")
    

def get_forms(url):
    soup = bs(url.content, "html.parser")
    forms = soup.find_all("form")

    inputs = []
    details = {}

    action = dict( ("actions",form.attrs.get("action", "").lower()) for form in forms)
    method = dict(("method", form.attrs.get("method").lower()) for form in forms)
    input_type = inputs.append(dict(("type", input_elem.attrs.get("type", "text"))for input_elem in soup.find_all("input")))
    input_name = inputs.append(dict(("name", input_elem.attrs.get("name"))for input_elem in soup.find_all("input")))
    input_id = inputs.append(dict(("id", input_elem.attrs.get("id"))for input_elem in soup.find_all("input")))
    
    details.update(action)
    details.update(method)
    details["input"] = inputs
    #print(details)
    return details

def get_xpath(url):
    inputs = get_forms(url)
    if "method" in inputs:
        for x, input in inputs.items():
            pass
        for y in input:
            print(y.values())

get_xpath(url)