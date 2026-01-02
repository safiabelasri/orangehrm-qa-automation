from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class BaseTest:

    def setup_method(self):
        """
        This method runs before each test.
        Initializes WebDriver and opens OrangeHRM application.
        """
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def teardown_method(self):
        """
        This method runs after each test.
        Closes the browser.
        """
        if self.driver:
            self.driver.quit()
