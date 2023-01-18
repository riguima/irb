import pytest
import json
import pandas as pd
from irb.main import get_votes_from_post, generate_df, save_worksheet
from pathlib import Path


@pytest.fixture(scope='module')
def votes():
    return get_votes_from_post('CnCS-Y8rM_q')


def test_votes(votes):
    assert votes[:10] == json.load(open('tests/expected_votes.json', 'r'))


def test_generate_df(votes):
    expected_df = pd.read_excel('tests/expected_worksheet.xlsx')
    df = generate_df(votes[:10])
    assert df.equals(expected_df)
