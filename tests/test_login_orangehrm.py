from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")

# Login
username = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "username"))
)
username.send_keys("Admin")

password = driver.find_element(By.NAME, "password")
password.send_keys("admin123")

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Verify Dashboard
dashboard = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
)
assert dashboard.is_displayed(), "Dashboard not displayed!"

print("Login Test Passed")

driver.quit()
def test_login_invalid_password(self):
    wait = WebDriverWait(self.driver, 10)

    wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
    self.driver.find_element(By.NAME, "password").send_keys("wrongpass")
    self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    error = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Invalid')]"))
    )

    assert error.is_displayed()
