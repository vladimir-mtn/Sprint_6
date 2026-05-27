from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        self.wait.until(
            EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    def click_to_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def scroll_to_element(self, locator):
        self.find_element_with_wait(locator)

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_to_element(self, locator):
        return self.find_element_with_wait(locator).text
    
    def format_locators(self, locator_1, number):
        method, locator = locator_1 
        locator = locator.format(number)
        return method, locator    

    def switch_to_new_window(self):
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])  # берём последнее окно
        return self

    def get_current_url(self):
        return self.driver.current_url
    