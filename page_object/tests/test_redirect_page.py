import allure
import pytest
from page_object.urls import URL_MAIN_PAGE

@allure.epic('Тестирование переходов')
class TestRedirectPage:
    
    @allure.title('Проверка перехода на главную страницу YA по логотипу "Яндекса"')
    @allure.description('Проверяем, что при нажатии на логотип "Яндекса" открывается главная страница YA.')
    def test_yandex_logo_redirects_to_ya(self, redirect_page):
        
        redirect_page.go_to_url(URL_MAIN_PAGE)
        redirect_page.click_yandex_logo()

        assert redirect_page.is_ya_page_opened()
 