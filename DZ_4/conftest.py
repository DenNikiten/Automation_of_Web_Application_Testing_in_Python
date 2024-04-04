import pytest
import requests
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open('datatest.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    browser_name = data['browser_name']
    url = data['url']
    username_for_api = data['username_for_api']
    password_for_api = data['password_for_api']


@pytest.fixture(scope="session")
def browser():
    if browser_name == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def auth_by_address():
    data_token = requests.post(url=url, data={'username': username_for_api, 'password': password_for_api})
    token_n = data_token.json()['token']
    return token_n


@pytest.fixture()
def username_negative():
    return 'Jarred54NOT'


@pytest.fixture()
def username():
    return 'Jarred54'


@pytest.fixture()
def password():
    return '278d8006df'


@pytest.fixture()
def error_name():
    return '401'


@pytest.fixture()
def title_new_post():
    return 'Is it true'


@pytest.fixture()
def description_new_post():
    return 'No no no'


@pytest.fixture()
def content_new_post():
    return 'May be'


@pytest.fixture()
def name_contact():
    return 'Petr'


@pytest.fixture()
def mail_contact():
    return 'yyy@gmail.com'


@pytest.fixture()
def content_contact():
    return 'Hi everybody'
