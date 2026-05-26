import allure
from page_object.locators.main_page_locators import MainPagesLocators
from page_object.pages.base_page import BasePage


class MainPage(BasePage):
    
    @allure.step('Клик по вопросу')
    def click_to_question(self, number):
        locator_question_formatted = self.format_locators(
            MainPagesLocators.QUESTION_LOCATOR, number)
        self.scroll_to_element(MainPagesLocators.QUESTION_LOCATOR_TO_SCROLL)
        self.click_to_element(locator_question_formatted)

    @allure.step('Получение ответа на вопрос')
    def get_answer_text(self, number):
        locator_answer_formatted = self.format_locators(
            MainPagesLocators.ANSWER_LOCATOR, number)
        return self.get_text_to_element(locator_answer_formatted)
    
    @allure.step('Проверка блока вопрос ответ')
    def check_question_and_answer(self, number):
        self.click_to_question(number)
        return self.get_answer_text(number)
    
    @allure.step('Клик на логотип Самоката')
    def click_scooter_logo(self):
        self.click_to_element(MainPagesLocators.SCOOTER_LOGO)
        return self
    
    @allure.step('Проверка, что открыта главная страница')
    def is_on_main_page(self):
        return self.find_element_with_wait(MainPagesLocators.MAIN_PAGE_HEADER)
