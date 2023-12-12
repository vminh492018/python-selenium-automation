# Step:
# go to my account
# fill in email
# fill in password
# click register
# verify user is register


import pytest
import time
from Tests_with_Pytest_Framework.ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from Tests_with_Pytest_Framework.ssqatest.src.pages.MyAccountSignedIn import MyAccountSignedIn
from Tests_with_Pytest_Framework.ssqatest.src.helpers.generic_helpers import generate_random_email_and_password
@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:

    @pytest.mark.tcid2
    def test_register_valid_new_user(self):
        my_account_o = MyAccountSignedOut(self.driver)
        my_account_i = MyAccountSignedIn(self.driver)
        my_account_o.go_to_my_account()

        random_email = generate_random_email_and_password()
        my_account_o.input_register_email(random_email["email"])
        time.sleep(2)
        my_account_o.input_register_password("Miil@11")
        time.sleep(2)
        my_account_o.click_register_button()
        time.sleep(5)

        my_account_i.verify_user_is_signed_in()