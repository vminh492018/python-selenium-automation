import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
def add_1_item_to_cart():
    driver.find_element(By.CLASS_NAME,"add_to_cart_button").click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH,'//*[@id="site-header-cart"]/li[1]/a/span[2]'), '1 item'))
# classss ="button wp-element-button product_type_simple add_to_cart_button ajax_add_to_cart"

def click_cart_in_top_menu():
    driver.find_element(By.XPATH,'//*[@id="site-header-cart"]/li[1]/a/span[2]').click()

def input_coupon_and_hit_enter(coupon_code):
    coupon_filed = wait.until(EC.visibility_of_element_located((By.ID,'coupon_code')))
    # coupon_filed = driver.find_element(By.ID,"coupon_code")
    coupon_filed.send_keys(coupon_code)
    time.sleep(5)
    coupon_filed.send_keys(Keys.ENTER)
    #time.sleep(10)

def verify_total_is_0():
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="post-7"]/div[1]/div/div[2]/div/table/tbody/tr[3]/td/strong/span/bdi'),'0 ₫'))


if __name__ == '__main__':
    coupon_code = "UTC100"
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver,10)
    driver.get("http://vuminhutc.local/")
    add_1_item_to_cart()
    time.sleep(3)
    click_cart_in_top_menu()
    time.sleep(3)
    input_coupon_and_hit_enter(coupon_code)
    time.sleep(5)
    verify_total_is_0()
    time.sleep(5)
    print("----------PASS----------")
    driver.quit()
