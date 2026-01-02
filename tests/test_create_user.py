from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from utils.base_test import BaseTest 
import time

class TestCreateUser(BaseTest):

    def test_create_new_user(self):
        wait = WebDriverWait(self.driver, 15)

        # -------- LOGIN --------
        wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # -------- NAVIGATE TO ADMIN > USERS --------
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='User Management']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Users']"))).click()

        # -------- CLICK ADD --------
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//text()='Add']"))).click()

        # -------- FILL USER FORM --------

        # User Role dropdown
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class,'select-text')])[1]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='ESS']"))).click()

        # Employee Name (Auto-suggest)
        employee_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']")))
        employee_input.send_keys("a")
        time.sleep(2)
        employee_input.send_keys("\ue007")  # ENTER key

        # Status dropdown
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class,'select-text')])[2]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Enabled']"))).click()

        # Username
        username = f"qa_user_{int(time.time())}"
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]").send_keys(username)

        # Password
        self.driver.find_element(By.XPATH, "(//input[@type='password'])[1]").send_keys("Test@1234")
        self.driver.find_element(By.XPATH, "(//input[@type='password'])[2]").send_keys("Test@1234")

        # -------- SAVE --------
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # -------- VERIFICATION --------
        search_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
        search_input.send_keys(username)

        self.driver.find_element(By.XPATH, "//button[.//text()='Search']").click()

        result = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='oxd-table-card']"))
        )

        assert result.is_displayed(), "User was not created successfully"
