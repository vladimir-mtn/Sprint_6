import allure
from page_object.pages.base_page import BasePage
from page_object.locators.order_page_locators import OrderPagesLocators


class OrderPage(BasePage):

    @allure.step('Заполнение первой страницы заказа')
    def set_first_page_info(self, data):
        self.find_element_with_wait(OrderPagesLocators.ORDER_HEADER)
        self.add_text_to_element(OrderPagesLocators.NAME_INPUT, data['name'])
        self.add_text_to_element(OrderPagesLocators.SECOND_NAME_INPUT, data['surname'])
        self.add_text_to_element(OrderPagesLocators.ADDRESS_INPUT, data['address'])
        self.click_to_element(OrderPagesLocators.METRO_INPUT)
        self.click_to_element(OrderPagesLocators.METRO_STATION_OPTION)
        self.add_text_to_element(OrderPagesLocators.PHONE_INPUT, data['phone'])
        self.click_to_element(OrderPagesLocators.NEXT_BUTTON)
        return self
    
    @allure.step('Заполнение второй страницы заказа')
    def set_second_page_info(self, data):
        self.find_element_with_wait(OrderPagesLocators.RENTAL_HEADER)
        self.click_to_element(OrderPagesLocators.DELIVERY_DATE_INPUT)
        self.click_to_element(OrderPagesLocators.CALENDAR_DAY)
        self.click_to_element(OrderPagesLocators.RENTAL_PERIOD)
        self.click_to_element(OrderPagesLocators.RENTAL_PERIOD_DAYS)
        self.click_to_element(OrderPagesLocators.BLACK_PEARL)
        self.add_text_to_element(OrderPagesLocators.COMMENT_INPUT, data['comment'])
        return self

    @allure.step('Оформление заказа')
    def set_order(self, data):
        self.set_first_page_info(data)
        self.find_element_with_wait(OrderPagesLocators.RENTAL_HEADER)
        self.set_second_page_info(data)
        self.click_to_element(OrderPagesLocators.ORDER_BUTTON)
        return self

    @allure.step('Подтверждение заказа')
    def confirm_order(self):
        self.find_element_with_wait(OrderPagesLocators.CONFIRM_MODAL)
        self.click_to_element(OrderPagesLocators.CONFIRM_YES_BUTTON)
        return self
    
    @allure.step('Успешное завершение заказа')
    def is_order_successful(self):
        element = self.find_element_with_wait(OrderPagesLocators.SUCCESS_TITLE)
        return "Заказ оформлен" in element.text
  