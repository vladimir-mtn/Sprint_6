import allure
from page_object.locators.main_page_locators import MainPagesLocators
from page_object.locators.redirect_page_locators import RedirectPagesLocators
from page_object.pages.base_page import BasePage


class RedirectPage(BasePage):

    @allure.step('Клик на логотип Яндекса')
    def click_yandex_logo(self):
        self.click_to_element(MainPagesLocators.YANDEX_LOGO)
        return self
    
    @allure.step('Редирект на главную страницу YA')
    def is_ya_page_opened(self):
        self.switch_to_new_window()
        return self.find_element_with_wait(RedirectPagesLocators.IMAGE_SEARCH_BUTTON)
