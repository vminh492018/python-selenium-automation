from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random
import time

# time.sleep(3)
#Go to the website
driver = webdriver.Chrome()
url = "http://vuminhutc.local/my-account/"
driver.get(url)
driver.implicitly_wait(10)
#Element values
email_filed_id = "reg_email"
psswd_filed_id = "reg_password"
register_btn_css = 'button[value="Register"]'
logout_btn_css = "li.woocommerce-MyAccount-navigation-link--customer-logout a"

#Generate random email
letters = string.ascii_lowercase
rand_string = "".join(random.choice(letters) for i in range(15))
rand_email = rand_string + '@gmail.com'
#Type in the email filed
email_filed = driver.find_element(By.ID,email_filed_id)
email_filed.send_keys(rand_email)
#find password filed and enter password
psswd_filed = driver.find_element(By.ID, psswd_filed_id)
psswd_filed.send_keys("minh@181403383")
#Click register button
# time.sleep(10)
register_btn = driver.find_element(By.CSS_SELECTOR,register_btn_css)
register_btn.click()
time.sleep(10)
try:
    logout_btn = driver.find_element(By.CSS_SELECTOR,logout_btn_css)
except:
    raise Exception("User not logged in after registering !!")
if logout_btn.is_displayed():
    print("---------------------PASS---------------------")
else:
    raise Exception("User not logged in after registering !!")