from tests.web_element.element_list import ElementList
from tests.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time
from data_providers import logging_data

logger = logging_data.log_message(log_level="INFO", logger_name="root")


class order_received_page(BasePage):

    @property
    def thank_you_label(self):
        return ElementList.LABEL(
            self.driver, (By.CSS_SELECTOR, 'div.woocommerce-order p.woocommerce-thankyou-order-received'))
    # ===================================================== actions ================================================== #

    def verify_order_received(self):
        time.sleep(5)
        if self.thank_you_label.is_element_visible():
            logger.info("\n\nOrder Received\n\n")
        else:
            logger.info("\n\nFailed to place Order\n\n")
