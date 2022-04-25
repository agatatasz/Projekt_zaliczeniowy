# Import bibliotek
import unittest
from selenium import webdriver

class BaseTestHome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://ccc.eu/pl/")
        self.driver.implicitly_wait(10)

    def test_checkBrowser(self):
        driver = self.driver

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


