from selenium.webdriver.common.by import By
class MyAcoountSingedOutLocator:
    Login_Username = (By.ID,'username')
    Login_Password = (By.ID,'password')
    Login_Btn = (By.CSS_SELECTOR,'button[value="Log in"]')

    Error_ul = (By.CSS_SELECTOR,'ul.woocommerce-error')

    Register_Email = (By.ID, 'reg_email')
    Register_Password =(By.ID, 'reg_password')
    Register_Btn = (By.CSS_SELECTOR,'button[value="Register"]')