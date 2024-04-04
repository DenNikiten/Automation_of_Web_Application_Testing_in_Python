import requests

from base_page import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml

with open("datatest.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)


class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml", encoding='utf-8') as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelpers(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

    # ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description='login form')

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description='password form')

    def enter_title(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_TITLE_FIELD"], word, description='title')

    def enter_description(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_DESCRIPTION_FILED"], word, description='description')

    def enter_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT_FILED"], word, description='content')

    def enter_contact_name(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_NAME"], word, description='contact name')

    def enter_contact_mail(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_MAIL"], word, description='contact mail')

    def enter_contact_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_CONTENT"], word,
                                   description='contact content')

    # GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], description='error label')

    def get_user_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_USER_NAME_FIELD"], description='username')

    def get_res_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_RES_LBL"], description='result')

    def get_alert(self):
        logging.info("Get alert text")
        text = self.get_alert_text()
        logging.info(text)
        return text

    # CLICK
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description='login')

    def click_new_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_NEW_POST_BTN"], description='new post')

    def click_save_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_SAVE_POST_BTN"], description='save')

    def click_contact_link(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_BTN"], description='contact')

    def click_contact_send_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_SEND_BTN"], description='send')


# API
def title_for_posts_owner_not_me(token):
    try:
        res = requests.get(url=data["url2"], headers={'X-Auth-Token': token}, params={'owner': 'notMe'})
        if res.status_code == 200:
            title_res = [item['title'] for item in res.json()['data']]
            return title_res
        else:
            logging.error(f"Error. Status code {res.status_code}")
            return None
    except:
        logging.exception(f"Exception with get")
        return None


def get_new_post(token):
    try:
        res = requests.post(url=data["url2"],
                            data={'title': 'Motorolla',
                            'description': 'telefon',
                            'content': 'not working now'},
                            headers={'X-Auth-Token': token})
        if res.status_code == 200:
            return res.json()
        else:
            logging.error(f"Error. Status code {res.status_code}")
            return None
    except:
        logging.exception(f"Exception with post")
        return None


def get_post_description(token):
    try:
        res = requests.get(data['url2'], headers={'X-Auth-Token': token})
        if res.status_code == 200:
            description_res = [item['description'] for item in res.json()['data']]
            return description_res
        else:
            logging.error(f"Error. Status code {res.status_code}")
            return None
    except:
        logging.exception(f"Exception with get")
        return None

