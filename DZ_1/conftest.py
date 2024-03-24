import pytest
import yaml
import requests

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

url = data['URL']
username = data['USERNAME']
password = data['PASSWORD']


@pytest.fixture()
def auth_by_address():
    data_token = requests.post(url=url, data={'username': username, 'password': password})
    token = data_token.json()['token']
    return token


@pytest.fixture()
def text_post():
    return "New Post Title"
