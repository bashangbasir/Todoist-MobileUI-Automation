"""
This module contain the page object for the user home page.
"""

from appium.webdriver.common.mobileby import MobileBy 
import time
class UserHomePage:
    
    TOOLBAR_TITLE = (MobileBy.XPATH,"*//android.widget.TextView[@text='Today']")
    BURGER_NAV = (MobileBy.ACCESSIBILITY_ID,"Change the current view")
    ALL_PROJECT_LISTS = (MobileBy.XPATH,"*//android.widget.RelativeLayout[@resource-id='android:id/content']")
    PROJECT_TEXT = (MobileBy.XPATH,"//android.widget.TextView[@resource-id='com.todoist:id/name']")
    PROJECTS_BTN = (MobileBy.XPATH,"*//android.widget.RelativeLayout/android.widget.TextView[@text='Projects']")


    def __init__(self,driver):
        self.driver = driver

    def get_toolbar_title(self):
        return self.driver.find_element(*self.TOOLBAR_TITLE).text

    def get_all_projects(self):
        all_projects = []
        self.driver.find_element(*self.BURGER_NAV).click()
        self.driver.find_element(*self.PROJECTS_BTN).click()
        project_elems = self.driver.find_elements(*self.ALL_PROJECT_LISTS)
        for elem in project_elems:
            #append all the project name seen from mobile app 
            all_projects.append(elem.find_element(*self.PROJECT_TEXT).text)
        return all_projects

