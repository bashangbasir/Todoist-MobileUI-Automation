"""
This module contain the page object for the welcome page.
"""

from appium.webdriver.common.mobileby import MobileBy 

class WelcomePage:
    
    EMAIL_BTN = (MobileBy.ID,"com.todoist:id/btn_welcome_continue_with_email")
    WELCOME_TITLE = (MobileBy.ID,"com.todoist:id/title")

    def __init__(self,driver):
        self.driver = driver
        
    def start_login_with_email(self):
        self.driver.find_element(*self.EMAIL_BTN).click()

    def start_login_with_fb(self):
        #TODO
        pass

    def start_login_with_google(self):
        #TODO
        pass

    def get_welcome_message(self):
        return self.driver.find_element(*self.WELCOME_TITLE).text
        
        