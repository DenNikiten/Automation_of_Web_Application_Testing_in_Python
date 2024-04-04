import time
import yaml
import pytest
import logging
from testpage import OperationsHelpers, title_for_posts_owner_not_me, get_new_post, get_post_description

with open('datatest.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


def test_negative_auth(browser, username_negative, password, error_name):
    logging.info("Test negative starting")
    auth_page = OperationsHelpers(browser)
    auth_page.go_to_site()
    auth_page.enter_login(username_negative)
    auth_page.enter_pass(password)
    auth_page.click_login_button()
    assert auth_page.get_error_text() == error_name


def test_login_success(browser, username, password):
    logging.info("Test auth login Starting")
    auth_page = OperationsHelpers(browser)
    auth_page.enter_login(username)
    auth_page.enter_pass(password)
    auth_page.click_login_button()
    assert auth_page.get_user_text() == f"Hello, {username}"
    # time.sleep(data['sleep_time'])


def test_title_new_post(browser, title_new_post, description_new_post, content_new_post):
    logging.info("Test create new post Starting")
    new_post = OperationsHelpers(browser)
    new_post.click_new_post_button()
    new_post.enter_title(title_new_post)
    new_post.enter_description(description_new_post)
    new_post.enter_content(content_new_post)
    new_post.click_save_btn()
    time.sleep(data['sleep_time'])
    assert new_post.get_res_text() == title_new_post


def test_contact(browser, name_contact, mail_contact, content_contact):
    logging.info("Test Contact us Starting")
    contact_us = OperationsHelpers(browser)
    contact_us.click_contact_link()
    contact_us.enter_contact_name(name_contact)
    contact_us.enter_contact_mail(mail_contact)
    contact_us.enter_contact_content(content_contact)
    time.sleep(data['sleep_time'])
    contact_us.click_contact_send_btn()
    time.sleep(data['sleep_time'])
    assert contact_us.get_alert() == "Form successfully submitted"


def test_title_post(auth_by_address):
    logging.info("Test check title post Starting")
    assert data["text_post"] in title_for_posts_owner_not_me(auth_by_address), "Test failed"


def test_new_post(auth_by_address):
    logging.info("Test check description new post Starting")
    get_new_post(auth_by_address)
    assert data['text_new_post'] in get_post_description(auth_by_address), "Test failed"


if __name__ == '__main__':
    pytest.main(['-vv'])
