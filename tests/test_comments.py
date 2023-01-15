import pytest
import json
import pandas as pd
from irb.main import get_comments_from_post, make_login, create_browser


@pytest.fixture
def comments():
    return get_comments_from_post('https://www.instagram.com/p/CnCS-Y8rM_q/')


@pytest.fixture
def browser():
    return create_browser()


def test_make_login(browser):
    make_login(browser)
    assert 'Messages' in browser.page_source


def test_comments(comments):
    assert comments[:20] == json.load(open('tests/expected_comments.json', 'r'))


def test_generate_df(comments):
    expected_df = pd.read_excel('tests/expected_worksheet.ods')
    assert generate_df(comments) == expected_df
