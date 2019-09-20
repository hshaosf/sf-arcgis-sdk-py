"""Tests for screendoorapi package"""
import json
from unittest.mock import patch
from boilerplate_sdk.example import Example

def test_get_url():
    """ Test get api url """
    params = {'userId':'1'}

    example = Example()
    url = example.get_url({
        'path' : '/posts',
        'params' : params
        })

    expected_url = 'https://jsonplaceholder.typicode.com/posts?'
    expected_url += '&userId=1'

    assert expected_url == url

def test_get_posts():
    """ Test get_posts """
    with open('tests/mocks/posts.json', 'r') as file_obj:
        mock_posts = json.load(file_obj)

    assert mock_posts

    if mock_posts:

        example = Example()
        with patch('boilerplate_sdk.example.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = mock_posts
            responses = example.get_posts({'userId':'1'})
        assert mock_posts == responses

    with patch('boilerplate_sdk.example.requests.get') as mock_get:
        mock_get.return_value.status_code = 401
        mock_get.return_value.json.return_value = {'error': 'not authorized'}
        responses = example.get_posts()
    assert [] == responses
