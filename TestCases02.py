import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestAddCart(unittest.TestCase):

    def setUp(self):
       self.driver = webdriver.Chrome(ChromeDriverManager().install())

    # def a_success_login(self):
    #     self.driver.get("https://www.saucedemo.com")
    #     time.sleep(6)
    #     self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
    #     time.sleep(1)
    #     self.driver.find_element(By.ID,"password").send_keys("secret_sauce")
    #     time.sleep(2)
    #     self.driver.find_element(By.ID,"login-button").click()
    #     time.sleep(4)

    def test_a_success_add_to_cart(self):

        # Login
        self.driver.get("https://www.saucedemo.com")
        time.sleep(3)
        self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        self.driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(2)
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(3)

        # Test Button Add
        self.driver.find_element(By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"add-to-cart-sauce-labs-onesie").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)

        # Test Button Remove
        self.driver.find_element(By.ID,"remove-to-cart-test.allthethings()-t-shirt-(red)").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"remove-to-cart-sauce-labs-bike-light").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"remove-to-cart-sauce-labs-bolt-t-shirt").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"remove-to-cart-sauce-labs-onesie").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"remove-to-cart-sauce-labs-fleece-jacket").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"remove-to-cart-sauce-labs-backpack").click()
        time.sleep(1)

        # Mulai Pilih Orderan
        self.driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"add-to-cart-sauce-labs-onesie").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"shopping_cart_container").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"remove-to-cart-sauce-labs-onesie").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"checkout").click()
        time.sleep(1)

        # Mengosongkan Detail Alamat
        self.driver.find_element(By.ID,"afirst-name").send_keys("")
        time.sleep(1)
        self.driver.find_element(By.ID,"last-name").send_keys("")
        time.sleep(1)
        self.driver.find_element(By.ID,"postal-code").send_keys("")
        time.sleep(1)
        self.driver.find_element(By.ID,"continue").click()
        time.sleep(1)

        # Mengisi Detail Alamat
        self.driver.find_element(By.ID,"afirst-name").send_keys("Gianyar")
        time.sleep(1)
        self.driver.find_element(By.ID,"last-name").send_keys("Alam")
        time.sleep(1)
        self.driver.find_element(By.ID,"postal-code").send_keys("32003")
        time.sleep(1)
        self.driver.find_element(By.ID,"continue").click()
        time.sleep(1)


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()