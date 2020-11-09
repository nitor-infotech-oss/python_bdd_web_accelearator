# -*- coding: utf-8 -*-
from behave import *
from tests.pages.fashion_site_cart_page import fashion_site_cart_page


@step("I checkout the cart list page")
def proceed_to_checkout(context):
    fashion_site_cart_page(context.driver).select_free_shipping_radio()
    fashion_site_cart_page(context.driver).verify_free_shipping_selected()
    fashion_site_cart_page(context.driver).click_proceed_to_checkout_btn()
