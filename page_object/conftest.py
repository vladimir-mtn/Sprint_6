import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from page_object.pages.main_page import MainPage
from page_object.pages.order_page import OrderPage
from page_object.pages.redirect_page import RedirectPage
from page_object.urls import URL_MAIN_PAGE


@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get(URL_MAIN_PAGE)
    driver.add_cookie({"name": "Cartoshka", "value": "true"})
    driver.add_cookie({"name": "Cartoshka-legacy", "value": "true"})
    driver.refresh()
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.timeout = 10
    return page

@pytest.fixture
def order_page(driver):
    page = OrderPage(driver)
    page.timeout = 10
    return page

@pytest.fixture
def redirect_page(driver):
    page = RedirectPage(driver)
    page.timeout = 10
    return page
