
from Tests_with_Pytest_Framework.ssqatest.src.pages.locators.MyAccountSignedInLocators import MyAccountSignedInLocators
from Tests_with_Pytest_Framework.ssqatest.src.SeleniumExtended import SeleniumExtended

class MyAccountSignedIn(MyAccountSignedInLocators):

    def __init__(self,driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_user_is_signed_in(self):
        self.sl.wait_until_element_is_visible(self.Left_nav_logout_btn)
