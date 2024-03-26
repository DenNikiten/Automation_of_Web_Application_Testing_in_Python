import pytest
import yaml
from module import Site

with open('datatest.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


@pytest.fixture(scope="session")
def site():
    site_instance = Site(data['address'])
    yield site_instance
    site_instance.quit()


@pytest.fixture()
def username():
    return 'Jarred54'


@pytest.fixture()
def password():
    return '278d8006df'


@pytest.fixture()
def set_locator1():
    return '''//*[@id="login"]/div[1]/label/input'''


@pytest.fixture()
def set_locator2():
    return '''//*[@id="login"]/div[2]/label/input'''


@pytest.fixture()
def set_locator3():
    return '''button'''


@pytest.fixture()
def set_locator4():
    return '''h2'''


@pytest.fixture()
def set_locator5():
    return '''ul.svelte-1rc85o5 > li:last-child a'''


@pytest.fixture()
def set_locator6():
    return '''#create-btn'''


@pytest.fixture()
def set_locator7():
    return '''//*[@id="create-item"]/div/div/div[1]/div/label/input'''


@pytest.fixture()
def set_locator8():
    return '''[form="create-item"]'''


@pytest.fixture()
def set_locator9():
    return '''h1'''


@pytest.fixture()
def auth_username():
    return 'Hello, Jarred54'


@pytest.fixture()
def title_new_post():
    return 'Is it true'


@pytest.fixture()
def error_name():
    return '401'
