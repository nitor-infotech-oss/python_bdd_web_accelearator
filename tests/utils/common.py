"""
Module containing common function used in several tests.
Functions that are not test or feature specific.
"""
from faker import Faker
from selenium import webdriver
from data_providers import logging_data
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.ie.options import Options

fake = Faker()


def go_to(context, page, **kwargs):
    """
    Function to start instance of the specified browser and navigate to the specified url.
    """
    browser = context.config.userdata.get('browser')
    headless = context.config.userdata.get('headless')
    log_level = context.config.userdata.get('log_level')
    env = context.config.userdata.get('env')
    base_url = "http://mystore." + env + "/"
    if not page.startswith('http'):
        base_url = base_url
        if page == 'home' or page is None:
            url = base_url
        else:
            url = base_url + str(page)

    logger = logging_data.log_message(log_level, "root")

    if not browser:
        browser = 'edge'
    if not headless:
        headless = 'true'
    if browser.lower() == 'chrome':
        if str(headless).lower() == 'true':
            logger.info("\nRunning Test on Headless Chrome......\n")
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            context.driver = webdriver.Chrome(options=options)
        else:
            logger.info("\nRunning Test on Chrome......\n")
            context.driver = webdriver.Chrome()

    elif browser.lower() in ('ff', 'firefox'):
        if str(headless).lower() == 'true':
            logger.info("\nRunning Test on Headless Firefox......\n")
            options = webdriver.FirefoxOptions()
            options.add_argument('-headless')
            context.driver = webdriver.Firefox(firefox_options=options)

        else:
            logger.info("\nRunning Test on Firefox......\n")
            context.driver = webdriver.Firefox()

    elif browser in ('edge', 'EDGE'):
        if str(headless).lower() == 'true':
            logger.info("\nRunning Test on Headless EDGE......\n")
            options = EdgeOptions()
            options.use_chromium = True
            options.add_argument("headless")
            options.add_argument("disable-gpu")
            context.driver = Edge(options=options)

        else:
            logger.info("\nRunning Test in EDGE......\n")
            options = EdgeOptions()
            options.use_chromium = True
            context.driver = Edge(options=options)

    elif browser in ('ie', 'IE'):
        print("\nRunning Test Internet explorer......\n")
        opts = Options()
        opts.ignore_protected_mode_settings = True
        opts.ignore_zoom_level = True
        opts.require_window_focus = True
        context.driver = webdriver.Ie(options=opts)

    else:
        raise Exception("The browser type '{}' is not supported".format(browser))

    # clean the url and go to the url
    wait = int(kwargs['implicitly_wait']) if 'implicitly_wait' in kwargs.keys() else 15
    context.driver.implicitly_wait(wait)

    url = url.strip()
    logger.info("Navigating to URL : {}".format(url))
    context.driver.maximize_window()
    context.driver.get(url)


def generate_random_email_and_password():
    email = fake.email()

    password_string = fake.password()

    random_info = {
        'email': email,
        'password': password_string
    }
    return random_info


def generate_random_first_and_last_name():
    random_f_name = fake.first_name()
    random_l_name = fake.last_name()

    return {
        'f_name': random_f_name,
        'l_name': random_l_name
    }


def generate_random_details():
    full_addr = fake.address()
    addr_1 = full_addr.split("\n")[0]
    company_name = fake.company()
    city_name = fake.city()
    zip_code = fake.zipcode()
    phone_number = fake.random_int(9000000000, 9999999999)

    return {
        'company': company_name,
        'city': city_name,
        'addr_1': addr_1,
        'zip': "{}{}".format(zip_code, fake.random_int(0, 9)),
        'phone': str(phone_number)

    }
