from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class SeleniumTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    # TC1 - Login thành công
    def test_TC1_login_success(self):

        self.driver.get(
            "https://the-internet.herokuapp.com/login"
        )

        self.driver.find_element(
            By.ID,
            "username"
        ).send_keys("tomsmith")

        self.driver.find_element(
            By.ID,
            "password"
        ).send_keys("SuperSecretPassword!")

        self.driver.find_element(
            By.CSS_SELECTOR,
            "button[type='submit']"
        ).click()

        message = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "flash")
            )
        )

        self.assertIn(
            "You logged into a secure area!",
            message.text
        )

    # TC2 - Login sai mật khẩu
    def test_TC2_login_fail(self):

        self.driver.get(
            "https://the-internet.herokuapp.com/login"
        )

        self.driver.find_element(
            By.ID,
            "username"
        ).send_keys("tomsmith")

        self.driver.find_element(
            By.ID,
            "password"
        ).send_keys("123456")

        self.driver.find_element(
            By.CSS_SELECTOR,
            "button[type='submit']"
        ).click()

        message = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "flash")
            )
        )

        self.assertIn(
            "Your password is invalid!",
            message.text
        )

    # TC3 - Logout
    def test_TC3_logout(self):

        self.driver.get(
            "https://the-internet.herokuapp.com/login"
        )

        self.driver.find_element(
            By.ID,
            "username"
        ).send_keys("tomsmith")

        self.driver.find_element(
            By.ID,
            "password"
        ).send_keys("SuperSecretPassword!")

        self.driver.find_element(
            By.CSS_SELECTOR,
            "button[type='submit']"
        ).click()

        logout_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "a.button")
            )
        )

        logout_btn.click()

        message = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "flash")
            )
        )

        self.assertIn(
            "You logged out of the secure area!",
            message.text
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)