from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Tests_with_Pytest_Framework.ssqatest.src.pages.locators.MyAccountSignedOutLocator import MyAcoountSingedOutLocator
from Tests_with_Pytest_Framework.ssqatest.src.SeleniumExtended import SeleniumExtended
from Tests_with_Pytest_Framework.ssqatest.src.helpers.config_helpers import get_base_url
class MyAccountSignedOut(MyAcoountSingedOutLocator):

    endpoint = '/my-account/'

    def __init__(self,driver):
        self.driver =driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_account(self):
        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        self.driver.get(my_account_url)

    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.Login_Username, username)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.Login_Password, password)

    def click_login_button(self):
        self.sl.wait_and_click(self.Login_Btn)

    def  wait_until_error_is_displayed(self,exp_err):
        self.sl.wait_until_element_constains_text(self.Error_ul,exp_err)

    def input_register_email(self, email):
        self.sl.wait_and_input_text(self.Register_Email, email)

    def input_register_password(self, password):
        self.sl.wait_and_input_text(self.Register_Password, password)

    def click_register_button(self):
        self.sl.wait_and_click(self.Register_Btn)
