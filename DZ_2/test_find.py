import time
import yaml

with open('datatest.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


def test_login_success(site, set_locator1, username, set_locator2, password, set_locator3, set_locator5, auth_username):
    input1 = site.find_element('xpath', set_locator1)
    input1.send_keys(username)
    input2 = site.find_element('xpath', set_locator2)
    input2.send_keys(password)
    input3 = site.find_element('css', set_locator3)
    input3.click()
    find1 = site.find_element('css', set_locator5)
    assert find1.text == auth_username
    time.sleep(data['sleep_time'])


def test_title_new_post(site, set_locator1, username, set_locator2, password, set_locator3, set_locator6, set_locator7,
                        title_new_post, set_locator8, set_locator9):
    create1 = site.find_element('css', set_locator6)
    create1.click()
    time.sleep(data['sleep_time'])
    input4 = site.find_element('xpath', set_locator7)
    input4.send_keys(title_new_post)
    find1 = site.find_element('css', set_locator8)
    find1.click()
    time.sleep(data['sleep_time'])
    find2 = site.find_element('css', set_locator9)
    assert find2.text == title_new_post

