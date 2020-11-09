# -*- coding: utf-8 -*-
from behave import *
from tests.pages.fashion_site_checkout_page import fashion_site_checkout_page
from tests.pages.fashion_site_order_received_page import order_received_page
import time


@step("I verify the details on order confirmation page")
def verify_order_received(context):
    fashion_site_checkout_page(context.driver).verify_checkout_page_loaded()
    fashion_site_checkout_page(context.driver).fill_details()
    fashion_site_checkout_page(context.driver).place_order()
    time.sleep(20)
    order_received_page(context.driver).verify_order_received()
