from selenium.webdriver.common.by import By
from tests.web_element.element_list import ElementList
from tests.pages.base_page import BasePage
from data_providers import logging_data

logger = logging_data.log_message(log_level="INFO", logger_name="root")


class my_account_fashion_site_page(BasePage):

    @property
    def Logout_link(self):
        return ElementList.LINK(
            self.driver, (By.XPATH,
                          '//a[text()="Logout"]'))

    @property
    def Account_details_link(self):
        return ElementList.LINK(
            self.driver,
            (By.XPATH,
             '//a[@href="http://mystore.local/my-account/edit-account/" and text()="Account details"]'))

    @property
    def password_TEXTBOX(self):
        return ElementList.TEXTBOX(
            self.driver, (By.CSS_SELECTOR, 'input[id="password"]'))

    @property
    def username_TEXTBOX(self):
        return ElementList.TEXTBOX(
            self.driver, (By.CSS_SELECTOR, 'input[id="username"]'))

    @property
    def login_button(self):
        return ElementList.BUTTON(
            self.driver,
            (By.CSS_SELECTOR, 'button[class="woocommerce-button button woocommerce-form-login__submit"]'))

    @property
    def register_password_TEXTBOX(self):
        return ElementList.TEXTBOX(
            self.driver, (By.CSS_SELECTOR, 'input[id="reg_password"]'))

    @property
    def register_email_TEXTBOX(self):
        return ElementList.TEXTBOX(
            self.driver, (By.CSS_SELECTOR, 'input[id="reg_email"]'))

    @property
    def register_button(self):
        return ElementList.BUTTON(
            self.driver, (By.CSS_SELECTOR,
                          'button[class="woocommerce-Button woocommerce-button button woocommerce-form-register__submit"]'))

    @property
    def cartcontents_link(self):
        return ElementList.LINK(
            self.driver, (By.CSS_SELECTOR, 'a[class="cart-contents"]'))

    # ===================================================== actions ================================================== #

    def user_login(self, username, password):
        self.username_TEXTBOX.enter_text(username)
        self.password_TEXTBOX.enter_text(password)
        self.driver.execute_script("window.scrollBy(0, 1000);")
        self.login_button.click()

    def user_logout(self):
        self.driver.execute_script("window.scrollBy(0, 1000);")
        self.Logout_link.click()

    def valid_user_registration(self, email, password):
        logger.info("\n\n\t\tRegistering user........")
        logger.info("\n\t\tEmail: {}\n\t\tPassword: {}\n\n".format(email, password))
        self.register_email_TEXTBOX.enter_text(email)
        self.register_password_TEXTBOX.enter_text(password)
        self.driver.execute_script("window.scrollBy(0, 1000);")
        self.register_button.click()

    def invalid_user_registration(self, email, password):
        self.register_email_TEXTBOX.enter_text(email)
        self.register_password_TEXTBOX.enter_text(password)
        try:
            if self.register_button.is_clickable() is False:
                logger.info("\n\nRegister Button Disabled : Please Enter Valid Username and Password\n\n")
        except:
            pass

    def verify_user_login(self):
        if self.Account_details_link.is_displayed() and self.Logout_link.is_displayed():
            logger.info("\n\nLogin Successful!\n\n")

    def verify_user_registration(self):
        self.verify_user_login()
        logger.info("\n\nUser Registration Successful!\n\n")

    def verify_login_or_registration_failed(self):
        if self.login_button.is_element_visible():
            logger.info("\n\nPlease Enter Valid Credentials\n\n")
