from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.base_test import BaseTest # type: ignore

class TestLogout(BaseTest):

    def test_logout(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown-tab"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))).click()

        assert "login" in self.driver.current_url
