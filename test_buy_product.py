"""
DigitalHarbor Confidential
CODE-123
(c) Copyright DH Corp. 2020
The source code for this program is not published. Copyright.
test_buy_a_product.py
    A set of tests to validate the buy of product via online.
"""

import time
import unittest
from selenium import webdriver

class BuyProduct(unittest.TestCase):
    """
    Class BuyProduct, this file have a set of tests to validate buy of products.
    """

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='./driver/geckodriver')
        self.driver.get('http://automationpractice.com/index.php')

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        """
        Test to validate login process.
        """
        self.driver.find_element_by_link_text("Sign in").click()
        self.driver.find_element_by_id("email").send_keys("devsoftbol@gmail.com")
        self.driver.find_element_by_id("passwd").send_keys("control123")
        self.driver.find_element_by_id("SubmitLogin").click()
        time.sleep(5)

    def test_search_shoes_item_to_buy(self):
        """
        Test to search an item to buy via online.
        """
        self.driver.find_element_by_id("search_query_top").send_keys("shoes")
        self.driver.find_element_by_name("submit_search").click()
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/div[3]/div[2]/ul/li[2]/div/div[1]/div/a[1]/img").click()
        self.driver.find_element_by_name("Submit").click()
        time.sleep(5)


if __name__ == "__main__":
    unittest.main()
