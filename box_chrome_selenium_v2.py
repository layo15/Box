#!/usr/bin/python

import sys
import unittest
from time import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

class BoxUpload(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Chrome session with Apple Connect extension
        chrome_options = Options()
        chrome_options.add_extension('/Users/laodo/Downloads/AppleConnect-Extension-for-Chrome_v1.0.4.crx')
        inst.driver = webdriver.Chrome(chrome_options=chrome_options)
        #inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()

        try:

            # navigate to the box home page
            inst.driver.get("http://www.box.com/")

            # wait for login button to be present and click on it
            login_button = WebDriverWait(inst.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".user-nav--login.user-nav--item"))
                )

            login_button.click()

            # wait for login field to be present and enter login id
            login_field = WebDriverWait(inst.driver, 10).until(
                            EC.presence_of_element_located((By.NAME, "login"))
                        )

            login_field.send_keys("lao_do@gmail.com")
            login_field.submit()
        except Exception:
                inst.driver.quit()
                raise


    def test_small_file_upload(self):
        # wait for page to finish loading with upload menu button.
        upload_menu = WebDriverWait(self.driver, 30).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-primary.upload-menu-btn"))
                            )

        # click on upload menu button
        upload_menu.click()

        # make upload file element visible and upload a file.
        upload_element = self.driver.find_element_by_class_name("upload-handler-picker")

        self.driver.execute_script('document.getElementsByClassName("upload-handler-picker")[0].removeAttribute("style")')

        start_time = time()
        upload_element.send_keys("/Users/laodo/temp")

        WebDriverWait(self.driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".uploads-manager.is-completed"))
            )
        end_time = time()

        # print out file upload duration
        print("Upload time for small file: " + str(round(end_time-start_time, 3)))

    def test_large_file_upload(self):
        # wait for page to finish loading with upload menu button.
        upload_menu = WebDriverWait(self.driver, 30).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-primary.upload-menu-btn"))
                            )

        # click on upload menu button
        upload_menu.click()

        # make upload file element visible and upload a file.
        upload_element = self.driver.find_element_by_class_name("upload-handler-picker")

        self.driver.execute_script('document.getElementsByClassName("upload-handler-picker")[0].removeAttribute("style")')

        start_time = time()
        upload_element.send_keys("/Users/laodo/lao_go.tar")

        WebDriverWait(self.driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".uploads-manager.is-completed"))
            )
        end_time = time()

        # print out file upload duration
        print("Upload time for large file: " + str(round(end_time-start_time, 3)))

    @classmethod
    def tearDownClass(inst):
        # close browser
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()
