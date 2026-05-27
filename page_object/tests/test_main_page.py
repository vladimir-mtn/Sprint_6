import allure
import pytest 

from page_object.data import QuestionsData
from page_object.urls import URL_MAIN_PAGE, URL_ORDER_PAGE

@allure.epic('Тестирование главной страницы')
class TestMainPage:

    @allure.title('Проверка блока вопрос и ответ в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что при нажатии на стрелочку рядом с вопросом открывается соответствующий текст ответа.')
    @pytest.mark.parametrize('number', [0,1,2,3,4,5,6,7])
    def test_questions_and_answers(self, number, main_page):
        main_page.go_to_url(URL_MAIN_PAGE)
        assert(
            main_page.check_question_and_answer(number) == QuestionsData.ANSWERS_DATA[number])

    @allure.title('Проверка перехода на главную страницу по логотипу "Самоката"')
    @allure.description('Проверяем, что при нажатии на логотип "Самоката" открывается главная страница.')
    def test_scooter_logo_redirect_to_main_page(self, main_page):
        main_page.go_to_url(URL_ORDER_PAGE)
        main_page.click_scooter_logo()
    
        assert main_page.get_current_url() == URL_MAIN_PAGE
        assert main_page.is_on_main_page()
