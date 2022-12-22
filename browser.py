from io import BytesIO
from time import sleep

from selenium.common import exceptions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains, Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from logger import logger
from captcha_solver import CaptchaServiceError, CaptchaSolver, SolutionTimeoutError
from PIL import Image

LOGGER = logger('browser')


class Browser:
    def __init__(self, proxy=None):
        self.options = ChromeOptions()
        if proxy:
            self.options.add_argument(f'--proxy-server={proxy}')
        self.driver = Chrome(r'C:\Users\KIEV-COP-4\chromedriver.exe', options=self.options)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()

    def first_page(self, f_name, l_name, nickname, password):
        try:
            WebDriverWait(self.driver, 10).until(
                lambda d: self.driver.find_element_by_xpath('//*/input[@name="firstName"]')
            ).send_keys(f_name)
            self.driver.find_element_by_xpath('//*/input[@name="lastName"]').send_keys(l_name)
            self.driver.find_element_by_xpath('//*/input[@name="Username"]').send_keys(nickname)
            self.driver.find_element_by_xpath('//*/input[@name="Passwd"]').send_keys(password)
            self.driver.find_element_by_xpath('//*/input[@name="ConfirmPasswd"]').send_keys(password)
            return True
        except (TimeoutException, Exception) as error:
            LOGGER.error(error)
            return False

    def phone_input(self, phone):
        try:
            WebDriverWait(self.driver, 10).until(
                lambda d: self.driver.find_element_by_xpath('//*/input[@type="tel"]')).send_keys(phone)
            self.driver.find_element_by_xpath('//*/div[2]/div/div[1]/div/div/button').click()
            return True
        except Exception as error:
            LOGGER.error(error)
            return False

    def phone_confirmation(self, code):
        try:
            telephone_element = lambda d: self.driver.find_element_by_xpath('//*/input[@type="tel"]')
            WebDriverWait(self.driver, 10).until(
                telephone_element).send_keys(code)
            self.driver.find_element_by_xpath('//*/div[2]/div[2]/div[1]/div/div/button').click()
            WebDriverWait(self.driver, 10).until_not(
                telephone_element).send_keys(code)
        except Exception as error:
            LOGGER.error(error)
            return False

    def second_page(self):
        breakpoint()
        '//*/input[@name="day"]'
        '//*[@id="month"]/option[2]'
        '//*/input[@name="year"]'

    def reg(self, phone, f_name='test', l_name='test', nickname='test', password='test', ):
        self.driver.get('https://accounts.google.com/signup/v2/webcreateaccount?service=mail&cont'
                        'inue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=Gli'
                        'fWebSignIn&flowEntry=SignUp')
        result = self.first_page(f_name, l_name, nickname, password)
        if result:
            self.driver.find_element_by_css_selector('#accountDetailsNext > div > button').click()
        self.phone_input(phone)
        return result
