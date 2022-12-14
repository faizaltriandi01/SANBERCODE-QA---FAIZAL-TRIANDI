import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
       self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_login(self):
        self.driver.get("https://www.saucedemo.com")
        time.sleep(6)
        self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        self.driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(2)
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(4)

    def test_b_failed_login_with_empthy_username(self):
        self.driver.get("https://www.saucedemo.com")
        time.sleep(6)
        self.driver.find_element(By.ID,"user-name").send_keys("")
        time.sleep(1)
        self.driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(2)
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(4)

    def test_c_failed_login_with_empthy_password(self):
        self.driver.get("https://www.saucedemo.com")
        time.sleep(6)
        self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        self.driver.find_element(By.ID,"password").send_keys("")
        time.sleep(2)
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(4)

    def test_d_failed_login_with_wrong_username(self):
        self.driver.get("https://www.saucedemo.com")
        time.sleep(6)
        self.driver.find_element(By.ID,"user-name").send_keys("kalvy_dawn")
        time.sleep(1)
        self.driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(2)
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(4)

    def test_e_failed_login_with_wrong_username(self):
        self.driver.get("https://www.saucedemo.com")
        time.sleep(6)
        self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        self.driver.find_element(By.ID,"password").send_keys("kalvindawn")
        time.sleep(2)
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(4)

    def tearDown(self):
        self.driver.close()
