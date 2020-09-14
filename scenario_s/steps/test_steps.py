from pytest_bdd import given, when, then
from start_point import browser
from helpers import funcs
import time
import pytest


@given('I am on the main page with having menu opened')
def open_page1():
    funcs.feb_cn('mega-menu-link')

#    time.sleep(3)

@when('I click on the "all wedding dresses" link')
def open_page2():
    funcs.feb_lt('All wedding dresses')

# @when('I click on first product in the list')
# def open_page3():
#     funcs.feb_cn('woocommerce-loop-product__title')

@when('I click on first product in the list')
def open_page3():
    funcs.feb_lt('WEDDING DRESS MARINA')

@when('I click on the "Pay deposit" button')
def open_page4():
    funcs.feb_xp('/html/body/div[2]/div[3]/div/div[2]/div/div/div[3]/div[2]/form/div/div[2]/ul/li[1]/label')

@when('I click on the "Add to cart" button')
def open_page5():
    funcs.feb_xp('/html/body/div[2]/div[3]/div/div[2]/div/div/div[3]/div[2]/form/div/div[3]/button')

@when('I click on the "View cart" button')
def open_page6():
    funcs.feb_xp('//*[@id="content"]/div[2]/div/a')

@then('"payable in total" text is against product name in the cart')
def verify():
    try:
        quantity = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/main/div/div/div[1]/form/table/tbody/tr[1]/td[4]/div/input')
        if quantity.get_attribute('value') == 1:
            assert 'payable in total' in browser.find_element_by_xpath(
                '//*[@id="post-10"]/div/div[1]/form/table/tbody/tr[1]/td[5]/small/text()')

    finally:
        browser.close()


# #@pytest.fixture()
# def teardown():
#     # yield browser
#     browser.close()