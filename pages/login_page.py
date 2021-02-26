"""
This module contain the page object for the login page.
"""

from appium.webdriver.common.mobileby import MobileBy 
import time


class LoginPage:

    EMAIL_TEXTBOX = (MobileBy.ID,"com.todoist:id/email_exists_input")
    CONTINUE_WITH_EMAIL_BTN = (MobileBy.ID,"com.todoist:id/btn_continue_with_email")
    PASSWORD_TEXTBOX = (MobileBy.ID,"com.todoist:id/log_in_password")
    LOGIN_BTN = (MobileBy.ID,"com.todoist:id/btn_log_in")
    

    def __init__(self,driver):
        self.driver = driver

    def login(self):
        #TODO read login creds from other files
        self.driver.find_element(*self.EMAIL_TEXTBOX).send_keys("bashang.basir@gmail.com")
        self.driver.find_element(*self.CONTINUE_WITH_EMAIL_BTN).click()
        self.driver.find_element(*self.PASSWORD_TEXTBOX).send_keys("basebaser3")
        self.driver.find_element(*self.LOGIN_BTN).click()

    

