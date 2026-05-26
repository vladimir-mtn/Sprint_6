import allure
import pytest
from page_object.data import OrderDate
from page_object.locators.order_page_locators import OrderPagesLocators
from page_object.urls import URL_MAIN_PAGE


@allure.epic('Тестирование заказа самоката')
class TestOrderPage:
    
    @allure.title('Проверка заказа самоката')
    @allure.description('Проверяем заказ самоката с разными точками входа')
    @pytest.mark.parametrize('locator, order_data', [
        (OrderPagesLocators.ORDER_TOP_BUTTON, OrderDate.ORDER_DATE_1),
        (OrderPagesLocators.ORDER_BOTTOM_BUTTON, OrderDate.ORDER_DATE_2)
    ])
    def test_create_order(self, order_page, locator, order_data):
    
        order_page.go_to_url(URL_MAIN_PAGE)
        order_page.click_to_element(locator)
        order_page.set_order(order_data)
        order_page.confirm_order()

        assert order_page.is_order_successful()
