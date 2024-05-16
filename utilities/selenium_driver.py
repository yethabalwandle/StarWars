from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.wait import WebDriverWait

class SeleniumDriver():
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome()

    def open_browser(self, url: str):
        # Open the webpage
        self.driver.get(url)
        # Wait for a few seconds to let the page load
        time.sleep(3)

        # Print the title of the page
        print(self.driver.title)
        return True

    def click_elementby_xpath(self, xpath: str):
        # Find an element by its XPATH and interact with it
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()

    def get_text_by_xpath(self, xpath: str):
        # element = self.driver.find_element(By.XPATH, xpath)
        get_list = []
        count = self.driver.find_elements(By.XPATH, xpath)
        elements = len(count)
        for i in range(0, elements):
            get_list.append(self.driver.find_elements(By.XPATH, xpath)[i].text)

        return get_list


    def wait_for_element_byxpath(self, xpath: str):
        # wait for element to be present by its XPATH
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def enter_text_byxpath(self, xpath: str, text_to_enter: str):
        # Find an element by its xpath and send some text to it
        input_element = self.driver.find_element(By.XPATH)
        input_element.send_keys(text_to_enter)
        input_element.send_keys(Keys.RETURN)

    def kill_driver(self):
        # Close the browser window
        webdriver.Chrome().quit()






