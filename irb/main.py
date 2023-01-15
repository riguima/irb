from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def get_comments_from_post(post):
    load_dotenv('.env')
    browser = create_browser()
    make_login(browser)
    browser.get(post)
    print('username' in browser.page_source)
    soup = BeautifulSoup(str(browser.page_source), 'lxml')
    result = [comment.get_text() for comment in soup.select('.x1i10hfl')]
    return result


def create_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


def make_login(browser):
    browser.get('https://www.instagram.com/')
    browser.find_element(By.CSS_SELECTOR, 'input[name=username]').send_keys(os.getenv('USERNAME'))
    password_input = browser.find_element(By.CSS_SELECTOR, 'input[name=password]')
    password_input.send_keys(os.getenv('PASSWORD'))
    password_input.submit()
