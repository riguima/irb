import requests
import pandas
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup


def get_comments_from_post(post):
    load_dotenv('.env')
    session = requests.Session()
    session.auth = ('marcela_morilo@hotmail.com', '23102019rml')
    with session:
        response = session.get(post)
        soup = BeautifulSoup(str(response.content), 'lxml')
        result = [comment.get_text() for comment in soup.select('.x1i10hfl')]
    return result
