import pytest
import json
import pandas as pd
from irb.main import get_comments_from_post


@pytest.fixture
def comments():
    return get_comments_from_post('https://www.instagram.com/p/CnCS-Y8rM_q/')


def test_comments(comments):
    assert comments[:20] == json.load(open('tests/expected_comments.json', 'r'))


def test_generate_df(comments):
    expected_df = pd.read_excel('tests/expected_worksheet.ods')
    assert generate_df(comments) == expected_df
