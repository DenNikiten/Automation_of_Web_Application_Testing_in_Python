from base_page import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, '''//*[@id="login"]/div[1]/label/input''')
    LOCATOR_PASS_FIELD = (By.XPATH, '''//*[@id="login"]/div[2]/label/input''')
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, '''button''')
    LOCATOR_ERROR_FIELD = (By.CSS_SELECTOR, '''h2''')

    LOCATOR_USER_NAME_FIELD = (By.CSS_SELECTOR, '''ul.svelte-1rc85o5 > li:last-child a''')

    LOCATOR_NEW_POST_BTN = (By.CSS_SELECTOR, '''#create-btn''')
    LOCATOR_TITLE_FIELD = (By.XPATH, '''//*[@id="create-item"]/div/div/div[1]/div/label/input''')
    LOCATOR_DESCRIPTION_FILED = (By.XPATH, '''//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea''')
    LOCATOR_CONTENT_FILED = (By.CSS_SELECTOR, '''[aria-controls="SMUI-textfield-helper-text-1"]''')
    LOCATOR_SAVE_POST_BTN = (By.CSS_SELECTOR, '''[form="create-item"]''')
    LOCATOR_RES_LBL = (By.CSS_SELECTOR, '''h1''')

    LOCATOR_CONTACT_BTN = (By.CSS_SELECTOR, '''nav > ul > li:nth-child(2) a''')
    LOCATOR_CONTACT_NAME = (By.CSS_SELECTOR, '''div:nth-child(1) > label > input''')
    LOCATOR_CONTACT_MAIL = (By.CSS_SELECTOR, '''div:nth-child(2) > label > input''')
    LOCATOR_CONTACT_CONTENT = (By.CSS_SELECTOR, '''[aria-controls="SMUI-textfield-helper-text-0"]''')
    LOCATOR_CONTACT_SEND_BTN = (By.CSS_SELECTOR, '''.button.mdc-button''')


class OperationsHelpers(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def get_user_text(self):
        user_text = self.find_element(TestSearchLocators.LOCATOR_USER_NAME_FIELD)
        text = user_text.text
        logging.info(f"We find text {text} in user name field {TestSearchLocators.LOCATOR_USER_NAME_FIELD[1]}")
        return text

    def click_new_post_button(self):
        logging.info("Click new post button")
        self.find_element(TestSearchLocators.LOCATOR_NEW_POST_BTN).click()

    def enter_title(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_NEW_POST_BTN[1]}")
        title_field = self.find_element(TestSearchLocators.LOCATOR_TITLE_FIELD)
        title_field.clear()
        title_field.send_keys(word)

    def enter_description(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_DESCRIPTION_FILED[1]}")
        description_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION_FILED)
        description_field.clear()
        description_field.send_keys(word)

    def enter_content(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTENT_FILED[1]}")
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_FILED)
        content_field.clear()
        content_field.send_keys(word)

    def click_save_btn(self):
        logging.info("Click save new post button")
        self.find_element(TestSearchLocators.LOCATOR_SAVE_POST_BTN).click()

    def get_res_text(self):
        res_text = self.find_element(TestSearchLocators.LOCATOR_RES_LBL)
        text = res_text.text
        logging.info(f"We find text {text} in title new post {TestSearchLocators.LOCATOR_RES_LBL[1]}")
        return text

    def click_contact_link(self):
        logging.info("Click contact link")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()

    def enter_contact_name(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTACT_NAME[1]}")
        contact_name = self.find_element(TestSearchLocators.LOCATOR_CONTACT_NAME)
        contact_name.clear()
        contact_name.send_keys(word)

    def enter_contact_mail(self, word):
        logging.info(f"Send {word} in element {TestSearchLocators.LOCATOR_CONTACT_MAIL[1]}")
        contact_mail = self.find_element(TestSearchLocators.LOCATOR_CONTACT_MAIL)
        contact_mail.clear()
        contact_mail.send_keys(word)

    def enter_contact_content(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTACT_CONTENT[1]}")
        contact_content = self.find_element(TestSearchLocators.LOCATOR_CONTACT_CONTENT)
        contact_content.clear()
        contact_content.send_keys(word)

    def click_contact_send_btn(self):
        logging.info("Click contact send button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_SEND_BTN).click()