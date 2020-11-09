from behave import *
from tests.pages.fashion_site_product_page import fashion_site_product_page


@step("I verify the '{item}' search result")
def verify_search_result(context, item):
    fashion_site_product_page(context.driver).add_to_cart(item)
