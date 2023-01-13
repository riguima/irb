import json


def test_get_comments_from_post():
    expected = json.load('tests/expected_comments.json')
    assert get_comments_from_post('https://www.instagram.com/p/CnCS-Y8rM_q/')[:20] == expected
