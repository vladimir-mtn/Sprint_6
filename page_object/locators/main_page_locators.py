from selenium.webdriver.common.by import By

class MainPagesLocators:

    MAIN_PAGE_HEADER = By.XPATH, "//div[contains(@class, 'Home_Header') and contains(text(), 'Самокат')]"
    QUESTION_LOCATOR = By.XPATH, "//*[@id='accordion__heading-{}']"
    ANSWER_LOCATOR =  By.XPATH, "//*[@id='accordion__panel-{}']"
    QUESTION_LOCATOR_TO_SCROLL = By.XPATH, "//*[@id='accordion__heading-7']"
    SCOOTER_LOGO = By.XPATH, "//img[@alt='Scooter']"
    YANDEX_LOGO = By.XPATH, "//img[@alt='Yandex']"
