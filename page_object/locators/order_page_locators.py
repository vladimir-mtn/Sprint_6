from selenium.webdriver.common.by import By

class OrderPagesLocators:

    ORDER_TOP_BUTTON = By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']"
    ORDER_BOTTOM_BUTTON = By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"
    ORDER_HEADER = By.XPATH, "//div[text()='Для кого самокат']"
    NAME_INPUT = By.XPATH, "//input[@placeholder='* Имя']"
    SECOND_NAME_INPUT = By.XPATH, "//input[@placeholder='* Фамилия']"
    ADDRESS_INPUT = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    METRO_INPUT = By.XPATH, "//input[@placeholder='* Станция метро']"
    METRO_STATION_OPTION = By.XPATH, "//div[text()='Черкизовская']"
    PHONE_INPUT = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    NEXT_BUTTON = By.XPATH, "//button[text()='Далее']"

    RENTAL_HEADER = By.XPATH, "//div[text()='Про аренду']"
    DELIVERY_DATE_INPUT = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    CALENDAR_DAY = By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='10']"
    RENTAL_PERIOD = By.XPATH, "//div[text()='* Срок аренды']"
    RENTAL_PERIOD_DAYS = By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']"
    BLACK_PEARL = By.XPATH, "//label[text()='чёрный жемчуг']"
    COMMENT_INPUT = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    ORDER_BUTTON = By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']"
    CONFIRM_MODAL = By.XPATH, "//div[contains(text(), 'Хотите оформить заказ?')]"
    CONFIRM_YES_BUTTON = By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Да']"
    SUCCESS_TITLE = By.XPATH, '//div[text()="Заказ оформлен"]'
