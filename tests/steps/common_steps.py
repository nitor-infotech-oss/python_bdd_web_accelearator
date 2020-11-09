from behave import *
from tests.utils import common


@step("I navigate to '{page}' page")
def go_to(context, page):
    common.go_to(context, page)
