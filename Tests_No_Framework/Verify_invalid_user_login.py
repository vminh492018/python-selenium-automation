from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class InvalidUserLoginError():

    url = "http://vuminhutc.local/my-account/"
    invalid_email = "abc@gmail.com"
    password_rand = "abc@123456"
    username_filed_id = "username"
    pssword_filed_id = "password"
    login_btn_css = 'button[value="Log in"]'
    xpath_msg = '//*[@id="content"]/div/div[1]/ul/li'
    expected_msg = "Unknown email address. Check again or try your username."

    # def __init__(self, driver=None):
    #     if driver is None:
    #         driver = {}
    #     else:
    #         self.driver = driver
    #     self.driver = webdriver.Chrome()
    #     self.driver.implicitly_wait(10)

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        # time.sleep(2)

    def go_to_website(self):
        self.driver.get(self.url)

    def input_email(self):
        email_filed = self.driver.find_element(By.ID,self.username_filed_id)
        email_filed.send_keys(self.invalid_email)

    def input_password(self):
        pssword_filed = self.driver.find_element(By.ID,self.pssword_filed_id)
        pssword_filed.send_keys(self.password_rand)

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_btn_css).click()

    def verify_error_message(self):
        err_elm = self.driver.find_element(By.XPATH,self.xpath_msg)
        dissplayed_err = err_elm.text
        # Sử dụng ngoại lệ để xử lý thông báo lỗi
        assert dissplayed_err == self.expected_msg, "FAILED!! The displayed  error is not expected"
        print("---------------------PASS---------------------")

    def main(self):
        self.go_to_website()
        # time.sleep(2)
        self.input_email()
        # time.sleep(2)
        self.input_password()
        # time.sleep(2)
        self.click_login()
        # time.sleep(2)
        self.verify_error_message()
        # time.sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    obj = InvalidUserLoginError()
    obj.main()