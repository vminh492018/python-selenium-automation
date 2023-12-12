#go to my account
#type username->password
#click login
#verify error message
import time
import pytest
from Tests_with_Pytest_Framework.ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:
    @pytest.mark.tcid1
    def test_login_none_existing_user(self):

        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_username("aaabbbccc@gmail.com")
        my_account.input_login_password("ABC@D123456789")
        time.sleep(5)
        my_account.click_login_button()
        time.sleep(5)

        expected_err1 = "Unknown email address. Check again or try your username!!!!!!!"
        expected_err = "Unknown email address. Check again or try your username."
        my_account.wait_until_error_is_displayed(expected_err)
