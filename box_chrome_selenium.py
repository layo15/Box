import unittest
from time import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options

class BoxUpload(unittest.TestCase):
    def setUp(self):
        # create a new Chrome session with Apple Connect extension
        chrome_options = Options()
        chrome_options.add_extension('/Users/laodo/Downloads/AppleConnect-Extension-for-Chrome_v1.0.4.crx')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://www.box.com/")

        login_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".user-nav--login.user-nav--item"))
            )

        login_button.click()

        login_field = WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((By.NAME, "login"))
                        )

        login_field.send_keys("lao_do@gmail.com")
        login_field.submit()

        self.upload_menu = WebDriverWait(self.driver, 30).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-primary.upload-menu-btn"))
                            )

    def test_file_upload(self):

        #upload_menu = self.driver.find_element_by_xpath('//*[@id="mod-action-bar-1"]/div[2]/div[2]/div[2]/a')
        self.upload_menu.click()

        upload_element = self.driver.find_element_by_class_name("upload-handler-picker")

        self.driver.execute_script('document.getElementsByClassName("upload-handler-picker")[0].removeAttribute("style")')

        start_time = time()
        upload_element.send_keys("/Users/laodo/Projects/jmeter.log") 

        WebDriverWait(self.driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".uploads-manager.is-completed"))
            )
        end_time = time()

        print("Upload time: " + str(round(end_time-start_time, 3)))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
