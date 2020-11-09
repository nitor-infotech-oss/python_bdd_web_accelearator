from tests.pages.base_page import BasePage
from tests.web_element.element_list import ElementList
from selenium.webdriver.common.by import By
import time
from data_providers import logging_data

logger = logging_data.log_message(log_level="INFO", logger_name="root")


class fashion_site_cart_page(BasePage):

    @property
    def coupon_code_TEXTBOX(self):
        return ElementList.TEXTBOX(
            self.driver, (By.CSS_SELECTOR, 'input[id="coupon_code"]'))

    @property
    def apply_coupon_button(self):
        return ElementList.BUTTON(
            self.driver, (By.CSS_SELECTOR, 'button[name="apply_coupon"]'))

    @property
    def proceed_to_checkout_button(self):
        return ElementList.BUTTON(
            self.driver, (By.CSS_SELECTOR, '.checkout-button.button.alt.wc-forward'))

    @property
    def free_shipping_radio(self):
        return ElementList.RADIOBUTTON(
            self.driver, (By.ID, 'shipping_method_0_free_shipping1'))

    # ===================================================== actions ================================================== #

    def select_free_shipping_radio(self):
        time.sleep(5)
        logger.info("\n\nSelecting Free Shipping Option\n\n")
        self.free_shipping_radio.select()

    def verify_free_shipping_selected(self):
        time.sleep(5)
        logger.info("\n\nVerifying Shipping Method\n\n")
        self.free_shipping_radio.is_selected()

    def click_proceed_to_checkout_btn(self):
        time.sleep(5)
        logger.info("\n\nProceed to Checkout\n\n")
        self.proceed_to_checkout_button.click()

    def apply_coupon_to_cart(self):
        self.coupon_code_TEXTBOX.enter_text("TEST50")
        self.apply_coupon_button.click()
